[TOC]
# MySQL的基本操作
## MySQL连接
前提：必须启动MySQL软件服务，注册windows服务
```
mysql  -u用户名  -p密码  -P端口号
```
## SQL语言的基本使用
### SQL语言管理数据库一共分为四种
+ DDL语言：数据库定义语言，创建、删除、修改、查询数据库和数据表的语言
create  drop  alter  show
+ DML语言：数据操纵语言，增加删除修改表数据的
insert  update  delete
+ DQL语言：数据查询语言，查询表数据的语言
select 
+ DCL/TCL语言：事物控制语言
### 基本操作
```
1、查看MySQL有哪些数据库：show databases;
2、创建MySQL数据库：create database  database_name;
3、使用某一个数据库：use  数据库名
4、查看数据库中有哪些数据库表：show  tables;
5、创建数据表：create table  table_name(
     column_name int,
     column_name  varchar(20)
)
6、查看数据表的结构：desc  table_name;
7、查询表数据：select * from table_name;
8、向数据表中添加数据：insert table  table_name(字段列表)  values(值列表)
9、删除表数据：delete from  table_name;
10、删除数据表：drop table table_name;
11、删除数据库：drop database database_name;
```
[注意]一般在项目当中，我们需要创建多张数据表以及需要向数据表中添加一些测试数据，而数据表的创建和测试数据的添加我们一般都是通过SQL语句编写的。而这些SQL语句我们一般都会存储到一个后缀名为.sql文件中，然后在MySQL中通过source  xxx.sql文件统一一次性把SQL文件中所有的代码全部给执行了
## RDBMS操作数据库和数据时，使用SQL语句来完成操作
### SQL语言当中，#代表注释语法
### DDL语句：数据定义语言
DDL语言主要是用来负责数据库和数据表的管理操作，负责数据库和数据表的创建、修改、删除、查询等等操作  
```
主要涉及到的关键字：create  alter  drop  show
```
+ 数据库的管理操作
    + 创建数据库
    ```
    create database  [if not exists]  database_name  charset "编码集";
    ```
    + 修改数据库
    ```
    MySQL中数据库的名字无法修改，只能修改数据库的编码集
    alter database database_name set charset "编码集"
    ```
    + 查询数据库
    ```
    show databases;  查询所有的数据库
    show create database database_name;    查询指定数据库的创建细节
    ```
    + 删除数据库
    ```
    drop database [if exists] database_name;
    ```
+ 数据表的管理操作
    + 创建数据表
    ```
    create table [if not exists] table_name(
     column_name column_type  [约束]  [comment  '备注'],
     column_name column_type  [约束]  [comment  '备注']
    )[engine="引擎"],[charset="编码集"];
    #根据其他数据表的结构创建当前数据表(创建结构，数据进不来)
    create table table_name like table_name1
    #根据其他数据表的结构和数据创建一个全新的数据表
    create table table_name  select查询语句
    ```
    + 修改数据表
    ```
    修改表名：alter  table table_name rename  new_table_name
    给表中添加新的字段：alter table table_name  add  column_name  column_type  字段的约束  字段的备注
    修改表字段（修改表字段的类型 约束等等）： alter table table_name modify column_name  new_column_type 约束 备注等等
    修改表字段的名字：alter table table_name change  column_name  new_column_name  type  约束 备注等等
    删除表字段：alter table table_name  drop  column_name；
    ```
    + 查询数据表
    ```
    show tables; 查询当前数据库下有哪些数据表的
    desc  table_name; 查询某个数据表中字段信息的
    show create table table_name; 查询数据表的详细的创建语句。
    ```
    + 删除数据表
    ```
    截断数据表的：清空数据表中的所有数据
    truncate table table_name
    删除表：drop table if exists table_name,table_name1,table_name2,...
    如果数据库中设置了外键，必须先删除从表，然后才能删除主表
    ```
