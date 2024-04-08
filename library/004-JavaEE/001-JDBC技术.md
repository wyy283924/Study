[TOC]
# JDBC技术
## 引入JDBC的原因
MySQL是一个数据库技术，是专门用来进行数据的存储和管理的，但是我们后期操作数据并不是在数据库中完成的。因为数据库只能存储和管理数据，完成不了我们的业务功能，业务功能通过编程代码来完成。
## 概念
JDBC技术是JavaEE十三种技术之一，技术规定了Java如何操作数据库（数据库不是唯一）。所有代码都位于java.sql包下。java.sql包下提供的JDBC技术基本上都是接口，JDBC技术JDK官方只提供了规范，没有提供具体的实现，具体的实现是由数据库厂商或者第三方组织给实现的，实现一般数据库厂商或者第三方组织封装成为一个jar包，而这个jar包称之为驱动jar包。
## JDBC通过JavaBean封装DQL查询回来的数据
实体类：实体类也是JavabBean，当JavaBean只是用来封装从数据库查询来的数据
``` java
public static void main(String[] args) {
		//通过控制台输入 用户名和密码，然后我们可以从数据库校验用户名和密码是否存在，如果存在，返回用户的详细信息
		//1、接受用户输入的用户名和密码
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入用户名：");
		String username = sc.next();
		System.out.println("请输入密码：");
		String password = sc.next();
		//2、根据用户名和密码查询数据库的信息 如果信息存在返回用户的信息，如果不存在返回null
		SysUser sysUser = getUserByUsernameAndPassword(username, password);
		if(sysUser == null) {
			System.out.println("数据库暂无此用户信息");
		}else {
			System.out.println(sysUser);
		}
		
		
	}
	
	public static SysUser getUserByUsernameAndPassword(String username,String password) {
		Connection connection = null;
		Statement statement = null;
		ResultSet rs = null;
		try {
			DriverManager.registerDriver(new Driver());
			connection = DriverManager.getConnection(
					"jdbc:mysql://localhost:3306/demo?serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=utf-8",
					"root", "root");
			//select  * from sys_user where username='xx' and password ='xx'
			String sql = "select * from sys_user where username='"+username+"' and password ='"+password+"'";
			statement = connection.createStatement();
			rs = statement.executeQuery(sql);
			if(rs.next()) {
				int userId = rs.getInt("user_id");
				String user = rs.getString("username");
				String pass = rs.getString("password");
				String sex = rs.getString("sex");
				String phoneNumber = rs.getString("phone_numer");
				SysUser sysUser = new SysUser(userId, username, password, sex, phoneNumber);
				return sysUser;
			}else {
				return null;
			}

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			if (statement != null) {
				try {
					statement.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			if (connection != null) {
				try {
					connection.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		return null;
		
	}
```
## JDBC操作数据库的规范一共分为8步
+ 在项目中引入驱动jar包
+ 注册和加载驱动：告诉JDBC连接哪个数据库，告诉JDBC要使用哪个驱动jar包
+ 获取和数据库的连接
+ 定义Java操作数据库使用的SQL语句
+ 创建Statement
+ 执行SQL并且得到返回结果
+ Java中处理返回结果
+ 释放资源：Connection  Statement  Resultset
```java
Connection connection = null;
		Statement statment = null;
		try {
			/**
			 * 1、加载和注册驱动：在mysql驱动8版本已经没有必要写了
			 * 因为com.mysql.cj.jdbc.Driver类中通过静态代码块自动注册
			 */
			DriverManager.registerDriver(new Driver());
			/**
			 * 2、创建和数据库的连接DriverManager
			 *  三个参数
			 *  URL：如果我们连接的是MySQL8版本，那么一定要夹serverTimezone
			 *    jdbc:mysql://localhost:3306/demo?serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=UTF-8
			 *  user
			 *  password
			 */
			connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/demo?serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=UTF-8", "root", "root");
			System.out.println(connection);
			/**
			 * 3、准备操作类型的SQL语句：Java操作数据库的SQL
			 *  操作类型的SQL语句 DDL  DML  DQL
			 *  TCL/DCL不是操作性的SQL，设置性的SQL
			 */
			String sql ="create table student(student_id int primary key auto_increment,student_name varchar(20))charset='utf8'";
			/**
			 * 4、创建Statement:是由connection连接对象创建
			 */
			statment = connection.createStatement();
			/**
			 * 5、车带着SQL去数据库执行 并且得到返回结果
			 *  statement:
			 *     execute(String sql):boolean   既可以执行DDL,DML,DQL
			 *        返回值如果执行的是SQL 返回true 如果不是DQL返回false
			 *        但是我们一般只用这个执行DDL语句
			 *     executeUpdate(String sql):int  执行DML语句
			 *     executeQuery(String sql):ResultSet  执行DQL语句
			 */
			boolean flag = statment.execute(sql);
			//如果flag有值 那么代表SQL语句一定是执行成功
			/**
			 * 6、java处理结果
			 */
			System.out.println("创建成功");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			/**
			 * 7、释放资源 Connection Statement
			 */
			if(statment != null) {
				try {
					statment.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			if(connection != null) {
				try {
					connection.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
        }
```
## JDBC中常用的一些接口和类
+ DriverManager类：注册驱动  获取连接 
+ Connection接口：代表的是和数据库之间的连接对象
+ Statement接口：代表的是一个执行器 封装SQL并且去数据库执行SQL得到返回结果的
+ Resultset接口：代表的是查询语句执行结果的虚拟结果集在Java中的抽象表示
## Statement
Statement理解为一个执行器，携带SQL去数据库执行并且获取返回结果。
### 执行SQL
```
execute(String sql):boolean,执行DQL返回true,执行DDL、DML返回false
executeUpdate(String sql):int
executeQuery(String sql):Resultset
Resultset获取数据的时候有如下几个方法需要注意：
	next()：boolean方法，next方法有两个作用，1、判断结果集中有没有下一条数据，2、如果有下一条数据，会把一个指针指向下一行数据 获取这一行的数据
    指针默认指向在第一条数据的前面
	getString|Int|float|xxxx(int|String)
	如果我们查询的结果集的数量大于1，那么需要通过循环来获取每一行的数据
```
### 存在的问题
Statement携带的SQL存在一个问题，如果SQL中存在变量的话，我们需要使用Java字符串拼接的方式把变量拼接到SQL中，但是这样拼接会存在一些问题    
+ 拼接变量的时候，如果变量是字符串类型，必须在字符串两边加上''  否则JDBC执行的时候SQL会报错
+ SQL注入问题
    SQL注入就是因为我们JDBC在创建SQL语句的时候，把变量直接拼接到了SQL语句当中，因此一些不法分子可以根据SQL的注释语法造出一个万能SQL，获取到原先无法获取的数据。
