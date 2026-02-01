from Openai_LLM import OpenAILLM

# 实例化OpenAI LLM类，分别用于调用gpt-4和gpt-3.5-turbo模型
gpt_4 = OpenAILLM("gpt-4")
gpt_3_5_turbo = OpenAILLM("gpt-3.5-turbo")


# 银行客服产品推荐实践
# 牢记我们的Prompt设计与优化原则，如果我们希望模型能够向客户推荐适合它的金融产品，那么首先模型应该知道客户的需求是什么，其次模型应该知道哪些产品适合客户的需求。为了简单起见，我们将客户分为以下三种类型，针对每种类型我们有不同的金融产品推荐策略：

# |客户类型|推荐产品|原因|
# |:---:|:---:|:---:|
# |期望高收益高风险的客户|股票|股票收益高，但风险也高|
# |期望低收益低风险的客户|国家债券|国家债券收益低，但风险也低|
# |期望平衡收益和风险的客户|基金|基金收益和风险都处于中等水平|
# 首先，我们设计一个简单的对话状态管理系统，它可以根据用户的意图要求模型执行不同的动作。

# 针对产品推荐的Prompt，我们使用了与刚刚的意图识别类似的技巧，例如身份指定，任务分配，原则指导，情感提示等。我们还使用了**思维链技术**，让模型在推荐产品时能够充分考虑到客户的需求。

class Dialog_manage():
    def __init__(self,model):
        # 初始化使用的模型
        self.model = model
        # 意图识别Prompt
        self.intent_prompt = (
            """
                背景：你是一个资深的语言学家，擅长对金融领域的对话进行意图识别。
                任务：请你根据用户对你说的话的话判断用户的意图。
                原则：你只能回答每个意图类型所对应的字母。如果无法识别或确定，请选择E。
                
                意图类型：
                A:查询账户余额
                B:转账
                C:查询交易记录
                D:金融产品推荐
                E:没有进一步提出要求或者无法识别意图

                我相信你能很好地完成这个任务，这对于我的工作非常重要！
                    
                用户的话：我觉得我看看我昨天花了多少钱真的很重要
                意图类型：C
                用户的话：你好帅啊！
                意图类型：E
                用户的话：{text}
                意图类型：
        """
        )
        # 产品推荐Prompt
        self.recommend_prompt = (
            """
                背景：你是一个资深的金融投资学家，擅长提取客户的信息，从而为客户推荐最适合的金融产品。
                任务：首先询问客户对风险和收益的偏好，待客户回答后以此为依据为客户推荐最适合的金融产品。
                原则：
                1.你只能根据我给你的推荐策略来进行推荐。如果无法识别或确定，请进一步询问客户。
                2.完成推荐任务后，以TERMINATE结尾。
                3.你不应该自己编造客户给你的回复。
                
                推荐策略：
                高风险高收益：股票
                低风险低收益：国家债券、储蓄
                风险和收益的平衡：货币基金

                我相信你能很好地完成这个任务，这对于我的工作非常重要！

                请你在推荐产品时一步步思考客户的回复，展现你的推理过程，得出你的推荐结果，阐释你的推荐理由。

                首先，询问客户信息：
        """
        )

    # 意图识别函数：直接利用对应的Prompt调用模型
    def Intention_Detection(self,text):
        Result = self.model.chat(self.intent_prompt.format(text=text))
        return Result
    # 产品推荐函数
    def Recommendation(self,text):
        # 得到最初的结果
        Result = self.model.history_chat(self.recommend_prompt)
        print(Result)
        # 如果模型没有给出TERMINATE，则继续对话
        while 'TERMINATE' not in Result:
            Result = self.model.history_chat(input("客户："))
            print(Result)
        return Result
    # 聊天函数
    def Dialog(self,text):
        # 首先进行意图识别
        Intention = self.Intention_Detection(text)
        # ‘D’对应的是产品推荐
        if Intention == "D":
            Recommendation = self.Recommendation(text)
            return '产品推荐结束'
        else:
            return '客户意图是{}'.format(Intention)
        
# 实例化对话管理类
my_dialog = Dialog_manage(gpt_4)
gpt_4.conversation_history = []
while True:
    content = input("客户：")
    if 'exit' in content:
        break
    print(my_dialog.Dialog(content))
    