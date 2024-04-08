[TOC]
# JavaGUI技术
## 概述
	GUI技术就是Java用来编写界面的一种技术，技术awt技术、swing技术。JavaFX技术全新的Java界面编程技术
## Swing界面编程的方式
Swing是纯Java组件，使得应用程序在不同的平台上运行时具有相同外观和相同的行为。
Swing中的大部分组件类位于javax.swing包中.
Swing中的组件非常丰富，支持很多功能强大的组件
关于GUI组件的类都在Swing包里
## 布局管理器
组件不能单独存在，必须放置于容器当中，而组件在容器中的位置和尺寸是由布局管理器来决定的。在java.awt包中提供了五种布局管理器，分别是FlowLayout (流式布局管理器) 、BorderLayout （边界布局管理器）、GridLayout(网格布局管理器) 、GridBagLayout (网格包布局管理器)和CardLayout (卡片布局管理器)。每个容器在创建时都会使用一种默认的布局管理器，在程序中可以通过调用容器对象的setLayout()方法设置布局管理器通过布局管理器来自动进行组件的布局管理。例如把一个Frame窗体的布局管理器设置为FlowLayout，代码如下所示:
```
Frame frame = new Frame();
frame.setlayout(new FlowLayout());
```
### FlowLayout
流式布局管理器 (FlowLayout) 是最简单的布局管理器，在这种布局下，容器会将组件按照添加顺序从左向右放置。当到达容器的边界时，会自动将组件放到下一行的开始位置。这些组件可以左对齐、居中对齐(默认方式)或右对齐的方式排列。FlowLayout对象有三个构造方法，如表所示		

|方法声明|功能描述|
|-------|--------|
|FlowLayout()|组件默认居中对齐，水平、垂直间距默认为5个单位|
|FlowLayout(int align)|指定组件相对于容器的对齐方式，水平、垂直间距默认为5个单位|
|FlowLayout(int align,int hgap,int vgap)|指定组件的对齐方式和水平、垂直间距|


表中，列出了FlowLayout的三个构造方法，其中，参数align决定组件在每行中相对于容器边界的对齐方式，可以使用该类中提供的常量作为参数传递给构造方法，其中FlowLayout.LEFT用于表示左对齐、FlowLayout.RIGHT用于表示右对齐FlowLayout.CENTER用于表示居中对齐。参数hgap和参数vgap分别设定组件之间的水平和垂直间隙，可以填入一个任意数值。
```java
import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
 
public class Example02 {
	public static void main(String[] args) {
		//创建一个名为FlowLayout的窗体
		Frame f = new Frame("FlowLayout");
		//设置窗体中的布局管理器FlowLayout,所有组件左对齐，水平间距为20，垂直间距30
		f.setLayout(new FlowLayout(FlowLayout.LEFT, 20, 30));
		//设置窗体的大小
		f.setSize(220, 300);
		//设置窗体显示位置
		f.setLocation(300, 200);
		//把按钮添加到窗口
		f.add(new Button("第1个按钮"));
		f.add(new Button("第2个按钮"));
		f.add(new Button("第3个按钮"));
		f.add(new Button("第4个按钮"));
		
		//设置窗体可见
		f.setVisible(true);
		
	}
}
```
![这是一张图片](amWiki/images/2.1/9.png)	
### BorderLayout
BorderLayout (边界布局管理器) 是一种较为复杂的布方式，它将容器划分为五个区域，分别是东(EAST)、南(SOUTH)、西(WEST)、北(NORTH)、中(CENTER)。组件可以被放置在这五个区域中的任意一个。BorderLayout布局的效果如图所示	

