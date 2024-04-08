[TOC]
# Java的单元测试工具Junit
+ 引入test_jar文件夹中的jar文件
+ 在Java当中，如果要去测试一些代码，目前都是通过编写main函数完成。
main函数一次只能运行一种逻辑。  
+ 单元测试工具junit可以帮助通过注解的方式将一个普通的Java方法变成一个main函数然后执行和运行。这样就可以实现在一个类中定义多个可执行的方法。
## 三个注解（都是用来修饰方法）
### @Before
等同于代码块，修饰的方法会自动执行，当执行@Test修饰的方法之前会自动执行@Before修饰的方法
### @Test
修饰的方法等用于Java中main函数，是可以执行运行的
### @After
修饰的方法等@Test方法执行完成之后会自动执行

通过单元测试验证JDBC的增删改查四个方法
```java
package junit_study;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class Demo {
	@Before
	public void a() {
		System.out.println("a");
	}
	
	@Test
	public void b() {
		System.out.println("b");
	}
	
	@Test
	public void c() {
		System.out.println("c");
	}
	
	@After
	public void d() {
		System.out.println("d");
	}
}

```