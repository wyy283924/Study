[TOC]
# html常用标签
## head中的子标签
+ title
+ link：引入外部的CSS文件，可以定义网页的标签logo
rel  href  type
+ meta 
+ style:css代码
+ script：js代码
## body中的子标签
+ 文本标签：双标签
不独占一行
```
span
b/strong
i /  em
u
s
```
+ 标题标签  双标签
默认独占一行的
```
h1~h6  六级标题
align属性   位置  left  right  cente
```
+ 段落标签
```
p标签中的文本换行，空格是不会识别的
pre：被包围在 pre 元素中的文本通常会保留空格和换行符，在浏览器中显示时，按照编辑工具中文档预先排好的形式显示内容
```
+ HTML实体
```
在HTML当中，有一些特殊的字符HTML是不会识别的，因为和语法产生了冲突，<     >
实体就相当于是特殊字符的表示方式
```     

|代码|效果|代码|效果|
|-|-|-|-|
|&quot;|"|&amp;|&|
|&lt;|<|&gt;|>|
|&nbsp;|空格|&copy;|©|
|&sect;|§|&curren;|¤|

## 换行标签

```
单标签  <br/>
```

## 区段标签
区分段落的，下划线   hr

```html
 <hr/>水平线
  <hr size='9'>水平线(设定大小)  
  <hr width='80%'>水平线(设定宽度)
  <hr color='ff0000'>水平线(设定颜色)
  <br/>(换行)
```

## 超链接标签：a标签

```html
<a> 文件/另外一个子标签 </a>
``` 

|属性|描述|版本|
|-|-|-|
|href|	链接地址|	HTML4|
|target|打开方式|	HTML4|
|title|鼠标悬停提示文字|	HTML4|
|download|下载，href写文件的路径，download属性是下载文件的名字|HTML5|
|rel|	指定当前文档与被链接文档的关系||
### href  超链接链接的地址
+ 绝对路径
+ 相对路径
### target  打开的地址在什么地方
+ _blank 在新窗口中打开链接
+ _self 在当前窗口打开链接,此为默认值
+ framename 窗口名称

```html
<!--在当前窗口打开链接-->
<a href="" target="_self">test</a>
<!--在新窗口中打开链接-->
<a href="" target="_blank">test</a>
<!--在指定窗口打开链接-->
<a href="" target="main">test</a>
<iframe name="main"></iframe>
```

### title  鼠标放到超链接上显示的提示性文字
### download  当a链接下载文件时，download中显示的就是下载文件的文字
href写文件的路径，download属性是下载文件的名字

```html
<a href="/images/logo.png" download="logo.png">
```

### name锚链接
给页面当中的某个特定位置添加标记，可以通过a链接直接指向这个位置，经常用在页面内容比较多的情况

```html
1、需要在界面需要定位的地方打上标记
<a name="top"></a>
2、然后制作一个超链接 链接到标记上即可
<a href=""#top>回顶部</a>
```

### rel
指定当前文档与被链接文档的关系。

```html
<a href="part_12.html" rel="nofollow"></a>
```

```
如果A网页上有一个链接指向B网页，但A网页给这个链接加上了 rel="nofollow" 标注，则搜索引擎不把A网页计算入B网页的反向链接。搜索引擎看到这个标签就可能减少或完全取消链接的投票权重。

反向链接即外链是搜索引擎给网站排名的一个重要因素。

Nofollow标签的作用有两方面，简单的说，一是不给链接投票，降低此链接的权重，二是使添加nofollow的部分内容不参与网站排名，便于集中网站权重，减少权重的分散。
```

## 列表标签
### 有序列表
```html
<ol type = "1">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ol>
<ol type = "a">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ol>
<ol type = "A">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ol>
<ol type = "i">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ol>
<ol type = "I">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ol>
```
### 无序列表
```html
<ul type="circle">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ul>
<ul type="square">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ul>
<ul type="disc">
  <li>第一点</li>
  <li>第二点</li>
  <li>第三点</li>
</ul>
```
## 多媒体标签
### img:单标签
+ src
+ alt：如果图片地址不存在，默认显示的提示性文字
+ title
+ width   height
+ border
+ usemap="#xxxx" 结合map和area标签使用

```html
<img src = "图片4.png" alt = "图片丢失" title = "科技感" width = "500px" />
```
#### 图像地图
```
图像地图：图像地图 效果的实质是把一幅图片划分为不同的作用区域，再让不同的区域链接不同的地址
```