从图可以看出BorderLayout边界布局管理器，将容器划分为五个区域，其中箭头是指改变容器大小时，各个区域需要改变的方向。也就是说，在改变容器时NORTH和SOUTH区域高度不变长度调整，WEST和EAST区域宽度不变高度调整CENTER会相应进行调整。 
![这是一张图片](amWiki/images/2.1/10.png)	
当向BorderLayout布局管理器的容器中添加组件时，需要使用add(Componentcomp,Object constraints)方法。其中参数comp表示要添加的组件，constraints指定将组件添加到布局中的方式和位置的对象，它是一个Obiect类型，在传参时可以使用BorderLayout类提供的5个常量，它们分别是EAST、SOUTH、WEST、NORTH和CENTER。	
案例代码	
接下来通过一个案例来演示一下BorderLayout布局管理器对组件布局的效果：
```java
package cn.itcast.chapter08.example03;
 
import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Frame;
 
public class Example03 {
	public static void main(String[] args) {
		
		Frame f = new Frame("BorderLayout");	//创建一个BorderLayout的窗体
		f.setLayout(new BorderLayout());	//设置窗体中的布局管理器
		f.setSize(300, 300);	//设置窗体大小
		f.setLocation(300, 200);	//设置窗体显示位置
		f.setVisible(true);		//设置窗体可见
		//下面代码是创建5个按钮，分别用于填充BorderLayout的5个区域
		Button but1 = new Button("东部");
		Button but2 = new Button("西部");
		
		Button but3 = new Button("南部");
		Button but4 = new Button("北部");
		Button but5 = new Button("中部");
		
		//将创建好的按钮添加到窗体中，并设置按钮所在区域
		f.add(but1,BorderLayout.EAST);
		f.add(but2,BorderLayout.WEST);
		f.add(but3,BorderLayout.SOUTH);
		f.add(but4,BorderLayout.NORTH);
		f.add(but5,BorderLayout.CENTER);
		
		
	}
 
}
```
![这是一张图片](amWiki/images/2.1/11.png)	
### GridLayout
GridLayout(网格布局管理器) 使用纵横线将容器分成n行m列大小相等的网格每个网格中放置一个组件。添加到容器中的组件首先放置在第1行第1列(左上角)的网格中，然后在第1行的网格中从左向右依次放置其他组件，行满后继续在下一行中从左到右放置组件。与FlowLayout不同的是，放置在GridLayout布局管理器中的组件将自动占据网格的整个区域。	

接下来学习下GridLayout的构造方法，如表所示	 

|方法声明|功能描述|
|-------|--------|
|GridLayout()|默认只有一行，每个组件占一列|
|GridLayout(int rows,int cols)|指定容器的行数和列数|
|GridLayout(int rows,int cols,int hgap,int vgap)|指定容器的行数、列数和水平、垂直间距|

表中，列出了GridLayout的三个构造方法，其中，参数rows代表行数，cols代表列数，hgap和vgap规定水平和垂直方向的间隙。水平间隙指的是网格之间的水平距离，垂直间隙指的是网格之间的垂直距离。	

案例代码	
接下来通过一个案例演示GridLayout布局的用法 ：
```java
package cn.itcast.chapter08.example04;
 
import java.awt.Button;
import java.awt.Frame;
import java.awt.GridLayout;
 
public class Example04 {
	public static void main(String[] args) {
		Frame f = new Frame("GridLayout");	//创建一个GridLayout窗体
		f.setLayout(new GridLayout(3,3));	//设置GridLayout网格布局管理器,该窗体网格为3*3
		f.setSize(300, 300);	//设置窗体大小
		f.setLocation(400, 300);	//设置窗体位置
		
		
		//循环添加9个按钮到GridLayout
		for (int i = 1; i <= 9; i++) {
			Button but = new Button("but"+i);
			f.add(but);	//想窗体中添加按钮
		}
		f.setVisible(true); //设置窗体可见
	}
}
```
![这是一张图片](amWiki/images/2.1/12.png)	
### 绝对布局
当设置 frame.setLayout(null) ；时，可以使用给panel设置坐标的方式控制布局，更具灵活性！
```java
package AWT;
​
import javafx.scene.layout.Pane;
​
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
​
public class panel {
 public static void main(String[] args) {
 Frame frame = new Frame(); //new一个窗口出来
 Panel panel = new Panel(); //new一个面板
 Panel panel1 = new Panel(); //new一个面板
 Panel panel2 = new Panel(); //new一个面板
​
 frame.setLayout(null); //设置布局为空
​
 frame.setBounds(200,200,500,500); //设置窗口位置大小
​
 panel.setBounds(20,15,460,50); //设置第一个面板
 panel.setBackground(new Color(253, 228,1)); //设置面板颜色
 panel1.setBounds(20,70,100,415);
 panel1.setBackground(new Color(0, 71, 254));
 panel2.setBounds(130,70,350,415);
 panel2.setBackground(new Color(1,1,1));
​
 frame.add(panel); //面板加入到窗口中
 frame.add(panel1);
 frame.add(panel2);
​
 frame.setVisible(true);
​
 frame.addWindowListener(new WindowAdapter() {
 @Override
 public void windowClosing(WindowEvent e) {
 System.exit(0);
 }
 }); {
​
 }
​
 }
​
}
```
## 容器组件
Java的图形用户界面的基本组成部分是组件，组件是一个以图形化的方式显示在屏幕上并能与用户进行交互的对象；	

组件不能独立地显示出来，必须将组件放在一定的容器(container)中才可以显示出来。	

容器可以容纳多个组件，通过调用容器的add(Component comp)方法向容器中添加组件。窗口(Frame)和面板(Panel)是最常用的两个容器。	
## 常用容器
1. 窗体
在java中提供JFrame类，用于在Swing程序中创建窗体	
*** (1) JFrame类的构造方法 ***

