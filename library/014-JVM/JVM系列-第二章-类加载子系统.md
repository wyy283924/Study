## 第2章-类加载子系统

## 内存结构概述

#### 简图

#### 详细图

**英文版**

**中文版**

注意：方法区只有HotSpot虚拟机有，J9，JRockit都没有

如果自己想手写一个Java虚拟机的话，主要考虑哪些结构呢？

1. 类加载器
2. 执行引擎

## 类加载器子系统

#### 类加载器子系统作用：

1. 类加载器子系统负责从文件系统或者网络中加载Class文件，class文件在文件开头有特定的文件标识。
2. ClassLoader只负责class文件的加载，至于它是否可以运行，则由Execution Engine决定。
3. 加载的类信息存放于一块称为方法区的内存空间。除了类的信息外，方法区中还会存放运行时常量池信息，可能还包括字符串字面量和数字常量（这部分常量信息是Class文件中常量池部分的内存映射）

#### 类加载器ClassLoader角色

1. class file（在下图中就是Car.class文件）存在于本地硬盘上，可以理解为设计师画在纸上的模板，而最终这个模板在执行的时候是要加载到JVM当中来根据这个文件实例化出n个一模一样的实例。
2. class file加载到JVM中，被称为DNA元数据模板（在下图中就是内存中的Car Class），放在方法区
3. 在.class文件–>JVM–>最终成为元数据模板，此过程就要一个运输工具（类装载器Class Loader），扮演一个快递员的角色。

## 类加载过程

#### 概述

```java
public class HelloLoader {

    public static void main(String[] args) {
        System.out.println("谢谢ClassLoader加载我....");
        System.out.println("你的大恩大德，我下辈子再报！");
    }
}
```

它的加载过程是怎么样的呢?

+ 执行 main() 方法（静态方法）就需要先加载main方法所在类 HelloLoader
+ 加载成功，则进行链接、初始化等操作。完成后调用 HelloLoader 类中的静态方法 main
+ 加载失败则抛出异常

完整的流程图如下所示：

#### 加载阶段

**加载：**

1. 通过一个类的全限定名获取定义此类的二进制字节流

+ 做什么：JVM 的首要任务是找到这个类。它根据类的全限定名（如 java.lang.String）去获取其对应的二进制字节流（即 .class 文件的原始内容）。
+ 如何实现：JVM 的类加载器（ClassLoader）被设计得非常灵活，它没有限制这串二进制字节流必须从何而来。它可以从文件系统、网络、ZIP包、运行时动态生成等多种途径获取。这种灵活性是 Java 动态扩展能力的基石。

2. 将这个字节流所代表的静态存储结构转化为方法区的运行时数据结构

+ **做什么：**上一步获取的字节流是符合 JVM 规范的静态存储格式。这一步 JVM 需要解析这个字节流，并将其转换为方法区（Method Area） 内部的运行时数据结构。
+ **关键概念：**
  + **方法区：**是 JVM 的一块内存区域，它存储了已被加载的**类型信息**（包括类名、父类、接口、字段、方法等）、常量、静态变量、即时编译器编译后的代码缓存等。注意： 在 HotSpot 虚拟机中，方法区常被称为“永久代”（JDK 7及以前）或“元空间”（Metaspace，JDK 8及以后）。
  + 转换：这个过程不仅仅是简单的拷贝，还包括了格式的验证和重组，使其成为 JVM 运行时可以高效操作的数据结构。

3. **在内存中生成一个代表这个类的java.lang.Class对象**，作为方法区这个类的各种数据的访问入口

+ 做什么：这是“加载”阶段的最终产物。JVM 在 Java 堆内存 中创建了一个 java.lang.Class 类的实例。
+ 关键角色：这个 Class 对象极其重要，它扮演了双重角色：
  + 对于 JVM：它是方法区中该类所有数据的访问入口和抽象表示。你想获取类的任何信息（如它的方法、字段、注解等），都必须通过这个 Class 对象。
  + 对于程序员：在程序运行时，你可以通过 MyClass.class、obj.getClass() 或 Class.forName("MyClass") 等方式获取到这个 Class 对象，并利用反射（Reflection） API 来动态地分析和操作这个类，这是 Java 高级编程的核心特性之一。

**加载class文件的方式：**

