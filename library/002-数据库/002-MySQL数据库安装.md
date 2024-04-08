[TOC]
# MySQL数据库安装
## 1.访问与下载
### 1.1 商业版
[oracle官网](https://www.oracle.com/cn/)    
![产品](amWiki/images/2.1/3.png)  
![产品](amWiki/images/2.1/4.jpg)  
![产品](amWiki/images/2.1/5.jpg)  
### 1.2 开源免费版
[下载页面](https://www.mysql.com/downloads/)  
点击MySQL Community(GPL)Downloads   
![点击](amWiki/images/2.1/4.png)   
点击MySQL Installer for Windows
![点击](amWiki/images/2.1/5.png) 
版本选择
![版本选择](amWiki/images/2.1/6.jpg)     

## 2.安装
1.找到下载好的安装包文件目录并点击
2.开始安装
3.进入页面后选择最后一个自定义选项之后点击next
![版本选择](amWiki/images/2.1/6.png)  
4.删除三个文件夹
![版本选择](amWiki/images/2.1/7.png)  
```
C:\Program Files\MySQL
C:\Program Files (x86)\MySQL
C:\ProgramData\MySQL\MySQL Server 8.0
``` 
5.点击execute
![版本选择](amWiki/images/2.1/7.jpg)  
6.点击下一步
![版本选择](amWiki/images/2.1/8.jpg)    
![版本选择](amWiki/images/2.1/9.jpg)   
![版本选择](amWiki/images/2.1/10.jpg)   
7.选择Use Legacy Authentication Method (Retain MySQL 5.x Compatibility)
![版本选择](amWiki/images/2.1/11.jpg)   
8.写入密码，添加其他用户
![版本选择](amWiki/images/2.1/12.jpg)   
9.windows service
![版本选择](amWiki/images/2.1/13.jpg)   
10.检查服务是否有MySQL80，如果有，以管理员身份打开cmd,输入sc delete mysql80
11.点击excute

## 3.安装不上的情况
如果卸载不干净导致MySQL安装不上，清理注册表和删除MySQL残留文件再重新安装即可
+ 清理残留文件(保证在控制版本已经把MySQL相关的所有软件全部卸载了)
+ 清理注册表：ccleaner

## 4.MySQL的可视化工具的使用
工具：navicat、chat2db、sqlyog、dbeaver.....
### 4.1 navicat
1.直接搜索navicat   
2.点击navicat   
![版本选择](amWiki/images/2.1/14.jpg)   
3.免费试用  
4.直接下载  
![版本选择](amWiki/images/2.1/15.jpg)   
### 4.2 chat2db
1.搜索chat2db官网   
![版本选择](amWiki/images/2.1/16.jpg)   
2.下载.exe