|构造方法|说明|
|--------|-------|
|JFrame()|创建新窗体，该窗体初始化为不可见|
|JFrame(String title)|创建新窗体,使用参数title指定标题，该窗体初始化为不可见|
|继承JFrame，使用this|创建新窗体，该窗体初始化为不可见|
*** (2) JFrame类的常用方法 ***
|常用方法|说明|
|--------|---|
|void setSize(int width, int height)|设置窗体大小,可以指定宽度和高度|
|void setVisible(boolean b)|设置窗体为可见的或者不可见，默认不可见|
|void setTitle(String title)|设置窗体标题|
|void setResizable(boolean resizable)|设置窗体是否可以被拉长，默认为可以|
|void setLocation(int x,int y)|设置窗体相对坐标原点的位置,默认为(0,0)左上角|
|void setLocationRelativeTo(null)|使窗体位于屏幕正中间|
|void setDefaultCloseOperation(int operation)|设置窗体关闭时程序的状态|
|void dispose()|销毁当前窗体|
2. 面板
java中的Jpanel类，为我们提供了面板，因为我们有了窗体只是空架子,并不能在窗体上设置各种组件，而是在面板上，所以我们再创建一个窗体后紧接着要创建一个面板,在面板上设置各种组件	
*** (1)JPanel类的构造方法 ***

|构造方法|说明|
|--------|---|
|JPanel()|创建一个空面板,默认为流式布局|
|JPanel(LayoutManaer layout)|创建带有指定布局的面板|

*** (2)JPanel类的常用方法 ***

|常用方法|说明|
|--------|---|
|void setBackground(Color bg)|设置面板的背景色,由参数bg指定颜色|
|void setLayout(LayoutManager mgr)|设置面板的布局，参数是布局管理器|
|Component add(Component comp)|往面板中添加一个组件|

## 常用组件
### 1.标签(JLabel)
标签分为文本标签和图片标签，顾名思义是用来在面板上增加文字或图片信息.	

*** (1)JLabel的构造方法 ***

|构造方法|说明|
|-----|-----|
|JLabel()|创建一个标签|
|JLabel(String text)|创建一个带文本的标签|
|JLabel(Icon image)|创建一个图像的标签|

*** (2)JLabel的常用方法 ***

|常用方法|说明|
|------|----|
|void setText(String text)|设置标签上的文本|
|String getText()|获得标签上的文本|
|setFont(new Font(“宋体”,Font.BOLD, 18))|设置字体|

### 2.单行文本(JTextField)
用来输入单行文本的文本框，不能输入回车	

*** (1)JTextField的构造方法 ***

|构造方法|说明|
|-----|-----|
|JTextField()|创建一个空白文本框如上图|
|JTextField(String text)|创建一个带内容的文本框|
|JTextField(String text, int columns)|创建一个带内容，并且指定列数的单行文本框|

*** (1)JTextField的常用方法 ***		

|常用方法|说明|
|-------|-----|
|void setText(String text)|设置文本框中的文本|
|String getText()|获得文本框中的文本|
|void setEditable(boolean b)|设置文本框是否可以编辑,默认可以编辑|
|setColumns(20);|设置列数|	

### 3.多行文本框(JTextArea)
用来输入多行文本，可以输入回车换行	
*** (1)JTextArea的构造方法 ***

|构造方法|说明|
|-------|----|
|JTextArea()|创建一个空的文本域|
|JTextArea(String text)|用指定文本初始化文本域|
|JTextArea(int rows, int columns)|创建一个指定行数和列数的空文本域|
|JTextArea(String text,int rows, int columns)|创建一个带文本，并指行数和列数的空文本域|	

*** (2)JTextArea的常用方法 ***

|常用方法|说明|
|-------|-----|
|void setText(String text)|设置文本域中的文本|
|String getText()|获得文本域中的文本|
|void setFont(Font font)|设置文本域中文本的字体|
|void setLineWrap(boolean wrap)|是否自动换行,默认false|	

如果需要文本区自动出现滚动条，可将文本区对象放入滚动窗格(JScrollPane)中	
```
JScrollPane scrollPane = new JScrollPane(txtArea);

add(scrollPane );
```

### 4.密码框(JPasswordField)
用于输入密码时不可见	
*** (1)JPasswordField的构造方法 ***

|构造方法|说明|
|-------|----|
|JPasswordField()|创建一个空的密码框|
|JPasswordField(String text)|创建一个带文本的密码框|
|JPasswordField(String text, int columns)|创建一个带文本的密码框，并且可以规定列数|

*** (2)JPasswordField的常用方法 ***		