1. 从本地系统中直接加载

   这是**最常见、最基础**的加载方式。它指的是从当前系统的磁盘路径下读取.class文件。

   + **实现方式：**由Java虚拟机默认的**应用程序类加载器（Application ClassLoader）** 完成。

   + **加载路径：**就是我们熟悉的CLASSPATH环境变量、-cp或-classpath命令行参数所指定的目录和JAR包。

   + **示例：**当你运行java MyApp命令时，JVM会在CLASSPATH下寻找并加载MyApp.class文件。

2. 通过网络获取，典型场景：Web Applet

   这种方式允许从网络上的某个URL动态加载类。

   + **典型场景：**
     + Web Applet：这是早期的Java小程序技术，它在浏览器中运行。浏览器（或Java插件）会从一个Web服务器下载Applet的.class文件并在本地的沙箱环境中运行。虽然现在已被淘汰，但它是网络加载的经典案例。
     + 远程方法调用（RMI）：在分布式系统中，客户端可以从服务器动态下载所需的Stub类。

   + 实现方式：需要开发者自己继承ClassLoader类，并重写findClass()方法，在其中使用URLConnection等网络API获取字节流，然后调用defineClass()方法来定义这个类。

3. 从zip压缩包中读取，成为日后jar、war格式的基础

   这是对第一种方式的扩展，也是极其普遍的方式。它将大量的.class文件、资源文件打包成一个压缩文件，便于分发和部署

   + **基础：**正如您所说，它源自从ZIP包读取。

   + **演进：**JAR（Java Archive）是基于ZIP格式的包，通常用于打包库和应用程序。WAR（Web Archive）是专门为Web应用程序设计的JAR包，包含了Servlet、JSP、XML配置文件、静态网页等。

   + **实现方式：**JVM的类加载器内置了对ZIP/JAR格式的支持，能够直接遍历压缩包内的条目（entry）并加载所需的类。

4. 运行时计算生成，使用最多的是：动态代理技术

   这是**Java高级特性**的体现，意味着JVM加载的类并非预先存在于某个文件中的，而是在程序运行过程中动态创建出来的。

   + 最典型技术：

     + **动态代理（Dynamic Proxy）**：当使用Proxy.newProxyInstance()方法创建代理对象时，JVM会在内存中动态地生成代理类的字节码（如$Proxy0.class），然后通过类加载器将其加载到JVM中。这个.class文件在磁盘上是找不到的。

   + 其他技术：

     + **字节码增强库（如ASM, CGLib, Javassist）**：这些库可以在运行时操作和生成字节码，用于实现AOP（面向切面编程）、性能监控、热部署等功能。

     + **JSP编译**：从技术角度看，JSP最终会被应用服务器（如Tomcat）编译成Servlet的.class文件，这个过程也是在运行时发生的。

5. 由其他文件生成，典型场景：JSP应用从专有数据库中提取.class文件，比较少见

   这种方式比较特殊，其来源不是标准的.class文件，但最终会转换成JVM可以执行的字节码。

   **典型场景：**

   + **JSP（JavaServer Pages）**：这是最符合这一条的例子。用户访问一个.jsp文件时，Web容器（如Tomcat）会先将JSP文件翻译和编译成一个完整的Java Servlet类（.java文件），然后调用JDK的编译器（或内置编译器）将其编译成.class文件，最后由类加载器加载这个新生成的类。所以，类的源头是.jsp文件。
   + **从专有数据库提取：**一些特殊的应用可能将类的字节码以二进制形式存储在数据库的BLOB字段中。应用程序需要实现自定义的类加载器，从数据库中读取字节数组，然后调用defineClass来加载它。

6. 从加密文件中获取，典型的防Class文件被反编译的保护措施

   这主要是一种商业化和安全保护的手段，目的是防止核心代码被轻易反编译。

   + **工作原理**：将关键的.class文件进行加密或混淆，使其无法用标准的反编译工具直接查看。

   + **实现方式：**同样需要自定义类加载器。在findClass()方法中，先找到加密的文件，读取其加密的字节流，然后执行相应的解密算法，得到明文的字节码数据，最后再调用defineClass()完成加载。

   + **目的：**保护知识产权，防止商业代码被逆向工程。

#### 链接阶段

链接分为三个子阶段：验证 -> 准备 -> 解析

1. **验证（Verify）**
   **目的：**确保Class文件的字节流信息符合JVM规范，保证被加载类的正确性，不会危害虚拟机安全。

​		**四个验证步骤：**

+ 文件格式验证：验证字节流是否符合Class文件格式规范（如魔数CAFE BABE、版本号等）

+ 元数据验证：对类的元数据信息进行语义校验（如是否有父类、是否继承final类等）

