##  MyBatis

### 一. MyBatis概述

#### 1.1 原始的JDBC操作

谈及MyBatis，必然需要先了解Java和数据库的连接技术——JDBC。但是原始JDBC操作中，却存在如下**缺点**：

1. 数据库连接创建、释放频繁造成**系统资源浪费**从而影响系统性能。

2. SQL语句在代码中硬编译，造成代码**不易维护**，实际应用SQL变化的可能较大，SQL变动需要改变Java代码。

3. 查询操作时，需要**手动**将结果集中的数据手动封装到实体中；插入操作时，需要**手动**将实体的数据设置到SQL语句的占位符位置。

   如下为原始JDBC操作

```java
 
public class JDBCDemo {
    public static void main(String[] args) throws Exception{
        //获取数据库连接对象
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db1","root","root");
        //定义sql语句
        String sql = "select * from db1.emp";
        //获取执行sql的对象Statement
        Statement stmt = conn.createStatement();
        //执行sql
        ResultSet resultSet = stmt.executeQuery(sql);
        //处理结果
        while(resultSet.next()) {             
            int id = resultSet.getInt(1);                    //获取id
            String name = resultSet.getString("ename");             //获取姓名
            System.out.println("id:" + id + " name:" + name);
        }
        //释放资源
        stmt.close();
        conn.close();
    }
}
```

#### 1.2 如何克服JDBC固有缺陷

面对上述缺点，我们的**解决方案**是：

1. 使用数据库连接池技术（C3P0或Druid）初始化连接资源；
2. 将SQL语句抽取到**xml配置文件**中（解耦合）；
3. 使用反射、内省等底层技术，自动将实体与表进行属性与字段的自动映射（比较困难）。

#### 1.3 什么是MyBatis

+ Mybatis是一款优秀的半自动的ORM持久化层框架，它支持自定义SQL、存储过程以及高级映射。
+ MyBatis免除了几乎所有的JDBC代码以及设置参数和获取结果集的工作。
+ 