### DML语句
数据操纵语言，负责进行表数据的增加、删除和修改操作。DML语言有一个特性，所有的DML都会返回一个int类型的值，这个值代表数据库受影响的行数。 
insert  delete  update
+ 增加表数据
```
语法一：insert into table_name(字段列表) values(字段对应的值列表),(),.....
【注意】如果向表中所有字段增加数据，那么字段列表可以不用写，值的顺序就是创建数据表的时候字段的顺序
语法二：insert into table_name(字段列表)  select查询语句
根据查询语句的结果的把数据增加到数据表中，要求查询语句的字段结果必须和字段列表的个数保持一致。
```
+ 删除表数据
```
delete from table_name [where 条件]
```
+ 修改表数据
update table_name set 字段=值,字段=值....   【where  筛选条件】
#### where条件有三种写法
+ 条件表达式写法
```
where 条件表达式（比较运算符>  <  =  <=  >=  !=） 字段 = 值
```
+ 逻辑表达式写法
```
is null、is not null、and 、or 、in、not in、between xxx and xxx
```
+ 模糊匹配的写法
模糊匹配适用于我们需要根据字段值的一部分进行精准匹配使用
```
where  字段名  like  模糊匹配条件
模糊匹配条件是一个字符串，使用的时候需要结合两个特殊字符使用：
%  0个或多个字符
_    1个字符
_如果当作普通字符使用，需要转义一下，
like "x_" escape "x"  x可以自定义
```
【注意】delete from table_name可以清空表数据，效果和DDL中truncate table table_name效果一模一样的。最大一个区别是，delete清空数据以后，如果再增加数据，自增列不会从头开始，而是从上一次删除的位置继续自增，truncate删除之后自增列会从头开始。
### DQL语句
DQL语句负责查询数据表中相关数据的，查询主要分为如下几种查询：单表查询、多表查询、联合查询、子查询
#### 单表查询
所需要查询的数据只来自于一张表，此时可以使用单表查询语句
```
语法：
select   查询列表
[from table_name]
[where 筛选条件]
[group by 分组条件][having 筛选条件]
[order by 排序条件]
[limit  分页条件]
执行的顺序:
from where group by having  select order by limit
```
+ select子语句
```
select 查询列表;
查询列表可以是常量、表字段、表达式、函数
如果没有加from子语句，那么一定不能写表字段
查询语句查询出来的结果也是一个二维表格，二维表格的表头存在一些问题，如果查询的是常量，常量就是表头名，如果查询的是表达式，表达式就是表头名，如果查询的是函数，函数名就是表头名
查询列表支持更改查询回来的表头名的
select   xxx as  别名
```
+ from子语句
```
如果我们查询的数据来自于数据表的话，那么必须加from 表名 指定查询的数据库
如果加上from之后，select 查询列表中就可以出现表字段了，而且表字段可以是表中的任何一个字段，也可以是一个通配符* *代表的意思就是表中的所有列的数据
```
+ where子语句
from子语句查询的是表中所有行的数据，如果我们想查询指定行的数据，那么需要通过where筛选数据
+ group by分组查询
```
有时候查询表中的数据的时候，需要将相关的信息聚合起来才能得到结果。
group by 表字段,表字段,....
根据表字段的值，将相同值的数据划分到同一个数据组当中。然后可以对这个数据组进行聚合统计得到只有聚合才能得到一些信息
一旦使用了分组查询，那么select中查询列表不能随便写了，查询列表只能写常量、表达式、分组字段、聚合函数（sum、avg、max、min、count）
【注意】如果没有使用分组查询，也能使用聚合函数，只不过聚合函数不能和普通字段一起出现
```
+ having子语句
```
having子语句不能单独出现，必须和group by一起出现，having也是用来筛选数据的。
只不过having和where的区别在于，where是在分组前进行筛选的，having是在分组后进行筛选的
having筛选一般用于只有通过分组之后才能得到的信息数据筛选
```
+ order by子语句
```
是用于将查询出来的结果数据按照指定的字段值进行排序的，排序的字段最好必须是select 查询列表中出现的字段
order by  字段名  [asc|desc],字段名 asc|desc
```
+ limit子语句
```
limit作用有两个，即可以实现限制展示的数据量，可以进行分页查询
限制展示的数据量：limit  n
分页查询：limit  offset,size
offset代表每一页起始的数据的索引，从0开始
size代表每一页的数量
```
#### 联合查询
```
语法： select查询语句  union|union all  select查询语句  union|union all select查询语句......
```
[注意:] 
+ 多个select查询语句的结果必须保持一致。
+ 联合查询结果的表头是第一个查询语句的表头
+ union不会保留重复的数据，union all会保留重复的数据
#### 多表查询
查询的数据无法从一张表获取，需要从多张表去获取，而且多张数据表之间存在关联关系（外键）
```
select   查询列表
from table_nameA  as  A
inner|left|right|full  join  table_nameB  as B
on  tableNameA的字段=tableNameB的字段
where  group by  having order by  limit
```
+ 多表查询的四种连接方式
    + 内连接：将两张表的关联数据保留，不关键的数据全部删除
    + 左外连接：将左表的所有数据全部保留，右表只保留匹配数据
    + 右外连接：将右表的所有数据全部保留，左表只保留匹配数据
    + 全外连接：mysql只支持语法，但是无法使用，两张表的所有数据全部保留