+ 字节码验证：通过数据流和控制流分析，验证程序语义是否合法、符合逻辑

+ 符号引用验证：确保解析动作能正常执行（如符号引用能否找到对应的类）

举例：使用BinaryViewer等工具查看字节码文件，合法的Class文件开头必须是CAFE BABE（魔数），否则验证将失败。

2. **准备（Prepare）**
**目的：**为类变量（static变量）分配内存并设置默认初始值（零值）。

​		**重要细节：**

+ 不包括用final修饰的static常量，因为final在编译时就会分配默认值

+ 不会为实例变量分配初始化，实例变量随对象分配到Java堆中

+ 类变量分配在方法区中

举例分析：

```java
public class HelloApp {
    private static int a = 1;        // 准备阶段：a = 0 → 初始化阶段：a = 1
    static {
        a = 2;                      // 初始化阶段：a = 2
        num = 20;                   // 初始化阶段：num = 20
    }
    private static int num = 10;     // 初始化阶段：num = 10 (覆盖之前的20)
    
    public static void main(String[] args) {
        System.out.println(a);       // 输出: 2
        System.out.println(num);     // 输出: 10
	}
}  
```

3. **解析（Resolve）**
**目的：**将常量池内的符号引用转换为直接引用。

​		**关键点：**

+ 符号引用：一组符号来描述所引用的目标（如类名、方法名）

+ 直接引用：直接指向目标的指针、相对偏移量或间接定位句柄

+ 解析操作往往在初始化之后执行

+ 主要针对类/接口、字段、方法等进行解析,对应常量池中的CONSTANT Class info、CONSTANT Fieldref info、CONSTANT Methodref info等

符号引用示例：
		通过javap -v反编译Class文件，可以看到常量池中以#开头的符号引用，如：

```
#1 = Methodref          #4.#20         // java/lang/Object."<init>":()V
#2 = Fieldref           #21.#22        // java/lang/System.out:Ljava/io/PrintStream;
```

#### 初始化阶段

##### 类的初始化时机

1. **创建类的实例**

- **场景**：使用 `new` 关键字创建对象。
- **示例**：`new MyClass();`
- **注意**：对于数组实例，情况特殊。`MyClass[] arr = new MyClass[10];` 并不会导致 `MyClass` 初始化。这条语句只是由虚拟机在堆上开辟了一段连续空间，这是一个**对数组类型的主动引用**，但**不是对数组元素类（`MyClass`）的主动引用**。`MyClass` 的初始化要等到第一个数组元素被初始化时才会发生。

2. **访问某个类或接口的静态变量，或者对该静态变量赋值**

- **场景**：读取或设置一个类的静态字段（被 `static` 修饰的字段，**不包括静态常量**）。
- **示例**：
  - `System.out;` (访问 `System` 类的静态字段 `out`)
  - `MyClass.staticField = 10;` (对静态字段赋值)
- **重要例外**：如果静态字段是**编译期常量**（即被 `static final` 修饰，并且在编译期就能确定其值），那么对此字段的引用不会触发初始化。因为在编译阶段，这个常量的值已经被直接“拷贝”到了调用类的常量池中，不再与定义它的类有任何关联。
  - `public static final int MAX_VALUE = 100;` // 是编译期常量，访问 `MyClass.MAX_VALUE` **不会**导致 `MyClass` 初始化。
  - `public static final int RANDOM_VALUE = new Random().nextInt();` // **不是**编译期常量，访问它会触发初始化。

3. **调用类的静态方法**

- **场景**：调用一个类的静态方法。
- **示例**：`MyClass.staticMethod();`

4. 反射（比如：Class.forName(“com.xxx.Test”)）

- **场景**：使用 `java.lang.reflect` 包的方法或 `Class` 类的方法进行反射调用。
- **示例**：`Class.forName("com.example.MyClass")` **默认情况下**会进行类的初始化。该方法有一个重载版本 `Class.forName(String name, boolean initialize, ClassLoader loader)`，其中 `initialize` 参数为 `false` 时则不会触发初始化，仅完成类的加载。

5. **初始化一个类的子类**

- **场景**：当初始化一个子类时，如果其父类还未被初始化，那么虚拟机会先保证其父类被初始化。
- **示例**：`class Child extends Parent {}`。执行 `new Child()` 时，会先触发 `Parent` 的初始化，再触发 `Child` 的初始化。
- **注意**：通过子类引用父类的静态字段，**不会**导致子类初始化。
  - `System.out.println(Child.parentStaticField);` // 只会初始化父类 `Parent`，而不会初始化子类 `Child`。

