## Java的类加载器机制

1. Java程序的启动并运行的过程(Java中的类加载都是在运行时动态完成的)

   + JVM启动
   + 加载main方法所在的类（起始类initial class）
   + 执行main方法
   + 加载所依赖的类
   + 执行其它方法

2. 类加载器

   + 使用Java代码或JVM触发一个加载动作
     - Class.forName
     - ClassLoader.loadClass
     - 由JVM触发
   + 将类的全限定类名传给类加载器，通过类名获取到字节码的二进制流
     + 从本地硬盘读取类文件
     + 从网络读取类文件
     + 运行时计算字节码流
   + 根据字节码二进制流创建加载对应的Class对象

3. Java8内置的类加载器

   + AppClassLoader:应用类加载器，负责加载当前Java应用classpath中的类，classpath通常是通过java命令的参数 -cp / -classpath 来指定
   + ExtClassLoader：扩展类加载器，负责加载扩展目录中的类，扩展目录通常是<JAVA_HOME>/lib/ext,从Java9开始扩展机制已经被移除，ExtClassLoader也因此被PlatformClassLoader所取代
   + Bootstrap ClassLoader：启动类加载器，负责加载Java中核心类加载器，例如Java8中<JAVA_HOME>/jre/lib中的rt.jar。在JVM中，Bootstrap ClassLoader通常是使用C/C++语言原生实现的，他不能表现为一个Java类，所以将它打印出来是null
   + ![36](img/36.png)

4. 双亲委派模型

   除了Bootstrap ClassLoader,其它的类加载器有且只有一个parent

   并非继承关系，而是组合关系

   + 每个Class都有对应的ClassLoader

   + 每个ClassLoader都有一个“父”类加载器（Parent ClassLoader）。Bootstrap ClassLoader除外，它是最顶层的类加载器

   + 对于一个类加载的请求，总是优先委派给“父”类加载器来尝试加载

   + 对于用户自定义的类加载器，默认的“父”类加载器是AppClassLoader

     ![37](img/37.png)

     

5. 