+ 连接查询直接对表起别名
+ 笛卡尔乘积
```
出现在内连接中，当我们使用内连接但是我们没有加连接条件的数据就会出现一个笛卡尔乘积
左表的每一条数据都会和右表的每一条数据匹配。
```
#### 子查询：一般都是用于多表查询的情况下
+ 子查询就是指的是查询当中有嵌套了一个查询
+ 嵌套的查询可以出现在很多地方，比如where子语句中，from子语句中
+ 子查询可以出现在where子语句中，如果出现在where子语句子查询返回的结果取决于where的判断条件
#### MySQL常用函数
+ 单行函数
一对一函数，函数输入一个数据，返回一个数据
 + 字符串有关的单行函数
    ```
    length(字符串或者字段名)  获取字符串的长度
    concat(str或者字段名...)  拼接字符串，concat拼接字符串的时候，如果某一个字符串为null那么结果为null
    concat_ws(分隔符,str或者字段名....)   以指定分隔符将字符串拼接起来，不会拼接null值
    substring|substr:
        (str,位置,长度) str从某个位置开始截取指定长度的字符串
        (str，位置)  str从某个位置开始截取到字符串结束,位置从1开始
    lpad  |  rpad(str,len,padstr):将str以padstr填充到len长度
    ltrim  |  rtrim| trim(str)   去除字符串两边的空格的
    replace(str,要替换的字符串，替换成的字符串)
    upper(大写)  |  lower(小写)
    instr(str,queryStr)  返回queryStr在str中第一次出现的位置，从1开始
    ```
 + 数学有关的函数
 ```
 round(X,[D])  四舍五入
 ceil 向上取整
 floor 向下取整
 pow(x,n) x^n
 abs 绝对值
 sqrt(n)  根号n
 mod(x,y)  x%y
 truncate(x,n)  x小数点后保留几位
 ```
 + 时间日期有关的函数
 ```
 current_date()  返回当前系统的日期 年-月-日
 current_time() 年回当前系统的时间  时：分：秒
 now()  返回当前系统的时间   年月日 时分秒
 year|month|day|minute|hour|seconds..(时间类型的字段)  返回时间中指定成分内容
 datediff(时间1，时间2) 返回两个时间相差的天数
 date_format(时间，格式)
 ```
 ![格式](amWiki/images/2.1/8.png) 
 + MySQL的一些系统有关函数
 ```
 version()
 current_user()
 ```
+ 分支函数
 + if类型的分支函数
 ```
 if(表达式1,表达式2,表达式3)
表达式1返回的是一个真或者假的结果，如果返回为真 执行表达式2，如果返回为假 执行表达式3
 ```
 + case类型的分支函数
 ```
 第一种用法 值相等判断的
 case  值|字段
 when 值1  then 表达式
 when 值2  then  表达式
 .....
 else 表达式
 end
 第二种用法 范围判断的类似于if else
 case
 when  条件  then 表达式
 。。。。
 else  表达式
 end
 ```
+ 聚合函数
多对一函数，输入多个数据，返回一个结果
```
sum、max、min、count、avg
```
+ 开窗函数
 - 开窗函数是为了解决一个问题，聚合函数无法和普通字段一起查询的问题
 - 开窗函数是在MySQL8版本以后才引入的一个新特性
 - 开窗函数的语法：开窗结合函数  over(partition by  字段名  order by 字段名  desc|asc)
```
聚合函数：sum、count、max、min、avg
排名函数:把一个数据划分到一个窗口中，然后根据窗口的排序规则给这条数据带上一个排名编号，编号从1开始的
    1.row_number()：会依次编号，如果两条数据的排名一致，也会依次编号 1 2 3 4 5 6 7
    2.rank()  会依次编号，如果两条数据的排名一致，那么编号一致 ，下一条数据会跳排名 1 2 2 4 5 6
    3.dense_rank()   会依次编号，如果两条数据的排名一致，那么编号一致 ，下一条数据会不会排名 1 2 2 3 4 5
first_value()   last_value()    lag(column,n)
```
### DCL/TCL语句
#### 概念
事务控制语言，事务是关系型数据库中很重要的一块内容，是为了解决数据操作的时候出现数据不一致的问题的。    
事务指的就是完成一件事情的时候，这个事情要么全部成功，要么全部失败。在数据库当中指的是，当我们完成一件事情的时候，可能会执行多个SQL语句，多个SQL语句要么全部执行成功，要么一个都不执行。    
在数据库中，默认情况下，一条SQL语句就是一个事物，如果想让多个SQL语句成为一个事物，那么我们需要进行单独的设置。
#### 数据库中事务有四个特性（ACID特性）
+ 原子性：事务是一个整体，不可被拆分，一个事务中所有的SQL语句要么全部成功，要么一个都不执行
+ 一致性：事务一旦执行成功，数据从一个一致性状态转化成为另外一个一致性状态，
+ 隔离性：如果两个事务操作同一个数据，应该是相互独立，互不干扰。
+ 持久性：事务一旦操作完成，那么操作的结果持久化到数据库中，不可更改。
#### 如何在数据库中开启事务
+ 开始事务，说白了就是设置自动提交事务 set autocommit = 0;
+ 将一个事务的多个SQL语句依次执行
 【注意】多个SQL语句执行不会保存到数据库，而是在内存中先把数据临时更改了，但是不会持久化