6. **Java虚拟机启动时被标明为启动类的类**

- **场景**：包含 `main(String[])` 方法的那个类。JVM 启动时，会先初始化这个主类。
- **示例**：执行 `java com.example.MainApp`，`MainApp` 类会首先被初始化。

7. **动态语言支持（JDK7+）**

- **场景**：涉及到 `java.lang.invoke.MethodHandle` 实例的解析结果。
- **说明**：这是一个相对高级的特性。如果一个方法句柄（MethodHandle）的解析结果是 `REF_getStatic`（获取静态字段）、`REF_putStatic`（设置静态字段）、`REF_invokeStatic`（调用静态方法），并且这个句柄对应的类还没有被初始化，那么就需要先初始化该类。

------

被动使用（不会导致初始化）

除了以上 7 种“主动使用”，其他情况都属于“被动使用”（Passive Use），**不会触发类的初始化**。

**常见的被动使用场景包括：**

1. **通过子类引用父类的静态字段**：只会初始化父类，不会初始化子类。
2. **通过数组定义来引用类**：`MyClass[] arr = new MyClass[10];` 不会初始化 `MyClass`。
3. **访问类的编译期常量（static final）**：因为值已在编译期被内联到调用代码中。
4. **加载类时（`ClassLoader.loadClass()`）**：`ClassLoader.loadClass()` 方法只负责加载（Loading）阶段，不会触发初始化。而 `Class.forName()` 默认会触发初始化。
5. **访问一个已在别处被初始化的类的静态字段**：类只会在第一次被“主动使用”时初始化一次。

**关键方法：`<clinit>()`**

- **是什么**：是由编译器自动收集类中的所有**类变量（静态变量）的赋值动作**和**静态语句块（`static{}` 块）** 中的语句合并产生的。构造器 `<init>()` 是初始化对象实例的，而 `<clinit>()` 是初始化类本身的。
- **何时执行**：在“初始化”阶段，JVM 会执行 `<clinit>()` 方法。
- **特点**：虚拟机会保证在多线程环境下，一个类的 `<clinit>()` 方法只会被一个线程执行一次，并且其他线程会被阻塞直到它执行完毕。这确保了类静态变量只被初始化一次。

除了以上七种情况，其他使用Java类的方式都被看作是对类的被动使用，都不会导致类的初始化，即不会执行初始化阶段（不会调用 clinit() 方法和 init() 方法）

**clinit()**

1. 初始化阶段就是执行类构造器方法<clinit>()的过程
2. 此方法不需定义，是javac编译器自动收集类中的所有类变量的赋值动作和静态代码块中的语句合并而来。也就是说，当我们代码中包含static变量的时候，就会有clinit方法
3. <clinit>()方法中的指令按语句在源文件中出现的顺序执行
4. <clinit>()不同于类的构造器。（关联：构造器是虚拟机视角下的<init>()）
5. 若该类具有父类，JVM会保证子类的<clinit>()执行前，父类的<clinit>()已经执行完毕
6. 虚拟机必须保证一个类的<clinit>()方法在多线程下被同步加锁

> IDEA 中安装 JClassLib Bytecode viewer 插件，可以很方便的看字节码。安装过程可以自行百度

**1，2，3说明**
		**举例1：有static变量**

查看下面这个代码的字节码，可以发现有一个<clinit>()方法。

```java
public class ClassInitTest {
   private static int num = 1;

   static{
       num = 2;
       number = 20;
       System.out.println(num);
       //System.out.println(number);//报错：非法的前向引用。
   }

   /**
    * 1、linking之prepare: number = 0 --> initial: 20 --> 10
    * 2、这里因为静态代码块出现在声明变量语句前面，所以之前被准备阶段为0的number变量会
    * 首先被初始化为20，再接着被初始化成10（这也是面试时常考的问题哦）
    *
    */
   private static int number = 10;

    public static void main(String[] args) {
        System.out.println(ClassInitTest.num);//2
        System.out.println(ClassInitTest.number);//10
    }
}
```

<clint字节码>：

```java
 0 iconst_1
 1 putstatic #3 <com/atguigu/java/ClassInitTest.num>
 4 iconst_2
 5 putstatic #3 <com/atguigu/java/ClassInitTest.num>
 8 bipush 20	 //先赋20
10 putstatic #5 <com/atguigu/java/ClassInitTest.number>
13 getstatic #2 <java/lang/System.out>
16 getstatic #3 <com/atguigu/java/ClassInitTest.num>
19 invokevirtual #4 <java/io/PrintStream.println>
22 bipush 10	//再赋10
24 putstatic #5 <com/atguigu/java/ClassInitTest.number>
27 return
```

