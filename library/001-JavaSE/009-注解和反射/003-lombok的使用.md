[TOC]
# lombok的使用
+ 帮助我们快速生成JavaBean类，内部采用了注解开发帮助我们生成。
+ lombok使用的注解都是SOURCE生命周期的，这个注解帮助我们生成的JavaBean的内容是在.java源文件编译成为.class文件的过程中完成的。一旦一个类上加上了lombok注解，那么再将类的.java源文件编译成为.class文件的时候，会根据注解的含义往.class文件中添加针对性的代码块
+ 如果要使用lombok,必须安装一个lombok的编译插件，安装好这个插件之后，插件会和javac结合。
## 注解
+ @Data
    + @Getter
    + @Setter
    + @ToString
    + @EqualsAndHashCode
+ @NoArgsConstructor
+ @AllArgsConstructor
+ @Builder
```
Student student2 = Student.builder().studentId(1).studentName("zs").build();
```
## 使用步骤
+ 在项目引入lombok jar包
+ 给eclipse安装lombok插件
```
打开cmd，切换到lombok插件的目录下，输入
java -jar lombok文件名
打开插件，找到eclipse的安装目录下的exe文件，点击下载
```
+ 开启项目的注解识别进程
```
项目--》右键--》properties-->java Compiler-->annotition xxx-->enable
```   
## 补充
class文件在jd-gui.exe中打开