+ 如果一组SQL有一个失败了，执行rollback，让事务回归到一开始的状态   
  如果一组SQL全部成功了，执行commit，让事务持久化到数据库。
#### MySQL事务的隔离性
两个事务在操作同一份数据时，可能会产生一些并发问题  
+ 并发问题主要有三个    
    - 脏读：A事务读取到了B事务执行了但是还没有提交的数据
    - 不可重复读：针对的修改操作，A事务读取了一个数据，然后B事务对数据进行了修改并且提交了，此时A事务再次读取数据，发现数据发生了更改
    - 幻读：针对的是删除和添加操作，A事务根据条件读取数据，然后B事务对这个条件下的数据进行了增加和删除操作，此时A事务再重新读取该条件的数据发现数据多了或者少了几行
+ MySQL中可以设置事务的隔离级别，专门用来解决隔离性问题
    - 读未提交：read uncommitted   三个并发问题都会存在
    - 读已提交：read committed  解决脏读的问题，但是不可重复读和幻读的问题依然存在
    - 可重复读（默认级别）：repeatable read   解决了脏读和不可重复读的问题，同时还解决了大部分的幻读问题
    - 串行化：serializable  彻底解决了所有的并发问题，但是这个级别的效率是最低的
+ 如何设置隔离级别
    - 设置隔离级别之前，必须先把事务关闭
        select @@autocommit;  0开启了事务 1没有开事务
        set autocommit=1
    - 两种设置方式
        会话（从账号登录到账号退出）级别：只对当前会话有效
        set session transaction isolation level 隔离级别
        全局：对每一个新开的会话有效 mysql一旦重启隔离级别就重置了
        set global transaction isolation level 隔离级别
    - 查看MySQL隔离级别
        select @@transaction_isolation
## MySQL中的视图view
+ mysql中视图也是一张表格，但是视图view和table的区别在于，table是一张物理上真实存在的表格，view只是一张逻辑表格，物理上不存在。view其实就是一段select查询语句
+ 视图一般用在所查询的数据可能来自于多张表格，如果每一次查询都使用连接查询，比较麻烦，我们就可以把多表查询语句制作为一个视图，以后需要这些数据直接查询视图中的数据即可。但是因为视图底层是一个查询语句，所以数据最终还是来自于table中。
+ 视图一般就是用在如下情况下，我们需要从一个复杂的SQL语句中二次查询，那么就可以把负责的SQL语句定义成为一个视图，然后二次查询就简单了
+ 一定注意，视图只是一张虚拟表格，视图不存储数据，数据还是在table中存放的，视图存放的只是一段SQL查询语句，视图虽然和表格类似，但是视图一般只做查询使用，不做增加删除修改数据使用。
+ 创建语法
```
create view  view_name  as  select语句
```
+ 视图底层是一个SQL查询语句，使用方式和数据表类似，也可以进行数据的增加、删除和修改，但是注意，视图的数据增删改是有限制的
+ 如果视图中出现了分组查询、聚合函数、连接查询、视图中没有出现原始表中必填字段，那么增删改无法执行的。

## JAR包的制作和使用
JAR包首先是一个压缩包，压缩包比较特殊，是Java编程语言专属的压缩包，jar包存放了我们编写的Java代码的class文件或者source源文件
+ JAR包的制作
eclipse-->项目名--->右键--->export--->java-->jar file--->选择导出的内容、jar包的路径、mainclass
+ JAR包的使用
    - 运行jar包
    ```
    java -jar  xxx.jar     要求制作jar包的时候必须选择mainclass文件
    java -cp xxx.jar  main函数所在Java类的全限定类名
    ```
    - 在项目中引入jar包，使用jar包中代码
    ```
    在eclipse的项目中创建一个lib文件夹，将jar包放到lib目录下，然后在jar包上右键--》build path--->add to build path
    一旦项目jar包引入成功，jar包的源文件千万别删除或者移动
    ```