当我们代码中包含static变量的时候，就会有clinit方法

**举例2：无 static 变量**

**<clinit>() 方法的生成规则**

+ 自动生成：此方法并非由程序员直接编写，而是由 javac 编译器在编译期自动生成。

+ 内容来源：编译器会遍历整个类，收集所有类变量（静态变量）的显式赋值语句和静态代码块（static {} 块） 中的语句，将它们合并后生成 <clinit>() 方法。

+ 必要条件：如果一个类中没有 static 变量，也没有 static {} 块，那么编译器就不会为该类生成 <clinit>() 方法。

**3.说明** 执行顺序：按源码顺序执行

```java
public class Example {
    private static int x = 10; // 第一步：x被赋值为10
    
    static {
        x = 20; // 第二步：x被重新赋值为20
        y = 30; // 第三步：可以给后面的y赋值（准备阶段已分配内存）
        // System.out.println(y); // 第四步：这里如果打印y，会编译失败（非法前向引用）
    }
    
    private static int y = 40; // 第五步：y被赋值为40（覆盖之前的30）
    
    public static void main(String[] args) {
        System.out.println(x); // 输出：20
        System.out.println(y); // 输出：40
    }
}
```



**4.说明**<clinit>() vs <init>()

| 特性     | <clinit>() (类构造器)         | <init>() (实例构造器)                     |
| -------- | ----------------------------- | ----------------------------------------- |
| 触发时机 | 类初始化时（主动使用）        | 创建对象实例时（new）                     |
| 执行次数 | 整个生命周期只执行一次        | 每创建一个新对象就执行一次                |
| 内容来源 | static 变量赋值 + static{} 块 | 非静态变量赋值 + {} 实例块 + 构造函数代码 |
| 目的     | 初始化类（静态域）            | 初始化对象实例（实例域）                  |

**5说明** 父类 <clinit>() 优先执行

```java
class Parent {
    static {
        System.out.println("Parent's static block");
    }
    public static int value = 100;
}

class Child extends Parent {
    static {
        System.out.println("Child's static block");
        System.out.println("Parent's value: " + value); // 可以访问，因为父类已初始化
    }
}

// 输出顺序：
// Parent's static block
// Child's static block
// Parent's value: 100
```



**6说明**
虚拟机必须保证一个类的<clinit>()方法在多线程下被同步加锁

```java
public class DeadThreadTest {
    public static void main(String[] args) {
        Runnable r = () -> {
            System.out.println(Thread.currentThread().getName() + "开始");
            DeadThread dead = new DeadThread();
            System.out.println(Thread.currentThread().getName() + "结束");
        };

        Thread t1 = new Thread(r,"线程1");
        Thread t2 = new Thread(r,"线程2");

        t1.start();
        t2.start();
    }
}

class DeadThread{
    static{
        if(true){
            System.out.println(Thread.currentThread().getName() + "初始化当前类");
            while(true){

            }
        }
    }
}
```

输出结果：

```
线程2开始
线程1开始
线程2初始化当前类

/然后程序卡死了
程序卡死，分析原因：
```

+ 两个线程同时去加载 DeadThread 类，而 DeadThread 类中静态代码块中有一处死循环
+ 先加载 DeadThread 类的线程抢到了同步锁，然后在类的静态代码块中执行死循环，而另一个线程在等待同步锁的释放
+ 所以无论哪个线程先执行 DeadThread 类的加载，另外一个类也不会继续执行。（一个类只会被加载一次）

## 类加载器的分类

#### 概述

1. JVM严格来讲支持两种类型的类加载器 。分别为引导类加载器（Bootstrap ClassLoader）和自定义类加载器（User-Defined ClassLoader）

2. 从概念上来讲，自定义类加载器一般指的是程序中由开发人员自定义的一类类加载器，但是Java虚拟机规范却没有这么定义，而是将所有派生于抽象类ClassLoader的类加载器都划分为自定义类加载器

3. 无论类加载器的类型如何划分，在程序中我们最常见的类加载器始终只有3个，如下所示

   

