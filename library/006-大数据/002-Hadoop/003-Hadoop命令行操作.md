[TOC]
## HDFS命令
1. 上传文件到HDFS上
    - hdfs dfs -put 本地文件路径HDFS文件路径
    - hdfs dfs -copyFromLocal本地文件路径HDFS文件路径
    - hdfs dfs -moveFormLocal本地文件路径 HDFS文件路径下载
2. 文件到本地（HDFS的安装的主机）上
    - hdfs dfs -get hdfs路径本地路径
    - hdfs dfs -copyToLocal hdfs路径本地路径
    - hdfs dfs -moveToLocal hdfs路径本地路径﹑官方提供了但是未实现
3. 删除HDFS上的文件
    - hdfs dfs -rm -r HDFS文件路径
4. 重命名HDFS上的文件，移动文件
    - hdfs dfs -mv HDFS路径HDFS路径
5. 复制HDFS上的文件到HDFS的某一个目录下
    - hdfs dfs -cp hdfs路径HDFS路径
6. 在HDFS上创建文件夹
    - hdfs dfs -mkdir [-p] hdfs目录路径
7. 在HDFS上创建文件--不使用
    - hdfs T dfs -touch hdfs文件路径
8. HDFs没有编辑文件的命令，HDFS一般不允许用户编辑文件，只允许用户上传或者下载、重命名等等操作去操作文件，不支持编辑文件。HDFS适合一次写入，多次查询的场景
9. HDFS支持查看文件内容
    - hdfs dfs -cat HDFS文件路径
    - hdfs dfs -tail -fHDFS文件路径
10. 给HDFs上的文件设置权限、设置用户、设置用户组（与linux操作一样，只是在前面加一个hdfs dfs）
kill -9 进程号
hadoop-daemon.sh start datanode