# 首先应该安装对应的依赖： pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 首先，我们需要导入一些必要的库，包括os、dotenv、OpenAI和lru_cache
import os
from dotenv import load_dotenv
load_dotenv('../.env')
from openai import OpenAI
from functools import lru_cache

# 基类LLM，用于实现通用的接口方法
class BaseLLM:
    @lru_cache(maxsize=1024)
    def chat(self, text):
        return self._chat(text)

    # 虚方法，子类需要实现这个方法
    def _chat(self, text):
        raise NotImplementedError

# OpenAI LLM类，具体实现了与OpenAI API的交互
class OpenAILLM(BaseLLM):
    # 初始化方法，接收模型名称作为参数
    def __init__(self, model_name):
        # 初始化OpenAI客户端，并设置API密钥和基础URL
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),   # 从环境变量中获取API密钥，你自己使用的话，需要替换成你的API密钥
            base_url=os.getenv("OPENAI_API_BASE")  # 同样，你应该替换成你的API基础URL
        )
        # 保存模型名称
        self.model_name = model_name
        # 初始化对话历史列表
        self.conversation_history = []

    # 将文本转换为prompt
    def convert_text_to_prompt(self, instr, target):
        return instr.format(target)

    # 重载__call__魔法方法，使得实例可以直接调用以调用chat方法
    def __call__(self, text):
        return self.chat(text)

    # 主要的聊天方法，接收文本、温度、对话历史和停止条件作为参数
    def chat(self, text, temperature=0, messages=[], stops=None):
        return self._chat(text, temperature, messages, stops)

    # 实现聊天方法，与上面的主聊天方法的区别在于此方法用于内部调用，不需要处理参数
    def _chat(self, text, temperature, messages=[], stops=None):
        # 如果没有提供对话历史，则将当前文本作为用户输入添加到对话历史中
        if not messages:
            messages = [{"role": "user", "content": text}]
        print(f"开始请求模型{self.model_name}")

        # 发送请求并获取响应
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            stream=False,
            stop=stops,
            temperature=temperature,
        )

        # 返回模型的回答
        return response.choices[0].message.content

    # 使用对话历史的聊天方法
    def history_chat(self, text, messages=[], stops=None):
        # 将当前文本作为用户输入添加到对话历史中
        self.conversation_history.append({"role": "user", "content": text})

        # 创建请求
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.conversation_history,  # 传递完整的对话历史
            stream=False,
        )

        # 将模型的回答添加到对话历史中
        answer = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": answer})

        # 返回模型的回答
        return answer
    