[TOC]
## MapReduce
### MapReduce进程
*** 一个完整的mapreduce程序在分布式运行时有三类实例进程： ***
+ MRAppMaster：负责整个程序的过程调度及状态协调
+ MapTask：负责map阶段的整个数据处理流程(只分，不合)
+ ReduceTask：负责reduce阶段的整个数据处理流程
### MapReduce的编程规范
> 用户编写的程序核心主要分成三个部分：Mapper，Reducer，Driver(提交运行mr程序的客户端)   
+ *** Mapper阶段编程 ***
    - 用户自定义的Mapper要继承父类org.apache.hadoop.mapreduce.Mapper
    - Mapper的输入数据是KV对的形式（KV的类型根据InputFormat定义）
    - Mapper中的业务逻辑写在map()方法中
    - Mapper的输出数据是KV对的形式（KV的类型可自定义）
    - map()方法（maptask进程）对Mapper阶段输入的每一个调用一次
+ *** Reducer阶段编程 ***
   -  用户自定义的Reducer要继承父类org.apache.hadoop.mapreduce.Reducer
    - Reducer的输入数据类型对应Mapper的输出数据类型，也是KV键值对类型
    - Reducer的业务逻辑写在reduce()方法中
    - Reducetask进程对每一组相同k的组调用一次reduce()方法(一组相同的key调用一次reduce方法)
+ *** Driver驱动程序编写 ***
   整个MR程序需要一个Drvier驱动程序用来封装MR程序各个阶段以及来进行代码的提交，提交的是一个描述了各种必要信息的job对象
#### wordcount案例
+ 1.WCMapper    

```java
 /**
 * 第一步 编写Mapper类，Mapper类中主要编写MR程序中Mapper阶段的MapTask的计算逻辑
 * 1、需要让自定义的Java类继承一个MR的类Mapper类
 * 2、继承成功之后，需要定义MapTask输入和输出的key、value数据类型
 *     Map阶段的输入和输出的kv类型必须都得是序列化之后的数据类型，序列化不是Java的序列化，而是Hadoop的序列化机制
 *     int--IntWritable
 *     String-Text
 *     Map阶段的输入类型（默认的类型）：LongWritable Text
 *     Map阶段的输出类型（单词 1）：Text  LongWritable
 * 3、重写一个方法map,map方法中需要编写MapTask的核心计算逻辑
 *
 *
 */

public class WcMapper extends Mapper<LongWritable,Text,Text,LongWritable> {
    /**
     * map方法是MR程序中Mapper阶段每一个MapTask的核心计算逻辑方法
     * map方法是每个MapTask一行触发一次
     * @param key   这一行数据的偏移量
     * @param value 这一行的数据本身
     * @param context  MR程序的上下文对象，用于将Mapper阶段的数据输出到下一个阶段的
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, LongWritable>.Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] values = line.split(" ");
        for (String v : values) {
            context.write(new Text(v),new LongWritable(1L));
        }
    }

}
```

+ 2.WCReducer   

```java
/**
 * 第二步：编写Reducer阶段的计算逻辑
 * 1、自定义类继承Hadoop中Reducer类
 * 2、定义Reducer阶段输入和输出的kv类型
 *         输入类型就是Map阶段的输出类型
 *              Text LongWritable
 *         输出类型以单词为key 以单词的总次数为value
 *              Text LongWritable
 * 3、重写reduce方法
 */
public class WcReducer extends Reducer<Text, LongWritable,Text,LongWritable> {
    /**
     * reduce是reduceTask聚合数据的一个核心逻辑
     * reduce方法一组相同的key触发一次reduce方法的执行
     * @param key  这一组相同的key值
     * @param values  集合  这一组相同key值的value数据的集合
     * @param context 上下文对象
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Reducer<Text, LongWritable, Text, LongWritable>.Context context) throws IOException, InterruptedException {
        long count = 0;
        for (LongWritable value : values) {
            count += value.get();
        }
        context.write(key,new LongWritable(count));
    }
}

```

+ 3.WCDriver    

