[TOC]

## spring-01-ioc

### 框架

•建筑学：用于承载一个系统必要功能的基础要素的集合

•计算机：某特定领域系统的一组约定、标准、代码库以及工具的集合

### 框架 vs 工具

框架作为项目的骨架和基础结构，提供了高层次的抽象和可复用性；

而工具则作为辅助手段，帮助开发者完成特定任务并提高工作效率

### Spring Framework

+ Spring是一个 **IOC(DI)** 和 **AOP** 框架
+ Spring有很多优良特性：
  + 非侵入式：基于Spring开发的应用中的对象可以不依赖于Spring的API
  + 依赖注入：DI（Dependency Injection）是反转控制（IOC）最经典的实现
  + 面向切面编程：Aspect Oriented Programming - AOP
  + 容器：Spring是一个容器，包含并管理应用对象的生命周期
  + 组件化：Spring通过将众多简单的组件配置组合成一个复杂应用。
  + 一站式：Spring提供了一系列框架，解决了应用开发中的众多问题

### IoC和DI

+ IoC：Inversion of Control（控制反转）设计思想
  + 控制：资源的控制权（资源的创建、获取、销毁等）
  + 反转：和传统的方式不一样了

+ DI ：Dependency Injection（依赖注入）
  + 依赖：组件的依赖关系，如 NewsController 依赖 NewsServices
  + 注入：通过setter方法、构造器、等方式自动的注入（赋值）

### 注册组件的各种方式

#### @Bean

```java
@Bean
    public Person person1(){
        Person p = new Person();
        return p;
    }
```

#### @Scope 调整组件的作用域，默认是单例的

1. @Scope("prototype") 非单实例
        容器启动的时候，不会创建实例组件的对象
2. @Scope("singleton")单实例，默认值
        容器启动的时候会创建单实例组件的对象，
        容器启动完成之前就会创建
3. @Scope("request")同一个请求单实例
4. @Scope("session")同一次会话单实例

```java
@Scope("singleton")
    @Bean
    public Person person(){
        Person p = new Person();
        return p;
    }
```

#### 获取Bean(给容器中注册一个自己的组件； 容器中的每个组件都有自己的名字，方法名就是组件的名字)

1、跑起一个Spring的应用；  ApplicationContext：Spring应用上下文对象； IoC容器

```java
ConfigurableApplicationContext ioc = SpringApplication.run(Spring01IocApplication.class, args);
```

2、获取到容器中所有组件的名字；容器中装了哪些组件； Spring启动会有很多默认组件

```java
String[] names = ioc.getBeanDefinitionNames();
for (String name : names) {
    System.out.println("name = " + name);
}
```

3、获取容器中的组件对象；精确获取某个组件

+ 组件的四大特性：(名字、类型)、对象、作用域

+ 组件名字全局唯一；组件名重复了，一定只会给容器中放一个最先声明的哪个。

4、从容器中获取组件

1）组件不存在，抛异常：NoSuchBeanDefinitionException

2）组件不唯一，

按照类型只要一个：抛异常：NoUniqueBeanDefinitionException

```java
Person bean = ioc.getBean(Person.class);
```

按照名字只要一个：精确获取到指定对象

```java
Person zhangsan = (Person) ioc.getBean("zhangsan");
```

按照类型获取多个：返回所有组件的集合（Map）

```java
Map<String, Person> type = ioc.getBeansOfType(Person.class);
```

按照类型+名字

```java
Person bean = ioc.getBean("zhangsan", Person.class);
```

3）组件唯一存在，正确返回。

5、组件是单实例的....

#### @Configuration

组件：框架的底层配置

配置文件：指定配置

配置类：分类管理组件的配置，配置类也是容器中的一种组件。

创建时机：容器启动过程中就会创建组件对象

单实例特性：所有组件默认是单例的，每次获取直接从容器中拿。容器提前会创建组件

```java
@Configuration//告诉Spring这是一个配置类
public class PersonConfig {
}
```