```html
<map name=''>
  <area shape="" coords="" alt="" href="">
</map>
<!--
shape 形状 "rect" "circle" "poly"
coords：坐标
矩形  两个坐标
圆：三个值
多边形  n个坐标
title鼠标经过提示的文字
href 指向的链接
target 以哪种方式打开 -->
```
```html
<img src="https://t7.baidu.com/it/u=3922293839,2103564073&fm=193&f=GIF" width="500px" height="400px" usemap="#myMap" />
<map name="myMap">
  <area shape="rect" coords="0,0,250,400" href="https://image.baidu.com/" title="百度" target="_self">
  <area shape="rect" coords="250,0,500,400" href="https://www.88ys.com" title="影视网" target="_blank">
</map>
```
### video
### audio
+ src：视频或者音频的链接地址
+ controls  不需要值   显示播放控件
+ autoplay  不需要值  基本不能使用
+ loop  不需要值 循环播放
+ width  height
+ poster：图片地址,设置未播放前的封面

```html
<video src="https://poss-videocloud.cns.com.cn/oss/2024/03/14/chinanews/MEIZI_YUNSHI/onair/96DF1B6DEC32418695EBD3082F9D7E82.mp4" controls autoplay loop width="300px" poster="https://t7.baidu.com/it/u=3922293839,2103564073&fm=193&f=GIF"></video>
<audio src="http://music.163.com/song/media/outer/url?id=569200212.mp3"  controls autoplay loop></audio>
```
## iframe
可以将另外一个标签嵌套到当前页面当中
+ scrolling   yes  no  auto
+ width
+ height
+ frameborder =0
+ src
```html
<h1>一级标题</h1>
<iframe src="img.html" width="500px" height="800px" scrolling="no" frameborder="0"></iframe>
```
name 框架起个名字 通过a链接的target属性将a链接链接的地址放到frame中打开   
```html
<a href="img.html" target="a">lalallaa</a>
<iframe name="a" frameborder="1" width="100%" height="800px"></iframe>
```
## 表格标签
### table 
+ thead th
+ tbody tr td
```html
<table>
  <thead>
    <th></th>
    <th></th>
    <th></th>
  </thead>
  <tbody>
    <tr>
      <td></td>  <!--td表示单元格 -->
      <td></td>
      <td></td>
    </tr>  <!--tr表示行-->
  </tbody>
</table>
```
### table属性
+ border 设置表格的边框
+ cellpadding 单元格的内边距
+ cellspacing 单元格之间的距离
+ width height
+ align 让表格水平居中
### thead  tbody属性
align 水平居中
### 不规则表格的制作
*** td中的两个属性 ***
+ rowspan 	横跨的行数（合并行）
+ colspan 	横跨的列数（合并列）  

```
如果表格样式能使用CSS实现,则尽量使用css达到页面与效果分离
```

```html
<table border="1">
  <caption>支出 </caption> <!-- 表格标题-->
  <thead> <!-- 表格头部-->
    <tr>
      <th>Month</th> <!-- th 表头默认大写居中-->
      <th>Savings</th>
    </tr>
  </thead>

  <tfoot> <!-- 表格底部-->
    <tr>
      <td>Sum</td>
      <td>$180</td>
    </tr>
  </tfoot>

  <tbody> <!-- 表格内容-->
    <tr>
      <td>January</td>
      <td>$100</td>
    </tr>
    <tr>
      <td>February</td>
      <td>$80</td>
    </tr>
  </tbody>
</table>
```

```
如果您使用 thead、tfoot 以及 tbody 元素，您就必须使用全部的元素。它们的出现次序是：thead、tfoot、tbody，这样浏览器就可以在收到所有数据前呈现页脚了。您必须在 table 元素内部使用这些标签。

注意：如果单元格数据为空在IE等浏览器中会不显示，所以要保证单元格不能为空，可以添加&nbsp;实体空格
```
## 表单标签
表单标签是HTML设计用来向web服务端传递HTTP协议的消息并且接受web服务端数据回应的标签
### HTTP协议
HTTP协议是用于请求互联上的某一个资源，并且从资源处获得数据或者网页的
#### HTTP请求
通常情况下，如果URL没有特别指明端口号，那么HTTP协议默认是80端口，HTTPS默认443端口。
##### 请求行
请求方式  请求资源路径 请求协议
+ 请求方式有很多种：get  delete post  put   
  get请求从URL资源处获取数据的
  delete请求从URL资源处删除数据的
  post请求从URL资源处添加数据
  put请求从URL资源处修改数据
+ 不管哪种请求方式，都可能会携带参数
  get delete携带参数方式一致的，会在URL后面使用?key=value&key=value...方式传递参数
  post put携带参数方式一致的，不会再URL后面拼接，而是把参数放到请求主体中，我们再URL中看不到参数的
+ get delete请求不太安全，post和put请求安全一点，getdelete请求传递的参数是有大小限制，post和put传递数据没有限制。如果传递文件数据，必须使用post或者put请求
##### 请求头
包含一些附加的信息，如用户代理、请求的主机、内容类型等
##### 请求主体
可选部分，用于传输请求的数据，常用于POST请求中传递表单数据或上传文件。
##### 空行

