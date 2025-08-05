# 数据获取

```
爬虫:
	概述:	爬虫是批量化自动获取既有数据
		批量化
		自动
		既有数据
	通常来说,都是获取既有数据,也有特殊的,例如批量注册一些账号,批量的去领取优惠券,批量下单买商品,自动做任务等
	
	实际应用:
		1.在企业中,应用最多的为做竞品调研数据采集,或是办公自动化(自动从公司的后台等地方,获取数据进行处理)
		2.个人服务,爬取小说网站等等
		3.盈利:例如抢票,自动评论,自动点赞
		
	分类:
		1.聚焦爬虫:完成某项特定数据的采集,基本90%爬虫都为该类
		2.通用爬虫:就是什么内容都采集,都存下来,例如搜索引擎(百度和谷歌)
		3.增量爬虫:既可以是聚焦爬虫,也可以是通用爬虫,当内容发生变化的时候,它可以增量的获取内容
		4.暗网爬虫:	深网爬虫,该爬虫可以是前三者的任何一种,但是很少见,本身该行为见不得光
		
		
	合法性:
		机器人协议(robots.txt):	协议中规定了哪些内容可以获取,哪些内容不能获取,通常协议中会标明哪些不让爬,但是国内比较顶级的购物网站都没有写机器人协议
		君子协议:未标注是否可以爬取
	注意:
		1.给服务器留活路,爬虫开启后,使用其他设备去访问爬虫网站试一试
		2.脱离敏感数据
		3.不要公开收费
		4.不要爬国家的这种公共资源的网站
		
	爬虫准备工作:
		1.要有一台电脑
		2.python开发环境  Anaconda(https://www.anaconda.com/)
		3.了解爬虫的实现和原理
			直接使用代码去控制终端(App 浏览器)
			另外就是使用代码自己去发生请求
			CS/BS模型
		4.了解Chrome的优点:
			4.1 提供了被代码控制的方式
			4.2 Chrome中提供了请求的分析工具
					网络交互
					数据存储
					源码
					
	爬虫核心流程:
		1.明确目标
		2.搜寻哪些网站或者App中有我们要的资源
		3.分析数据所在位置 加载方式
		4.数据获取
		5.数据提取
		6.数据存储
		7.提升性能
```

```
Anaconda工具:
	打开:
		Anaconda中选择Anaconda prompt
		之后在终端中输入jupyter notebook 回车
		系统一般会自动打开一个网页 这个工具就是学习爬虫的工具
	注意:
		jupyter Notebook有两种模式:编辑模式(允许往单元中键入代码) 命令模式(键盘输入允许程序命令)
		
Ipython使用:
	帮助文档:
		help()
		?
		??
		tab自动补全
		shift+tab 查看函数和参数说明 (主要)
	魔法命令:
		运行外部python文件:%run
		运行计时:%time
		平均运行时间:%timeit
		多行代码的平均运行时间:%%timeit
		更多魔法命令:lsmagic
```

```
数据获取:
	1.驱动客户端App Browser
		Selenium
		playwright
		Appium
	2.发生请求
		前置条件:
			2.1明确浏览器的版本
			2.2需要使用python安装Selenium的驱动(如果在终端中安装,使用pip install selenium 如果在notebook安装,前面加各!)
			2.3下载浏览器对应的浏览器驱动(chromedriver)
```

```
Selenium常见API:
	from selenium import webdriver
	driver=webdriver.Chrome()
	
	打开页面API
	driver.get(url)
	
	回到上一个页面
	driver.back()
	
	前进到下一个页面
	driver.forward()
	
	和页面中的元素进行交互
		1.找到元素
		element=driver.find_element("id","kw")
		2.向输入框发送值
		element.send_keys("内容")
		3.点击按钮
		element.click()
	
	获取页面中的内容
	content=driver.page_source
```

```
Cookie特性:
	Cookie由服务器返回
	Cookie存储在浏览器中
	Cookie支持过期 具有时效性
		关闭浏览器失效
		指定时间后失效
		Cookie是键值存储key-value
	Cookie不能跨网站 不能跨域名
	网络请求会自动携带本网站所有有效Cookie
```

```
提取Cookie代码:
	from selenium import webdriver
	driver=webdriver.Chrome()
	#打开页面 手动进行登录
	driver.get(url)
	#提取cookie
	cookies=driver.get_cookies()
	#将数据进行json的序列化 转换成文本进行存储
	import json
	cookies_str=json.dumps(cookies)
	#使用文件存储,将字符串存到文件中
	with open("xxx.txt","w",encoding="utf-8") as file:
		file.write(cookies_str)
```

```
使用Cookie进行登录:
	from selenium import webdriver
	driver=webdriver.Chrome()
	#读取我们存储在文件中的Cookie
	with open("cookies.txt"，"r",encoding="utf-8") as file:
		cookies_str=file.read()
	#使用json将字符串转换为json格式的数据
	import json
	cookies=json.loads(cookies_str)
	#向浏览器中注入cookie
	for cookie in cookies:
		driver.add_cookie(cookie)
	driver.get(url)
```

```
数据获取之双R与Chrome检查工具使用:
	双R:
		Request
		Response
	构成:
		请求行
		请求头
		请求体
		响应行
		响应头
		响应体
```

![1](./images/1.png)

Chrome检查工具

- 右击可选择
- 功能
  - 箭头
    - 当箭头选中的时候
    - 箭头滑到哪些元素上，右侧就会显示相应的代码
- 在右上角的三个点的折叠菜单中，可以配置调试框的位置
- 还支持设备类型切换
  - PC
  - 平板
  - 手机
  - 主要功能
    - 是前端工程师去适配Web显示的
  - 对爬虫工程师来说
    - 如果你遇到了解决不掉的数据选取了，可以尝试换一种方式
    - PC版本抓不到了，可以尝试抓取手机版本的，平板版本的
- Elements
  - 就是当前显示的页面对应的HTML
- console
  - 控制台，终端
  - 前端工程师开发时，日志输出的位置，就是那些打印
  - 我们也可以在这里面写js代码进行调试
- source
  - 从服务器中获取回来的原始数据的样子
  - 最常见的一个问题 source和elements有什么区别
    - elements中的内容是source的内容经过了浏览器的一个渲染转换出来的东西
  - source中支持断点调试的
- network
  - 网络
  - 做的操作叫做抓包
  - 在这里面是可以看到双R的
- Application
  - 网站应用的一些资源，主要是存储信息
  - Cookie，缓存

```
Request获取动态数据和静态数据:
	使用python去构造请求,需要的库就是网络库(requests)
	静态资源:	给好url和请求头就行
	动态资源:	根据实际分析情况
```

```
数据提取:
	提取格式:
		html
		json
		xml
	实现方式:
		正则re
		截取
		xpath(主要)
		css
		bs4
```

```
xpath大致实现思路:
	#构建xpath的对象
	from lxml import etree
	tree=etree.HTML(response.text)
	#使用xpath规则进行提取
	elements=tree.xpath(规则)
```

```
数据存储:
	分类:
		文本类数据:txt csv excel 数据库
		多媒体数据:图片 音频 视频
	代码:
		import requests
		response=requests.get(url)
		content=response.content
		.....
```

# mysql前置学习

```
数据库系统中的单元:
	数据库系统===(1->n)====>数据库===(1-->n)===>数据表===(1-->n)===>多个字段

数据库的相关操作:
	登录数据库
	mysql -u用户名 -p
	密码
	
	创建数据库:
	create database 数据库名
	
	删除数据库
	drop database 数据库名
	
	使用某个库
	use 数据库名
	
	创建数据表
	create table 数据表名(字段1 类型,字段2 类型)
	
	查看数据表结构
	desc 数据表名字
	
	查看所有数据表
	show tables
	
	修改表名
	alter table 旧数据表名 rename 新数据表名
	
	删除表
	drop table 数据表名
```

```
数据表字段操作:
	增加表字段
	alter table 数据表名 add 字段名 类型
	修改表字段
	alter table 数据表名 modify 字段名 类型
	删除表字段
	alter table 数据表名 drop 字段名
	表字段改名
	alter table 数据表名 change 字段原名 字段新名 类型
```

```
mysql中常见的索引:
	索引用于快速找出某个列中有一特定值的行
	分类:
		唯一索引:某一行启用了唯一索引则不准许这一列的行数据中有重复的值,针对这一列的每一行数据都要求是唯一的
		主键索引:它是一种特殊的唯一索引,不允许有空值,一般是在建表的时候同时创建主键索引,常用于id
		全文索引:对于需要全局搜索的数据,进行全文索引
```

```
mysql中sql语句的增删改查:
	查询所有:
		select * from 表名
	插入:
		insert into 表名 values(值1,值2...)
	查询指定字段:
		select 字段1 字段2 from 表名
	条件查询:
		select * from 表名 where 条件
	结果集排序:
		select * from 表名 order by 字段 排序关键词(desc asc)
	限制查询的结果集:
		select * from 表名 limit 偏移量 数量
	分组:
		select * from 表名 group by 字段名
	结果集过滤:
		select * from 表名 group by 字段 having 条件
	修改数据:
		update 表名 set 字段1=值1,字段2=值2 where 条件
	删除数据:
		delete from 表名 where 条件
```

```
常见统计函数:
	sum() 求和
	count() 统计数据量
	max 最大值
	min 最小值
	avg 平均值
```

# NumPy

```
介绍:
	NumPy是Python的一种开源的数值计算扩展。提供多维数组对象，各种派生对象，这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表结构要高效的多，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库，包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅立叶变换、基本线性代数，基本统计运算和随机模拟等等。
安装:
	Anaconda自带NumPy库
导入:
	# 数据分析 “三剑客”
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
```

```
创建ndarray:
	1.使用np.array(list)由python list创建
		参数:
			list为列表
		注意:
			1.numpy默认ndarray的所有元素的类型是相同的
			2.如果传进来的列表中包含不同的类型,则统一为同一类型,优先级: str>float>int
			3，ndarray的数据类型:
				int: int8 uint8 int16 int32 int64
				float: float16 float32 float64
				str: 字符串
				
	2.使用常规函数np.ones(sharp,dtype=None,order='C')创建一个所有元素都为1的多维数组
		参数:
			sharp:形状
			dtype=None 元素类型
			order ： {‘C’，‘F’}，可选，默认值：C 是否在内存中以行主（C-风格）或列主（Fortran-风格）顺序存储多维数据, 一般默认即可
			
	3.np.zeros(sharp,dtype=float,order='C')创建一个所有元素都为0的多维数组
		参数:与上述一致
		
	4.np.full(sharp,fill_value,dtype=None,order='C')创建一个所有元素都为指定元素的多维数组
		参数:
			sharp:形状
			fill_value:填充值
			dtype=None:元素类型
			
	5.np.eye(N,M=None,k=0,dtype=float)
		参数:
			N 行数
			M 列数
			k 偏移量
			type 元素类型
			
	6.np.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)创建一个等差数列
		参数:
			start:开始值
			stop:结束值
			num:等差数列的个数
			endpoint:是否包含结束值
			retstep:是否返回等差值(步长)
			type 元素类型
			
	7.np.arange([start, ]stop, [step, ]dtype=None) 创建一个数值范围的数组
		参数:
			start:开始值
			stop:结束值(不包含)
			step:步长
			type:元素类型
				
	8.np.random.randint(low,high=None,size=None,dtype='l')创建一个随机整数的多维数组
		参数:
			low:最小值
			high:最大值(high=None时,生成的数值在[0,low)区间内,如果使用high这个值,则生成的数值在[low,high)之间)
			size:数组形状,默认只输出一个
			type:元素类型
			
	9.np.random.randn(d0, d1, ..., dn) 创建一个服从标准正态分布的多维数组
	
	10.np.random.normal(loc=0.0, scale=1.0, size=None) 创建一个服从正态分布的多维数组
	
	11.np.random.random(size=None)  创建一个元素为0~1(左闭右开)的随机数的多维数组
	
	12.np.random.rand(d0, d1, ..., dn) 创建一个元素为0~1(左闭右开)的随机数的多维数组
```

```
ndarray的属性:
	ndim:维度
	shape:形状
	size:总长度(形状各个数相乘)
	dtype:元素类型
```