```java
public class ClassLoaderTest {
    public static void main(String[] args) {

        //获取系统类加载器
        ClassLoader systemClassLoader = ClassLoader.getSystemClassLoader();
        System.out.println(systemClassLoader);//sun.misc.Launcher$AppClassLoader@18b4aac2

        //获取其上层：扩展类加载器
        ClassLoader extClassLoader = systemClassLoader.getParent();
        System.out.println(extClassLoader);//sun.misc.Launcher$ExtClassLoader@1540e19d

        //获取其上层：获取不到引导类加载器
        ClassLoader bootstrapClassLoader = extClassLoader.getParent();
        System.out.println(bootstrapClassLoader);//null

        //对于用户自定义类来说：默认使用系统类加载器进行加载
        ClassLoader classLoader = ClassLoaderTest.class.getClassLoader();
        System.out.println(classLoader);//sun.misc.Launcher$AppClassLoader@18b4aac2

        //String类使用引导类加载器进行加载的。---> Java的核心类库都是使用引导类加载器进行加载的。
        ClassLoader classLoader1 = String.class.getClassLoader();
        System.out.println(classLoader1);//null


    }
}
```

+ 我们尝试获取引导类加载器，获取到的值为 null ，这并不代表引导类加载器不存在，因为引导类加载器右 C/C++ 语言，我们获取不到
+ 两次获取系统类加载器的值都相同：sun.misc.Launcher$AppClassLoader@18b4aac2 ，这说明系统类加载器是全局唯一的

#### 虚拟机自带的加载器

**启动类加载器**

> 启动类加载器（引导类加载器，Bootstrap ClassLoader）

1. 这个类加载使用C/C++语言实现的，嵌套在JVM内部
2. 它用来加载Java的核心库（JAVA_HOME/jre/lib/rt.jar、resources.jar或sun.boot.class.path路径下的内容），用于提供JVM自身需要的类
3. 并不继承自java.lang.ClassLoader，没有父加载器
4. 加载扩展类和应用程序类加载器，并作为他们的父类加载器
5. 出于安全考虑，Bootstrap启动类加载器只加载包名为java、javax、sun等开头的类

**扩展类加载器**

> 扩展类加载器（Extension ClassLoader）

1. Java语言编写，由sun.misc.Launcher$ExtClassLoader实现
2. 派生于ClassLoader类
3. 父类加载器为启动类加载器
4. 从java.ext.dirs系统属性所指定的目录中加载类库，或从JDK的安装目录的jre/lib/ext子目录（扩展目录）下加载类库。如果用户创建的JAR放在此目录下，也会自动由扩展类加载器加载

**系统类加载器**

> 应用程序类加载器（也称为系统类加载器，AppClassLoader）

1. Java语言编写，由sun.misc.LaunchersAppClassLoader实现
2. 派生于ClassLoader类
3. 父类加载器为扩展类加载器
4. 它负责加载环境变量classpath或系统属性java.class.path指定路径下的类库
5. 该类加载是程序中默认的类加载器，一般来说，Java应用的类都是由它来完成加载
6. 通过classLoader.getSystemclassLoader()方法可以获取到该类加载器

```java
public class ClassLoaderTest1 {
    public static void main(String[] args) {
        System.out.println("**********启动类加载器**************");
        //获取BootstrapClassLoader能够加载的api的路径
        URL[] urLs = sun.misc.Launcher.getBootstrapClassPath().getURLs();
        for (URL element : urLs) {
            System.out.println(element.toExternalForm());
        }
        //从上面的路径中随意选择一个类,来看看他的类加载器是什么:引导类加载器
        ClassLoader classLoader = Provider.class.getClassLoader();
        System.out.println(classLoader);

        System.out.println("***********扩展类加载器*************");
        String extDirs = System.getProperty("java.ext.dirs");
        for (String path : extDirs.split(";")) {
            System.out.println(path);
        }

        //从上面的路径中随意选择一个类,来看看他的类加载器是什么:扩展类加载器
        ClassLoader classLoader1 = CurveDB.class.getClassLoader();
        System.out.println(classLoader1);//sun.misc.Launcher$ExtClassLoader@1540e19d

    }
}
```

**输出结果**

```java
**********启动类加载器**************
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/lib/resources.jar
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/lib/rt.jar
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/lib/sunrsasign.jar
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/lib/jsse.jar
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/lib/jce.jar
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/lib/charsets.jar
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/lib/jfr.jar
file:/C:/Program%20Files/Java/jdk1.8.0_131/jre/classes
null
***********扩展类加载器*************
C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext
C:\Windows\Sun\Java\lib\ext
sun.misc.Launcher$ExtClassLoader@29453f44
```

#### 用户自定义类加载器