#### @Primary 主组件：默认组件

```
@Primary //主组件：默认组件
@Bean("zhangsan")
public Person haha() {
    Person person = new Person();
    person.setName("张三2");
    person.setAge(20);
    person.setGender("男");
    return person;
}
//3、给容器中注册一个自己的组件； 容器中的每个组件都有自己的名字，方法名就是组件的名字
@Bean("zhangsan")
public Person zhangsan() {
    Person person = new Person();
    person.setName("张三1");
    person.setAge(20);
    person.setGender("男");
    return person;
}
```

#### 分层注解

默认，分层注解能起作用的前提是，这些组件必须在主程序所在的包及其子包的结构下

Spring为我们提供了快速的MVC分层注解
   1. @Controller控制器

      ```java
      @Controller
      public class UserService {
      }
      ```

   2. @Service服务层

      ```java
      @Service
      public class UserService {
      }
      ```

   3. @Repository持久层

      ```java
      @Repository
      public class UserDao {
      }
      ```

   4. @Component组件

      ```java
      @Component
      public class UserComponent {
      }
      ```

#### @ComponentScan 批量扫描

```
@ComponentScan(basePackages = "org.example.spring01ioc")//批量扫描
```

#### @Lazy 懒加载

容器启动之前不会创建,单例

什么时候获取，什么时候创建

```java
@Lazy //单例模式，可以继续调整为懒加载
```

#### @Import 按需导入

```java
@Import({CoreConstants.class})
@Configuration
@ComponentScan(basePackages = "com.atguigu.spring") //组件批量扫描； 只扫利用Spring相关注解注册到容器中的组件
public class AppConfig {


}
```

#### FactoryBean  工厂Bean

FactoryBean在容器中放的组件的类型，是接口中泛型指定的类型，组件的名字是 工厂自己的名字

```java
//场景：如果制造某些对象比较复杂的时候，利用工厂方法进行创建
@Component
public class BYDFactory implements FactoryBean<Car> {
    @Override
    public boolean isSingleton() {
        return FactoryBean.super.isSingleton();
    }

    @Override
    public Car getObject() throws Exception {
        return new Car();
    }

    @Override
    public Class<?> getObjectType() {
        return Car.class;
    }
}
```

#### @Conditional【难点】条件注册

| **@Conditional** **派生注解**      | **作用**                                                     |
| ---------------------------------- | ------------------------------------------------------------ |
| @ConditionalOnCloudPlatform        | 判定是否指定的云平台，支持：NONE、CLOUD_FOUNDRY、HEROKU、SAP、NOMAD、KUBERNETES、AZURE_APP_SERVICE |
| @ConditionalOnRepositoryType       | 判定是否指定的JPA类型，支持：AUTO、IMPERATIVE、NONE、REACTIVE |
| @ConditionalOnJava                 | 判断Java版本范围，支持：EQUAL_OR_NEWER、OLDER_THAN           |
| @ConditionalOnMissingBean          | 容器中没有指定组件，则判定true                               |
| @ConditionalOnMissingFilterBean    | 容器中没有指定的Filter组件，则判定true                       |
| @ConditionalOnGraphQlSchema        | 如果GraphQL开启，则判定true                                  |
| @ConditionalOnSingleCandidate      | 如果容器中指定组件只有一个，则判定true                       |
| @ConditionalOnClass                | 如果存在某个类，则判定true                                   |
| @ConditionalOnCheckpointRestore    | 判断是否导入了 org.crac.Resource ，导入则判定true            |
| @ConditionalOnNotWebApplication    | 如果不是Web应用，则判定true                                  |
| @ConditionalOnEnabledResourceChain | 如果web-jars存在或者resource.chain开启，则判定true           |