```
变形:
	使用reshape函数,注意参数是一个tuple
	例如:n=np.reshape(n,(4,5))
	
级联:
	#上下合并,垂直级联
	np.concatenate((n1, n2))
	np.concatenate((n1, n2), axis=0)  # axis=0表示行，第一个维度
	# 左右合并:水平级联
	np.concatenate((n1, n2), axis=1)  # axis=1表示列，第二个维度
	# 左右合并:水平级联
	np.hstack((n1, n2)) 
	# 上下合并:垂直级联
	np.vstack((n1, n2))
	
拆分:
	# 垂直方向，平均切成3份
	np.vsplit(n, 3)
	# 如果是数组
	np.vsplit(n, (1,2,4))
	# 水平方向
	np.hsplit(n, 2)
	# 通过axis来按照指定维度拆分
	np.split(n, 2, axis=1) 1水平 0垂直

拷贝/复制/副本:
	# 赋值: 不使用copy
	n1 = np.arange(10)
	n2 = n1
	n1[0] = 100
	display(n1, n2)
	# array([100,   1,   2,   3,   4,   5,   6,   7,   8,   9])
	# array([100,   1,   2,   3,   4,   5,   6,   7,   8,   9])

	# 拷贝: copy
	n1 = np.arange(10)
	n2 = n1.copy()
	n1[0] = 100
	display(n1, n2)
	# array([100,   1,   2,   3,   4,   5,   6,   7,   8,   9])
	# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	
转置:
	# transpose改变数组维度
	n = np.random.randint(0, 10, size=(3, 4, 5)) # shape(3, 4, 5)
	np.transpose(n, axes=(2,0,1))  
```

```
ndarray聚合操作:
	np.sum(n)  求和
	np.sum(n, axis=0)  垂直算   axis=1  水平算
	np.max(n)  最大值
	np.min(n)  最小值
	np.average(n) 平均值
	np.argmin(n) 最小数下标
	np.argmax(n) 最大数下标
	n = np.array([1,2,3,np.nan])
	# array([ 1.,  2.,  3., nan])
	np.sum(n)  # nan
	np.nansum(n)  # 6.0  计算nan以外的元素
```

```
ndarray的矩形操作:
	算术运算(直接运算)
	矩阵积
	np.dot(n1,n2)
	# 线性代数常用
	n = np.array([[1, 2, 3],
              	[2, 5, 4],
              	[4, 5, 8]]) 
	np.linalg.inv(n) # 逆矩阵
	np.linalg.det(n) # 计算矩阵行列式
	# 矩阵的秩(满秩矩阵或奇异矩阵)
	np.linalg.matrix_rank(n)
```

```
其他数学函数:
	np.abs(n) # 绝对值
	np.sqrt(n) # 开平方
	np.square(n) # 平方
	np.exp(n) # 指数
	np.log(n) # 自然对数,以e为底的对数
	np.log(np.e)  # 自然对数,以e为底的对数
	np.log(1)  # 0
	np.log2(n) # 对数
	np.log10(n) # 10为底的对数  常用对数
```

```
ndarray广播机制:
	规则一：为缺失的维度补维度
	规则二：缺失元素用已有值填充
```

```
ndarray的排序:
	np.sort()不改变输入
	ndarray.sort()本地处理，不占用空间，但改变输入
```

```
ndarray文件操作:
	save : 保存ndarray到一个npy文件
	np.save("x",x)
	savez : 将多个array保存到一个npz文件中
	np.savez("arr.npz",xarr = x,yarr=y)
```

# Pandas

####  一、Pandas课程介绍

- Pandas 是基于NumPy的一种工具，该工具是为解决数据分析任务而创建的, Pandas提供了大量能使我们快速便捷地处理数据的函数和方法。

- Pandas与出色的 Jupyter工具包和其他库相结合，Python中用于进行数据分析的环境在性能、生产率和协作能力方面都是卓越的。
- Pandas的主要数据结构是 **Series(**一维数据)与 **DataFrame **(二维数据)，这两种数据结构足以处理金融、统计、社会科学、工程等领域里的大多数案例
- 处理数据一般分为几个阶段：数据整理与清洗、数据分析与建模、数据可视化，Pandas 是处理数据的理想工具。

#### 二、Pandas安装

- Anaconda环境: 无需安装
- 普通Python环境: pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple

#### 三、Pandas数据结构

#### Series

Series是一种类似于一维数组的对象，由下面两个部分组成：

- values：一组数据（ndarray类型）
- index：相关的数据索引标签

##### 1）Series的创建

两种创建方式：

###### (1) 由列表或NumPy数组创建

```python
list1 = [11, 22, 33, 44]
n = np.array(list1)
# type(n)  # numpy.ndarray

s = Series(n)
display(n, s, type(s))  
# pandas.core.series.Series
```

Series属性: index和values

```python
# values属性
s.values 
# array([11, 22, 33, 44])

s.index
# RangeIndex(start=0, stop=4, step=1)
list(s.index)

# 修改索引
s.index = list("abcd")
s.index = ["鲁班", "李白", "诸葛亮", "张飞"]
display(s)

# 通过索引取值
s.鲁班, s['鲁班']

# 通过索引修改值
s['鲁班'] = 100
```

###### (2) 还可以通过字典创建

```python
d = {
    'a': 11,
    'b': 22,
    'c': 33,
    'd': 44
}
s = Series(d)
s.index = list("ABCD")
display(s)


d = {
    'a': np.random.randint(0, 10, size=(2,3)),
    'b': np.random.randint(0, 10, size=(2,3)),
    'c': np.random.randint(0, 10, size=(2,3)),
    'd': np.random.randint(0, 10, size=(2,3))
}
s = Series(d)
display(s)


# 创建时同时设置索引
s = Series([1,2,3], index=["张三", '李四', '王五'])
display(s)
```

##### 2）Series的索引

可以使用中括号取单个索引（此时返回的是元素类型），或者中括号里一个列表取多个索引（此时返回的仍然是一个Series类型）。分为显示索引和隐式索引：

###### (1) 显式索引：

 - 使用index中的元素作为索引值
 - 使用.loc[]

注意，此时是闭区间

```python
s = Series({'语文': 150, "数学": 100, "英语": 120, "Python": 99})

# 显式索引：使用索引名字
s['语文']  # int类型
s[['语文', "Python", "数学"]]  # Series类型
s[['语文']]  # Series类型

# .loc[ ]
s.loc['语文']
s.loc[['语文', "Python", "数学"]] 
s.loc[['语文']]
```

###### (2) 隐式索引：

- 使用整数作为索引值
- 使用.iloc[]（推荐）

注意，此时是半开区间

```python
s = Series({'语文': 150, "数学": 100, "英语": 120, "Python": 99})

# 隐式索引： 使用数字下标
s[0]
s[[0, 2, 1]]
s[[0]]

# iloc[ ]
s.iloc[0]
s.iloc[[0, 2, 1]]
s.iloc[[0]]
```

##### 3）Series的切片

- Series一维数组切片

```python
s = Series({'语文': 150, "数学": 100, "英语": 120, "Python": 99, "Numpy": 66, "Pandas": 199})

# Series是一维数组

# 隐式切片 : 左闭右开
s[1: 4]
s.iloc[1: 4]

# 显式切片： 闭区间
s["数学": "Python"]
s.loc["数学": "Python"]
```

##### 4）Series的属性和方法

- shape 形状
- size 大小
- index 索引
- values 值
- dtype 元素类型
- name  Series名字

```python
s.shape  # 形状
s.size  # 元素个数
s.index  # 索引
s.values  # 值
s.dtype  # 元素类型

s = Series([11, 22, 33], name="年龄")
s.name
```

查看首尾数据

- head()  查看前几条数据，默认5条
- tail()  查看后几条数据，默认5 

```python
# 查看前几条数据，默认5条
head() 
s.head()  
s.head(2)

# 查看后几条数据，默认5
tail() 
s.tail()
s.tail(2)
```

检测缺失数据

- pd.isnull()
- pd.notnull()
- isnull()
- notnull()

```python
# s.isnul()
pd.isnull(s)

# s.notnull()
pd.notnull(s)

# 可以通过True，Flase过滤数据

# 保留不为空的数据
s[ pd.notnull(s) ]
```

##### 5）Series的运算

###### (1) 适用于NumPy的数组运算也适用于Series

```python
s = Series(np.random.randint(10, 100, size=10))

s + 100
s - 100
s * 100
s / 100
s // 10
s ** 2
```

###### (2) Series之间的运算

- 在运算中自动对齐索引的数据
- 如果索引不对应，则补NaN
- Series没有广播机制 

```python
s1 = Series(np.random.randint(10, 100, size=3))
s2 = Series(np.random.randint(10, 100, size=4))
display(s1 + s2)

# Numpy中有广播机制
n1 = np.array(np.random.randint(1, 10, size=(1, 3)))
n2 = np.array(np.random.randint(1, 10, size=(3, 1)))
display(n1 + n2)
```

- 注意：要想保留所有的index，则需要使用.add()函数

```python
s1.add(s2, fill_value=100)
```

#### DataFrame

DataFrame是一个【表格型】的数据结构，可以看做是【由Series组成的字典】（共用同一个索引）。DataFrame由按一定顺序排列的多列数据组成。设计初衷是将Series的使用场景从一维拓展到多维。DataFrame既有行索引，也有列索引。

- 行索引：index
- 列索引：columns
- 值：values（numpy的二维数组）

##### 1）DataFrame的创建

最常用的方法是传递一个字典来创建。DataFrame以字典的键作为每一【列】的名称，以字典的值（一个数组）作为每一列。

此外，DataFrame会自动加上每一行的索引（和Series一样）。

同Series一样，若传入的列与字典的键不匹配，则相应的值为NaN

```python
d = {
    'name' : ["鲁班", '陈咬金', "猪八戒"],
    'age' : [7, 9, 8],
    'sex': ['男', '女', '男']
}
df = DataFrame(d)
```

###### DataFrame属性和方法

- values 值
- columns 列索引
- index 行索引
- shape 形状
- head() 查看前几行数据
- tail() 查看后几行数据

```python
# 创建DataFrame
df = DataFrame(d, index=["第一行", "第二行", "第三行"])

df.values  # 值，二维ndarray数组
df.columns   # 列索引
df.index  # 行索引
df.shape  # 形状

# 查看首尾数据
df.head(2)
df.tail(2)
```

创建DataFrame的其他方式

```python
df = DataFrame(
    data=np.random.randint(0, 100, size=(4, 6)),
    index=['小明', "小红", '小绿', '小黄'],
    columns=['语文', '数学', '英语', 'Python', 'Numpy', 'Pandas']
)
df
```

##### 2）DataFrame的索引

###### (1) 对列进行索引

- 通过类似字典的方式
- 通过属性的方式

可以将DataFrame的列获取为一个Series。返回的Series拥有原DataFrame相同的索引，且name属性也已经设置好了，就是相应的列名。

```python
df = DataFrame(
    data=np.random.randint(0, 100, size=(4, 6)),
    index=['小明', "小红", '小绿', '小黄'],
    columns=['语文', '数学', '英语', 'Python', 'Numpy', 'Pandas']
)

df.语文
df['语文']  # Series

df[['语文', 'Python']]  # DataFrame
df[['语文']]
```

###### (2) 对行进行索引

- 使用.loc[ ]加index来进行行索引
- 使用.iloc[ ]加整数来进行行索引

同样返回一个Series，index为原来的columns。

```python
df = DataFrame(
    data=np.random.randint(0, 100, size=(4, 6)),
    index=['小明', "小红", '小绿', '小黄'],
    columns=['语文', '数学', '英语', 'Python', 'Numpy', 'Pandas']
)

# DataFrame默认取列索引
df.loc['小明']  # Series
df.iloc[0]

df.loc[['小明', '小绿']]  # DataFrame
df.loc[['小明']] 
df.iloc[[0, 2]]  # DataFrame
df.iloc[[0]]
```

###### (3) 对元素索引的方法

- 使用列索引
- 使用行索引(iloc[3,1]相当于两个参数;iloc[[3,3]] 里面的[3,3]看做一个参数)
- 使用values属性（二维numpy数组）

```python
df = DataFrame(
    data=np.random.randint(0, 100, size=(4, 6)),
    index=['小明', "小红", '小绿', '小黄'],
    columns=['语文', '数学', '英语', 'Python', 'Numpy', 'Pandas']
)

# 先取列，再取行
df['语文'][1]
df['语文']['小明']

# 先取行，再取列
df.iloc[1]['语文']
# df.loc['小明', '语文']  
```