##### 什么时候需要自定义类加载器？

在Java的日常应用程序开发中，类的加载几乎是由上述3种类加载器相互配合执行的，在必要时，我们还可以自定义类加载器，来定制类的加载方式。那为什么还需要自定义类加载器？

1. 隔离加载类（比如说我假设现在Spring框架，和RocketMQ有包名路径完全一样的类，类名也一样，这个时候类就冲突了。不过一般的主流框架和中间件都会自定义类加载器，实现不同的框架，中间价之间是隔离的）
2. 修改类加载的方式
3. 扩展加载源（还可以考虑从数据库中加载类，路由器等等不同的地方）
4. 防止源码泄漏（对字节码文件进行解密，自己用的时候通过自定义类加载器来对其进行解密）

##### 如何自定义类加载器？

1. 开发人员可以通过继承抽象类java.lang.ClassLoader类的方式，实现自己的类加载器，以满足一些特殊的需求
2. 在JDK1.2之前，在自定义类加载器时，总会去继承ClassLoader类并重写loadClass()方法，从而实现自定义的类加载类，但是在JDK1.2之后已不再建议用户去覆盖loadClass()方法，而是建议把自定义的类加载逻辑写在findclass()方法中
3. 在编写自定义类加载器时，如果没有太过于复杂的需求，可以直接继承URIClassLoader类，这样就可以避免自己去编写findclass()方法及其获取字节码流的方式，使自定义类加载器编写更加简洁。

**代码示例**