| **@****ConditionalOnMissingClass** | **如果不存在某个类，则判定****true**     |
| ---------------------------------- | ---------------------------------------- |
| @ConditionalOnWebApplication       | 如果是Web应用，则判定true                |
| @ConditionalOnResource             | 如果系统中存在某个资源文件，则判定true   |
| @ConditionalOnNotWarDeployment     | 如果不是war的部署方式，则判定true        |
| @ConditionalOnDefaultWebSecurity   | 如果启用了默认的Security功能，则判断true |
| @ConditionalOnExpression           | 如果表达式计算结果为true，则判定true     |
| @ConditionalOnWarDeployment        | 如果是war的部署方式，则判定true          |
| @ConditionalOnBean                 | 如果容器中有指定组件，则判定true         |
| @ConditionalOnThreading            | 如果指定的threading激活，则判定true      |
| @ConditionalOnProperty             | 如果存在指定属性，则判定true             |
| @ConditionalOnJndi                 | 如果JNDI位置存在，则判定true             |

```java
public class MacCondition implements Condition {
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        Environment environment = context.getEnvironment();

        String property = environment.getProperty("OS");

        return property.contains("mac");
    }
}
```

```java
public class WindowsCondition implements Condition {
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        //判断环境变量中的OS 包含windows，就是windows系统
        Environment environment = context.getEnvironment();
        String property = environment.getProperty("OS");
        return property.contains("Windows");
    }
}
```

```java
//场景：判断当前电脑的操作系统是windows还是mac
    //  windows 系统，容器中有 bill
    //  mac 系统，容器中有 joseph
    @Conditional(MacCondition.class)
    @Bean("joseph")
    public Person joseph(){
        Person person = new Person();
        person.setName("乔布斯");
        person.setAge(20);
        person.setGender("男");
        return person;
    }

    @Conditional(WindowsCondition.class)
    @Bean("bill")
    public Person bill(){
        Person person = new Person();
        person.setName("比尔盖茨");
        person.setAge(20);
        person.setGender("男");
        return person;
    }

```

#### 自动装配流程（先按照类型，再按照名称）

1. 按照类型，找到这个组件；
        1.0、只有且找到一个，直接注入，名字无所谓
        1.1、如果找到多个，再按照名称去找; 变量名就是名字（新版）。
             1.1.1、如果找到： 直接注入。
             1.1.2、如果找不到，报错

```java
@Autowired //自动装配； 原理：Spring 调用 容器.getBean
UserService abc;

@Autowired
Person bill;

@Autowired  //把这个类型的所有组件都拿来
List<Person> personList;

@Autowired
Map<String,Person> personMap;

@Autowired //注入ioc容器自己
ApplicationContext applicationContext;
```

#### @Primary 主组件：默认组件

```
@Primary //主组件：默认组件
@Bean("zhangsan")
public Person haha() {
    Person person = new Person();
    person.setName("张三2");
    person.setAge(20);
    person.setGender("男");
    return person;
}
//3、给容器中注册一个自己的组件； 容器中的每个组件都有自己的名字，方法名就是组件的名字
@Bean("zhangsan")
public Person zhangsan() {
    Person person = new Person();
    person.setName("张三1");
    person.setAge(20);
    person.setGender("男");
    return person;
}
```

#### @Qualifier 类型/具名注入

精确指定：如果容器中这样的组件存在多个，则使用@Qualifier精确指定组件名

精确指定：如果容器中这样的组件存在多个，且有默认组件。我们可以使用 @Qualifier 切换别的组件。

@Primary 一旦存在，改属性名就不能实现组件切换了。

```java
@Qualifier("bill") 
    @Autowired
    Person atom; // @Primary 一旦存在，改属性名就不能实现组件切换了。
```



#### @Resource 扩展其他非Spring注解支持

@Resource 和 @Autowired 区别？
			1、@Autowired 和 @Resource 都是做bean的注入用的，都可以放在属性上
			2、@Resource 具有更强的通用性



```java
  @Resource
    UserDao userDao;
```



#### setter方法注入 setter方法注入



#### 构造器注入 



#### xxxAware 感知接口