##### 3）DataFrame的切片

【注意】 直接用中括号时：

- 索引表示的是列索引
- 切片表示的是行切片

```python
df = DataFrame(
    data=np.random.randint(0, 100, size=(4, 6)),
    index=['小明', "小红", '小绿', '小黄'],
    columns=['语文', '数学', '英语', 'Python', 'Numpy', 'Pandas']
)

# 索引： 优先使用列索引， 先取行就需要写loc或iloc
# 切片： 优先按行切片， 和Numpy操作类似

# 行： 行名， 行数字索引
# 列： 列名

# 行切片
df[1 : 3]  # 左闭右开
df['小明' : "小绿"]  # 闭区间

df.iloc[1 : 3]
df.loc['小明' : "小绿"]

# 列切片: 需要使用loc或iloc
df.iloc[:, 1:3]
df.loc[:, "数学": "Python"]

df.loc["小明":"小绿", "数学":"Python"]
df.iloc[:3, 1:4]
```

##### 4）DataFrame的运算

###### （1） DataFrame之间的运算

- 在运算中自动对齐索引的数据 
- 如果索引不对应，则补NaN
- DataFrame没有广播机制 

```python
# 创建DataFrame df1 不同人员的各科目成绩，月考一
df1 = DataFrame(
    data={
      'Python': [100, 90, 80], 
      'Java': [80, 70, 60], 
      'PHP': [60, 50, 40]
    },
    index=['张飞', "吕布", '关羽']
)

# 创建DataFrame df2 不同人员的各科目成绩，月考二
df2 = DataFrame(
    data={
      'Python': [100, 90, 80, 70], 
      'Java': [80, 70, 60, 50], 
      'PHP': [60, 50, 40, 30], 
      'Go': [40, 30, 20, 10]
    },
    index=['张飞', "吕布", '关羽', "刘备"]
)

# DataFrame和数的运算
display(df1 + 100)

# DataFrame之间的运算
display(df1 + df2)

# 自动填充， 再相加
df1.add(df2, fill_value=1000)
```

###### （2）Series与DataFrame之间的运算

- 使用Python操作符：以行为单位操作（参数必须是行），对所有行都有效。（类似于numpy中二维数组与一维数组的运算，但可能出现NaN）

- 使用pandas操作函数：

  axis=0：以列为单位操作（参数必须是列），对所有列都有效。
  axis=1：以行为单位操作（参数必须是行），对所有行都有效。

```python
# 创建DataFrame df1 不同人员的各科目成绩，月考一
df1 = DataFrame(
    data={
      'Python': [100, 90, 80], 
      'Java': [80, 70, 60], 
      'PHP': [60, 50, 40]
    },
    index=['张飞', "吕布", '关羽']
)

s = Series([100, 10, 1], index=df1.columns)

# 直接相加
df1 + s

# 使用add函数
df1.add(s)
df1.add(s, axis='columns')  # 列
df1.add(s, axis=1)  # 第二个维度

s = Series([100, 10, 1], index=df1.index)
df1.add(s, axis='index')  # 行
df1.add(s, axis=0)  # 行
```



#### 四、Pandas层次化索引

##### 1. 创建多层行索引

###### 1) 隐式构造

- 最常见的方法是给DataFrame构造函数的index参数传递两个或更多的数组

```python
data = np.random.randint(0, 100, size=(6, 6))

index = [
    ['1班', '1班', '1班', '2班', '2班', '2班'],
    ['张三', '李四', '王五', '赵六', '田七', '孙八']
]

columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]

df = pd.DataFrame(data=data, index=index, columns=columns)
df
```

- Series也可以创建多层索引

```python
data = np.random.randint(0, 100, size=6)

index = [
    ['1班', '1班', '1班', '2班', '2班', '2班'],
    ['张三', '李四', '王五', '赵六', '田七', '孙八']
]

s  = pd.Series(data=data, index=index)
s
```

###### 2) 显示构造pd.MultiIndex

- 使用数组

```python
data = np.random.randint(0, 100, size=(6, 6))

index = pd.MultiIndex.from_arrays( [
    ['1班', '1班', '1班', '2班', '2班', '2班'],
    ['张三', '李四', '王五', '赵六', '田七', '孙八']
] )

columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]

df = pd.DataFrame(data=data, index=index, columns=columns)
df
```

- 使用tuple

```python
data = np.random.randint(0, 100, size=(6, 6))

index = pd.MultiIndex.from_tuples( 
    (
        ('1班', '张三'), ('1班', '李四'), ('1班', '王五'), 
        ('2班', '赵六'), ('2班', '田七'), ('2班', '孙八'), 
    )
)

columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]

df = pd.DataFrame(data=data, index=index, columns=columns)
df
```

- 使用product 

```python
data = np.random.randint(0, 100, size=(6, 6))

# 笛卡尔积：{a, b} {c, d} => {a,c}, {a,d}, {b,c}, {b,d}
index = pd.MultiIndex.from_product( 
    [
        ['1班',  '2班'],
        ['张三', '李四', '王五']
    ]
)

columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]

df = pd.DataFrame(data=data, index=index, columns=columns)
df
```

##### 2. 创建多层列索引(同行索引)

除了行索引index，列索引columns也能用同样的方法创建多层索引

##### 3. 多层索引对象的索引与切片操作

###### 1）Series的操作

【重要】对于Series来说，直接中括号[]与使用.loc()完全一样

```python
# (1) 索引
data = np.random.randint(0, 100, size=6)

index = [
    ['1班', '1班', '1班', '2班', '2班', '2班'],
    ['张三', '李四', '王五', '赵六', '田七', '孙八']
]

s  = pd.Series(data=data, index=index)
s

# 显式索引
s['1班']
s.loc['1班']

s.loc[['1班']]
s.loc[['1班', '2班']]

s['1班']['张三']
s.loc['1班']['张三']
s.loc['1班','张三']
s['1班', '张三']

#隐式索引
s[1]
s.iloc[1]
s.iloc[[3, 2]]


# (2) 切片
# 显式切片
s['1班': '1班']
s.loc['1班': '2班']
# s.loc['李四': '田七']  # 没有结果
# s.loc[('1班', '李四'): ('2班', '田七')]   # 报错， 显式切片只对最外层索引有效

# 建议使用隐式切片
s[1: 4]
s.iloc[1: 5]
```

###### 2）DataFrame的操作

- 可以直接使用列名称来进行列索引
- 使用行索引需要用iloc()，loc()等函数 
- 无法直接对二级索引进行索引

```python
data = np.random.randint(0, 100, size=(6, 6))

index = pd.MultiIndex.from_product( 
    [
        ['1班',  '2班'],
        ['张三', '李四', '王五']
    ]
)
columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]
df = pd.DataFrame(data=data, index=index, columns=columns)


# 获取元素
df['期中']['数学'][1]

df.iloc[1, 3]  # 第1行，第3列（索引）  42
df.loc[('1班', '李四'), ('期末', '语文')]  # 42

# 列索引
df['期中']
df['期中']['数学']
df['期中', '数学']
# df[('期中', '数学')]
# df.期中.数学

df.iloc[:, 2]
df.iloc[:, [1,2,3]]

# 行索引
df.loc['1班']
df.loc['1班'].loc['张三']
df.loc['1班', '张三']
df.loc[('1班', '张三')]

df.iloc[1]
df.iloc[[1]]
df.iloc[[1,2,3]]

# 切片
# 行切片
df.iloc[1:5]
df.loc['1班' : '2班']
df.loc[('1班', '李四') : ('2班', '李四')]

# 列切片
df.iloc[:, 1: 5]
df.loc[:, '期中': '期末']
# df.loc[:, ('期中', '数学'): ('期末', '数学')]  # 报错
```

##### 4. 索引的堆叠（stack）

- stack()
- unstack()

【小技巧】使用stack()的时候，level等于哪一个，哪一个就消失，出现在行里。

```python
data = np.random.randint(0, 100, size=(6, 6))
index = pd.MultiIndex.from_product( 
    [
        ['1班',  '2班'],
        ['张三', '李四', '王五']
    ]
)
columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]
df = pd.DataFrame(data=data, index=index, columns=columns)

# stack: 列索引变成行索引
df.stack()  # 默认level=-1 (倒数第一层)，将最里层的列索引 变成行索引
df.stack(level=1) 

df.stack(level=0)  # 将最外层的列索引 变成行索引
```

【小技巧】使用unstack()的时候，level等于哪一个，哪一个就消失，出现在列里。

```python
# unstack : 将行索引 变成 列索引
df.unstack()
df.unstack(level=1)

df.unstack(level=0)
```

使用fill_value填充

```python
data = np.random.randint(0, 100, size=(6, 6))
index = pd.MultiIndex.from_tuples( 
    (
        ('1班', '张三'), ('1班', '李四'), ('1班', '王五'), 
        ('2班', '赵六'), ('2班', '田七'), ('2班', '孙八'), 
    )
)
columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]
df2 = pd.DataFrame(data=data, index=index, columns=columns)

df2.unstack()
df2.unstack(fill_value=0)
```

##### 5. 聚合操作

【注意】

- 需要指定axis
- 【小技巧】和unstack()相反，聚合的时候，axis等于哪一个，哪一个就保留。

```python
data = np.random.randint(0, 100, size=(6, 6))
index = pd.MultiIndex.from_tuples( 
    (
        ('1班', '张三'), ('1班', '李四'), ('1班', '王五'), 
        ('2班', '赵六'), ('2班', '田七'), ('2班', '孙八'), 
    )
)
columns = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],
    ['语文', '数学', '英语', '语文', '数学', '英语']
]
df2 = pd.DataFrame(data=data, index=index, columns=columns)


# DataFrame聚合操作：求和，平均值，最大值，最小值....
df3 = df.loc['1班', '期中']

# axis : 0表式行index, 1表式列columns
df3.sum()
df3.sum(axis=0)  # 对同一列的多行进行求和
df3.sum(axis=1)  # 对同一行的多列进行求和


# 多层索引聚合操作
df.sum()  #  默认是对同一列的多行求和
df.sum(axis=1)   # 对同一行的多列求和
df.sum(axis=0, level=0)   # 表式 行 索引中的最外层
df.sum(axis=1, level=0)   # 表式 列 索引中的最外层
df.sum(axis=0, level=1)   # 表式 行 索引中的最里层
df.sum(axis=1, level=1)   # 表式 列 索引中的最里层
```



#### 五、Pandas数据合并

- pd.concat
- pd.append
- pd.merge 

为了方便，我们首先定义一个生成DataFrame的函数：

```python
def make_df(indexs, columns):    
    data = [[str(j)+str(i) for j in columns] for i in indexs]
    df = pd.DataFrame(data=data, index=indexs, columns=columns)
    return df
  
# 调用
# make_df([1, 2, 3, 4], list('ABCD'))
```

##### 1. 使用pd.concat()级联

Pandas使用pd.concat函数，与NumPy中的concatenate函数类似，只是多了一些参数：

###### 1) 简单级联

```python
df1 = make_df([1, 2], ['A', 'B'])
df2 = make_df([3, 4], ['A', 'B'])
display(df1, df2)

# 上下合并，垂直合并
pd.concat([df1, df2])  

# 左右合并，水平合并
pd.concat([df1, df2], axis=1) 

# 忽略行索引，重置行索引
pd.concat([df1, df2], ignore_index=True)  

# 使用多层索引 keys
pd.concat([df1, df2], keys=['x', 'y'])    
# pd.concat([df1, df2], keys=['x', 'y'], axis=1)    
```

###### 2) 不匹配级联

不匹配指的是级联的维度的索引不一致。例如纵向级联时列索引不一致，横向级联时行索引不一致

```python
df3 = make_df([1, 2, 3, 4], ['A', 'B', 'C', 'D'])
df4 = make_df([2, 3, 4, 5], ['B', 'C', 'D', 'E'])
display(df3, df4)

# 对应索引没有值的会自动用NaN填充
pd.concat([df3, df4])

# 外连接：补NaN（默认模式）, 默认值outer，类似并集， 所有数据都会显示
pd.concat([df3, df4])
pd.concat([df3, df4], join='outer')

# 内连接：只连接匹配的项, 交集， 只显示共同的列或行
pd.concat([df3, df4], join='inner')
```

