[TOC]
# javascript
[TOC]
# JavaScript 前端脚本语法  

JavaScript 通常被称为 JS，他发明的目的，就是作为浏览器的内置脚本语言，为网页开发者提供操控浏览器的能力，他可以让网页呈现出各种特殊效果，为用户提供友好的互动体验。随着 Ajax 技术的出现，前端可以在不刷新页面的情况下和后端进行数据交换，更新页面数据，jQuery 等库的盛行让 JS 编写变得异常简单。

## BOM
BOM(Browser Object Model) 浏览器对象模型

### window对象
1. window对象属性
![属性](amWiki/images/w1.png)
2. window对象方法
![方法](amWiki/images/w2.png)

### console对象
1. console对象方法
![方法](amWiki/images/console.png)

### location 对象
1. location对象属性
![属性](amWiki/images/loc1.png)
2. location对象方法
![方法](amWiki/images/loc2.png)

### history 对象
1. history对象属性
![属性](amWiki/images/h1.png)
2. history对象方法
![方法](amWiki/images/h2.png)

### Navigator 对象
1. Navigator对象属性
![属性](amWiki/images/nav1.png)


## DOM
DOM 是 Document Object Model（文档对象模型）的缩写。 是用来呈现以及与任意 HTML 或 XML 交互的API文档。DOM 是载入到浏览器中的文档模型，它用节点树的形式来表现文档，每个节点代表文档的构成部分。
### DOM属性和方法
1. DOM属性
![属性](amWiki/images/dom1.png)
2. DOM方法
![方法](amWiki/images/dom2.png)

### 事件集合
1. 鼠标事件
    - onclick	点击
    - ondblclick	双击
    - onmousedown	按下
    - onmouseup	抬起
    - onmousemove	移动
    - onmouseover	移入
    - onmouseout	移出
    - onmouseenter	鼠标指针移动到元素上时触发(不支持冒泡)
    - onmouseleave	鼠标指针移出元素上时触发(不支持冒泡)
    - oncontextmenu	右键
2. 键盘事件
    - onkeydown	按下
    - onkeyup	抬起
    - onkeypress	按下(只能触发数字字母符号)
3. 表单事件
    - onfocus	获得焦点
    - onblur	失去焦点
    - onchange	失去焦点并内容改变
    - onsubmit	提交事件（form标签事件）
    - onreset	重置事件（form标签事件）
    - oninput	表单输入
4. 其他事件
    - onscroll	滚动条事件(滚动条位置改变)
    - onwheel	鼠标滚轮事件
    - onresize	页面尺寸改变
    - onload	页面加载完成之后执行该事件
    - DOMContentLoaded	页面结构加载完成执行该事件

### 绑定事件的方式
1. 标签绑定事件
    ```
        <button onclick="click_fn()">click</button>
        <script>
        function click_fn(){
            console.log(this);
        }
        </script>
    ```
2. Document对象来绑定事件
    ```
        <button>click</button>
        <script>
            var button1 = document.querySelector('button')
            button1.onclick=function(){
                console.log("第一个点击事件的方法");
            }
            var button2 = document.querySelector('button')
            button2.onclick=function(){
                console.log("第二个点击事件的方法");
            }      //第二个点击事件的方法会覆盖第一个方法,所以点击只会触发第二次的点击事件方法     
        </script>
    ```

### DOM节点
1. 节点属性
![属性](amWiki/images/jiedian1.png)
2. 节点方法
![方法](amWiki/images/jiedian2.png)

### 表单
获得表单元素的引用：
1. 直接获取
    - document.getElementById();
    - document.getElementsByName();
    - document.getElementsByTagName();
2. 通过集合来获取
    - 表单对象.elements 获得表单里面所有元素的集合
    - 表单对象.elements[下标]
    - 表单对象.elements["name"]
    - 表单对象.elements.name
3. 直接通过name的形式
    - 表单对象.name

### 监听
    ```
        <button id="myBtn"></button>
        <script type="text/javascript">
        var btn=document.getElementById('myBtn');
        function handle(){
            console.log(this);
        }
        //兼容到IE9及其以上
        btn.addEventListener('click',handle,false);      //添加事件处理程序
        btn.removeEventListener('click',handle,false);    //移除事件处理程序

        //  ie8及以下
        btn.attachEvent('onclick',handle);       // 添加
        btn.detachEvent('onclick',handle);       // 移除
        </script>
    ```