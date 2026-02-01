#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 使用OpenAI服务协议
# 调用qwen-turbo模型完成Function Call，注意：deepseek-v3目前不支持 function call


# In[1]:


import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # read local .env file

def get_weather(location):
    return "24 摄氏度"

def send_messages(messages):
    response = client.chat.completions.create(
        model="qwen-turbo", #deepseek-v3
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

client = OpenAI(api_key="sk-882e296067b744289acf27e6e20f3ec0",
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of an location, the user shoud supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

tool = message.tool_calls[0]

messages.append(message)

# tool.function.arguments
# return: '{"location": "Hangzhou"}'

# tool.function.name
# return: 'get_weather'

funcs_to_call = {'get_weather':get_weather}

func = funcs_to_call[tool.function.name]
res = func(*list(json.loads(tool.function.arguments)))

messages.append({"role": "tool", "tool_call_id": tool.id, "content": res})

message = send_messages(messages)

print(f"Model>\t {message.content}")