### 解决方法
为了解决字符串变量拼接问题以及SQL注入问题，JDBC引入了一个全新的执行器，叫做PreparedStatement, PreparedStatement是Statement的一个子接口  
```
PreparedStatement防止SQL注入和字符串变量拼接，它是通过预编译SQL和占位符来解决这个问题的
String sql = "select * from sys_user where username=?  and password = ?";
通过？把变量的位置给占住，紧跟着SQL编译（把SQL结构固定了）一下
PreparedStatement当中提供可一系列的setxxx(int i,xxx data)
设置占位符的值的
setString(1,"zs");
setInt(2,1)
```
```java
public static void main(String[] args) {
		int id = 1;
		int deleteUser = deleteUser(id);
		if(deleteUser > 0) {
			System.out.println("删除成功");
		}else {
			System.out.println("删除失败");
		}
		
	}
	public static int deleteUser(int id) {
		Connection connection =  null;
		PreparedStatement prepareStatement = null;
		try {
			DriverManager.registerDriver(new Driver());
			connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/demo?serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=UTF-8", "root", "root");
			String sql = "delete from sys_user where user_id = ?";
			//创建Statement  PreparedStatement
			prepareStatement = connection.prepareStatement(sql);
			//不能执行SQL，而是将SQL中占位符替换成我们的参数
			prepareStatement.setInt(1, id);
			//执行SQL
			int executeUpdate = prepareStatement.executeUpdate();
			return executeUpdate;
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			if(prepareStatement != null) {
				try {
					prepareStatement.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			if(connection != null) {
				try {
					connection.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		return 0;
	}
```
## ResultSet结果集
Resultset结果集：结果集是查询得到的虚拟表格的一个抽象表示
```java
ResultSetMetaData metaData = rs.getMetaData();
System.out.println(metaData.getColumnCount());
//获取某一列的名字 1代表第1列
System.out.println(metaData.getColumnName(1));
System.out.println(metaData.getColumnTypeName(2));
```
## 通过JDBC操作数据库的blob类型的数据
```java
String sql = "insert into demo(p3,p4) values(?,?)";
			
prepareStatement = connection.prepareStatement(sql);
//二进制数据其实就是Java中的io流  InputStream
prepareStatement.setBlob(1, new FileInputStream("C:\\Users\\11018\\Pictures\\壁纸\\图片3.png"));
prepareStatement.setBlob(2, new FileInputStream("C:\\Users\\11018\\Pictures\\壁纸\\图片3.png"));
//prepareStatement.setBlob(3, new FileInputStream("C:\\Users\\11018\\Pictures\\壁纸\\图片3.png"));
//prepareStatement.setBlob(4, new FileInputStream("C:\\Users\\11018\\Pictures\\壁纸\\图片3.png"));
```
## JDBC操作事务
```java
        Connection connection = null;
		PreparedStatement prepareStatement = null;
		try {
			DriverManager.registerDriver(new Driver());
			connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/myemployees?serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=UTF-8", "root", "root");
			//开启事务
			connection.setAutoCommit(false);
			/**
			 * 执行多个SQL
			 * update account set amount = amount-xx where account = xxx
			 * update account set amount = amount+xx where account = xxx
			 */
			String sql1 = "update account set amount = amount-? where account = ?";
			prepareStatement = connection.prepareStatement(sql1);
			prepareStatement.setInt(1, 1000);
			prepareStatement.setString(2,"123");
			int executeUpdate = prepareStatement.executeUpdate();
			
			String sql2 = "updatexxxx account set amount = amount+? where account = ?";
			prepareStatement = connection.prepareStatement(sql2);
			prepareStatement.setInt(1, 1000);
			prepareStatement.setString(2,"231");
			int executeUpdate1 = prepareStatement.executeUpdate();
			
			//try块的最后一行执行提交事务的代码
			connection.commit();
			connection.setAutoCommit(true);
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			//因为SQL出现了异常 一定会执行catch块
			if(connection != null) {
				try {
					connection.rollback();
					connection.setAutoCommit(true);
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
		}finally {
			if(prepareStatement != null) {
				try {
					prepareStatement.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			if(connection != null) {
				try {
					connection.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
```
## JDBC批量添加
批量添加数据只有PreparedStatement支持，Statement不支持批量添加  
批量添加指的每创建一个SQL语句，不是立马去数据库执行，积攒，积攒到一定的量，统一去数据库执行依次，这样的话就可以节省Java和数据库通信的次数，提升执行效率 
### PreparedStatement接口中定义三个方法
+ addBath()：将创建的SQL语句积攒起来
+ executeBatch()：统一去数据库执行依次积攒的SQL
+ clearBatch()：将以前积攒的SQL清空了，重新积攒
JDBC默认不支持批量添加的，如果想让JDBC批量添加非常简单，只需要在URL中增加一个参数：开启批量添加的支持的  
```
rewriteBatchedStatements=true
```
```java

Connection connection = null;
		PreparedStatement prepareStatement = null;
		try {
			DriverManager.registerDriver(new Driver());
			connection = DriverManager.getConnection(
					"jdbc:mysql://localhost:3306/demo?serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=utf-8&rewriteBatchedStatements=true",
					"root", "root");
			String sql = "insert into student(student_name) values(?)";
			prepareStatement = connection.prepareStatement(sql);
			
			long startTime = System.currentTimeMillis();
			//500执行一次
			for (int i = 1; i <= 10000; i++) {
				prepareStatement.setString(1, "index"+i);
				//积攒SQL
				prepareStatement.addBatch();
				if(i % 10000 == 0) {
					//一次执行500条SQL
					int[] executeBatch = prepareStatement.executeBatch();
					//执行完成需要把这已经执行了的500条数据清理了
					prepareStatement.clearBatch();
				}
			}
			long endTime = System.currentTimeMillis();
			System.out.println(endTime-startTime);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			if (prepareStatement != null) {
				try {
					prepareStatement.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			if (connection != null) {
				try {
					connection.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
```
## JDBC的工具类的封装
现在操作JDBC的时候，操作一般就分为增删改查四种，但是不管操作那种，我们JDBC都分为七步完成的，七步中其实就第三步和第五步不一样，剩余的步骤都是一模一样的。
### JDBC的六步曲
+ 加载驱动
+ 创建和数据库连接的
+ 创建SQL语句：不一样
+ 创建小推车PreparedStatement,并且替换占位符：一样的
+ 执行SQL并且返回结果的：DML：int，DQL：返回的是实体类对象或者是实体类对象的集合
+ 释放资源
### JDBC工具类的封装
+ 创建一个配置文件：db.properties  将数据库的连接信息全部写到配置文件
+ 创建工具类
	- 1、获取连接的方法
	- 2、封装一个创建小推车和替换占位符的方法
	- 3、封装三个用来执行SQL的方法
		1、执行DML类型的方法：int
		2、执行查询单条结果SQL的方法：实体类对象
		3、执行查询多条结果SQL的方法：实体类对象的集合
	- 4、封装两个重载方法：关闭资源的重载方法