##### 2. 使用append()函数添加

由于在后面级联的使用非常普遍，因此有一个函数append专门用于在后面添加

```python
df3 = make_df([1, 2, 3, 4], ['A', 'B', 'C', 'D'])
df4 = make_df([2, 3, 4, 5], ['B', 'C', 'D', 'E'])
display(df3, df4)

df3.append(df4, sort=True)
```

##### 3.使用merge()合并

- 类似MySQL中表和表之间的合并 
- merge与concat的区别在于，merge需要依据某一共同的行或列来进行合并
- 使用pd.merge()合并时，会自动根据两者相同column名称的那一列，作为key来进行合并。
- 每一列元素的顺序不要求一致

###### 1) 一对一合并

```python
df1 = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'id' : [1, 2, 3],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id' : [2, 3, 4],
    'sex': ['男', '女', '女'],
    'job': ['saler', 'CTO', 'Programer']
})
display(df1, df2)

# 合并
# pd.merge(df1, df2)
df1.merge(df2)
```

###### 2) 多对一合并

```python
df1 = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'id' : [1, 2, 2],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id' : [2, 3, 4],
    'sex': ['男', '女', '女'],
    'job': ['saler', 'CTO', 'Programer']
})
display(df1, df2)

# 合并
df1.merge(df2)
```

###### 3) 多对多合并

```python
df1 = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'id' : [1, 2, 2],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id' : [2, 2, 4],
    'sex': ['男', '女', '女'],
    'job': ['saler', 'CTO', 'Programer']
})
display(df1, df2)

# 合并
df1.merge(df2)
```

###### 4) key的规范化

- 使用on=显式指定哪一列为key,当有多个key相同时使用

```python
df1 = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'id' : [1, 2, 3],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id' : [2, 3, 4],
    'name': ['李四', '王五', '赵六'],
    'job': ['saler', 'CTO', 'Programer']
})
display(df1, df2)

# 如果有多列名称相同， 则需要指定一列作为连接的字段
df1.merge(df2, on='id')
df1.merge(df2, on='name')
```

- 使用left_on和right_on指定左右两边的列作为key，当左右两边的key都不想等时使用

```python
# 如果没有相同的列名，则需要使用left_on和right_on来分别指定2个表的列作为连接的字段
df1.merge(df2, left_on='id', right_on='id2')
```

- 当左边的列和右边的index相同的时候,使用right_index=True

```python
df1.merge(df2, left_index=True, right_on='id2')
```

###### 5) 内合并与外合并

- 内合并：只保留两者都有的key（默认模式）

```python
df1 = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'id' : [1, 2, 3],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id' : [2, 3, 4],
    'sex': ['男', '女', '女'],
    'job': ['saler', 'CTO', 'Programer']
})
display(df1, df2)

# 内连接： inner join
df1.merge(df2)
df1.merge(df2, how='inner')
```

- 外合并 how='outer'：补NaN

```python
# 外连接: 
df1.merge(df2, how='outer')
```

- 左合并、右合并：how='left'，how='right'

```python
# 左连接: 
df1.merge(df2, how='left')

# 右连接: 
df1.merge(df2, how='right')
```

###### 6) 添加后缀

- 当列冲突时，即有多个列名称相同时，需要使用on=来指定哪一个列作为key，配合suffixes指定冲突列名
- 可以使用suffixes=自己指定后缀

```python
df1 = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'id' : [1, 2, 3],
    'age': [22, 33, 44]
})
df2 = pd.DataFrame({
    'id' : [2, 3, 4],
    'name': ['李四', '王五', '赵六'],
    'job': ['saler', 'CTO', 'Programer']
})
display(df1, df2)

df1.merge(df2, on='id', suffixes=['_表1', '_表2'])
```

###### merge合并总结:

- 合并有三种现象: 一对一, 多对一, 多对多.
- 合并默认会找相同的列名进行合并, 如果有多个列名相同,用on来指定.
- 如果没有列名相同,但是数据又相同,可以通过left_on, right_on来分别指定要合并的列.
- 如果想和index合并, 使用left_index, right_index来指定.
- 如果多个列相同,合并之后可以通过suffixes来区分.
- 还可以通过how来控制合并的结果, 默认是内合并, 还有外合并outer, 左合并left, 右合并right.



#### 六、Pandas缺失值处理

有两种缺失值(空值)：

- None
- np.nan

##### 1. None

- None是Python自带的，是Python中的空对象。None不能参与到任何计算中。

- object类型的运算要比int类型的运算慢得多 


```python
# 计算不同数据类型求和时间
%timeit np.arange(1e5, dtype=object).sum()
# 6.1 ms ± 122 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit np.arange(1e5, dtype=np.int32).sum()
# 134 µs ± 7.16 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

##### 2. np.nan（NaN）

- np.nan是浮点类型，能参与到计算中。但计算的结果总是NaN。

```python
type(np.nan)
# float
```

- 但可以使用np.nan*()函数来计算nan，此时会过滤掉nan。

```python
n = np.array([1, 2, 3, np.nan, 5, 6])

# np.sum(n)  # nan
np.nansum(n)

np.nan + 10
```

##### 3. pandas中的None与NaN

###### 1) pandas中None与np.nan都视作np.nan

- 创建DataFrame

```python
data = np.random.randint(0 ,100, size=(5, 5))
df = pd.DataFrame(data=data, columns=list('ABCDE'))

# 修改数据,增加2种nan
df.loc[2, 'B'] = np.nan
df.loc[3, 'C'] = None
display(df)

# 查看结果
df.loc[2, 'B']  # nan
df.loc[3, 'C']  # nan
```

###### 2) pandas中None与np.nan的操作

- isnull()
- notnull()
- all()
- any()
- dropna():  过滤丢失数据
- fillna():  填充丢失数据

(1)判断函数

- isnull()
- notnull()

```python
# isnull
df.isnull()

# notnull
df.notnull()

# all(): 必须全部为True才为True， 类似and
# any(): 只要有一个为True即为True,  类似or

df.isnull().any()  # 常用， 尽可能找到所有的空值
# df.isnull().all()

df.notnull().all()  # 常用，尽可能找到所有的空值
# df.notnull().any()

df.isnull().any(axis=1)  # axis=1 表式列，判断一行中的每一列数据进行判断
df.notnull().all(axis=1)
```

- 使用bool值索引过滤数据

```python
# 行过滤
# 将df中有空的列过滤掉
cond = df.isnull().any(axis=1)
# display(cond, ~cond)
# ~ 取反
df[~cond]

cond = df.notnull().all(axis=1)
# cond
df[cond]

# 列过滤
cond = df.notnull().all()
# cond
df.loc[:, cond]

cond = df.isnull().any()
# cond
df.loc[:, ~cond]
```

(2) 过滤函数

- `dropna()`

可以选择过滤的是行还是列（默认为行）

```python
df.dropna()  # 默认是删除有空的行
df.dropna(axis=1)  # 删除有空的列
```

也可以选择过滤的方式 how = 'all'

```python
df.dropna(how='any')  # 默认值，默认有空就会删除
df.dropna(how='all', axis=1)  # 所有的值都为空（整行或整列为空），才删除
```

inplace=True 修改原数据

```python
df2 = df.copy()

# inplace=True: 表式修改原数据
df2.dropna(inplace=True)
df2
```

(3) 填充函数 Series/DataFrame

- `fillna()`

```python
# 填充
df.fillna(value=100)

df2 = df.copy()
df2.loc[1, 'B'] = np.nan
df2.loc[4, 'C'] = None
display(df2)

# limit: 限制对应维度上填充的次数
df2.fillna(value=100, limit=1, inplace=True)

# 可以选择前向填充还是后向填充
# method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
#     Method to use for filling holes in reindexed Series
#     pad/ffill: propagate last valid observation forward to next valid
#     backfill/bfill: use next valid observation to fill gap.

df.fillna(method='ffill')  # 用上面数据来填充自己
# df.fillna(method='pad')

df.fillna(method='bfill')  # 用下面数据来填充自己
# df.fillna(method='backfill')

df.fillna(method='ffill', axis=1)  # 用左边数据来填充自己

df.fillna(method='bfill', axis=1)  # 用右边数据来填充自己
```



#### 七、Pandas处理重复值和异常值

```python
def make_df(indexs, columns):    
    data = [[str(j)+str(i) for j in columns] for i in indexs]
    df = pd.DataFrame(data=data, index=indexs, columns=columns)
    return df
  
# make_df([1, 2, 3, 4], ['A', 'B', 'C', 'D'])
```

##### 1. 删除重复行

- 使用duplicated()函数检测重复的行，返回元素为布尔类型的Series对象
- 每个元素对应一行，如果该行不是第一次出现，则元素为True

```python
# 让第一行和第二行重复
df.loc[1] = df.loc[2]

# 判断是否和前面的行重复了
df.duplicated()

# df.duplicated(keep='first')  # 保留第一行
# df.duplicated(keep='last')  # 保留最后一行
# df.duplicated(keep=False)  # 标记所有重复行

df.loc[1, 'D'] = 'DDD'
# subset: 子集， 只需要子集相同就可以判断重复
df.duplicated(subset=['A', 'B', 'C'])
```

使用drop_duplicates()函数删除重复的行

```python
df.drop_duplicates(subset=['A', 'B', 'C'])
df.drop_duplicates(subset=['A', 'B', 'C'], keep='last')
```

##### 2. 映射

映射的含义：创建一个映射关系列表，把values元素和一个特定的标签或者字符串绑定

包含三种操作：

- replace()函数：替换元素
- map()函数：处理某一单独的列, 最重要
- rename()函数：替换索引

###### 1) replace()函数：替换元素

使用replace()函数，对values进行替换操作

```python
index = ['鲁班', '张三丰', '张无忌', '杜甫', '李白']
columns = ['Python', 'Java', 'H5', 'Pandas']
data = np.random.randint(0, 100, size=(5, 4))

df = pd.DataFrame(data=data, index=index, columns=columns)

# replace还经常用来替换NaN元素
df.replace({1: 100})
```

###### 2) map()函数: 适合处理某一单独的列

```python
df2 = df.copy()
df2

# map是Series调用，不能使用DataFrame调用
df2['Python'].map({12: 100, 11: 90})

# map()函数中可以使用lambda函数
# 新建一列
df2['NumPy'] = df2['Python'].map(lambda x: x+100)
df2

# 新增一列：判断java成绩是否及格
df2['是否及格'] = df2['Java'].map(lambda n:  "及格" if n>=60 else "不及格")
df2

# 新增一列：判断Java成绩的等级（>=80优秀，>=60及格，<60不及格）
def fn(n):
    if n >= 80:
        return '优秀'
    elif n >= 60:
        return '及格'
    return '不及格'

df2['等级'] = df2['Java'].map(fn)
df2
```

###### 3) rename()函数：替换索引

```python
df3 = df.copy()
df3

# 更改索引名称
df3.rename({'鲁班': "Mr Lu"})  # 默认更改行索引
df3.rename({'Python': 'PYTHON'}, axis=1)  # 更改列索引

df3.rename(index={'鲁班': "Mr Lu"})  # 更改行索引
df3.rename(columns={'Python': 'PYTHON'})  # 更改列索引
```

###### 4) apply()函数：既支持 Series，也支持 DataFrame

```python
df = pd.DataFrame(data=np.random.randint(0, 10, size=(5,3)),
                  index=list('ABCDE'),
                  columns=['Python', 'NumPy', 'Pandas'])

# 用于Series，其中x是Series中元素
df['Python'].apply(lambda x:True if x >5 else False) 

# 用于DataFrame，其中的x是DataFrame中列或者行，是Series
df.apply(lambda x : x.median(), axis=0)  # 列的中位数
df.apply(lambda x : x.median(), axis=1)  # 行的中位数

# 自定义方法
def convert(x): 
    return (np.round(x.mean(), 1), x.count())
df.apply(convert, axis=1)  # 行平均值，计数

# applymap: DataFrame专有, 其中的x是DataFrame中每个元素
df.applymap(lambda x : x + 100) # 计算DataFrame中每个元素
```

###### 5) transform()函数

```python
df = pd.DataFrame(data=np.random.randint(0, 10, size=(10,3)),
                  index=list('ABCDEFHIJK'),
                  columns=['Python', 'NumPy', 'Pandas'])
                  
