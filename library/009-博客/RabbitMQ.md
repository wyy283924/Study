## RabbitMQ

消息队列是一种用于应用程序之间传递信息的通信方式，消息队列允许应用程序异步发送和接收消息，并且不需要直接连接到对方。

**作用：**

+ 异步处理

  上游系统或者服务只需要处理完核心业务即可返回，无需同步调用相关的下游系统或者服务。异步调用比同步调用具有更强的容错性，在下游系统短期故障时可以保证上有系统正常运行，而且可以提高核心业务的响应速度。如：电商平台的下单处理流程，如果所有流程都依次处理，则下单的响应时间是无法保证的，而且只要有一个处理流程出现异常，下单就无法完成。

+ 应用解耦

  由于使用了消息中间件，系统与系统或者服务与服务之间不再有点对点调用的耦合关系

+ 缓冲

  大多数的消息中间件会内嵌消息队列来保存消息，借助这个特性，可以将瞬发的大量请求放入消息中间件，从而避免大量的并发请求冲击下游系统，如：电商抢购的流量消峰、日志采集的日志缓存都属于这类应用场景。

AMQP：即Advanced Message Queuing Protocol,是一个应用层协议，为面向消息的中间件设  计。基于此协议的客户端与消息中间件可传递消息，并不受客户端/中间件的不同产品、不同的开发语言等条件的限制。

### RabbitMQ的安装

### 1. 文件下载

RabbitMQ：https://packagecloud.io/rabbitmq/erlang/packages/el/7/erlang-23.3.4.11-1.el7.x86_64.rpm/
		erlang：https://packagecloud.io/rabbitmq/erlang/packages/el/7/erlang-23.3.4.11-1.el7.x86_64.rpm/download.rpm?distro_version_id=140

### 2. 安装文件

#### 2.1 安装命令

rpm -ivh erlang-23.3.4.11-1.el7.x86_64.rpm

yum install socat -y

rpm -ivh rabbitmq-server-3.8.16-1.el7.noarch.rpm

开机启动：chkconfig rabbitmq-server on

启动服务：/sbin/service rabbitmq-server start

查看服务状态：/sbin/service rabbitmq-server status

停止服务(选择执行)：/sbin/service rabbitmq-server stop

开启web管理插件（先将服务关闭掉）：rabbitmq-plugins enable rabbitmq_management

访问地址：http://192.168.16.128:15672/（默认端口号：15672），如果遇到访问不了，看看是否防火墙开着

关闭防火墙：systemctl stop firewalld

开机关闭防火墙：systemctl disable firewalld

查看防火墙状态：systemctl status firewalld

#### 2.2 添加一个新的用户

1. 创建账号

   rabbitmqctl add_user admin 123456

2. 设置用户角色

   rabbitmqctl set_user_tags admin administrator

3. 设置用户权限

   rabbitmqctl set_permissions [-p <vhostpath>] <user> <conf> <write> <read>

   rabbitmqctl set_permissions -p “/” admin “.*” “.*” “.*”

   用户admin具有/vhost1这个virtual host中所有的配置，写，读权限

4. 查询当前用户和角色

   rabbitmqctl list_users

### RabbitMQ的工作原理

**Broker**:接收和分发消息的应用，RabbitMQ Server 就是 Message Broker

**Virtual host**: Virtual host是一个虚拟主机的概念，一个Broker中可以有多个Virtual host,每个Virtual host都有一套自己的Exchange和Queue,同一个Virtual host中的Exchange和Queue不能重名，不同的Virtual host中的Exchange和Queue名字可以一样。这样，不同的用户在访问一个RabbitMQ Broker时，可以创建自己单独的Virtual host,然后在自己的Virtual host中创建Exchange和Queue,很好地做到了不同用户之间相互隔离的效果。

**Connection**:发送消息的通道，如果每一次访问RabbitMQ都建立一个Connection,在消息量大的时候建立TCP Connection的开销将是巨大的，效率也较低。Channel是在connection内部建立的逻辑连接，如果应用程序支持多线程，通常每个thread创建单独的channel进行通讯，AMQP method包含了 channel id 帮助客户端和message broker识别 channel,所以channel之间是完全隔离的。Channel作为轻量级的Connection极大减少了操作系统建立TCP connection的开销

**Exchange**:message到达broker的第一站，根据分发规则，匹配查询表中的routing key,分发消息到queue中去。常用的类型有：direct(point-to-pointer),topic(publish-subscribe) and fanout (multicast)

**Queue** : Queue是一个用来存放消息的队列，生产者发送的消息会被放到Queue中，消费者消费消息时也是从Queue中取走消息。

**Binding** : exchange 和 queue 之间的虚拟连接，binding 中可以包含 routing key,Binding 信息被保存到 exchange 中的查询表中，用于 message 的分发依据

### 如何实现生产者和消费者

#### 1. 引入包依赖

```java
<dependency>
	<groupId>com.rabbitmq</groupId>
	<artifactId>amqp-client</artifactId>
	<version>5.7.3</version>
</dependency>
```

#### 2. 生产者代码