```java
@Getter
@ToString
@Service
public class HahaService implements EnvironmentAware, BeanNameAware {

    private Environment environment;
    private String myName;

    @Override
    public void setEnvironment(Environment environment) {
        this.environment = environment;
    }

    public String getOsType(){
       return environment.getProperty("OS");
    }

    @Override
    public void setBeanName(String name) {
        this.myName = name;
    }
}
```



#### @Value 配置文件取值

1、@Value("字面值"): 直接赋值

2、@Value("${key}")：动态从配置文件中取出某一项的值。

3、@Value("#{SpEL}")：Spring Expression Language；Spring 表达式语言

更多写法：https://docs.spring.io/spring-framework/reference/core/expressions.html

```java
@ToString
@Data
@Component
public class Dog {

//    @Autowired // 自动注入组件的。基本类型，自己搞。

    @Value("旺财")
    private String name;
    @Value("${dog.age}")
    private Integer age;

    @Value("#{10*20}")
    private String color;

    @Value("#{T(java.util.UUID).randomUUID().toString()}")
    private String id;

    @Value("#{'Hello World!'.substring(0, 5)}")
    private String msg;

    @Value("#{new String('haha').toUpperCase()}")
    private String flag;

    @Value("#{new int[] {1, 2, 3}}")
    private int[] hahaha;

    public Dog() {

        String string = UUID.randomUUID().toString();

        System.out.println("Dog构造器...");
    }
}

```



#### SpEL Spring表达式基本使用

```
https://docs.spring.io/spring-framework/reference/core/expressions.html
```

#### @PropertySource properties文件注入

说明属性来源： 把指定的文件导入容器中，供我们取值使用

1、classpath:cat.properties；从自己的项目类路径下找

2、classpath*:Log4j-charsets.properties；从所有包的类路径下找

```java
@PropertySource("classpath:conf/cat.properties")
@Data
@Component
public class Cat {

    @Value("${cat.name:Tom}") // : 后面是取不到的时候的默认值；
    private String name;
    @Value("${cat.age:20}")
    private int age;

}
```

#### @Profile 多环境

1、定义环境标识：自定义【dev、test、prod】； 默认【default】

2、激活环境标识：

+ 明确告诉Spring当前处于什么环境。

+ 默认是 default 环境

```java
//@Profile("dev") //整体激活
@Configuration
public class DataSourceConfig {
    //利用条件注解，只在某种环境下激活一个组件。
    @Profile({"dev","default"})  //  @Profile("环境标识")。当这个环境被激活的时候，才会加入如下组件。
    @Bean
    public MyDataSource dev(){
        MyDataSource myDataSource = new MyDataSource();
        myDataSource.setUrl("jdbc:mysql://localhost:3306/dev");
        myDataSource.setUsername("dev_user");
        myDataSource.setPassword("dev_pwd");

        return myDataSource;
    }


    @Profile("test")
    @Bean
    public MyDataSource test(){
        MyDataSource myDataSource = new MyDataSource();
        myDataSource.setUrl("jdbc:mysql://localhost:3306/test");
        myDataSource.setUsername("test_user");
        myDataSource.setPassword("test_pwd");

        return myDataSource;
    }


    @Profile("prod")
    @Bean
    public MyDataSource prod(){
        MyDataSource myDataSource = new MyDataSource();
        myDataSource.setUrl("jdbc:mysql://localhost:3306/prod");
        myDataSource.setUsername("prod_user");
        myDataSource.setPassword("prod_pwd");

        return myDataSource;
    }
}
```

第三方组件想要导入容器中：没办法快速标注分层注解
* 1、@Bean：自己new，注册给容器
* 2、@Component 等分层注解
* 3、@Import：快速导入组件

### 组件生命周期

#### InitializingBean

Bean初始化

#### DisposableBean

Bean销毁

#### @PostConstruct

构造器后置处理钩子

#### @PreDestroy

销毁预处理钩子

#### BeanPostProcessor

后置处理器机制