[TOC]
# Java的分类
## JavaSE:Java语法
1. Java基础语法
* 关键字和保留字
* 变量和常量
* 数据类型
* 运算符
* 流程控制
 + 顺序流程
 + 分支流程
 + 循环流程
2. 数组
3. 面向对象
* 类和对象
4. 集合体系
5. Java异常体系
6. Java IO流
7. Java反射机制
8. Java注解
9. JDK特性  
JavaSE再做一些大型的项目的时候，JavaSE的类库代码显得有些臃肿和无力，比如现在我想要通过JavaSE去操作数据库。
## JavaEE：Java企业级开发技术
Java官方基于JavaSE语法和常用类库封装了一些技术工具，用这些技术工具可以快速的构建一些大型的企业级应用。这些技术主要有十三种
### JDBC：Java用来专门操作数据库的一门企业级开发技术
### Javax Mail：Java邮箱技术
### XML技术：xml是一种Java中配置文件技术，xml使用等同于HTML
### Servlet：Java端的小程序，servlet技术主要是被设计用来接受网络的请求，以及给网络输出数据的
### JSP：java server page，本质上就是servlet的，这个servlet给网络传输的都是网页类型的数据（类似HTML、css、js代码）
### JNDI(Java Name and Directory Interface) 　　JNDI API被用于执行名字和目录服务
### EJB(Enterprise JavaBean) 　　JAVAEE技术之所以赢得媒体广泛重视的原因之一就是EJB
### RMI(Remote Method Invoke) 
### Java IDL/CORBA 
### JMS(Java Message Service) 　　JMS是用于和面向消息的中间件相互通信的应用程序接口(API)。
### JTA(Java Transaction Architecture) 　　JTA定义了一种标准的API，应用系统由此可以访问各种事务监控。
### JTS(Java Transaction Service) 　　JTS是CORBA OTS事务监控的基本的实现。
### JAF(JavaBeans Activation Framework) 　　JavaMail利用JAF来处理MIME编码的邮件附件。

## JavaME（使用场景不多）
## JavaCard（使用场景不多）

## 框架
JavaEE虽然提供了十三种企业级开发技术帮助提升开发效率，但是代码还是有点麻烦，不够清晰明了，所以在JavaEE当中又基于这些企业级开发技术诞生了一些框架技术（相当于对十三种技术进行了二次封装）
### Spring框架：管理JavaBean以及做一些切面编程和业务逻辑，还有web开发的
### SpringMVC框架：是Spring框架的一部分，底层是Servlet的封装
### MyBatis框架：是JDBC技术的封装
### SpringBoot框架：脚手架，把JavaEE中常见的框架技术的组装全部封装好了
### Spring Cloud 微服务技术生态