#### HTTP响应
##### 响应行
响应状态码  附带的ok或者其他信息
*** 响应状态码 ***
+ 1xx
+ 2xx:200 请求响应成功了
+ 3xx:302 重定向请求
+ 4xx:400 404-资源路径不存在 401 403  
  大部分都是web前端编写路径参数有问题
+ 5xx：500-内部服务器错误
  请求资源路径的问题
##### 响应头
##### 响应主体
##### 响应空行
### form属性
+ action   代表的请求的HTTP协议的URL地址
+ method  代表的请求方式 get  delete post put
+ enctype  请求规则 默认：application/x-www-form-urlencoded 可选： application/x-www-form-urlencoded(在发送前编码所有字符)、multipart/form-data(不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。)、text/plain(空格转换为 "+" 加号，但不对特殊字符编码。)
+ name 规定表单的名称。
+ target 规定在何处打开 action URL。
### form表单
form表单是用来向某个互联网资源路径发起HTTP请求的，但是请求一般都得需要携带参数，参数如何携带？包括请求如何发起？这些东西的实现需要基于form表单提供的组件来完成
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <form action="http://www.baidu.com" method="get" enctype="application/x-www-form-urlencoded" target="_self">
            <input type="text" name="username" placeholder="请输入用户名" />
            <input type="password" name="password" placeholder="请输入密码" >
            <input type="date" name="date" placeholder="请选择时间">
            <!-- <input type="file" name="header"> -->
            <input type="radio" name="sex" value="男">
            <input type="radio" name="sex" value="女">
            <input type="hidden" name="userid" value="1">

            <input type="checkbox" name="hobby" value="游戏">
            <input type="checkbox" name="hobby" value="睡觉">
            <input type="text" name="a" readonly>
            <input type="text" name="b" disabled>

            <input type="reset" value="重置">
            <input type="button" value="按钮">
            <input type="submit" value="提交">

            <input type="color" name="color">
            <input type="range" max="10" min="-10" name="num">
        </form>
        
    </body>
</html>
```
#### input组件
input组件：默认表示的是一个输入框组件，但是它也可以成为其他组件 单选框
```
type：text  password  date  email   file  radio  checkbox   button  sumbit  reset   hidden  range  color
value：控件的值
placeholder：text password的时候才会使用，输入框的提示性文字
name: 属性代表参数名字
disabled
readonly   设置只读
readonly只是不能编辑，但是还可以当作参数传递
disabled不仅不能编辑，还无法当作参数进行传递
```
#### 自动聚焦
+ 选中界面上一个文本或者组件，然后界面帮助我们自动选择上一个内容
+ label  for="id值"
id值是任何一个HTML元素都可以设置一个id属性值
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <form action="http://www.baidu.com" method="get" enctype="application/x-www-form-urlencoded">
            <label for="username"><span>用户名</span></label>
            <input type="text" name="username" placeholder="请输入用户名" id="username">
            <span>密码</span>
            <input type="password" name="password" placeholder="请输入密码">

            <input type="submit" value="登录">
        </form>

        <button>登录</button>
    </body>
</html>
```
#### select组件
下拉框
```html
<select name="sex" >
 <option value="man">男</option>
  <option value="woman" selected>女</option>
</select>

```
##### 属性
+ name  
+ size
+ multiple="false|true"
##### 子标签
option  下拉框的选项  
两个属性：value  selected 

```html
<select name="uek" size="1" multiple>
  　　<option value="webui" selected="selected">前端工程师</>
  　　<option value="ui" selected="selected">ui设计师</>
  　　<option value="php" selected="selected">php工程师</>
  </select>
```
#### textarea  文本域
+ name 用于指定文本输入框的名字
+ cols cols属性用于规定文本输入框的宽度。属性的参数值是数字，表示一行所能显示的最大字符数
+ rows rows属性用于规定文本输入框的高度。属性的参数值是数字，表示该文本输入框所占的行数

```html
<textarea name="intro" cols="30" rows="10"></textarea>
```
## 按钮标签 button
## 语义化标签
+ 没有实际的效果，只是用来表示这个标签内部放到是界面的那一部分的代码
+ 都是使用在body当中
+ 一般设计网页的时候，网页都是由头部、导航栏、正文、底部这么几部分组成的，内容都是写在HTML的body标签当中
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <header>

        </header>
        <nav>

        </nav>
        <article>

        </article>
        <footer>
            
        </footer>
    </body>
</html>
```
## div
等同于Java中Jpanel面板，是HTML提供的一个完全由我们自定义的组件，组件默认没有宽度、没有高度、没有边框、没有颜色 独占一行的