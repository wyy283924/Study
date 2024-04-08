[TOC]
# JUnit
Junit单元测试
+ 测试Java相关代码是否可以执行的
+ 单元测试可以通过注解的形式 让普通的Java方法具备main函数的执行能力，这样的话在一个类中定义多个可执行的方法
+ @Before：每执行一个@Test修饰的方法，@Before修饰的方法会先执行
+ @Test：修饰的方法会具备main函数执行能力
+ @After：每执行完成一个@Test修饰的方法，@After方法会执行一次