```java
public class Driver {
    /**
     * Driver是MR程序的驱动类，驱动类是用来整合MR程序的，整合的内容主要包括三方面
     *   1、MR程序的数据输入（来自于HDFS文件系统的）
     *   2、组装MR程序的各个阶段（核心Mapper、Reducer）
     *   3、MR程序的数据输出（HDFS的路径）
     *
     * 编写过程很固定的写法：核心就是一个main函数，Job对象
     *
     * 报错以及问题解决：
     *   1、Exception in thread "main" java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0(Ljava/lang/String;I)Z
     *      错误的原因是因为MR程序在windows上测试的时候也得需要hadoop的环境，但是windows上安装的Hadoop是个假的，不适配 所以导致报错了
     *      报错解决：MR程序底层的框架源码修改一下即可
     *      需要在项目的src/main/java路径下创建一个和源码类一样的包，然后把需要修改的源码类复制进来，把源码改掉：false true
     *   2、hadoop.home or hadoop.tmp.dir not set
     *      是因为Hadoop程序运行需要在本地有Hadoop的“假环境”，代表本地没有安装配置Hadoop的环境变量
     *   3、exitCode=-107xxxx
     *      是因为windows上缺少了一个c语言的运行环境，需要安装一下c语言的运行环境
     *      MSVBCRT_AIO_2018.07.31_X86+X64
     */
    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException, URISyntaxException {
        //1、创建一个Configuration配置文件对象（HDFS编程）
        Configuration conf = new Configuration();
        //配置HDFS的地址 MR程序处理的数据都是HDFS的
        // IP和主机映射：C:\Windows\System32\drivers\etc\HOSTS
        conf.set("fs.defaultFS","hdfs://node1:9000");
        //2、根据配置文件对象获取一个用于封装MR程序的Job对象
        Job job = Job.getInstance(conf);
        //如果MR程序需要打包在服务器上运行，必须增加如下代码，否则在服务器上无法运行
        job.setJarByClass(Driver.class);
        //3、通过Job对象封装MR程序的各个部分：先封装程序的输入路径
        //  /wc/wc.txt
        FileInputFormat.setInputPaths(job,new Path("/wc"));
        //4、封装MR程序的Mapper阶段 除了封装Mapper类 还要封装Mapper阶段的输出的KV类型
        job.setMapperClass(WcMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        //5、封装MR程序的Reducer阶段 除了封装reducer类，还要封装Reducer阶段的输出kv类型
        job.setReducerClass(WcReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);
        //6、封装MR程序结果的输出目录  输出目录一定不能提前存在，如果提前存在会报错
        Path outPath = new Path("/output");
        //通过HDFS代码判断目录是否存在，如果存在删除
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://node1:9000"), conf, "root");
        if(fileSystem.exists(outPath)){
            fileSystem.delete(outPath,true);
        }
        FileOutputFormat.setOutputPath(job,outPath);
        //7、提交MR程序去分布式运行，并且等待执行结果
        boolean flag = job.waitForCompletion(true);
        System.exit(flag?0:1);
    }
}
```

## Hadoop序列化机制
### 1.什么是序列化
> 序列化就是把内存中的对象，转换成字节序列（或其他数据传输协议）以便于存储（持久化）和网络传输;反序列化就是将收到字节序列（或其他数据传输协> 议）或者是硬盘的持久化数据，转换成内存中的对象。   

### 2、序列化的原因以及Java序列化和大数据序列化的区别
+ 一般来说，“活的” 对象只生存在内存里，关机断电就没有了。而且“活的”对象只能由本地的进程使用，不能被发送到网络上的另外一台计算机。然而序列化可以存储"活的” 对象，可以将“活的”对象发送到远程计算机。
+ 在MapReduce程序中，Mapper和Reducer阶段传递数据均是以key、Value类型的形式进行输入和输出，而且因为分布式计算的特性，传输的数据会涉及到跨节点、跨网络中传输，因此数据如果不能进行序列化，很难实现在网络中传输。
+ Java的序列化是一个重量级序列化框架（Serializable），一个对象被序列化后，会附带很多额外的信息（各种校验信息，header，继承体系等），不便于在网络中高效传输。所以，Hadoop自己开发了一套序列化机制（Writable），精简、高效。
+ Hadoop序列化特点:
    - 紧凑:高效使用存储空间。
    - 快速:读写数据的额外开销小。
    - 可扩展:随着通信协议的升级而可升级
    - 互操作:支持多语言的交互
### 3、常用数据序列化类型
### 4、自定义bean对象实现序列化接口
+ 如果Hadoop提供的序列化类型不能满足我们的需求，比如在传输数据时，数据只凭借key、value两个类型无法实现数据的完整输入和输出，此时就需要我们自定义JavaBean将传输的多个数据封装从而实现数据的传输。
+ 自定义的JavaBean对象要想序列化传输，必须实现序列化接口，需要注意以下7项:
    - 必须实现Writable接口
    - 反序列化时，需要反射调用空参构造函数，所以必须有空参构造
    - 重写序列化方法
    - 重写反序列化方法
    - 注意反序列化的顺序和序列化的字段顺序完全一致
    - 要想把结果显示在文件中，需要重写toString()，且用”\t”分开，方便后续用
    - 如果需要将自定义的JavaBean放在key中传输，则还需要实现comparable接口，因为mapreduce计算过程中需要对数据进行排序，排序的规则是基于key值得大小进行比较排序，因此key值必须能被比较大小。
### 5、自定义JavaBean实现Hadoop序列化的示例
+ 1.FlowBean 