```java
package top.shareedu.util;

import java.io.FileInputStream;
import java.io.IOException;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

import com.mysql.cj.jdbc.Driver;

/**
 * 工具类的特点：
 *   工具类中方法都是静态方法
 *   工具类不需要构造对象，工具类的构造器要私有化
 */
public class DBUtil {
	public static DataSource dataSource = new MyDataSource();
	// private static final String URL;
	// private static final String USERNAME;
	// private static final String PASSWORD;
	
	private DBUtil() {
		
	}
	
	static {
		//1、读取配置文件给三个属性赋值
		Properties prop = new Properties();
		try {
			prop.load(new FileInputStream("db.properties"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		URL = prop.getOrDefault("url", "").toString();
		USERNAME = prop.getOrDefault("username", "").toString();
		PASSWORD = prop.getOrDefault("password", "").toString();
		//2、加载驱动
		try {
			DriverManager.registerDriver(new Driver());
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/**
	 * 1、封装一个用于获取连接的方法
	 * @throws SQLException 
	 */
	public static Connection getConnection() throws SQLException {
		//DriverManager真正去获取与数据库的物理连接，这样太过浪费
		//Connection connection = DriverManager.getConnection(URL,USERNAME,PASSWORD);
		//通过数据库连接池获取连接
		Connection connection = dataSource.getConnection();
		return connection;
	}
	
	/**
	 * 封装一个用于创建的小推车以及替换占位符的方法
	 * @throws SQLException 
	 */
	public static PreparedStatement createStatement(Connection connection,String sql,Object... params) throws SQLException {
		//1、先根据SQL创建小推车
		PreparedStatement prepareStatement = connection.prepareStatement(sql);
		//2、替换小推车占位符
		/**
		 * 要求传递进来的参数个数必须和占位符的个数一致的 参数的顺序必须和占位符的顺序一致
		 */
		for(int i = 0;i<params.length;i++) {
			prepareStatement.setObject(i+1, params[i]);
		}
		return prepareStatement;
	}
	
	/**
	 * 封装一个执行所有DML类型SQL的方法
	 * @throws SQLException 
	 */
	public static int executeDMLSQL(PreparedStatement preparedStatement) throws SQLException {
		int executeUpdate = preparedStatement.executeUpdate();
		return executeUpdate;
	}
	/**
	 * 封装一个查询单个结果的SQL语句
	 *   单个结果的SQL查询语句返回的是一个实体类
	 * 泛型，反射
	 * @throws SQLException 
	 * @throws InvocationTargetException 
	 * @throws IllegalArgumentException 
	 * @throws IllegalAccessException 
	 * @throws InstantiationException 
	 * @throws SecurityException 
	 * @throws NoSuchMethodException 
	 */
	public static <T> T executeQueryOneSQL(PreparedStatement preparedStatement,Class<T> clz) throws SQLException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException {
		ResultSet resultSet = preparedStatement.executeQuery();
		/**
		 * 结果集转换成为T是有规律的
		 *   结果集中字段名就是T对象中属性名  字符名是下划线连接的 属性名是小驼峰连接
		 */
		Constructor<T> constructor = clz.getDeclaredConstructor();
		constructor.setAccessible(true);
		T t = constructor.newInstance();
		//获取t这个对象的所有属性
		if(resultSet.next()) {
			Field[] fields = clz.getDeclaredFields();
			for(Field f: fields) {
				//studentName
				String fieldName = f.getName();
				//将属性名转换成为列名 然后去rs中获取列对应的值
				char[] charArray = fieldName.toCharArray();
				StringBuffer sb = new StringBuffer();
				for(char ch : charArray) {
					if(ch >=97 && ch <=122) {
						sb.append(ch);
					}else {
						ch = (char)(ch+32);
						sb.append("_").append(ch);
					}
				}
				String columnName = sb.toString();
				Object value = resultSet.getObject(columnName);
				f.setAccessible(true);
				f.set(t, value);
			}
		}
		return t;
	}
	
	/**
	 * 查询多个结果的查询语句的封装
	 * @param <T>
	 * @param preparedStatement
	 * @param clz
	 * @return
	 * @throws SQLException
	 * @throws InstantiationException
	 * @throws IllegalAccessException
	 * @throws IllegalArgumentException
	 * @throws InvocationTargetException
	 * @throws NoSuchMethodException
	 * @throws SecurityException
	 */
	public static <T> List<T> executeQueryMoreSQL(PreparedStatement preparedStatement,Class<T> clz) throws SQLException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException {
		List<T> list = new ArrayList<T>();
		ResultSet resultSet = preparedStatement.executeQuery();
		/**
		 * 结果集转换成为T是有规律的
		 *   结果集中字段名就是T对象中属性名  字符名是下划线连接的 属性名是小驼峰连接
		 */
		Constructor<T> constructor = clz.getDeclaredConstructor();
		constructor.setAccessible(true);
		//获取t这个对象的所有属性
		while(resultSet.next()) {
			T t = constructor.newInstance();
			Field[] fields = clz.getDeclaredFields();
			for(Field f: fields) {
				//studentName
				String fieldName = f.getName();
				//将属性名转换成为列名 然后去rs中获取列对应的值
				char[] charArray = fieldName.toCharArray();
				StringBuffer sb = new StringBuffer();
				for(char ch : charArray) {
					if(ch >=97 && ch <=122) {
						sb.append(ch);
					}else {
						ch = (char)(ch+32);
						sb.append("_").append(ch);
					}
				}
				String columnName = sb.toString();
				Object value = resultSet.getObject(columnName);
				f.setAccessible(true);
				f.set(t, value);
			}
			list.add(t);
		}
		return list;
	}
	
	
	public static void closeResources(Connection connection,PreparedStatement preparedStatement) {
		if (preparedStatement != null) {
			try {
				preparedStatement.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		if (connection != null) {
			try {
				connection.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
}

```

