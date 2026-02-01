from Openai_LLM import OpenAILLM

# 实例化OpenAI LLM类，分别用于调用gpt-4和gpt-3.5-turbo模型
gpt_4 = OpenAILLM("gpt-4")
gpt_3_5_turbo = OpenAILLM("gpt-3.5-turbo")


# 多模型投票完成金融对话系统的意图识别
#这里我们使用了3个gpt-3.5-turbo模型，它们的提示不同。当然，你可以使用完全不同的模型。

Prompt_1 = (
    "已知意图有A:查询账户余额；B:转账；C:查询交易记录；D:未知意图；共四种，请你根据用户的话判断用户的意图。只需告诉我对应字母，不需要任何额外信息，包括标点。\n"
    "{text}"
)

#使用Few-Shot思维链
Prompt_2 = (
    "现在我正在完成一个银行客服机器人的开发，我需要你帮我完成意图识别的任务。假设意图有且仅有：\n"
    "A:查询账户余额\n"
    "B:转账\n"
    "C:查询交易记录\n"
    "D:未知意图\n"
    "请你根据用户的话判断用户的意图。你需要一步一步地解释你的推理逻辑。并在最后以你的答案所对应的字母结尾，而不是句号结尾。\n"
    "用户的话：今天天气可真好啊！"
    "推理和答案：从用户的话可以得知，客户正在跟您聊今天的天气。但这个话题与银行业务无关。因此意图是未知意图，即答案为D"
    "用户的话：{text}"
    "推理和答案："
)
#使用Few-Shot等
Prompt_3 = (
    """
        背景：你是一个资深的语言学家，擅长对金融领域的对话进行意图识别。
        任务：请你根据用户对你说的话的话判断用户的意图。
        原则：你只能回答每个意图类型所对应的字母。如果无法识别或确定，请选择D。
        
        意图类型：
        A:查询账户余额
        B:转账
        C:查询交易记录
        D:未知意图
        
        我相信你能很好地完成这个任务，这对于我的工作非常重要！
            
        用户的话：我觉得我看看我昨天花了多少钱真的很重要
        意图类型：C
        用户的话：你好帅啊！
        意图类型：D
        用户的话：{text}
        意图类型：
    """
    )

Prompt_list = [Prompt_1,Prompt_2,Prompt_3]
Letter_to_Intention = {"A":"查询账户余额","B":"转账","C":"查询交易记录","D":"未知意图"}

#定义检测装饰器，如果异常，默认输出D
#当然您可以自定义出错时的处理机制，比如重新调用模型，或者忽略该模型的输出
def Output_Check(func):
    def wrapper(*args, **kwargs):
        Result = func(*args, **kwargs)   #func指代的是被修饰的函数，也就是下面的Intention_Detection
        
        #在检测之前先处理模型输出，下面这个处理很简单，仅仅是为了防止Prompt_2的意外情况。然而它也可以很复杂
        Result = Result[-2] if '。' in Result[-1] else Result[-1]

        #检测
        if Result in ["A","B","C","D"]:
            return Result
        else:
            print("发生异常！进行默认选择。")
            return "D"
    return wrapper

#定义输出函数，使用检测装饰器修饰
@Output_Check
def Intention_Detection (text,model,Prompt):
    Result = model.chat(Prompt.format(text=text))
    return Result

#定义多模型投票函数
def Multi_Model_Vote (text, model, Prompt_list):
    print("正在进行多模型投票，一共有{}个模型".format(len(Prompt_list)))
    result_list = []
    #遍历所有的Prompt
    for i,Prompt in enumerate(Prompt_list):
        #得到经过检测后的结果
        Result = Intention_Detection(text,model,Prompt)
        #打印结果
        print("第{}个模型的结果是：{}".format(i+1,Letter_to_Intention[Result]))
        #加入结果列表
        result_list.append(Result)
    #选择投票数目最多的一个结果
    return max(set(result_list), key=result_list.count)


Multi_Model_Vote("我得给我妈打一笔钱，因为今天是她生日。",gpt_3_5_turbo,Prompt_list)
Multi_Model_Vote("是生存还是死亡，这是一个值得思考的问题。",gpt_3_5_turbo,Prompt_list)
Multi_Model_Vote("你好！我来查查看我最后的家底。",gpt_3_5_turbo,Prompt_list)

#下面这个错误来源于我们对客户意图的人为分类上。因为会有客户既想要查询余额，也想要查询交易记录。
#这个例子告诉我们，Prompt is not all you need（提示并不是你所需要的全部）。要想搭建一个好的大模型应用系统，好的Prompt仅仅是必要条件。
#但对于多意图情况是可以处理的，比如要求您可以显示地要求模型'如果意图不止一种，则依次输出它们的字母'。并接下来合理地编写处理模型输出的函数，这里不作过多讨论。
#第三个Prompt因为综合了多种方法，取得了较为合理的结果(多意图识别为未知意图)
Multi_Model_Vote("我发现我的账对不上了！我需要你帮我查查。",gpt_3_5_turbo,Prompt_list)