```java
/**
 * 自定义JavaBean当作MR的key、value传递
 * 必须实现Hadoop的序列化机制：
 *    如果只当value传递，只需要实现Writable接口就行
 *    如果当作key传递，除了Writable接口，还需要实现Comparable接口
 *          hadoop很贴心，他为了怕我们忘记key值需要比较大小，专门提供了一个接口WritableComparator接口
 */
public class FlowBean implements Writable {
    private String phoneNumber="";
    private Long upFlow;
    private Long downFlow;
    private Long sumFlow = 0L;

    public FlowBean() {
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public Long getUpFlow() {
        return upFlow;
    }

    public void setUpFlow(Long upFlow) {
        this.upFlow = upFlow;
    }

    public Long getDownFlow() {
        return downFlow;
    }

    public void setDownFlow(Long downFlow) {
        this.downFlow = downFlow;
    }

    public Long getSumFlow() {
        return sumFlow;
    }

    public void setSumFlow(Long sumFlow) {
        this.sumFlow = sumFlow;
    }

    /**
     * 序列化写的方法：写属性
     * @param out <code>DataOuput</code> to serialize this object into.
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeUTF(phoneNumber);
        out.writeLong(upFlow);
        out.writeLong(downFlow);
        out.writeLong(sumFlow);
    }

    /**
     * 反序列化读的方法：读属性的值
     * 序列化的顺序和反序列化的顺序必须保持一致
     * @param in <code>DataInput</code> to deseriablize this object from.
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        this.phoneNumber = in.readUTF();
        this.upFlow = in.readLong();
        this.downFlow = in.readLong();
        this.sumFlow = in.readLong();
    }

    @Override
    public String toString() {
        return phoneNumber+"="+upFlow+"="+downFlow+"="+sumFlow;
    }
}
```

+ 2.FlowMapper 

```java
public class FlowMapper extends Mapper<LongWritable, Text,Text,FlowBean> {
    /**
     * 读取到每一行的数据，以\t分割 得到每一个字段，
     * 手机号在第二个字段
     * 上行流量位于倒数第三个字段
     * 下行流量位于倒数第二个字段
     * 以手机号为key  以FlowBean为value
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, FlowBean>.Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] array = line.split("\t");
        //抽取手机号
        String phoneNumber = array[1];
        //抽取上行和下行的流量信息  long类型
        long upFlow =Long.parseLong(array[array.length-3]);
        long downFlow =Long.parseLong(array[array.length-2]);
        //将上行和下行用FlowBean封装
        FlowBean flowBean = new FlowBean();
        flowBean.setUpFlow(upFlow);
        flowBean.setDownFlow(downFlow);
        //以手机号为key 以flowbean为value写出数据
        context.write(new Text(phoneNumber),flowBean);
    }
}
```

+ 3.FlowReducer 

```java
public class FlowReducer extends Reducer<Text,FlowBean, NullWritable,FlowBean> {
    @Override
    protected void reduce(Text key, Iterable<FlowBean> values, Reducer<Text, FlowBean, NullWritable, FlowBean>.Context context) throws IOException, InterruptedException {
        long upFlow = 0;
        long downFlow = 0;
        for (FlowBean value : values) {
            upFlow += value.getUpFlow();
            downFlow += value.getDownFlow();
        }
        long sumFlow = upFlow+downFlow;
        FlowBean flowBean = new FlowBean();
        flowBean.setPhoneNumber(key.toString());
        flowBean.setUpFlow(upFlow);
        flowBean.setDownFlow(downFlow);
        flowBean.setSumFlow(sumFlow);
        //以null为key 以flowbean为value输出
        context.write(NullWritable.get(),flowBean);
    }
}
```

+ 4.FlowDriver  

```java
public class FlowDriver {
    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException, URISyntaxException {
        //1、创建一个Configuration配置文件对象（HDFS编程）
        Configuration conf = new Configuration();
        //配置HDFS的地址 MR程序处理的数据都是HDFS的
        conf.set("fs.defaultFS","hdfs://node1:9000");

        //2、根据配置文件对象获取一个用于封装MR程序的Job对象
        Job job = Job.getInstance(conf);
        //如果MR程序需要打包在服务器上运行，必须增加如下代码，否则在服务器上无法运行
        job.setJarByClass(FlowDriver.class);

        //3、通过Job对象封装MR程序的各个部分：先封装程序的输入路径
        //  /flow
        FileInputFormat.setInputPaths(job,new Path("/flow"));
        //4、封装MR程序的Mapper阶段 除了封装Mapper类 还要封装Mapper阶段的输出的KV类型
        job.setMapperClass(FlowMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(FlowBean.class);

        //5、封装MR程序的Reducer阶段 除了封装reducer类，还要封装Reducer阶段的输出kv类型
        job.setReducerClass(FlowReducer.class);
        job.setOutputKeyClass(NullWritable.class);
        job.setOutputValueClass(FlowBean.class);

        //6、封装MR程序结果的输出目录  输出目录一定不能提前存在，如果提前存在会报错
        Path outPath = new Path("/output");
        //通过HDFS代码判断目录是否存在，如果存在删除
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://node1:9000"), conf, "root");
        if(fileSystem.exists(outPath)){
            fileSystem.delete(outPath,true);
        }

        FileOutputFormat.setOutputPath(job,outPath);
        //7、提交MR程序去分布式运行，并且等待执行结果
        boolean flag = job.waitForCompletion(true);
        System.exit(flag?0:1);
    }
}
```