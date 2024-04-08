[TOC]
## Hadoop组成：
1. Hadoop HDFS：一个高可靠、高吞吐量的分布式文件系统。
    - NameNode（nn）:
        + 1.存储和管理HDFS集群的元数据
        + 2.响应客户端的读写操作
        + 3.管理整个HDFS集群的（管理HDFS的DN的）
    - DataNode(dn)：在本地文件系统存储文件块数据，以及块数据的校验和。
        + 1.负责存储数据块
        + 2.负责检测DN所在节点上的block块的一个状态
    - Secondary NameNode(2nn)：用来监控HDFS状态的辅助后台程序，每隔一段时间获取HDFS元数据的快照。
2. Hadoop MapReduce：一个分布式的离线并行计算框架。
    - Map阶段并行处理输入数据
    - Reduce阶段对Map结果进行汇总
3. Hadoop YARN：作业调度与集群资源管理的框架。
    - ResourceManager(rm)：处理客户端请求、启动/监控ApplicationMaster、监控NodeManager、资源分配与调度；
    - NodeManager(nm)：单个节点上的资源管理、处理来自ResourceManager的命令、处理来自ApplicationMaster的命令；
    - ApplicationMaster：数据切分、为应用程序申请资源，并分配给内部任务、任务监控与容错。
    - Container：对任务运行环境的抽象，封装了CPU、内存等多维资源以及环境变量、启动命令等任务运行相关的信息。
4. Hadoop Common：支持其他模块的工具模块。