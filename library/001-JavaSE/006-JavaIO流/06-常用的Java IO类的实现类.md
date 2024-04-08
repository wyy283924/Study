[TOC]
# 常用的Java IO类的实现类

##	节点流：直接连接到数据源上
###		文件流：连接文件数据源
			FileInputStream：字节输入流
			FileOutputStream：字节输出流
			FileReader：字符输入流
			FileWriter：字符输出流
			输入流：如果输入流连接的文件不存在，会报错FileNotFoundException
			输出流：有两种输出方式、覆盖输出，追加输出，如果文件不存在，会自动创建

###		数组流：连接内存中的数组数据源
			ByteArrayInputStream：将内存中一个字节数组以IO流的形式读取到Java程序中
			ByteArrayOutputStream：将Java程序中的数据输出到内存的一个字节数组中
			CharArrayReader
			CharArrayWriter

###		网络流

##	处理流：用来连接到节点流上，给节点流提供更加强大的功能的

###		缓冲流：
            内部维护了缓冲池，缓冲流可以连接连接另外一个处理流或者节点流，然后加快节点流的处理速度。
			缓冲池的作用就是当缓冲流连接到目的流上，读取数据的时候先把数据源的数据读取到缓冲池中，以后写出和读取数据的时候直接从缓冲池操作。缓冲池默认一般是8092字节的
			BufferedInputStream
			BufferedOutputStream
			BufferedReader
			BufferedWriter

###		转换流
			将一个字节流以指定的编码集转换为字符流的，解决了字符流处理数据乱码问题的
			InputStreamReader
			OutputStreamWriter

###		对象流：Java序列化机制
			序列化机制指的是将一个Java对象转换成为二进制数据，或者将一个二进制数据转换成为Java对象，Java序列化和反序列化。以后开发Java程序中，可能会涉及到Java对象数据的网络传输，Java对象数据如果想要通过网络进行传输，必须得是二进制数据才能进行传输
			对象流只有字节流，没有字符流

			ObjectInputStream
				对象输入流，反序列化机制，将一个二进制数据转换成为Java对象使用
			ObjectOutputStream
				对象输出流，序列化机制，可以将一个Java对象输出成为二进制数据
            如果一个Java对象想被转换二进制或者从二进制转换回来，那么对象必须是能被序列化的，Java中定义的类默认都不能被序列化，如果想被序列化，必须实现Java中序列化接口。

			Java中序列化接口有两个

				Serializable：没有任何的抽象方法，子类不需要重写任何的方法，一旦一个类实现了Serializable接口之后，如果不想让哪个属性被序列化，那么只需要让这个属性使用static或者transient修饰了即可

				Externalizable：里面有两个抽象方法
				writeExternal：序列化写出的方法
                readExternal：反序列化读取的方法
                要求类中必须有无参构造器

                对象序列化写出的二进制数据只包含了对象的属性和属性值。

			Java中任何一个类实现了序列化接口，最好定义一个属性serialVersionUID，这个属性是用来表示当前类的序列化版本的。每一次类变动之后，必须要把这个版本值更改一下，防止以前写出的二进制数据的反序列化。
###		打印流
只有输出流，print,println
System.in键盘输入流 System.out控制台输出流