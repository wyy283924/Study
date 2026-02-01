from Openai_LLM import OpenAILLM

# 实例化OpenAI LLM类，分别用于调用gpt-4和gpt-3.5-turbo模型
gpt_4 = OpenAILLM("gpt-4")
gpt_3_5_turbo = OpenAILLM("gpt-3.5-turbo")

# 银行客服转账任务实践
# 刚刚的对话管理系统并没有实现产品推荐以外的功能，因为转账功能需要更多的信息，例如转账金额、收款人等。只有当我们得到这些信息后，才能进行转账操作。
# 下面是用于提取转账金额的Prompt，类似地，这个Prompt也用到了之前提到的技巧，还给出了'要求进一步澄清'的要求，这对于最终结果的正确性有所帮助。需要强调的是，给模型一些示例对于这个任务很重要，这**既能够帮助模型更好地理解我们的需求，也能够帮助模型规范输出的格式**。

extract_info_prompt = (
    """
        背景：你是一个资深的语言学家，擅长提取客户的信息。
        任务：请你根据用户对你说的话提取出客户想给谁转账及转账金额。

        原则：
        1.如果客户没有提到转账金额或者转账对象，请输出再次询问客户，而不是自己编造。
        2.如果客户提到了转账金额或者转账对象，请输出提取结果，而不是自己编造。
        3.提取结果应该以“转账对象：转账金额”的形式输出。
        4.转账对象应该是真实存在的人名，转账金额应该是一个数字。

        相信你自己能很好地完成这个任务，这对于我的病非常重要！

        例子：
        用户的话：我想给我妈妈转100块钱。
        你的回答：抱歉，您的妈妈的名字是什么？我需要她真实的名字，才能帮您转账。

        用户的话：我要给小红转账100块钱。
        你的回答：小红：100

        接下来请识别以下用户的话，并输出提取结果或者再次询问客户：
        用户的话：{text}
        你的回答：
    """
    )

gpt_3_5_turbo.chat(extract_info_prompt.format(text="我得给小明1000元，虽然我一个月工资只有900，但是他遇到了困难，我得帮助他。他之后会还我2000的"))

# 合并转账功能的对话管理系统
class Dialog_manage():
    # 初始化用户账户信息
    def init_customer_info(self,balance,record):
        self.balance = balance
        self.record = record
    # 查看余额
    def View_balance(self):
        return "您的账户余额为{}元".format(self.balance)
    # 查看交易记录
    def View_record(self):
        #self.record是一个列表，列表中的每个元素是一个字典，字典中k是交易对象，v是交易金额
        description = "交易记录如下：\n"
        for i in self.record:
            description += "您向{}转账了{}元\n".format(i['name'],i['money'])
        return description
    # 转账
    def Transfer(self,text):
        Result = self.model.history_chat(self.extract_info_prompt.format(text=text))
        print(Result)
        # 判断是否已经再次询问客户
        if '：' not in Result:
            # 表明再次询问了客户
            while '：' not in Result:
                Result = self.model.history_chat(input("客户："))
                print(Result)
        # 提取转账对象和转账金额
        name = Result.split('：')[0]
        money = Result.split('：')[1]

        # 更新账户余额
        if self.balance >= int(money):
            self.balance -= int(money)
            # 更新交易记录
            self.record.append({'name':name,'money':money})
            print("您的转账已经受理\n")
            return "您的余额为{}".format(self.balance)
        else:
            return "您的账户余额不足！无法进行转账！"
        

    def __init__(self,model,balance,record):
        # 初始化模型
        self.model = model
        # 初始化用户信息
        self.init_customer_info(balance,record)
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
                意图类型：D
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
        # 信息提取Prompt
        self.extract_info_prompt = extract_info_prompt

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
        # 进行意图识别
        Intention = self.Intention_Detection(text)
        # 判断为未知意图
        if Intention == "E":
            return '抱歉，我不能理解您的意思。'
        # 判断为产品推荐
        elif Intention == "D":
            Recommendation = self.Recommendation(text)
            return '产品推荐结束'
        else:
            # 根据意图类型进行相应的操作
            if Intention == "A":
                return self.View_balance()
            elif Intention == "B":
                return self.Transfer(text)
            elif Intention == "C":
                return self.View_record()
            
# 初始化对话状态管理器
my_dialog = Dialog_manage(gpt_4,1000,[{'name':'小红','money':100},{'name':'小明','money':200}])
gpt_4.conversation_history = []

# 开始对话
while True:
    content = input("客户：")
    if 'exit' in content:
        break
    print(my_dialog.Dialog(content))
