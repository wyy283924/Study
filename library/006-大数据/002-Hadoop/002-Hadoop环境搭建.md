[TOC]
# Hadoop环境搭建  

## Linux的前期准备  

### 更改IP的命令（如果需要更改的话）  
> vim /etc/sysconfig/network-scripts/ifcfg-ens33  
> 重启网络使IP生效：systemctl restart network  
> 检查是否更改成功：ping www.baidu.com  

### 配置Linux系统的主机名  
查看系统的主机名：
> hostname   

修改主机名需要更改一个配置文件：
> vim /etc/hostname   

重启生效：  
> reboot  

### 配置Linux系统的域名和IP的映射关系  
> vim	/etc/hosts  
> IP地址(ip addr)  域名（一般与主机名相同）  
> :wq(保存文件并退出)  

### 配置免密登录  
生成公钥密钥(只需要生成1次)  
>	ssh-keygen -t rsa（回车四次生成完毕）  

发送公钥给要配置的目标用户  
>	ssh-copy-id 用户名@IP/域名(自己在/etc/hosts中配置的映射关系)   
>	输入目标用户密码，出现"number(1)"等提示添加成功的信息表示配置免密登录成功！  

克隆出来的虚拟机删除之前的公钥密钥  
>	cd ~/.ssh  
>		rm -rf *(删除之前的公钥密钥)  

## Hadoop运行环境搭建  

### Linux的环境变量配置  
全部都是通过更改配置文件和命令来操作  
Linux上的环境变量配置文件有很多  
> 系统变量   /etc/profile  
> 用户变量  ~/.bash_profile  

用于存放软件的目录:/opt/app 。  
> vim /etc/profile  

在配置文件中加入以下代码：  
> export JAVA_HOME=/opt/app/jdk  
> export PATH=$PATH:$JAVA_HOME/bin    
> export HADOOP_HOME=/opt/app/hadoop  
> export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin  
> 【注意】HADOOP 3.X版本还需要增加如下配置  
> export HDFS_NAMENODE_USER=root  
> export HDFS_DATANODE_USER=root  
> export HDFS_SECONDARYNAMENODE_USER=root  
> export YARN_RESOURCEMANAGER_USER=root  
> export YARN_NODEMANAGER_USER=root  

然后:wq保存退出，让配置文件生效：  
> [root@node1 /]# source /etc/profile  

检查Java环境和Hadoop环境:  
> java -version  
> hadoop version  

### Hadoop伪分布环境搭建  

#### Hadoop核心配置文件解析  
> Hadoop的安装就是进行各种配置文件的修改  所有的Hadoop配置文件都在Hadoop的安装目录的etc/hadoop下  
> Hadoop中有如下几个核心配置文件  
>   hadoop-env.sh: hadoop依赖环境配置  
>   core-site.xml ： hadoop 公共运行配置项配置文件：  
>   hdfs-site.xml ： hdfs相关配置项配置文件；  
>   mapred-env.sh ： mapreduce运行环境配置  
>   mapred-site.xml ： mapreduce配置项配置文件；  
>   yarn-env.sh  :   yarn环境变量配置文件  
>   yarn-site.xml ： yarn配置项配置文件；  
> 所有的参数配置，可以配置在一起的，只不过分开配置，便于管理；  

#### hadoop伪分布需修改的配置文件  

##### 配置Hadoop的公共配置文件core-site.xml    
> vim /opt/app/hadoop/etc/hadoop/core-site.xml  
> <!--在configuration标签中增加如下配置-->  
> <!-- 指定HDFS中NameNode的地址 -->  
> <property>  
>   <name>fs.defaultFS</name>  
>   <value>hdfs://node1:9000</value>  
> </property>  
> <!-- 指定hadoop运行时产生文件的存储目录  HDFS相关文件存放地址-->  
> <property>  
>   <name>hadoop.tmp.dir</name>  
>   <value>/opt/app/hadoop/metaData</value>  
> </property>  