```java
import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Producer {

    //队列名
    private static final String QUEUE_NAME = "hello-queue";
    //交换机
    private static final String EXCHANGE_NAME = "hello-exchange";

    public static void main(String[] args) throws Exception {
        //创建一个连接工厂
        ConnectionFactory factory = new ConnectionFactory();
        //服务地址
        factory.setHost("192.168.16.128");
        //账号
        factory.setUsername("admin");
        //密码
        factory.setPassword("123456");
        //端口号
        factory.setPort(5672);
        //创建连接
        Connection connection = factory.newConnection();
        //创建信道
        Channel channel = connection.createChannel();
        /**
         * 声明和创建交换机
         * 1.交换机的名称
         * 2.交换机的类型：direct、topic或者fanout和headers， headers类型的交换器的性能很差，不建议使用。
         * 3.指定交换机是否要持久化，如果设置为true，那么交换机的元数据要持久化到内存中
         * 4.指定交换机在没有队列与其绑定时，是否删除，设置为false表示不删除；
         * 5.Map<String, Object>类型，用来指定交换机其它一些结构化的参数，我在这里直接设置为null。
         */
        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.DIRECT, false, true, null);

        /**
         * 生成一个队列
         * 1.队列的名称
         * 2.队列是否要持久化，但是需要注意，这里的持久化只是队列名称等这些队列元数据的持久化，不是队列中消息的持久化
         * 3.表示队列是不是私有的，如果是私有的，只有创建它的应用程序才能从队列消费消息；
         * 4.队列在没有消费者订阅时是否自动删除
         * 5.队列的一些结构化信息，比如声明死信队列、磁盘队列会用到。
         */
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);

        /**
         * 将交换机和队列进行绑定
         * 1.队列名称
         * 2.交换机名称
         * 3.路由键，在直连模式下为队列名称。
         */
        channel.queueBind(QUEUE_NAME, EXCHANGE_NAME, QUEUE_NAME);
        /**
         * 发送消息
         * 1.发送到哪个交换机
         * 2.队列名称
         * 3.其他参数信息
         * 4.发送消息的消息体
         */
        String message = "hello world";
        channel.basicPublish(EXCHANGE_NAME, QUEUE_NAME, null, message.getBytes());
        System.out.println("消息发送成功");
    }
}
```

#### 3. 消费者代码

```java
import com.rabbitmq.client.CancelCallback;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DeliverCallback;

public class Consumer {

    //队列名
    private static final String QUEUE_NAME = "hello-queue";

    public static void main(String[] args) throws Exception {

        //创建一个连接工厂
        ConnectionFactory factory = new ConnectionFactory();
        //服务地址
        factory.setHost("192.168.16.128");
        //账号
        factory.setUsername("admin");
        //密码
        factory.setPassword("123456");
        //端口号
        factory.setPort(5672);
        //创建连接
        Connection connection = factory.newConnection();
        //创建信道
        Channel channel = connection.createChannel();

        //接受消息回调
        DeliverCallback deliverCallback = (consumerTag, message)-> {
            System.out.println(new String(message.getBody()));
        };
        
        /**
         * 消费消息
         * 1.消费哪个队列
         * 2.消费成功之后是否要自动应答，ture:自动应答
         * 3.消费者未成功消费的回调
         * 4.消费者取消消费的回调
         */
        channel.basicConsume(QUEUE_NAME, true, deliverCallback, cancelCallback);

    }
}
```

### RabbitMQ交换机类型

#### 1. direct

路由键与队列名完全匹配交换机，此种类型交换机，通过RoutingKey路由键将交换机和队列进行绑定，消息被发送到exchange时，需要根据消息的RoutingKey,来进行匹配，只将消息发送到完全匹配到此RoutingKey的队列。

比如：如果一个队列绑定到交换机要求路由键为“key”,则只转发RoutingKey标记为“key”的消息，不会转发“key1”,也不会转发“key.1”等等。它是完全匹配、单播的模式。

同一个key可以绑定多个queue队列；当匹配到key1时，queue1和queue2都可以收到消息

#### 2. fanout

Fanout,扇出类型交换机，此种交换机，会将消息分发给所有绑定了此交换机的队列，此时，RoutingKey参数无效。

fanout类型交换机下发送消息一条，无论RoutingKey时什么，queue1,queue2,queue3,queue4都可以收到消息。

#### 3. topic

Topic,主题类型交换机，此种交换机与Direct类似，也是需要通过routingkey进行匹配分发，区别在于Topic可以进行模糊匹配，Direct是完全匹配。

1. Topic中，将routingkey通过“.”来分为多个部分
2. “*” ：代表一个部分
3. “#”：代表0个或多个部分（如果绑定的路由键为“#”时，则接受所有消息，因为路由键所有都匹配）

然后发送一条消息，routingkey为“key1.key2.key3.key4”,那么根据“.”将这个路由键分为了4个部分，此条路由键，将会匹配：

1. key1.key2.key3.*：成功匹配，因为 *可以代表一个部分

2. key1.#：成功匹配，因为#可以代表0或多个部分

3. *.key2.*.key4：成功匹配，因为第一和第三部分分别为key1和key3,且为4个部分，刚好匹配

4. #.key3.key4：成功匹配，#可以代表多个部分，正好匹配中了我们的key1和key2

   如果



