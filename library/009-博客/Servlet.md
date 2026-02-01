[TOC]

## 什么是Servlet

Servlet是基于Java技术的、容器托管的、用于生成动态内容的Web组件。容器，有时候也叫做Servlet引擎，是Web服务器为支持Servlet功能扩展的部分。客户端通过Servlet容器实现的请求/应答模型与Servlet交互。

## Servlet逻辑结构

在Servlet体系中，Servlet容器是核心，它负责处理Web服务器转发的Servlet请求，在调用Servlet组件前，如果配置了过滤器，则调用Servlet前置的过滤器，而在请求处理或者容器发生相关事件时调用配置好的监听器。Servlet的逻辑结构如图3-1所示：

![20](img/20.png)

以下是一个典型的请求处理序列：

1. 客户端（如Web浏览器）发送一个按照HTTP协议组装的请求到Web服务器
2. Web服务器接受到请求后，判断请求的是否是动态内容，如果是，则把请求交给Servlet容器处理
3. Servlet通过请求对象得到远程用户参数和其他有关数据。Servlet执行我们编写的任意的逻辑，然后动态产生响应内容发送回客户端。
4. 一旦Servlet完成请求的处理，Servlet容器必须确保响应正确的刷出，并且将控制权还给宿主Web服务器。

## Servlet生命周期

Servlet 生命周期指的是 Servlet 对象从创建到销毁的整个过程，包括以下阶段：

1. 加载和实例化阶段（loading and instantiation）：当 Servlet 容器启动或者第一次请求某个 Servlet 时，会加载并创建 Servlet 对象的实例。在此阶段，容器会调用 ServletContext 的 getServlet 方法来获取 Servlet 实例，并调用其 init 方法进行初始化。在 init 方法中，Servlet 可以进行一些初始化工作，如加载配置文件、建立数据库连接等。init 方法被设计成只调用一次。它在第一次创建 Servlet 时被调用，在后续每次用户请求时不再调用。因此，它是用于一次性初始化，创建于用户第一次调用该 Servlet 的 URL 时，也可以指定 Servlet 在服务器第一次启动时被加载。

2. 就绪阶段（ready）：当 Servlet 初始化完成后，容器会将其放入就绪状态，表示它已经准备好处理客户端请求了。

3. 请求处理阶段（request handling）：当客户端发起请求时，Servlet 容器会为每个请求创建一个新的线程，并调用 Servlet 的 service 方法处理请求。在 service 方法中，Servlet 可以读取请求数据、进行业务处理，并生成响应数据发送给客户端。通过源代码可见，service()方法中对请求的方式进行了匹配，选择调用doGet,doPost等这些方法，然后再进入对应的方法中调用逻辑层的方法，实现对客户的响应。由于在Servlet接口和GenericServlet中是没doGet,doPost等等这些方法的，HttpServlet中定义了这些方法，所以，我们每次定义一个Servlet的时候，都必须实现doGet或 doPost等这些方法。

4. 销毁阶段（destruction）：当 Servlet 容器关闭或者 Web 应用程序被卸载时，会调用 Servlet 的 destroy 方法，此时 Servlet 会执行一些清理工作，如关闭数据库连接、保存会话数据等。在销毁阶段结束后，Servlet 实例将被销毁并释放资源。在调用 destroy() 方法之后，servlet 对象被标记为垃圾回收。

​    需要注意的是，**Servlet 生命周期中 init 和 destroy 方法只会在 Servlet 实例创建和销毁时被调用一次，而 service 方法则会在每个请求到达时被调用一次**。此外，Servlet 还可以实现其他生命周期方法，如 init(ServletConfig config)、getServletConfig() 等，以提供更加灵活的初始化和配置方式。

​    一般情况下，Servlet只有在容器关闭时才会被销毁，但也可以通过Servlet的destroy()方法手动销毁Servlet。当Servlet不再被需要时，可以通过调用destroy()方法来释放资源、关闭数据库连接、取消注册等操作。**Servlet的生命周期是整个应用程序中Servlet的初始化、请求处理和销毁的过程。**

​    Servlet 生命周期流程如下图所示：



![8](img/8.png)

​    下面通过一个案例加深对 Servlet 生命周期的理解：

```java
@WebServlet("/myServletLife")
public class MyServletLife extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private int initCount = 0;
    private int httpCount = 0;
    private int destoryCount = 0;
    @Override
    public void destroy() {
        destoryCount++;
        super.destroy();
        // 向控制台输出destory方法被调用次数
        System.out.println(
                "**********************************destroy方法：" + destoryCount + "*******************************");
    }

    @Override
    public void init() throws ServletException {
        initCount++;
        super.init();
        // 向控制台输出init方法被调用次数
        System.out.println("调用init方法：" + initCount);
    }

    public void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        httpCount++;
        // 控制台输出doGet方法次数
        System.out.println("doGet方法：" + httpCount);
        // 设置返回页面格式与字符集
        resp.setContentType("text/html;charset=UTF-8");
        PrintWriter writer = resp.getWriter();
        // 向页面输出
        writer.write("初始化次数:" + initCount + "<br/>" + "处理请求次数:" + httpCount + "<br/>" + "销毁次数:" + destoryCount);
        writer.close();
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        this.doGet(request, response);
    }
}
```


​    启动 Tomcat，在地址栏输入“localhost:8080/web/myServletLife”，多次访问 MyServlet，结果如下图。

![9](img/9.png)  

关闭 Tomcat 服务器，控制台输出如下图 

![10](img/10.png)