##### 配置HDFS的配置文件  
> vim /opt/app/hadoop/etc/hadoop/hdfs-site.xml  
> <!-- 指定HDFS副本的数量 -->  
> <property>  
>   <name>dfs.replication</name>  
>   <value>1</value>  
> </property>  

##### 配置YRAN的相关配置文件  
* 配置yarn-env.sh  
> vim /opt/app/hadoop/etc/hadoop/yarn-env.sh  
>   配置JAVA_HOME  
>   export JAVA_HOME=/opt/app/jdk  

* 配置yarn-site.xml  
> <!-- reducer获取数据的方式 -->  
>   <property>  
>   <name>yarn.nodemanager.aux-services</name>  
>   <value>mapreduce_shuffle</value>  
>   </property>  
> 
>   <!-- 指定YARN的ResourceManager的地址 -->  
>   <property>  
>   <name>yarn.resourcemanager.hostname</name>  
>   <value>node1</value>  
>   </property>  
>   <property>  
>       <name>yarn.application.classpath</name>  
>       <value>  
>       /opt/app/hadoop/etc/hadoop,  
>       /opt/app/hadoop/share/hadoop/common/*,  
>       /opt/app/hadoop/share/hadoop/common/lib/*,  
>       /opt/app/hadoop/share/hadoop/hdfs/*,  
>       /opt/app/hadoop/share/hadoop/hdfs/lib/*,  
>       /opt/app/hadoop/share/hadoop/mapreduce/*,  
>       /opt/app/hadoop/share/hadoop/mapreduce/lib/*,  
>       /opt/app/hadoop/share/hadoop/yarn/*,  
>       /opt/app/hadoop/share/hadoop/yarn/lib/*  
>       </value>  
>   </property>  

##### 配置MapReduce相关配置文件  
* 配置mapred-env.sh  
> export JAVA_HOME=/opt/app/jdk  

* 配置： (对mapred-site.xml.template重新命名为) mapred-site.xml  
> <!-- 指定mr运行在yarn上 -->  
>   <property>  
>       <name>mapreduce.framework.name</name>  
>       <value>yarn</value>  
>   </property>  
> 
>   <!-- 指定MR APP Master需要用的环境变量  hadoop3.x版本必须指定-->  
>   <property>  
>       <name>yarn.app.mapreduce.am.env</name>    
>       <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>  
>   </property>  
>   <!-- 指定MR 程序 map阶段需要用的环境变量 hadoop3.x版本必须指定-->  
>   <property>  
>       <name>mapreduce.map.env</name>  
>       <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>  
>   </property>  
>   <!-- 指定MR程序 reduce阶段需要用的环境变量 hadoop3.x版本必须指定-->  
>   <property>  
>       <name>mapreduce.reduce.env</name>  
>       <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>  
>   </property>  

#### 格式化NameNode   
> [root@node1 /]# hdfs namenode -format    

#### 启动HDFS和YARN集群    
> HDFS的启动：start-dfs.sh  
> YARN的启动：start-yarn.sh  

#### 启动成功的标签  
> 使用JPS命令可以看到如下进程  
> NameNode  
> DataNode  
> SecondaryNameNode  
> ResourceManager  
> DataManager  

#### 启动成功之后的Hadoop的相关访问地址  
* NameNode的访问地址  
> <!--hadoop2.x版本 ： http://ip:50070  
>       hadoop3.x版本：  http://ip:9870  
>   可以在hdfs.site.xml修改配置项更改默认访问端口-->   
>   <property>  
>       <name>dfs.namenode.http-address</name>  
>       <value>0.0.0.0:9870</value>  
>   </property>    
 
* DataNode的访问地址    
> <!--hadoop2.x版本 ： http://ip:50075  
>       hadoop3.x版本：  http://ip:9864  
>   可以在hdfs.site.xml修改配置项更改默认访问端口-->  
>   <property>  
>       <name>dfs.datanode.http.address</name>  
>       <value>0.0.0.0:9864</value>  
>   </property>   

* SecondaryNameNode的访问地址    
> <!--hadoop2.x版本 ： http://ip:50090  
>       hadoop3.x版本：  http://ip:9868  
>   可以在hdfs.site.xml修改配置项更改默认访问端口-->  
>   <property>  
>       <name>dfs.namenode.secondary.http-address</name>  
>       <value>0.0.0.0:9864</value>  
>   </property>  

* yarn的访问地址  
> <!--hadoop2.x版本 ： http://ip:8088  
>       hadoop3.x版本：  http://ip:8088  
>   可以在yarn-site.xml修改配置项更改默认访问端口-->  
>   <property>  
>       <name>yarn.resourcemanager.webapp.address</name>  
>       <value>0.0.0.0:8088</value>  
>   </property>  
> 

**【问题】HDFS的Block块大小一般是128MB原因是**  
**【答案】HDFS中平均寻址时间大概为10ms; 经过前人的大量测试发现,寻址时间为传输时间的1%时,为最佳状态; 所以最佳传输时间为10ms/0.01=1000ms=1s 目前磁盘的传输速率普遍为100MB/s; 计算出最佳block大小:100MB/s x 1s = 100MB 所以我们设定block大小为128MB。**    


## 完全分布式环境配置(最少三个节点)
1. 准备三台虚拟机、配置静态IP、主机名、主机和IP的映射、ssh免密登录、关闭防火墙
    - 克隆虚拟机可以快速的创建多台主机出来，但是克隆的虚拟机需要手动更改配置文件修改ip地址
    - ip addr查看主机的IP地址和mac地址的
    - /etc/sysconfig/network-scripts/ifcfg-ens33改IP地址和mac地址
2. 安装配置JDK
3. 安装配置Hadoop环境环境
4. 配置时间同步
    - 安装：yum install -y ntp
    - 修改ntp配置文件
        ```
            [root@node1 桌面]# vi /etc/ntp.conf
            修改内容如下:
            a）修改1:其中192.168.1.0代表虚拟机网络的IP段
            #restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap为restrict 192.168.100.0 mask 255.255.255.0 nomodify notrap
            b）修改2:
            server 0.centos.pool.ntp.org iburst
            server 1.centos.pool.ntp.org iburst
            server 2.centos.pool.ntp.org iburst
            server 3.centos.pool.ntp.org iburst
            #将这四行注释
            #server 0.centos.pool.ntp.org iburst
            #server 1.centos.pool.ntp.org iburst
            #server 2.centos.pool.ntp.org iburst
            #server 3.centos.pool.ntp.org iburst
            c）添加3:
            server 127.127.1.0
            fudge 127.127.1.0 stratum 10
        ```
    - 修改/etc/sysconfig/ntpd 文件
        ```
            [root@node1 桌面]# vim /etc/sysconfig/ntpd
            增加内容如下
            SYNC_HWCLOCK=yes
        ```
    - 重新启动ntpd
        ```
            [root@node1 桌面]# service ntpd status
            ntpd 已停
            [root@node2 桌面]# service ntpd start
            正在启动 ntpd： 
        ```
    - 开机自启动
        ```
            chkconfig ntpd on
        ```
    - 其他机器配置（必须root用户）
        ```
            crontab -e
              */10 * * * * /usr/sbin/ntpdate node2 10分钟与node2同步一次
        ```
5. 修改Hadoop的配置文件（HDFS、YARN，在haddop地安装目录/etc/haddop下）
    - hadoop-env .sh

        ```
        1. 配置jdk关联 （jdk的安装目录）
        2. 配置Hadoop关联 （Hadoop的安装目录）
        3. 配置Hadoop_dir关联 （在haddop地安装目录/etc/haddop）
        ```
    - core-site. xml

        ```
            <!-- 指定HDFS中NameNode的地址 -->
            <property>
                <name>fs.defaultFS</name>
                <value>hdfs://node1:9000</value>
            </property>
            <!-- 指定hadoop运行时产生文件的存储目录 -->
            <property>
                <name>hadoop.tmp.dir</name>
                <value>/opt/app/hadoop/metaData</value>
            </property>
        ```
    - hdfs-site.xml

        ```
            <property>
            <name>dfs.replication</name>
            <value>3</value>
            </property>
            <!--secondary namenode地址-->
            <property>
                <name>dfs.namenode.secondary.http-address</name>
                <value>node3:50090</value>
            </property>
            <!--hdfs取消用户权限校验-->
            <property>
                <name>dfs.permissions.enabled</name>
                <value>false</value>
            </property>

            <!--如果为true（默认值），则namenode要求必须将连接datanode的地址解析为主机名
            如果datanode配置的是主机名  那么此项可以不用填写 默认值为true 但是必须对主机名在/etc/hosts文件中配置主机映射
            如果datanode配置的是IP  那么需要将这个值改为false  否则IP会当作主机名进行主机ip校验
            注意：默认情况下配置hadoop使用的是host+hostName的配置方式 datanode需要配置为主机名
            -->
            <property>
                <name>dfs.namenode.datanode.registration.ip-hostname-check</name>
                <value>true</value>
            </property>
        ```
    - yarn-site.xml

        ```
            <!-- reducer获取数据的方式 -->
            <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
            </property>

            <!-- 指定YARN的ResourceManager的地址 -->
            <property>
            <name>yarn.resourcemanager.hostname</name>
            <value>node1</value>
            </property>
            <property>
                <name>yarn.application.classpath</name>
                <value>
                /opt/app/hadoop/etc/hadoop,  //改成自己电脑上的目录
                /opt/app/hadoop/share/hadoop/common/*,
                /opt/app/hadoop/share/hadoop/common/lib/*,
                /opt/app/hadoop/share/hadoop/hdfs/*,
                /opt/app/hadoop/share/hadoop/hdfs/lib/*,
                /opt/app/hadoop/share/hadoop/mapreduce/*,
                /opt/app/hadoop/share/hadoop/mapreduce/lib/*,
                /opt/app/hadoop/share/hadoop/yarn/*,
                /opt/app/hadoop/share/hadoop/yarn/lib/*
                </value>
            </property>
        ```
    - mapred-site. xml

        ```
            <!-- 指定mr运行在yarn上 -->
            <property>
                <name>mapreduce.framework.name</name>
                <value>yarn</value>
            </property>

            <!-- 指定MR APP Master需要用的环境变量  hadoop3.x版本必须指定-->
            <property>
                <name>yarn.app.mapreduce.am.env</name>
                <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
            </property>
            <!-- 指定MR 程序 map阶段需要用的环境变量 hadoop3.x版本必须指定-->
            <property>
                <name>mapreduce.map.env</name>
                <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
            </property>
            <!-- 指定MR程序 reduce阶段需要用的环境变量 hadoop3.x版本必须指定-->
            <property>
                <name>mapreduce.reduce.env</name>
                <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
            </property>
        ```
    - workers
        ```
            node1
            node2
            node3
        ```
6. 为集群上其他主机分发配置好的Hadoop文件
    ```
        scp -r /opt/app/hadoop root@node2:/opt/app
        scp -r /opt/app/hadoop root@node3:/opt/app
    ```
7. 格式化HDFShdfs namenode -format
8. 启动HDFS和YARN:start-dfs/yarn.sh
9. 检查是否启动成功:jps
10. 查看端口号netstat -untlp
11. 关闭HDFS和YARN：stop-dfs/yarn.sh
## 环境配置出现的错误
1.  - 错误：linux 启动network报错file exists
    - 解决方法：systemctl disable NetWorkManager

2.  - 错误：您在 /var/spool/mail/root 中有新邮件
    - 解决方法：
        ```
            1. 删除邮件:
            cat /dev/null > /var/spool/mail/root
            2. 禁止系统检查邮件:
            echo "unset MAILCHECK" >> /etc/profile
            source /etc/profile
        ```