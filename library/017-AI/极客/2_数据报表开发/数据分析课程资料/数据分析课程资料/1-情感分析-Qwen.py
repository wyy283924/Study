#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import os
import dashscope
from dashscope.api_entities.dashscope_response import Role
dashscope.api_key = "sk-882e296067b744289acf27e6e20f3ec0"

# 封装模型响应函数
def get_response(messages):
    response = dashscope.Generation.call(
        model='qwen-turbo', # 大模型的名称
        messages=messages, 
        result_format='message'  # 将输出设置为message形式
    )
    return response
    
review = '这款音效特别好 给你意想不到的音质。'
messages=[
    {"role": "system", "content": "你是一名舆情分析师，帮我判断产品口碑的正负向，回复请用一个词语：正向 或者 负向"},
    {"role": "user", "content": review}
  ]

response = get_response(messages)
response.output.choices[0].message.content


# ## Stream

# In[5]:


import json
import os
import dashscope
from dashscope.api_entities.dashscope_response import Role
dashscope.api_key = "sk-882e296067b744289acf27e6e20f3ec0"

# 封装模型响应函数
def get_response(messages):
    response = dashscope.Generation.call(
        model='qwen-turbo', # 大模型的名称
        messages=messages, 
        result_format='message',  # 将输出设置为message形式
        stream=True
    )
    return response
    
review = """针对金融机构的《个人借贷风险管理》场景，如何使用AIPL模型。
AIPL即用户行为路径，从意识=>兴趣=>购买=>忠诚的4个阶段。
可以观察AIPL与用户特征的统计分布，来制定重点营销人群，即ROI高的人群。
比如 AIPL消费者年龄段分布，如果发现0-1000元的低消费人群，在认知和兴趣人群比例较高，但是在购买和忠诚人群占比较低，即ROI低。而相反，2000元以上的高消费人群，在认知和兴趣人群比例较低，但是在购买和忠诚人群占比较高，即ROI高。所以很明显，把钱投给高消费人群的是明智的。
类似的情况还有很多，比如 AIPL X 月均消费能力分布，AIPL X 性别，AIPL X 地理位置， AIPL X 设备类型等。
===
请给出简短的方案，不超过100字。
重点考虑 AIPL X 哪个维度的用户特征，并举例说明
"""
messages=[
    {"role": "system", "content": "我是数据分析思维助手，用户告诉你业务场景，我将帮你进行方案设计"},
    {"role": "user", "content": review}
  ]

response = get_response(messages)
#for temp in response:
#response.output.choices[0].message.content
last_position = 0
for message in response:
    if message:
        temp_content = message['output']['choices'][0]['message']['content']
        new_content = temp_content[last_position:]
        last_position = len(temp_content)
        print(new_content, end='')