# 1、一列执行多项计算
df['Python'].transform([np.sqrt, np.exp]) # Series处理

# 2、多列执行不同计算
def convert(x):
    if x.mean() > 5:
        x *= 10
    else:
        x *= -10
    return x

df.transform({'Python':convert,'NumPy':np.max,'Pandas':np.min}) 
```

##### 3. 异常值检测和过滤

- describe(): 查看每一列的描述性统计量

```python
# 查看每一列的描述性统计
df.describe()
df.describe([0.3, 0.4, 0.5, 0.9, 0.99])  # 指定百分位数
df.describe([0.3, 0.4, 0.5, 0.9, 0.99]).T  # 转置，行和列转换，在列比较多的情况下使用
```

- df.std() : 可以求得DataFrame对象每一列的标准差

```python
df.std()
```

- df.drop(): 删除特定索引 

```python
df4 = df.copy()
df4

df4.drop('鲁班')  # 默认删除行
df4.drop('Java', axis=1)  # 删除列

df4.drop(index='鲁班')  # 删除行
df4.drop(columns='H5')  # 删除列

df4.drop(columns=['Java', 'Pandas'])  # 同时删除多列
```

- unique() : 唯一,去重

```python
index = ['鲁班', '张三丰', '张无忌', '杜甫', '李白']
columns = ['Python', 'Java', 'H5', 'Pandas']
data = np.random.randint(0, 10, size=(5, 4))

df = pd.DataFrame(data=data, index=index, columns=columns)
df

# unique() : 要用于Series, 不能用于DataFrame
df['Python'].unique()
```

- query() : 按条件查询

```python
# ==, >, <, 
# in
# and &
# or  |

df.query('Python == 5')
df.query('Python > 5')

df.query('Python==5 and Java==5')
df.query('Python==5 & Java==5')
df.query('Python==5 or Java==6')
df.query('Python==5 | Java==6')

# 使用变量
n = 5
df.query('Python > @n')  # @n 使用变量
df.query('Python in [3, 4, 5, 6]')
m = [3, 4, 5, 6]
df.query('Python in @m')
```

- df.sort_values(): 根据值排序

- df.sort_index(): 根据索引排序

```python
index = ['鲁班', '张三丰', '张无忌', '杜甫', '李白']
columns = ['Python', 'Java', 'H5', 'Pandas']
data = np.random.randint(0, 100, size=(5, 4))

df = pd.DataFrame(data=data, index=index, columns=columns)
df

df.sort_values('Python')  # 默认按照列名排序，默认升序
df.sort_values('Python', ascending=False)    # 降序
df.sort_values('鲁班', axis=1)  

# 按照行索引或列索引排序
df.sort_index(ascending=True, axis=1)
```

- df.info(): 查看数据信息

```python
df.info()
```

练习:

新建一个形状为10000*3的标准正态分布的DataFrame，去除掉所有满足以下情况的行：

- 其中任一元素绝对值大于3倍标准差

```python
df = pd.DataFrame(np.random.randn(10000, 3))
df.head()

# 标准差
df.std()
# 绝对值
df.abs()

# cond: 找到大于3倍标准差的值
cond = df.abs() > df.std() * 3
# cond.sum()
cond

# 找到有True（大于3倍标准差的值）的行
cond2 = cond.any(axis=1)
cond2

# 去除大于3倍标准差的值，取不满足大于3倍标准差的值
df.loc[~cond2]
```

##### 4. 抽样

- 使用.take()函数排序

- 可以借助np.random.permutation()函数随机排序

```python
# 使用前面的df2
df2.take([4, 1, 2, 3, 0])   # 行排列
df2.take([1, 0, 2, 3, 4, 5, 6], axis=1)  # 列排列

# 随机排序
np.random.permutation([0, 1, 2, 3, 4, 5])

# 无放回抽样：依次拿取，没有重复值
df2.take(np.random.permutation([0, 1, 2, 3, 4]))

# 有放回抽样： 可能出现重复值
# 当DataFrame规模足够大时，直接使用np.random.randint()函数，就配合take()函数实现随机抽样
np.random.randint(0, 10, size=10)
df2.take(np.random.randint(0, 5, size=5))
```



#### 八、Pandas数学函数

- 聚合函数

```python
df = pd.DataFrame(data=np.random.randint(0,100,size = (20,3)))

df.count() # 非空值的数量
df.max() # 最大值，axis=0/1
df.min() # 最小值, axis=0/1
df.median() # 中位数
df.sum() # 求和
df.mean(axis=1) # 每一行的平均值

df[0].value_counts() # 统计元素出现次数
df.cumsum() # 累加
df.cumprod() # 累乘

# 方差: 当数据分布比较分散（即数据在平均数附近波动较大）时，各个数据与平均数的差的平方和较大，方差就较大；当数据分布比较集中时，各个数据与平均数的差的平方和较小。因此方差越大，数据的波动越大；方差越小，数据的波动就越小
df.var() # 方差

# 标准差 = 方差的算术平方根
df.std() # 标准差
```

- 其他数学函数
  - 协方差
        - 两组数值中每对变量的偏差乘积的平均值 
        - 协方差>0 : 表式两组变量正相关
             - 如果两个变量的变化趋势一致，也就是说如果其中一个大于自身的期望值时另外一个也大于自身的期望值，那么两个变量之间的协方差就是正值；
        - 协方差<0 : 表式两组变量负相关
            - 如果两个变量的变化趋势相反，即其中一个变量大于自身的期望值时另外一个却小于自身的期望值，那么两个变量之间的协方差就是负值。
        - 协方差=0 : 表式两组变量不相关
     - 相关系数
          - 相关系数r = X与Y的协方差 / (X的标准差 * Y的标准差)
          - 相关系数值的范围在-1和+1之间
          - r＞0为正相关，r＜0为负相关。r＝0表示不相关
          - r 的绝对值越大，相关程度越高
          - 两个变量之间的相关程度，一般划分为四级：
            - 如两者呈正相关，r呈正值，r=1时为完全正相关；
            - 如两者呈负相关则r呈负值，而r=-1时为完全负相关，完全正相关或负相关时，所有图点都在直线回归线上；点分布在直线回归线上下越离散，r的绝对值越小。
            - 相关系数的绝对值越接近1，相关越密切；越接近于0，相关越不密切。
            - 当r=0时，说明X和Y两个变量之间无直线关系。
            - 通常｜r｜大于0.8时，认为两个变量有很强的线性相关性。

```python
# 协方差
#   两组数值中每对变量的偏差乘积的平均值

df.cov() 
df[0].cov(df[1])  # 第0列 和 第1列的协方差

