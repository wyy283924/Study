from Openai_LLM import OpenAILLM

# 实例化OpenAI LLM类，分别用于调用gpt-4和gpt-3.5-turbo模型
gpt_4 = OpenAILLM("gpt-4")
gpt_3_5_turbo = OpenAILLM("gpt-3.5-turbo")


# 4.2.1 APE (动作Action, 目标Purpose, 期望Expectation)
#数据可视化任务
Prompt = (
    "为我提供描述数据分布的散点图的python代码"
    "数据集由X，Y以及label表示，X，Y为浮点数，label为类别一共三类"
    "三个类别的点分别由红黄绿表示"
)
print(gpt_3_5_turbo.chat(Prompt))
print("---------------------")
# 4.2.2 RACE (角色Role, 动作Action, 上下文Context, 期望Expectation)
#文本风格转换任务
Prompt = (
    "你是一个擅长编写{style}风格文本的语言专家，请你把下面的文本转换成{style}风格的文本。\n"
    "文本：{sentence}"
)
style = "官方"
sentence = (
    "这个问题啊，我觉得还是要从根本上解决。怎么解决呢？我觉得还是要从实际出发，理论联系实际，实事求是。",
    "啊，我们没有说要一步登天，但是呢我们要脚踏实地，稳扎稳打，一步一个脚印，这样才能从根本上，来解决问题。"
    )
#打印Prompt
print(Prompt.format(sentence=sentence,style=style))
#打印转换结果
print(gpt_3_5_turbo.chat(Prompt.format(sentence=sentence,style=style)))
print("---------------------")
# 4.2.3 TAG (任务Task, 动作Action, 目标Goal)
Prompt = (
    "任务：教会我做开衫" 
    "动作：告诉我需要的材料，制作流程以及需要注意的点"
    "目标：为我的弟弟准备过年礼物"
    
)
result =gpt_3_5_turbo.chat(Prompt)
print(result)
print("---------------------")
# 4.2.4 ERA (期望Expectation, 角色Role, 动作Action)
#逻辑推理任务
Prompt = (
    "我们需要为顾客推荐符合他们需求的产品"
    "你作为一个专业的销售人员"
    "请先告诉顾客推荐的产品名称，再说出推荐的理由，同级别的产品应该由价格决定，差价10万以内为同档，当顾客提及性价比时请考虑同级别产品的价格 油耗/电耗等因素"
    "下面是产品信息清单"
    "名称 价格 能源类型 级别 油耗/电耗"
    "阿斯顿·马丁-阿斯顿·马丁DB11 235万 汽油 跑车 11.2"
    "奥迪A7L 58万 油电混合 中大型车 8.6"
    "宝马5系 50万 油电混合 中大型车 6.8"
    "比亚迪D1 17万 电动 MPV -"
    "顾客问：我的预算在55万上下，请告诉我所有符合要求的车然后告诉我性价比最高的是哪个"
)
result = gpt_3_5_turbo.chat(Prompt)
print(result)

