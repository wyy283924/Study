# Java环境安装
## JRE和JDK
** JRE(Java Runtime Environment) **:Java程序的运行时环境，包含JVM和运行时所需要的类库。
** JDK(Java Development Kit) **:是Java的开发工具包，包含JRE和开发人员使用的工具。

如果需要运行Java程序，那么只需要JRE就可以。

如果想要开发Java程序，那么必须安装JDK。
![这是一张图片](amWiki/images/1.1.1/11.png)


## Java环境安装
```
下载JDK

官方网址：

www.oracle.com

安装JDK

一直点击下一步即可。

建议：安装路径不要有中文或者特殊符号如空格等。

注意：当提示安装 JRE 时，可以选择不安装。
```
![这是一张图片](amWiki/images/1.1.2/1.jpg)
![这是一张图片](amWiki/images/1.1.2/2.jpg)
![这是一张图片](amWiki/images/1.1.1/12.png)
![这是一张图片](amWiki/images/1.1.1/13.png)
![这是一张图片](amWiki/images/1.1.1/14.png)
![这是一张图片](amWiki/images/1.1.1/15.png)
![这是一张图片](amWiki/images/1.1.1/16.png)
![这是一张图片](amWiki/images/1.1.1/17.png)
![这是一张图片](amWiki/images/1.1.1/18.png)

## 配置环境变量
1.安装完成后，右击"我的电脑"，点击"属性"，选择"高级系统设置"；
![这是一张图片](amWiki/images/1.1.2/3.png)
![这是一张图片](amWiki/images/1.1.2/4.png)
![这是一张图片](amWiki/images/1.1.2/5.png)

```
用户变量：当前用户可以使用
系统变量：所有用户可以使用

变量名：JAVA_HOME
变量值：C:\\Program Files (x86)\Java\\jdk1.8.0_91 // 要根据自己的实际路径配置
变量名：Path
变量值：%JAVA_HOME%\\bin;%JAVA_HOME%\\jre\\bin;
```
## IDE（集成开发环境）的使用
IDE就是一个软件，专门为了开发某种编程语言的代码的
### 记事本写代码存在的问题
1. 代码一个个字符手敲
2. main函数写法固定的代码，必须一个个自己写字符
3. 记事本写的代码，语法的问题我们都得再最后编译的时候才会发现
4. 记事本写的代码得在命令行中手动编译和手动运行
### IDE工具提升开发效率
    1. IDE工具可以和我们本地安装的JDK环境集成，我们就可以不再需要手动编译和手动运行了
    2. IDE中存在很多的快捷键，可以帮助我们进行代码的自动补全和提示
### IDE工具
```
C/C++:  DEV-C++、codeblocks、CLion
java：eclipse、idea
python：pycharm
html、css、js：vscode
```
### eclipse

```
IDE如果想要实现自动编译和运行Java程序，那么IDE中必须有JDK软件。eclipse中有一个自带的JRE，但是JRE的版本版本17版本，所以我们需要把ide自带的JRE换成我们自己安装的jdk

ide中也有JDK的编译工具，只不过默认的编译工具的版本是17版本的，也需要把编译版本换成8版本
Eclipse确实可以实现代码的自动编译、运行、补全等等操作，但是不是所有的代码eclipse都可以进行操作，需要按照eclipse的规范创建Java源文件，eclipse才会进行编译、运行、补全等等操作。
如果想在eclipse创建运行Java代码，那么必须先创建一个Java project
```