主要分为两个部分，第一部分介绍大模型提示工程，第二部分介绍调用大模型的API方案，以及使用插件（Plugins）和Actions的对比，最后介绍多场景的Function Calling与Assistant API使用对比，以及大模型应用技巧总结。

## Prompt Engineering （提示工程）

- 介绍 Prompt 的基本原理
- 介绍一些基本的 Prompt 工程技巧
- 介绍一些 Prompt 工程的应用场景
- 介绍一些 Prompt 工程的应用案例

## 使用 Python 调用各类大语言模型的 API

- 百度文心一言
- 星火大语言模型
- OpenAI：gpt-3.5-turbo, gpt-4, gpt-4v
- 使用 OneApi 统一调用各类大语言模型的 API

## Plugins and Actions （函数调用）

- 插件的原理
- OpenAI插件的使用
- 插件的应用场景
- 插件的应用案例
- 插件和 Actions 的对比
- 多场景的 Function Calling 与 Assistant API 的使用对比

最后对上面的三个部分进行内容总结，推出一些大模型应用的技巧。

## Reference 引用
- [Prompt Engineering](https://www.promptingguide.ai/zh)
- [Biadu Wenxin](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Slkkydake)
- [星火大语言模型](https://www.xfyun.cn/doc/spark/Web.html)
- [OpenAI API](https://beta.openai.com/docs/api-reference/introduction)
- [OpenAI Plugins](https://platform.openai.com/docs/plugins/introduction)
- [OpenAI Actions](https://platform.openai.com/docs/actions)
- [OpenAI Assistant API](https://platform.openai.com/docs/assistants/overview)
- [One Api Github](https://github.com/songquanpeng/one-api)



| 服务内容                                                     | 单价                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| ERNIE-Bot 4.0大模型公有云在线调用服务(**输入**)              | 0.12元/千tokens (限时优惠，**~~原价0.15元~~/千tokens**) |
| ERNIE-Bot 4.0大模型公有云在线调用服务(**输出**)              | 0.12元/千tokens (限时优惠，**~~原价0.3元~~/千tokens**)  |
| ERNIE-Bot-8k大模型公有云在线调用服务(**输入**)               | 0.024元/千tokens                                        |
| ERNIE-Bot-8k大模型公有云在线调用服务(**输出**)               | 0.048元/千tokens                                        |
| ERNIE-Bot大模型公有云在线调用服务(**输入**)                  | 0.012元/千tokens                                        |
| ERNIE-Bot大模型公有云在线调用服务(**输出**)                  | 0.012元/千tokens                                        |
| ERNIE-Bot-turbo-0922大模型公有云在线调用服务(**输入**)       | 0.008元/千tokens                                        |
| ERNIE-Bot-turbo-0922大模型公有云在线调用服务(**输出**)       | 0.008元/千tokens (限时优惠，**~~原价0.012~~/千tokens**) |
| [ERNIE-Bot-turbo-AI原生应用](https://console.bce.baidu.com/ai_apaas/app) | 0.008元/千tokens                                        |

| 官方榜单            | GPT-4 | 65.2 | 74.7 | 62.5 | 64.7 | 66.4 |
| ------------------- | ----- | ---- | ---- | ---- | ---- | ---- |
| ChatGPT             | 49    | 58   | 48.8 | 50.4 | 51   |      |
| Claude-v1.3         | 48.5  | 58.6 | 47.3 | 50.1 | 50.5 |      |
| Bloomz-mt-176B      | 39.1  | 53   | 47.7 | 42.7 | 44.3 |      |
| GLM-130B            | 36.7  | 55.8 | 47.7 | 43   | 44   |      |
| Claude-instant-v1.0 | 38.6  | 47.6 | 39.5 | 39   | 40.6 |      |
| ChatGLM-6B          | 33.3  | 48.3 | 41.3 | 38   | 38.9 |      |
| LLaMA-65B           | 32.6  | 41.2 | 34.1 | 33   | 34.7 |      |
| MOSS                | 31.6  | 37   | 33.4 | 32.1 | 33.1 |      |
| Chinese-Alpaca-13B  | 27.4  | 39.2 | 32.5 | 28   | 30.9 |      |
| Chinese-LLaMA-13B   | 28.8  | 32.9 | 29.7 | 28   | 29.6 |      |