# 相关系数 = X与Y的协方差 / (X的标准差 * Y的标准差)
df.corr() # 所有属性相关性系数
df.corrwith(df[2]) # 单一属性相关性系数
```

协方差： $Cov(X,Y) = \frac{\sum\limits_1^n(X_i - \overline{X})(Y_i - \overline{Y})}{n-1}$

相关性系数：$r(X,Y) = \frac{Cov(X,Y)}{\sqrt{Var[X]*Var[Y]}}$



#### 九、 数据分组聚合

数据聚合是数据处理的最后一步，通常是要使每一个数组生成一个单一的数值。

##### 分组

数据聚合处理：

- 分组：先把数据分为几组
- 用函数处理：为不同组的数据应用不同的函数以转换数据
- 合并：把不同组得到的结果合并起来

数据分类处理的核心： groupby()函数

```python
# 创建DataFrame
df = pd.DataFrame(
    {
        'color': ['green', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow'],
        'price': [4, 5, 3, 2, 7, 8, 9]
    }
)
df

# 使用.groups属性查看各行的分组情况：
# 根据color进行分组
df.groupby(by='color')
df.groupby(by='color').groups

# 分组 + 聚合
df.groupby(by='color').sum()
```

##### 分组聚合练习：

假设菜市场张大妈在卖菜，有以下属性：

- 菜品(item)：萝卜，白菜，辣椒，冬瓜

- 颜色(color)：白，青，红

- 重量(weight)

- 价格(price)

1. 要求以属性作为列索引，新建一个ddd
2. 对ddd进行聚合操作，求出颜色为白色的价格总和
3. 对ddd进行聚合操作，求出萝卜的所有重量以及平均价格
4. 使用merge合并总重量及平均价格

```python
ddd = pd.DataFrame(
    data={
        "item": ["萝卜","白菜","辣椒","冬瓜","萝卜","白菜","辣椒","冬瓜"],
        'color':["白","青","红","白","青","红","白","青"],
        'weight': [10,20,10,10,30,40,50,60],
        'price': [0.99, 1.99, 2.99, 3.99, 4, 5, 6,7]
    }
)
ddd

# 2. 对ddd进行聚合操作，求出颜色为白色的价格总和
ddd.groupby('color')['price'].sum()  # Series
ddd.groupby('color')[['price']].sum()  # DataFrame
ddd.groupby('color')[['price']].sum() .loc[['白']]

# 3. 对ddd进行聚合操作，求出萝卜的所有重量以及平均价格
df1 = ddd.groupby('item')[['weight']].sum()
df2= ddd.groupby('item')[['price']].mean()

# 4.使用merge合并总重量及平均价格
# display(df1, df2)
df1.merge(df2, left_index=True, right_index=True)
```



#### 十、Pandas加载数据

##### csv数据

```python
data = np.random.randint(0,50,size=(10,5))
df = pd.DataFrame(data=data, columns=['Python','Java','Go','C','JS'])


# 保存到csv
df.to_csv('data.csv',
          sep=',',  # 文本分隔符，默认是逗号
          header=True, # 是否保存列索引
          # 是否保存行索引，保存行索引，文件被加载时，默认行索引会作为一列
          index=True)  
         
# 加载csv数据
pd.read_csv('data.csv',
            sep=',', # 默认是逗号
            header=[0], # 指定列索引
            index_col=0)  # 指定行索引

pd.read_table('data.csv', # 和read_csv类似，读取限定分隔符的文本文件
            sep=',',
            header=[0], # 指定列索引
            index_col=0  # 指定行索引
             ) 
```

##### excel数据

```python
data = np.random.randint(0, 50, size=(10,5))
df = pd.pDataFrame(data=data, columns=['Python','Java','Go','C','JS'])

# 保存到excel文件
df.to_excel('data.xls',
            sheet_name='sheet1',# Excel中工作表的名字
            header=True, # 是否保存列索引
            index=False) # 是否保存行索引

# 读取excel
pd.read_excel('data.xls',
              sheet_name=0, # 读取哪一个Excel中工作表，默认第一个, 也可以写工作表名称
              header=0, # 使用第一行数据作为列索引
              names=list('ABCDE'), # 替换行索引
              index_col=1) # 指定行索引，B作为行索引
```

##### MySQL数据

- 需要安装pymysql
  - pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
- 需要安装sqlalchemy: 
  - pip install sqlalchemy -i https://pypi.tuna.tsinghua.edu.cn/simple
  - sqlalchemy是Python语言下的数据库引擎库, 在Django/Flask中常用ORM库

```python
from sqlalchemy import create_engine

data = np.random.randint(0,150,size=(150,3))
df = pd.DataFrame(data=data, columns=['Python','Pandas','PyTorch'])

# 数据库连接
# root: MySQL用户名
# 123456: MySQL密码
# localhost: 本机
# db: 数据库名(提前创建)
conn = create_engine('mysql+pymysql://root:123456@localhost/db')

# 保存到MySQL
df.to_sql('score', # 表名(会自动创建表)
          conn, # 数据库连接
          index=False,  # 是否保存行索引
          if_exists='append') # 如果表名存在，追加数据

# 从MySQL中加载数据
pd.read_sql('select * from score', # sql查询语句
            conn, # 数据库连接
            index_col='Python') # 指定行索引名
```

#### 十一、Pandas分箱操作

- 分箱操作就是将连续型数据离散化。
- 分箱操作分为等距分箱和等频分箱。 

```python
data = np.random.randint(0,150,size=(150,3))
df = pd.DataFrame(data=data, columns=['Python','Pandas','PyTorch'])

# 对Python列进行分箱
df.Python.values

# 1、等宽分箱
pd.cut(df.Python, bins=4)

# 指定宽度分箱
pd.cut(df.Python, # 分箱数据
       bins=[0, 30, 60, 80, 100], # 分箱断点
       right=False, # 左闭右开
       labels=['D','C','B','A']) # 分箱后分类标签

# 2、等频分箱
pd.qcut(df.Python, # 分箱数据
        q=4, # 4等份
        labels=['差', '中', '良', '优']) # 分箱后分类标签
```

#### 十二、Pandas绘图

- Series和DataFrame都有一个用于生成各类图表的plot方法
- Pandas的绘图是基于Matplotlib， 可以快速实现基本图形的绘制，复杂的图形还是需要用Matplotlib

常见可视化图形:

- 折线图
- 条形图/柱形图
- 饼图
- 散点图
- 箱型图
- 面积图
- 直方图

##### 1、折线图

```python
# 折线图
# Series画图
s = pd.Series([100, 200, 300, 200, 150, 400, 250])
s.plot()

# sin曲线：正弦曲线
x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
s = pd.Series(data=y, index=x)
s.plot()

# DataFrame画图
data = np.random.randint(50, 100, size=(5, 6))
index = ['1st', '2nd', '3th', '4th', '5th']
columns = ['Jeff', 'Jack', 'Rose', 'Lucy', 'Lily', 'Bob']
df = pd.DataFrame(data=data, index=index, columns=columns)
df.plot()  # 一列一根线
```

##### 2、条形图/柱形图

```python
# 条形图/柱形图
df = pd.DataFrame(data=np.random.rand(10,4))
df.plot.bar(stacked=True) # stacked 是否堆叠

# Series画图
# 可以使用plot中的kind属性来绘制不同图形
s = pd.Series(data=[100, 110, 130, 200])
s.index = ['Jeff', "千锋", 'Python', 'Rose']
s.plot(kind='bar')   # 柱状图
# 或
s.plot(kind='barh')   # 条形图
# kind:
#     - 'line' : line plot (default)
#     - 'bar' : vertical bar plot
#     - 'barh' : horizontal bar plot
#     - 'hist' : histogram
#     - 'box' : boxplot
#     - 'kde' : Kernel Density Estimation plot
#     - 'density' : same as 'kde'
#     - 'area' : area plot
#     - 'pie' : pie plot
#     - 'scatter' : scatter plot
#     - 'hexbin' : hexbin plot.

# DataFrame画图
data = np.random.randint(0, 100, size=(4, 3))
index = list('ABCD')
columns = ['Python', 'C', 'Java']

df = pd.DataFrame(data=data, index=index, columns=columns)
df.plot(kind='bar')
# 或
df.plot(kind='barh')
```

##### 3、饼图

```python
# 饼图
df = pd.DataFrame(data=np.random.rand(4,2),
                   index=list('ABCD'),
                   columns=['Python','Java'])

# subplots=True 子图:同时画多个图
# autopct='%.1f%%' 显示占比,保留1位小数
df.plot.pie(subplots=True, figsize=(8,8), autopct='%.1f%%')
```

##### 4、散点图

- 散点图是观察两个一维数据数列之间的关系的有效方法,DataFrame对象可用

```python
# 散点图
data = np.random.normal(size=(1000, 2))
df = pd.DataFrame(data=data, columns=list('AB'))
df.head()

# scatter： 散点图
# x='A'  ：使用A列作为x轴
# y='B'  ：使用B列作为y轴
df.plot(kind='scatter', x='A', y='B')
# 或
df.plot.scatter(x='A', y='B')  # A和B关系绘制
```

#####  5、面积图

```python
# 面积图
df = pd.DataFrame(data=np.random.rand(10, 4), columns=list('ABCD'))
df.plot.area(stacked=True)  # stacked 是否堆叠
```

##### 6、箱型图

```python
# 箱型图
df = pd.DataFrame(data=np.random.rand(10, 5), columns=list('ABCDE'))
df.plot.box()
# 或
df.plot(kind='box')
```

##### 7、直方图

```python
# 直方图
df = pd.DataFrame({'A': np.random.randn(1000) + 1, 
                    'B': np.random.randn(1000),
                    'C': np.random.randn(1000) - 1})
df.plot.hist(alpha=0.5) # 带透明度直方图
df.plot.hist(stacked=True)  # 堆叠图
# 或
df['A'].plot(kind='hist')
df.plot(kind='hist')
```

# Matplotlib数据可视化

####   强大的数据分析可视化工具

#### 一、 Matplotlib介绍

##### 安装

- anaconda环境: 
  - 自带matplotlib, 无需另外安装

- 其他Python环境: 
  - pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

##### 课程介绍

- Matplotlib 是 Python 中最受欢迎的数据可视化软件包之一，支持跨平台运行，它是 Python 常用的 2D 绘图库，同时它也提供了一部分 3D 绘图接口, Matplotlib 通常与 NumPy、Pandas 一起使用，是数据分析中不可或缺的重要工具之一

- 在数据分析和机器学习中, 我们经常要用到大量的可视化操作, 一张制作精美的图片, 可以直观展示数据信息, 字不如表, 表不如图, 一图胜千言.

- 通过 Matplotlib, 我们可以仅需要几行代码，便可以生成图表，直方图，条形图，箱型图，散点图等

- Matplotlib官方网站: https://matplotlib.org/

- 导包

  ```python
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  ```

  

#### 二、Matplotlib基本图形绘制

##### 导包

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

##### 配置

```python
# 运行时配置参数
# rcParams : runtime configuration Parameters

# 如果浏览器不显示图片，就需要加上这句话
%matplotlib inline  

# 让图片中可以显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'   
# 让图片中可以显示负号
plt.rcParams['axes.unicode_minus'] = False  

# 支持svg矢量图
%config Inlinebackend.figure_format = 'svg'  

# 查看自己电脑上的字体库
from matplotlib.font_manager import FontManager
fm = FontManager()
my_fonts = set(f.name for f in fm.ttflist)
my_fonts
```



##### 绘制基本图形

- plt.plot()

![](/images/2-1.png) 

##### 

```python
# 绘制抛物线
x = np.linspace(-5, 5, 50)
y =  x**2

# 画线形图
plt.plot(x, y)
```

##### 样式和颜色

- 样式： '-'，'--'，'-.'，':'，'.'，','，，o，^，v，<，>，s，+，x，D，d，1，2，3，4，h，H，p，| ，_

- 颜色： b(蓝色)，g(绿色)，r(红色)，c(青色)，m(品红)，y(黄色)，k(黑色)，w(白色)

![](/images/2-2.png)

```python
# 绘制抛物线
x = np.linspace(-5, 5, 50)
y =  x**2
plt.plot(x, y, 'r--')
```

##### 画布配置

- plt.figure()

![](/images/2-3.png)

```python
# 画布配置
# figsize: 画布大小，宽高
# dpi ：分辨率
# facecolor: 背景颜色
fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#11aa11')

# 绘制正弦曲线
x = np.linspace(0, 2*np.pi) 
y = np.sin(x)   
plt.plot(x,y)

# 设置网格线
plt.grid() 
```

##### 在一个画布上绘制多个图

![](/images/2-4.png)

```python
x = np.linspace(0, 8) 

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x), 'r')
plt.plot(x, -np.sin(x), 'g--')
```

##### 立刻显示图片 

- show

![](/images/2-5.png)

```python
x = np.linspace(0, 8) 
plt.plot(x, np.sin(x))
plt.show() 

plt.plot(x, np.cos(x), 'r')
plt.plot(x, -np.sin(x), 'g--')
```



#### 三、Matplotlib多图布局

- 均匀分布
  - subplot()函数:

![](/images/3-1.png)

```python
# 2行2列
fig = plt.figure(figsize=(8, 5))

x = np.linspace(-np.pi, np.pi, 30)
y = np.sin(x)

# 子图1
axes1 = plt.subplot(221)  # 2行2列的第1个子视图
axes1.plot(x, y)
axes1.set_title('子图1')

# 子图2
axes2 = plt.subplot(222)  # 2行2列的第2个子视图
axes2.plot(x, y)
axes2.set_title('子图2')

# 子图3
axes3 = plt.subplot(2, 2, 3)  # 2行2列的第3个子视图
axes3.plot(x, y)
axes3.set_title('子图3')

# 子图4
axes4 = plt.subplot(2, 2, 4)  # 2行2列的第4个子视图
axes4.plot(x, y)
axes4.set_title('子图4')

# 自动调整布局
fig.tight_layout()
```

- 不均匀分布
  - subplot()函数 

![](/images/3-2.png)

```python
plt.figure(figsize=(8, 5))

x = np.linspace(-np.pi, np.pi, 30)
y = np.sin(x)

# 子图1
axes1 = plt.subplot(2, 2, 1)  
axes1.plot(x, y, color='red')

# 子图2
axes2 = plt.subplot(2, 2, 2)
lines = axes2.plot(x, y)
lines[0].set_marker('*')   # 点的样式

# 子图3
axes3 = plt.subplot(2, 1, 2)  # 2行1列的第2行
axes3.plot(x, np.sin(x*x))
```

- 图形嵌套 
  - add_subplot()函数 

![](/images/3-3.png)

```python
fig = plt.figure(figsize=(8, 5))

# 使用 add_subplot() 函数
# 图1
axes1 = fig.add_subplot(1, 1, 1)
axes1.plot([1, 3])

# 图2
axes2 = fig.add_subplot(2, 2, 1, facecolor='pink')
axes2.plot([1, 3])
```

- 图形嵌套 
  - 使用 axes() 函数
  - 使用 add_axes() 函数

![](/images/3-4.png)

```python
fig = plt.figure(figsize=(8, 5)) 

# 图1
x = np.linspace(0, 2*np.pi, 30)
y = np.sin(x)
plt.plot(x, y)

# 图2
# [left, bottom, width, height]
axes1 = plt.axes([0.55, 0.55, 0.3, 0.3])  
axes1.plot(x, y, color='g')

# 图3
axes2 = fig.add_axes([0.2, 0.2, 0.25, 0.25]) 
axes2.plot(x, y, color='r')
```

- 均匀布局
  - 使用 subplots() 函数

![](/images/3-5.png)

```python
x = np.linspace(0, 2*np.pi)

# 3行3列
# subplots：一次性返回9个子图
fig, ax = plt.subplots(3, 3)
ax1, ax2, ax3 = ax
ax11, ax12, ax13 = ax1
ax21, ax22, ax23 = ax2
ax31, ax32, ax33 = ax3

# fig来设置画布大小
fig.set_figwidth(8)
fig.set_figheight(5)

ax11.plot(x, np.sin(x))
ax12.plot(x, np.cos(x))
ax13.plot(x, np.tanh(x))
ax21.plot(x, np.tan(x))
ax22.plot(x, np.cosh(x))
ax23.plot(x, np.sinh(x))
ax31.plot(x, np.sin(x) + np.cos(x))
ax32.plot(x, np.sin(x*x) + np.cos(x*x))
ax33.plot(x, np.sin(x)*np.cos(x))

# 自动调整布局
plt.tight_layout()
plt.show()
```

- 双轴显示

![](/images/3-6.png)

```python
plt.figure(figsize=(8, 5))

x = np.linspace(0, 10, 100)

# 图1
axes1 = plt.gca()  # 获取当前轴域
axes1.plot(x, np.exp(x), color='red') 

axes1.set_xlabel('time')  
axes1.set_ylabel('exp', color='red')
axes1.tick_params(axis='y', labelcolor='red') 

# 图2
axes2 = axes1.twinx()  # 和图1共享x轴
axes2.set_ylabel('sin', color='blue')
axes2.plot(x, np.sin(x), color='blue')
axes2.tick_params(axis='y', labelcolor='blue')

plt.tight_layout() 
```



#### 四、Matplotlib绘图属性设置

- 常用函数：

  | Pyplot函数  |           API方法            |              描述              |
  | :---------: | :--------------------------: | :----------------------------: |
  |   text()    |     mpl.axes.Axes.text()     |  在Axes对象的任意位置添加文字  |
  |  xlabel()   |  mpl.axes.Axes.set_xlabel()  |         为X轴添加标签          |
  |  ylabel()   |  mpl.axes.Axes.set_ylabel()  |         为Y轴添加标签          |
  |   title()   |  mpl.axes.Axes.set_title()   |       为Axes对象添加标题       |
  |  legend()   |    mpl.axes.Axes.legend()    |       为Axes对象添加图例       |
  | annnotate() |   mpl.axes.Axes.annotate()   | 为Axes对象添加注释（箭头可选） |
  | suptitle()  | mpl.figure.Figure.suptitle() |  为Figure对象添加中心化的标题  |

- 图例

  - legend()

![](/images/4-1.png)

```python
# 图形绘制
fig = plt.figure(figsize=(8, 5))