```java
public class CustomClassLoader extends ClassLoader {
    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {

        try {
            byte[] result = getClassFromCustomPath(name);
            if (result == null) {
                throw new FileNotFoundException();
            } else {
                //defineClass和findClass搭配使用
                return defineClass(name, result, 0, result.length);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        throw new ClassNotFoundException(name);
    }
	//自定义流的获取方式
    private byte[] getClassFromCustomPath(String name) {
        //从自定义路径中加载指定类:细节略
        //如果指定路径的字节码文件进行了加密，则需要在此方法中进行解密操作。
        return null;
    }

    public static void main(String[] args) {
        CustomClassLoader customClassLoader = new CustomClassLoader();
        try {
            Class<?> clazz = Class.forName("One", true, customClassLoader);
            Object obj = clazz.newInstance();
            System.out.println(obj.getClass().getClassLoader());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

#### 关于ClassLoader

> ClassLoader 类介绍

ClassLoader类，它是一个抽象类，其后所有的类加载器都继承自ClassLoader（不包括启动类加载器）

sun.misc.Launcher 它是一个java虚拟机的入口应用

##### 获取ClassLoader途径

```java
public class ClassLoaderTest2 {
    public static void main(String[] args) {
        try {
            //1.
            ClassLoader classLoader = Class.forName("java.lang.String").getClassLoader();
            System.out.println(classLoader);
            //2.
            ClassLoader classLoader1 = Thread.currentThread().getContextClassLoader();
            System.out.println(classLoader1);

            //3.
            ClassLoader classLoader2 = ClassLoader.getSystemClassLoader().getParent();
            System.out.println(classLoader2);

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

输出结果

```
null
sun.misc.Launcher$AppClassLoader@18b4aac2
sun.misc.Launcher$ExtClassLoader@1540e19d

Process finished with exit code 0
```

双亲委派机制
--------

### 双亲委派机制原理

Java虚拟机对class文件采用的是**按需加载**的方式，也就是说当需要使用该类时才会将它的class文件加载到内存生成class对象。而且加载某个类的class文件时，Java虚拟机采用的是双亲委派模式，即把请求交由父类处理，它是一种任务委派模式

1.  如果一个类加载器收到了类加载请求，它并不会自己先去加载，而是把这个请求委托给父类的加载器去执行；
2.  如果父类加载器还存在其父类加载器，则进一步向上委托，依次递归，请求最终将到达顶层的启动类加载器；
3.  如果父类加载器可以完成类加载任务，就成功返回，倘若父类加载器无法完成此加载任务，子加载器才会尝试自己去加载，这就是双亲委派模式。
4.  父类加载器一层一层往下分配任务，如果子类加载器能加载，则加载此类，如果将加载任务分配至系统类加载器也无法加载此类，则抛出异常

<img src="https://npm.elemecdn.com/youthlql@1.0.8/JVM/chapter_002/0020.png">

### 双亲委派机制代码演示



#### 举例1

1、我们自己建立一个 java.lang.String 类，写上 static 代码块

```java
public class String {
    //
    static{
        System.out.println("我是自定义的String类的静态代码块");
    }
}
```



2、在另外的程序中加载 String 类，看看加载的 String 类是 JDK 自带的 String 类，还是我们自己编写的 String 类

```java
public class StringTest {

    public static void main(String[] args) {
        java.lang.String str = new java.lang.String();
        System.out.println("hello,atguigu.com");

        StringTest test = new StringTest();
        System.out.println(test.getClass().getClassLoader());
    }
}
```

输出结果：

```
hello,atguigu.com
sun.misc.Launcher$AppClassLoader@18b4aac2
```



程序并没有输出我们静态代码块中的内容，可见仍然加载的是 JDK 自带的 String 类。





把刚刚的类改一下

```java
package java.lang;
public class String {
    //
    static{
        System.out.println("我是自定义的String类的静态代码块");
    }
    //错误: 在类 java.lang.String 中找不到 main 方法
    public static void main(String[] args) {
        System.out.println("hello,String");
    }
}
```

<img src="https://npm.elemecdn.com/youthlql@1.0.8/JVM/chapter_002/0021.png">

由于双亲委派机制一直找父类，所以最后找到了Bootstrap ClassLoader，Bootstrap ClassLoader找到的是 JDK 自带的 String 类，在那个String类中并没有 main() 方法，所以就报了上面的错误。



#### 举例2

```java
package java.lang;


public class ShkStart {

    public static void main(String[] args) {
        System.out.println("hello!");
    }
}
```

输出结果：

```java
java.lang.SecurityException: Prohibited package name: java.lang
	at java.lang.ClassLoader.preDefineClass(ClassLoader.java:662)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:761)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:467)
	at java.net.URLClassLoader.access$100(URLClassLoader.java:73)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:368)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:362)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:361)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:335)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:495)
Error: A JNI error has occurred, please check your installation and try again
Exception in thread "main" 
Process finished with exit code 1
```

即使类名没有重复，也禁止使用java.lang这种包名。这是一种保护机制



#### 举例3

当我们加载jdbc.jar 用于实现数据库连接的时候

1. 我们现在程序中需要用到SPI接口，而SPI接口属于rt.jar包中Java核心api
2. 然后使用双亲委派机制，引导类加载器把rt.jar包加载进来，而rt.jar包中的SPI存在一些接口，接口我们就需要具体的实现类了
3. 具体的实现类就涉及到了某些第三方的jar包了，比如我们加载SPI的实现类jdbc.jar包【首先我们需要知道的是 jdbc.jar是基于SPI接口进行实现的】
4. 第三方的jar包中的类属于系统类加载器来加载
5. 从这里面就可以看到SPI核心接口由引导类加载器来加载，SPI具体实现类由系统类加载器来加载



<img src="https://npm.elemecdn.com/youthlql@1.0.8/JVM/chapter_002/0022.png">



### 双亲委派机制优势



通过上面的例子，我们可以知道，双亲机制可以

1. 避免类的重复加载

2. 保护程序安全，防止核心API被随意篡改

   - 自定义类：自定义java.lang.String 没有被加载。
   - 自定义类：java.lang.ShkStart（报错：阻止创建 java.lang开头的类）

   

沙箱安全机制
--------



1.  自定义String类时：在加载自定义String类的时候会率先使用引导类加载器加载，而引导类加载器在加载的过程中会先加载jdk自带的文件（rt.jar包中java.lang.String.class），报错信息说没有main方法，就是因为加载的是rt.jar包中的String类。
2.  这样可以保证对java核心源代码的保护，这就是沙箱安全机制。



其他
----

### 如何判断两个class对象是否相同？

在JVM中表示两个class对象是否为同一个类存在两个必要条件：

1.  类的完整类名必须一致，包括包名
2.  **加载这个类的ClassLoader（指ClassLoader实例对象）必须相同**
3.  换句话说，在JVM中，即使这两个类对象（class对象）来源同一个Class文件，被同一个虚拟机所加载，但只要加载它们的ClassLoader实例对象不同，那么这两个类对象也是不相等的



### 对类加载器的引用

1.  JVM必须知道一个类型是由启动加载器加载的还是由用户类加载器加载的
2.  **如果一个类型是由用户类加载器加载的，那么JVM会将这个类加载器的一个引用作为类型信息的一部分保存在方法区中**
3.  当解析一个类型到另一个类型的引用的时候，JVM需要保证这两个类型的类加载器是相同的（后面讲）·