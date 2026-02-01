from Openai_LLM import OpenAILLM

# 实例化OpenAI LLM类，分别用于调用gpt-4和gpt-3.5-turbo模型
gpt_4 = OpenAILLM("gpt-4")
gpt_3_5_turbo = OpenAILLM("gpt-3.5-turbo")

# 自动优化Prompt的简单示例
# 最初使用的Prompt
Original_Prompt = (
"""请判断下面这段文本的情感是正面还是负面，只回答'正面'或者'负面'。请注意，文本中可能包含讽刺或者反语的情绪表达，需要仔细理解文本的真实含义。
文本：{sentence}
回答："""
)
# 用于生成较优Prompt的Prompt
Generate_New_Prompt = (
    "对于情感分类任务，使用了如下的Prompt\n"
    "Prompt：<{Original_Prompt}>\n\n"
    "如果我们把Prompt里的sentence里面的sentence使用{err_sample}替换，此Prompt下的模型的输出是：\n"
    "{err_answer}\n"
    "而正确的输出应该是：\n"
    "{correct_answer}\n"
    "改进<>中的内容，你应该反思错误原因，为使得模型能够得到正确结果而增加新的原则和注意事项。\n"
    "只修改<>中的内容，只给出修改后的<>中的内容结果："
)

#定义一个初始的Prompt节点
class Node():
    def __init__(self, prompt, children=None, parent=None):
        # 每个节点有该节点使用的Prompt、父节点、子节点
        self.prompt = prompt
        self.children = children
        self.parent = parent
    # 用于Print节点的方法
    def __str__(self) -> str:
        return self.prompt
    
    def generate_new_prompt(self,err_sample,err_answer,correct_answer):
        #根据错误样本生成新的Prompt
        new_prompt = gpt_4.chat(
            Generate_New_Prompt.format(Original_Prompt=self.prompt,err_sample=err_sample,err_answer=err_answer,correct_answer=correct_answer)
            )
        return new_prompt

    def get_answer(self,sentence):
        #根据Prompt得到模型的输出
        return gpt_3_5_turbo.chat(self.prompt.format(sentence=sentence))

# 假设模型对这句话判断有误       
sentence = "你这么能杠呀！好牛哦，不如来我这儿的工地抬杠吧。"
label = "负面"

# 实例化一个节点
root = Node(prompt=Original_Prompt)
# 得到答案
answer = root.get_answer(sentence)

print(f"模型的输出是{answer}")

if answer == label:
    print("模型的输出是正确的。")
else:
    print("模型的输出是错误的。")
    # 进行Prompt修正
    new_prompt = root.generate_new_prompt(sentence,answer,label)
    print("新的Prompt是：\n{}".format(new_prompt))
    root.prompt = new_prompt
    print(f"新的输出是：\n{root.get_answer(sentence)}")
            