x = np.linspace(0, 2*np.pi) 
plt.plot(x, np.sin(x) )  # 正弦曲线
plt.plot(x, np.cos(x))  # 余弦曲线

# 图例
plt.legend(['Sin','Cos'], 
           fontsize=18,
           loc='center',  # 居中
           ncol=2,  # 显示成几列
           bbox_to_anchor=[0, 1.05, 1, 0.2]  # 图例的位置
          )
```

#####  线条属性

- color 颜色
- linestyle 样式
- linewidth 宽度
- alpha 透明度
- marker 标记

- mfc: marker face color 标记的背景颜色

![](/images/4-2.png)

```python
fig = plt.figure(figsize=(8, 5))
x = np.linspace(0, 2*np.pi, 20)
y1 = np.sin(x)
y2 = np.cos(x)

# c : color 线颜色
# marker: 标记的样式或点的样式
# mfc: marker face color 标记的背景颜色
# ls : line style 线的样式
# lw: line width 线的宽度
# label: 线标签（图例中显示）
plt.plot(x, y1, c='r', marker='o', ls='--', lw=1, label='sinx', mfc='y', )

plt.plot(x, y2, c='b', marker='*', ls='-', lw=2, label='cosx', mfc='g', )

plt.plot(x, y1-y2, c='y', marker='^', ls='-', lw=3, label='sinx-cosx', mfc='b', alpha=0.5)

plt.plot(x, y1+y2, c='orange', marker='>', ls='-.', lw=4, label='sinx+cosx', 
         mfc='y', 
         markersize=10,  # 点大小
         markeredgecolor='green',  #点边缘颜色
         markeredgewidth=2  # 点边缘宽度
        )

# 图例
plt.legend()
```

```python
# **Line Styles**
# =============    ===============================
# character        description
# =============    ===============================
# ``'-'``          solid line style
# ``'--'``         dashed line style
# ``'-.'``         dash-dot line style
# ``':'``          dotted line style
# =============    ===============================

# **Colors**
# The supported color abbreviations are the single letter codes
# =============    ===============================
# character        color
# =============    ===============================
# ``'b'``          blue
# ``'g'``          green
# ``'r'``          red
# ``'c'``          cyan
# ``'m'``          magenta
# ``'y'``          yellow
# ``'k'``          black
# ``'w'``          white
# =============    ===============================

# **Markers**
# =============   ===============================
# character       description
# =============   ===============================
# ``'.'``         point marker
# ``','``         pixel marker
# ``'o'``         circle marker
# ``'v'``         triangle_down marker
# ``'^'``         triangle_up marker
# ``'<'``         triangle_left marker
# ``'>'``         triangle_right marker
# ``'1'``         tri_down marker
# ``'2'``         tri_up marker
# ``'3'``         tri_left marker
# ``'4'``         tri_right marker
# ``'8'``         octagon marker
# ``'s'``         square marker
# ``'p'``         pentagon marker
# ``'P'``         plus (filled) marker
# ``'*'``         star marker
# ``'h'``         hexagon1 marker
# ``'H'``         hexagon2 marker
# ``'+'``         plus marker
# ``'x'``         x marker
# ``'X'``         x (filled) marker
# ``'D'``         diamond marker
# ``'d'``         thin_diamond marker
# ``'|'``         vline marker
# ``'_'``         hline marker
# =============   ===============================
```

##### 坐标轴刻度

- xticks
- yticks

![](/images/4-3.png)

```python
# 图形绘制
x = np.linspace(0, 10) 
y = np.sin(x)   
plt.plot(x,y)

# 设置x轴y轴刻度
plt.xticks(np.arange(0, 11, 1))
plt.yticks([-1, 0, 1])
plt.show()
```

![](/images/4-4.png)

```python
# 图形绘制
x = np.linspace(0, 10) 
y = np.sin(x)   
plt.plot(x,y)

# 设置x轴y轴刻度标签
plt.yticks(ticks=[-1, 0, 1],    # 刻度值
               labels=['min', '0', 'max'],  # 刻度值对应的标签名（显示）
               fontsize=20,   # 文字大小
               ha='right',  # 水平对齐方式
               color='blue'  # 颜色
          )
plt.xticks(ticks=np.arange(0, 11, 1), fontsize=20, color='red' )
plt.show()
```

##### 坐标轴范围[¶](http://localhost:8888/notebooks/资料/代码/03_Matplotlib绘图属性设置.ipynb#坐标轴范围)

- xlim
- ylim

![](/images/4-5.png)

```python
# sin曲线
x = np.linspace(0, 2*np.pi)
y = np.sin(x)
plt.plot(x, y, c='r')

# 设置x轴范围
plt.xlim(-2, 8)

# # 设置 y轴范围
plt.ylim(-2, 2)
```

##### 坐标轴配置

- axis

![](/images/4-6.png)

```python
# sin曲线
x = np.linspace(0, 2*np.pi)
y = np.sin(x)
plt.plot(x, y, c='r')

# 坐标轴范围：[xmin, xmax, ymin, ymax]
plt.axis([-2, 8, -2, 2])

# 选项
# off ： 不显示坐标轴
# equal: 让x轴和y轴 刻度距离相等
# scaled：自动缩放坐标轴和图片适配
# tight：紧凑型自动适配图片
# square：x轴和y轴宽高相同
plt.axis('square')

plt.show()
```



##### 标题 和 网格

- title
- grid

![](/images/4-7.png)

```python
# 图形绘制
x = np.linspace(0, 10) 
y = np.sin(x)   
plt.plot(x, y)

# 图的标题
# fontsize : 标题大小
# loc：标题位置
plt.title('sin曲线', fontsize=20, loc='center')
# 父标题
plt.suptitle('父标题', 
             y=1.1,  # 位置
             fontsize=30 #文字大小
            )  

# 网格线
# ls: line style 网格线样式
# lw：line width  网格线宽度
# c: color 网格线颜色
# axis：画哪个轴的网格线，默认x轴和y轴都画
plt.grid(ls='--', lw=0.5, c='gray', axis='y')

plt.show()
```

##### 标签

- xlabel
- ylabel

![](/images/4-8.png)

```python
# 图形绘制
x = np.linspace(0, 10) 
y = np.sin(x)   
plt.plot(x, y)

# 坐标轴标签
plt.xlabel('y=sin(x)', 
               fontsize=20,   # 文字大小
               rotation=0,  # 旋转角度
          )
plt.ylabel('y=sin(x)', 
            rotation=90,  # 旋转角度
            horizontalalignment='right',   # 水平对齐方式
            fontsize=20 
          )

# 标题
plt.title('正弦曲线')
```

##### 文本

- text

![](/images/4-9.png)

```python
plt.figure(figsize=(8, 5))

x = np.linspace(0, 10, 10)
y = np.array([60, 30, 20, 90, 40, 60, 50, 80, 70, 30])
plt.plot(x, y, ls='--', marker='o')

# 文字
for a, b in zip(x, y):
    # 画文本
    plt.text(
            x=a+0.3,  # x坐标
            y=b+0.5,  # y坐标
            s=b,  # 文字内容
            ha='center',  # 水平居中
            va='center',   # 垂直居中
            fontsize=14,  # 文字大小
            color='r'  # 文字颜色
    )
    
plt.show()
```

##### 注释

- annotate 

![](/images/4-10.png)

```python
plt.figure(figsize=(8, 5))

x = np.linspace(0, 10, 10)
y = np.array([60, 30, 20, 90, 40, 60, 50, 80, 70, 30])
plt.plot(x, y, ls='--', marker='o')

# 注释（标注）
plt.annotate(
    text='最高销量',  # 标注的内容
    xy=(3, 90),  # 标注的坐标点
    xytext=(1, 80),  # 标注的内容的坐标点
    # 箭头样式
    arrowprops={
                'width': 2,   # 箭头线的宽度 
                'headwidth': 8,  # 箭头头部的宽度
                'facecolor': 'blue'  # 箭头的背景颜色
    }
)
```

##### 保存图片

- savefig 

![](/images/4-11.png)

```python
# 图形绘制
f = plt.figure(figsize=(8, 5))

x = np.linspace(0, 2*np.pi) 
plt.plot(x, np.sin(x) )
plt.plot(x, np.cos(x)) 

f.savefig(
            fname='pic_name2.png',  # 文件名：png、jpg、pdf
            dpi=100,  # 保存图片像素密度
            facecolor='pink',  # 背景颜色
            edgecolor='lightgreen',  # 边界颜色
            bbox_inches='tight',  # 保存图片完整
            pad_inches=1  # 内边距
)  
```



#### 五、Matplotlib常用视图



##### 折线图

折线图（line chart）是我们日常工作、学习中经常使用的一种图表，它可以直观的反映数据的变化趋势

- 一次画一条线

![](/images/5-1.png)

```python
plt.figure(figsize=(8, 5))

x = ["Mon", "Tues", "Wed", "Thur", "Fri","Sat","Sun"]
y = [20, 40, 35, 55, 42, 80, 50]

plt.plot(x, y, c="g", marker='D', markersize=5)

#绘制坐标轴标签
plt.xlabel("星期")
plt.ylabel("活跃度")
plt.title("Python语言活跃度")

for x1, y1 in zip(x, y):
    plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=16)

plt.show()
```

- 一次画多条线

![](/images/5-2.png)

```python
plt.figure(figsize=(8, 5))

x = np.random.randint(0, 10, size=15)

plt.plot(x, marker='*', color='r')
plt.plot(x.cumsum(), marker='o')
```

- 统计各科成绩变化趋势

![](/images/5-3.png)

```python
df = pd.read_excel('data/plot.xlsx', sheet_name='line')
df.head()

x, y1, y2, y3 = df['月份'], df['语文'], df['数学'], df['英语']

# 画折线图
# 画布大小
plt.figure(figsize=(7, 4))

# ms: marker size 标记点的大小
# alpha: 透明度 0~1之间，1表式不透明，0表式完全透明
plt.plot(x, y1, label='语文', c='g', ls='--', marker='*', mfc='y', ms=10, alpha=0.5)
plt.plot(x, y2, label='数学', c='b', ls='-.', marker='o', mfc='w', ms=10)
plt.plot(x, y3, label='英语', c='r', ls=':', marker='+', mfc='w', ms=10, alpha=0.5)

plt.yticks(range(0, 110, 10))  # y轴的刻度
plt.ylabel('成绩')
plt.xlabel('月份')
plt.title('成绩的变化趋势')

plt.legend()  # 图例
plt.grid(axis='y')
plt.show()
```



##### 柱状图和条形图

柱状图是一种用矩形柱来表示数据分类的图表，柱状图可以垂直绘制，也可以水平绘制，它的高度与其所表示的数值成正比关系

- 简单柱状图

![](/images/5-4.png)

```python
fig = plt.figure(figsize=(8, 5))

x = ['语文', '数学',  '英语', 'Python', '化学']
y = [20, 10, 40, 60, 10]

plt.bar(x, y)
plt.show()
```

- 统计年销量数据可视化

![](/images/5-5.png)

```python
df = pd.read_excel('data/plot.xlsx', sheet_name='bar1')

x, y = df.年份, df.销售额

plt.figure(dpi=100)
plt.title('2014年-2020年销售额')
plt.xlabel('年份')
plt.ylabel('销售额')

# 柱形图
plt.bar(x, y, width=0.6)

# 给每个柱形图加上数字
for a, b in zip(x, y):
    plt.text(x=a, y=b+5e4, s='{:.1f}万'.format(b/10000), 
                ha='center', fontsize=9
            )
plt.show()
```

- 簇状柱形图

![](/images/5-6.png)

```python
df2 = pd.read_excel('data/plot.xlsx', sheet_name='bar2')
x, y1, y2, y3 = df2.年份,  df2.北区, df2.中区, df2.南区

plt.figure(dpi=100)
plt.title('2014年-2020年销售额')
plt.xlabel('年份')
plt.ylabel('销售额')

width=0.2
plt.bar(x-width, y1, width=width, label='北区')
plt.bar(x, y2, width=width, label='中区')
plt.bar(x+width, y3, width=width, label='南区')

