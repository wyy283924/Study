[TOC]
# Thread多线程类（java.lang）
	多线程的四种实现方式，最终都是借助Thread类才能完成多线程的创建和启动，Thread类才是多线程的核心。

	currentThread():Thread对象   静态方法  获取当前方法所在的线程对象

	getName()：获取线程的名字的，线程的名字如果自己没有设置，JVM会自动给他一个名字Thread-num,可以设置名字。

	setName(String name)：设置线程的别名，设置线程的别名必须在启动线程之前完成。

	sleep(long ms)：也是一个静态方法，代表的是让当前线程“睡”一会

	run()：是多线程启动之后会自动执行的代码方法，run方法是多线程的执行逻辑核心，但是一定一定注意一个问题，如果要启动多线程程序，千万不要直接调用run方法，如果直接调用了run方法，只是属于一个普通的方法调用。

	start() ：是多线程启动的核心，如果要启动多线程程序，必须而且只能调用Thread类的start方法，而且start方法一旦启动多线程成功，多线程程序会自动调用run方法中逻辑代码去执行。

	isAlive()：boolean   代表判断当前线程是否存活

	setPriority(int)：设置线程的优先级的，优先级高的线程会获得抢占CPU的更高的概率。线程的优先级只有10级，1为最低 10为最高  5是创建的线程的默认优先级。设置优先级必须在线程启动之前完成。

	getPriority():int   获取线程的优先级的。

	yield()：让当前线程失去CPU的执行，然后和其他线程再竞争CPU的执行权，竞争的时候，线程优先级高的会有更大的可能性获得CPU执行权

	isDaemon()：boolean   判断当前线程是不是后台线程（守护线程），

	setDaemon(boolean)   如果传递的为true，代表设置当前线程为守护线程，否则为用户线程

	stop()    强制杀死某一个线程

	join（）：在一个线程A中可以调用另外一个线程B的join方法，一旦调用成功，A线程会进入阻塞状态，直到B线程全部运行完成，A线程才会就绪然后运行
# 线程的分类
	用户线程

	守护线程

	狡兔死，走狗烹

	如果一个线程里面只剩下守护线程，那么进程直接全部结束了。

	Java中创建出来的线程如果特殊的设置，都是用户线程
	普通的一个Java程序启动成功之后最少有三个线程：
        1、main线程---用户线程
        2、自动垃圾回收线程---守护线程
        3、异常线程--守护线程