|常用方法|说明|
|-------|-----|
|char [] getPassword()|获得密码框中的文本,存放在char数组中|

### 5.按钮(JButton)		
设置按钮组件	

*** (1)JButton的构造方法 ***	

|构造方法|说明|
|-------|----|
|JButton(String text)|创建一个带文本标签的按钮|
|JButton(Icon image)|创建一个带图像标签的按钮|

*** (2)JButton的常用方法 ***		

|常用方法|说明|
|-------|-----|
|void setBackground(Color bg)|设置按钮的背景色|
|void setEnabled(boolean b)|设置启用(或禁用按钮),由参数b决定|
|void setToolTipText(String text)|设置按钮的悬停提示信息|
|void setContentAreaFilled(boolean b)|设置按钮为透明色|

### 6.菜单栏组件	
给面板上添加一些菜单栏

*** (1)菜单栏的构造方法 ***		

|构造方法|说明|
|-------|----|
|JMenuBar()|创建一个菜单栏对象|

*** (2)菜单栏的常用方法 ***		

|常用方法|说明|
|-------|-----|
|add(menu)|向菜单栏中添加菜单|
|setJMenuBar(menuBar)|将菜单栏添加到窗口，这个方法要用窗体对象调用|

### 7.菜单组件

*** (1)菜单的构造方法 ***		

|构造方法|说明|
|-------|----|
|JMenu(“菜单名称")|创建一个菜单对象|

*** (2)菜单的常用方法 ***		

|常用方法|说明|
|-------|-----|
|add(menuItem)|向菜单中添加菜单选项|

### 8.菜单项组件	
*** 菜单项的构造方法 ***	

|构造方法|说明|
|-------|----|
|JMenuItem(“菜单项名称");|创建一个菜单项对象|	

## 对话框
对话框就是在事件处理时，和用户进行交互的对话框，分为消息对话框和确认对话框	
### JOptionPane对话框
*** (1)showMessageDialog() 消息对话框 ***	

消息对话框一般用于提示用户出现了什么问题或错误	

主要有五种消息类型，类型不同，图标不同：	
ERROR_MESSAGE 错误消息提示	
INFORMATION_MESSAGE 信息提示	
WARNING_MESSAGE 警告提示	
QUESTION_MESSAGE 问题提示	
PLAIN_MESSAGE 简洁提示	

如上述的账号密码为空就是警告提示	

*** (2)showConfirmDialog() 确认对话框 ***
确认对话框一般用于确认对象目前的操作是否继续往下执行	

主要有四种消息类型，类型不同，图标不同：	
DEFAULT_OPTION 默认选项	
YES_NO_OPTION 是/否选项	
YES_NO_CANCEL_OPTION 是/否/取消选项	
OK_CANCEL_OPTION 确定/取消	

## 设置文件选择器
```java
jl = new JLabel("请选择文件");
jl.addMouseListener(new MouseAdapter() {
	@Override
	public void mouseClicked(MouseEvent e) {
	//渲染一个文件选择器，可以选择文件
	JFileChooser chooser = new JFileChooser();
	chooser.setName("选择头像");
	//设置文件选择器能选择文件还是文件夹
	chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
	//设置文件选择器只能选择哪些后缀的文件
	chooser.setFileFilter(new FileNameExtensionFilter("图片", "png","PNG","jpg","JPG","jpeg","JPEG"));
	//展示文件选择器
	chooser.showOpenDialog(null);
	//接受用户选择的文件
	File file = chooser.getSelectedFile();
	jl.setIcon(new ImageIcon(file.getAbsolutePath()));
	}
});
```
## 设置单选框
```java
//设置单选效果，不是组件
ButtonGroup bg = new ButtonGroup();
//表格布局一次只能加一个组件，放在一个JPanel中将两个选择放在一个位置
JPanel temp = new JPanel();
JRadioButton jrb = new JRadioButton("男");
//默认选择
jrb.setSelected(true);
bg.add(jrb);
jrb1 = new JRadioButton("女");
bg.add(jrb1);
temp.add(jrb);
temp.add(jrb1);
jp.add(temp);
```
## 菜单制作 
```java
JTabbedPane jtp = new JTabbedPane();
jtp.setBounds(0, 157, 400, 600);
friend = new JScrollPane();
friendMain = new JPanel();
friendMain.setPreferredSize(new Dimension(390, (users.size() - 1)*101)); 
friendMain.setLayout(null);
friend.setViewportView(friendMain);
friend.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
group = new JScrollPane();
groupMain = new JPanel();
group.setViewportView(groupMain);
group.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
//添加标签
jtp.add("好友", friend);
jtp.add("群聊", group);
this.add(jtp);
```