plt.legend()
plt.show()
```

- 堆叠柱形图 

![](/images/5-7.png)

```python
plt.figure(dpi=100)
plt.title('2014年-2020年销售额')
plt.xlabel('年份')
plt.ylabel('销售额')

plt.bar(x, y1, label='北区')
plt.bar(x, y2, label='中区', bottom=y1)  # 画图的时候y轴的底部起始值
plt.bar(x, y3, label='南区', bottom=y1+y2)

plt.legend()
plt.show()
```

- 条形图 

![](/images/5-8.png)

```python
# 条形图
plt.barh(x, y1)
```



##### 直方图

直方图（Histogram），又称质量分布图，它是一种条形图的一种，由一系列高度不等的纵向线段来表示数据分布的情况。 直方图的横轴表示数据类型，纵轴表示分布情况。

直方图用于概率分布，它显示了一组数值序列在给定的数值范围内出现的概率；而柱状图则用于展示各个类别的频数。

- 简单的直方图

![](/images/5-9.png)

```python
x = np.random.randint(0, 10, 100)
pd.Series(x).value_counts()
# 直方图
# bins: 组数
plt.hist(x, bins=5)
plt.hist(x, bins=[0, 3, 6, 9, 10])
```

- 学生成绩分布情况

![](/images/5-10.png)

```python
df = pd.read_excel('data/plot.xlsx', sheet_name='hist')
x = df['分数']

x.min(), x.max()

# 直方图
# edgecolor: 边缘颜色
plt.hist(x, bins=range(40, 110, 6), facecolor='b', edgecolor='k', alpha=0.4)

plt.show()
```



##### 箱型图

箱型图（也称为盒须图）它能显示出一组数据的最大值、最小值、中位数、及上下四分位数。

![](/images/5-11-1.png)

- 箱型图 

![](/images/5-11.png)

```python
x = [1, 2, 3, 5, 7, 9, -10]

# 箱型图
plt.boxplot(x)
plt.show()

# 最大值
# 3/4
# 中位数
# 1/4
# 最小值

# 异常值
```

- 一次画多个箱型图 

![](/images/5-12.png)

```python
x1 = np.random.randint(10, 100, 100)
x2 = np.random.randint(10, 100, 100)
x3 = np.random.randint(10, 100, 100)

plt.boxplot([x1, x2, x3])
plt.show()
```

- 箱型图样式 

![](/images/5-13.png)

```python
data=np.random.normal(size=(500, 4)) 
lables = ['A','B','C','D']

# 画图
plt.boxplot(data, 
            notch=True,   # 箱型图样式
            sym='go',  # 颜色+marker样式
            labels=lables  # x轴标签
)  
plt.show()
```



##### 散点图

散点图用于在水平轴和垂直轴上绘制数据点，它表示了因变量随自变量变化的趋势。通俗地讲，它反映的是一个变量受另一个变量的影响程度

- 散点图 

![](/images/5-14.png)

```python
x = range(1, 7, 1)
y = range(10, 70, 10)

# 散点图
plt.scatter(x, y, marker='o')
```

- 气泡图 

![](/images/5-15.png)

```python
data = np.random.randn(100, 2)
s = np.random.randint(50, 200, size=100)
color = np.random.randn(100)

plt.scatter(
            data[:, 0],  # x坐标
            data[:, 1],  # y坐标
            s=s,  # 尺寸
            c=color,  # 颜色
            alpha=0.6  # 透明度
) 
```

- 广告费用与销售收入之间的关系分析 

![](/images/5-16.png)

```python
df = pd.read_excel('data/plot.xlsx', sheet_name='scatter')
x, y = df['广告费用'], df['销售收入']

plt.figure(dpi=100)
plt.scatter(x, y)

plt.title('广告费用和销售收入之间的关系')
plt.xlabel('广告费用')
plt.ylabel('销售收入')
```

- 六边形图

![](/images/5-17.png)

```python
plt.figure(dpi=100)

# 六边形图
# gridsize: 网格大小
# cmap: color map 颜色映射
#      rainbow: 彩虹色
plt.hexbin(x, y, gridsize=20, cmap="rainbow")

plt.title('广告费用和销售收入之间的关系')
plt.xlabel('广告费用')
plt.ylabel('销售收入')
```

#### 

##### 饼图

饼状图用来显示一个数据系列，具体来说，饼状图显示一个数据系列中各项目的占项目总和的百分比。

- 饼图

![](/images/5-18.png)

```python
x = [10, 20, 30, 40]

plt.pie(x, autopct='%.1f%%')
plt.show()
```

- 各省份销量占比

![](/images/5-19.png)

```python
df = pd.read_excel('data/plot.xlsx', sheet_name='pie1')
citys, values = df.省份, df.销量

# 饼图
plt.figure(figsize=(5, 5))
plt.pie(
            x=values,   # 值
            autopct='%.1f%%',  # 百分比
            labels=citys,  # 标签
            pctdistance=0.8,  # 百分比文字的位置
            explode=[0, 0, 0, 0.1, 0, 0.1, 0, 0, 0, 0],  # 分裂效果
            # 字体样式
            textprops={'fontsize': 12, 'color': 'blue'},
            shadow=True
       )

plt.show()
```

- 单个圆环: 甜甜圈

![](/images/5-20.png)

```python
# 饼图
plt.pie(
            x=values,   # 值
            autopct='%.1f%%',  # 百分比
            labels=citys,  # 标签
            pctdistance=0.8,  # 百分比文字的位置
            # 字体样式
            textprops={'fontsize': 10, 'color': 'k'},
            
            # 甜甜圈设置
            wedgeprops={'width': 0.4, 'edgecolor': 'w'}
       )

plt.show()
```

- 多个圆环

![](/images/5-21.png)

```python
df1 = pd.read_excel('data/plot.xlsx', sheet_name='pie1')
df2 = pd.read_excel('data/plot.xlsx', sheet_name='pie2')

citys1, values1 = df1.省份, df1.销量
citys2, values2 = df2.省份, df2.销量

plt.figure(dpi=200)

# 饼图
plt.pie(
            x=values1,   # 值
            autopct='%.1f%%',  # 百分比
            labels=citys1,  # 标签
            pctdistance=0.8,  # 百分比文字的位置
            # 字体样式
            textprops={'fontsize': 10, 'color': 'k'},
            
            # 
            wedgeprops={'width': 0.4, 'edgecolor': 'w'}
       )

# 饼图
plt.pie(
            x=values2,   # 值
            autopct='%.1f%%',  # 百分比
           #  labels=citys2,  # 标签
            pctdistance=0.8,  # 百分比文字的位置
            # 字体样式
            textprops={'fontsize': 8, 'color': 'k'},
            # 半径 
            radius=0.6
       ) 

plt.legend(citys1, fontsize=3)

plt.show()
```



##### 面积图

面积图又称区域图，和折线图差不多，强调y轴随x轴而变化的程度，可用于引起人们对总值趋势的注意

- 面积图

![](/images/5-22.png)

```python
x = [1, 2, 3, 4, 5]
y = np.random.randint(10, 100, 5)

# 面积图
plt.stackplot(x, y)
```

- 销售额趋势

![](/images/5-23.png)

```python
df = pd.read_excel('data/plot.xlsx', sheet_name='stackplot1')
x, y = df['年份'], df['销售额']

plt.figure(dpi=100)
plt.stackplot(x, y)
plt.plot(x, y)
```



##### 热力图

热力图是一种通过对色块着色来显示数据的统计图表。绘图时，需指定颜色映射的规则。

- 热力图

![](/images/5-24.png)

```python
df = pd.read_excel('data/plot.xlsx', sheet_name='imshow')
data = df.drop(columns='省份').values
y = df['省份']
# x = df.columns[1:]
x = df.drop(columns='省份').columns

plt.figure(figsize=(14, 10))

# 热力图
plt.imshow(data, cmap='Blues')

# 设置坐标轴刻度
plt.xticks(range(len(x)), x)
plt.yticks(range(len(y)), y)

# 添加文字
for i in range(len(x)):
    for j in range(len(y)): 
        plt.text(x=i, y=j, s=data[j, i], 
                 ha='center', 
                 va='center',
                fontsize=12
                )
    
# 颜色条
plt.colorbar()
plt.show()
```

#### 

##### 极坐标图

极坐标系是一个二维坐标系统,该坐标系统中任意位置可由一个夹角和一段相对原点—极点的距离来表示

- 极坐标图

![](/images/5-25.png)

```python
N = 8  # 分成8份

x = np.linspace(0,  2*np.pi, N, endpoint=False)   # 360度等分成8份
height = np.random.randint(3, 15, size=N)  # 值

width = np.pi / 4  # 宽度
colors = np.random.rand(8, 3)  # 随机颜色

# polar表示极坐标
ax = plt.subplot(111,  projection='polar') 
ax.bar(x=x, height=height, width=width, bottom=0, color=colors)
plt.show()
```



##### 雷达图

雷达图是以从同一点开始的轴上表示的三个或更多个定量变量的二维图表的形式显示多变量数据的图形方法

- 雷达图

![](/images/5-26.png)

```python
fig = plt.figure(figsize=(6, 6))

x = np.linspace(0, 2*np.pi, 6, endpoint=False)
y = [83, 61, 95, 67, 76, 88]

# 保证首位相连
x = np.concatenate((x, [x[0]]))
y = np.concatenate((y, [y[0]]))

# 雷达图
axes = plt.subplot(111, polar=True)   

axes.plot(x, y, 'o-', linewidth=2)  # 连线
axes.fill(x, y, alpha=0.3)  # 填充

# 显示刻度
axes.set_rgrids([20, 40, 60, 80], fontsize=14)
plt.show()
```



##### 等高线图

- 等高线图：也称水平图，是一种在二维平面上显示 3D 图像的方法

![](/images/5-27.png)

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# 将上述数据变成网格数据形式
X, Y = np.meshgrid(x, y)

# 定义Z与X, Y之间的关系
Z = np.sqrt(X**2 + Y**2)

# 画等高线
cp = plt.contourf(X, Y, Z)
# 颜色柱
plt.colorbar(cp) 
plt.show()
```



#### 六、Matplotlib 3D图

- 三维折线图 

![](/images/6-1.png)

```python
# 3D引擎
from mpl_toolkits.mplot3d.axes3d import Axes3D 

fig = plt.figure(figsize=(8, 5))  

x = np.linspace(0, 100, 400)
y = np.sin(x)
z = np.cos(x)

# 三维折线图
axes = Axes3D(fig, auto_add_to_figure=False) 
fig.add_axes(axes)
axes.plot(x,y,z) 
```

- 三维散点图

![](D:/课件/images/6-2.png)

```python
from mpl_toolkits.mplot3d.axes3d import Axes3D 

fig = plt.figure(figsize=(8, 5))  

# 三维折线图
axes = Axes3D(fig, auto_add_to_figure=False) 
fig.add_axes(axes)

# 三维散点图
x = np.random.rand(50)  
y = np.random.rand(50)  
z = np.random.rand(50) 
axes.scatter(x, y, z, color='red', s=100)
```

- 三维柱形图

![](/images/6-3.png)

```python
from mpl_toolkits.mplot3d.axes3d import Axes3D 

fig = plt.figure(figsize=(8, 5))

# 二维变成了三维
axes = Axes3D(fig, auto_add_to_figure=False) 
fig.add_axes(axes)

x = np.arange(1, 5)

for m in x:
    axes.bar(
            np.arange(4),
            np.random.randint(10, 100, size=4),
            zs=m,  # 在x轴中的第几个
            zdir='x',  # 在哪个方向上排列
            alpha=0.7,  # 透明度
            width=0.5  # 宽度
    )
    
axes.set_xlabel('X轴', fontsize=18, color='red')
axes.set_ylabel('Y轴', fontsize=18, color='blue')
axes.set_zlabel('Z轴', fontsize=18, color='green')
plt.show()
```



#### 七、Matplotlib 图像处理

- 读取图片

```python
img = plt.imread('data/pandas.jpeg')
img
```

- 显示图片

```python
# 显示图片
plt.imshow(img)
```

- 垂直翻转

```python
# 垂直翻转显示
plt.imshow(img, origin='lower')
# 或
plt.imshow(img[::-1])
```

- 水平翻转

```python
# 水平翻转
plt.imshow(img[:, ::-1])
```

- 保存图片

```python
# 保存图片
plt.imsave('images/pandas.png', img)
```
