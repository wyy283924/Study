```
作者：支鹏  
时间：2021年2月
```
[TOC]
## Linux安装MySQL教程
### 安装包准备（下载上传到服务器或者使用wget命令直接下载到服务器） 
**[MySQL5的yum仓库的rpm包](http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm)**  
**[MySQL8的yum仓库的rpm包](https://dev.mysql.com/get/mysql80-community-release-el7-4.noarch.rpm)**  

### 安装步骤
* **0、下载MySQL的yum仓库的RMP包（MySQL5和MySQL8二选一）**  
    ```sh
    # 先切换到opt路径
    [root@localhost ~]# cd /opt
    # mysql5版本
    [root@localhost opt]# wget http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
    # mysq8版本
    [root@localhost opt]# wget https://dev.mysql.com/get/mysql80-community-release-el7-4.noarch.rpm
    ```
* **1、安装MySQL的yum仓库的rpm包（MySQL5和MySQL8二选一）**
    ```sh
    #安装MySQL5的yum仓库
    rpm -ivh mysql57-community-release-el7-10.noarch.rpm
    #安装MySQL5的yum仓库
    rpm -ivh mysql80-community-release-el7-4.noarch.rpm
    ```
* **2、yum安装MySQL（MySQL5和MySQL8同命令）**
    ```sh
    yum install -y mysql-server
    ```
    * 安装如果报错**获取 GPG 密钥失败**，原因是因为进行了gpg文件校验，关闭文件校验即可，操作方式如下：
        ```sh
        c
        将文件中所有的gpgcheck选型的值改为0
        ```
* **3、启动MySQL（MySQL5和MySQL8同命令）**
    ```sh
    #启动命令
    service mysqld start | systemctl start mysqld
    #查看运行状态
    service mysqld status | systemctl status mysqld
    ```
* **4、登录MySQL**
    ```sh
    #注 第一次登录MySQL需要查看MySQL的初始密码 查看方式
    cat /var/log/mysqld.log | grep "temporary password"
    # 查看到的密码：A temporary password is generated for root@localhost: 你的密码
    #登录  初始密码不能直接写到-p后  mysql -uroot -p 回车提示密码之后再输入
    mysql -uroot -p  回车写密码
    ```
* **5、修改密码**
    ```sql
    # 建议修改的密码最好包含大写字母 小写字母 数字 特殊符号几种，长度不少于8字符，否则MySQL认为密码简单。不允许修改，如果就是需要修改为简单密码，在MySQL中执行以下两行代码
    mysql> set global validate_password_length=1;
    mysql> set global validate_password_policy=0;
    # MySQL5版本修改密码
    mysql> set password = password("root");
    # MySQL8版本修改密码
    mysql> alter user 'root'@'localhost'IDENTIFIED BY 'Ww361958@';
    mysql> flush privileges;
    ```
* **6、赋予MySQL远程连接访问的权限**
    
    ```sh
    # mysql5版本开启远程MySQL访问权限
    mysql>GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '远程连接时的密码（一般为自己的MySQL密码）' WITH GRANT OPTION;
    mysql> FLUSH PRIVILEGES;
    # MySQL8版本开启远程MySQL访问权限
    mysql> CREATE USER 'root'@'%' IDENTIFIED BY 'Ww361958@'; 
    mysql> GRANT ALL ON *.* TO 'root'@'%'; 
    mysql> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'Ww361958@';
    mysql> FLUSH PRIVILEGES;
    ```