## 数据库连接池
+ 数据库连接资源是特别宝贵的资源，默认情况下，数据库只支持151个连接。JDBC操作数据库的时候诞生了一个思想：数据库连接池思想
+ 在项目当中，操作数据库的时候，不是每次操作建立一个和数据库的连接，而是在项目启动的时候，我们先自己创建n个数据库连接放到一个集合当中，到时候如果我们要使用数据库连接，那么从集合中获取一个，使用完成之后，连接不能释放，应该把连接放回到集合当中。
+ JDBC有一个接口叫做DataSouce，这个接口就是JDBC设计用来实现数据库连接池的。
### 如果我们想要使用数据库连接池，有两种方式
#### 自定义数据库连接池
自定义一个类实现DataSource接口
```java
public class MyDataSource implements DataSource {
	// 集合是可以存放Integer.MAX_VALUE
	private static final LinkedList<Connection> POOLS = new LinkedList<Connection>();
	// 定义1个属性 池子当中连接的数量
	private static final int POOLCOUNT = 10;

	static {
		// 1、读取配置文件给三个属性赋值
		Properties prop = new Properties();
		try {
			prop.load(new FileInputStream("db.properties"));
			DriverManager.registerDriver(new Driver());
			for (int i = 0; i < POOLCOUNT; i++) {
				/***
				 * 目前创建的Connection的对象 close方法是会销毁资源的 而不是将资源放到数据库连接池当中
				 * 需要将Connection的底层close方法重写了，可以重写，使用反射
				 * Java为了解决修改某些源码的代码问题，提供了一种设计模式（经过前人检验，比较优秀的一些代码）
				 *   Java一共有23种设计模式：单例设计模式、适配器模式、工厂模式、装饰器模式、动态代理模式等等
				 *   
				 * 动态代理模式可以修改Java底层的某些源码的。理解为中介
				 * 	
				 */
				Connection connection = DriverManager.getConnection(prop.getProperty("url"),prop.getProperty("username"),prop.getProperty("password"));
				/**
				 * 创建一个代理对象去代理Connection中的所有方法
				 *   代理的时候，如果不是close方法，那么还是调用Connection的逻辑
				 *   如果是close方法 那么就重写了
				 *   
				 * Proxy 专门用来创建动态代理对象的
				 */
				/**
				 * 方法需要传递三个参数：
				 * 1、类加载器--类加载器必须得是被代理对象的class实例获取的
				 * 2、代理对象和被代理对象共同的父接口
				 * 3、需要传入一个InvocationHandler的对象，里面有一个方法 invoke方法
				 *   这个方法就是代理对象如何调用被代理对象的方法
				 */
				Connection proxy = (Connection)Proxy.newProxyInstance(connection.getClass().getClassLoader(), connection.getClass().getInterfaces(), new InvocationHandler() {
					/**
					 * invoke方法的返回值就是代理对象执行完被代理对象方法之后的返回值
					 */
					@Override
					public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
						/**
						 * 除了close方法以外 剩余的方法还是要调用Connection的对象
						 */
						String name = method.getName();
						if(name.equals("close")) {
							//重写 放回数据库连接池
							POOLS.add(connection);
							System.out.println("数据库连接已经放回连接池");
							return null;
						}else {
							Object invoke = method.invoke(connection, args);
							return invoke;
						}
					}
				});
				POOLS.add(proxy);
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public PrintWriter getLogWriter() throws SQLException {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void setLogWriter(PrintWriter out) throws SQLException {
		// TODO Auto-generated method stub

	}

	@Override
	public void setLoginTimeout(int seconds) throws SQLException {
		// TODO Auto-generated method stub

	}

	@Override
	public int getLoginTimeout() throws SQLException {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public Logger getParentLogger() throws SQLFeatureNotSupportedException {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public <T> T unwrap(Class<T> iface) throws SQLException {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean isWrapperFor(Class<?> iface) throws SQLException {
		// TODO Auto-generated method stub
		return false;
	}

	/**
	 * 如何从数据库连接池获取一个连接对象
	 */
	@Override
	public Connection getConnection() throws SQLException {
		System.out.println("目前数据库连接池剩余"+POOLS.size());
		if(POOLS.size()>0) {
			Connection connection = POOLS.removeFirst();
			return connection;
		}else {
			System.out.println("目前数据库连接池没有连接可用，请稍后再试");
			return null;
		}
	}

	@Override
	public Connection getConnection(String username, String password) throws SQLException {
		// TODO Auto-generated method stub
		return null;
	}

}

```
#### 使用第三方提供好的数据库连接池
##### DBCP：速度快，但是不稳定
+ 需要创建一个配置文件xxx.properties
+ 需要增加如下几个配置项：driverClassName、url、username、password
```java
public static void main(String[] args) throws Exception {
	Properties prop = new Properties();
	prop.load(new FileInputStream("dbcp.properties"));
		
	DataSource dataSource = BasicDataSourceFactory.createDataSource(prop);
	Connection connection = dataSource.getConnection();
	System.out.println(connection);
}
```
##### C3P0：速度慢一点，但是稳定
+ 需要创建一个配置文件：c3p0-config.xml,配置文件必须放在src的目录下
```
<?xml version="1.0" encoding="UTF-8"?>
<c3p0-config>
  <named-config name="my"> 
  	<property name="driverClass">com.mysql.cj.jdbc.Driver</property>
  	<property name="jdbcUrl">jdbc:mysql://localhost:3306/demo?serverTimezone=Asia/Shanghai&amp;useUnicode=true&amp;characterEncoding=utf-8&amp;rewriteBatchedStatements=true
  	</property>
  	<property name="user">root</property>
  	<property name="password">root</property>
    <property name="acquireIncrement">50</property>
    <property name="initialPoolSize">100</property>
    <property name="minPoolSize">50</property>
    <property name="maxPoolSize">1000</property>

    <!-- intergalactoApp adopts a different approach to configuring statement caching -->
    <property name="maxStatements">0</property> 
    <property name="maxStatementsPerConnection">5</property>
  </named-config>
</c3p0-config>
```
+ 需要增加如下几个配置项：driverClass、jdbcUrl、user、password
```java
public static void main(String[] args) throws SQLException {
	DataSource datasource = new ComboPooledDataSource("my");
	Connection connection = datasource.getConnection();
	System.out.println(connection);
}
```
##### Druid：阿里巴巴开源的项目，集成了DBCP和C3P0的优点
+ 需要创建一个配置文件：xxx.properties
+ 配置项：driverClassName、url、username、password
```java
public static void main(String[] args) throws Exception {
	Properties prop = new Properties();
	prop.load(new FileInputStream("dbcp.properties"));
	DataSource dataSource = DruidDataSourceFactory.createDataSource(prop);
	Connection connection = dataSource.getConnection();
	System.out.println(connection);
}
```