[TOC]
## HDFS的Java API操作
1. 引入依赖dependency
    - hadoop-client
    - hadoop-hdfs
2. 在本地配置hdfs的环境变量

3. 创建配置信息对象
    - Configuration configuration = new Configuration();
4. 设置参数（参数优先级）:  
    1、在代码中设置的值：conf.set("fs.defaultFS","hdfs://192.168.1.200:9000");
    2、resources下的用户自定义配置文件。
    3、然后是服务器的默认配置（是默认的配置，不是自己改过的）

```java
public class HDFSStudy {
    FileSystem fileSystem;
    @Before
    public void getFS() throws URISyntaxException, IOException, InterruptedException {
        Configuration conf = new Configuration();
        fileSystem = FileSystem.get(new URI("hdfs://192.168.247.100:9000"), conf, "root");
    }
    /**
     * 1、Java API在HDFS上创建目录和文件
     */
    @Test
    public void mkdir() throws IOException {
        boolean mkdirs = fileSystem.mkdirs(new Path("/a/b"));
        System.out.println(mkdirs);
    }
    /**
     * 2、创建文件
     */
    @Test
    public void touchFile() throws IOException {
        boolean newFile = fileSystem.createNewFile(new Path("/a.txt"));
        System.out.println(newFile);
    }
    /**
     * 3、删除文件/文件夹
     */
    @Test
    public void deleteFile() throws IOException {
        //两个参数 第一个参数就是待删除的路径  第二参数如果为true代表递归删除（删除非空目录的）
        //删除非空文件夹不会，第二个参数为false，会报错，若找不到文件不会报错
        boolean delete = fileSystem.delete(new Path("/a"), true);
        System.out.println(delete);
    }
    /**
     * 4、判断HDFS路径是文件还是目录  两个方法已经过时了
     */
    @Test
    public void judge() throws IOException {
        boolean directory = fileSystem.isDirectory(new Path("/a.txt"));
        System.out.println(directory);
        boolean file = fileSystem.isFile(new Path("/a.txt"));
        System.out.println(file);
    }
    /**
     * 5、获取某个HDFS路径的详细信息
     */
    @Test
    public void getFileInfo() throws IOException {
        /**
         * FileStatus这个类中封装了很多和文件信息有关的方法
         *  文件的作者 文件的权限 文件的修改时间了等等
         */
        FileStatus fileStatus = fileSystem.getFileStatus(new Path("/a.txt"));
        System.out.println(fileStatus.getOwner());
        System.out.println(fileStatus.getGroup());
        System.out.println(fileStatus.getPermission());
        System.out.println(fileStatus.isFile());//判断路径是否为文件的  建议使用的 没有过时
        System.out.println(fileStatus.isDirectory());
        System.out.println(fileStatus.getModificationTime());
        System.out.println(fileStatus.getPath());
        System.out.println(fileStatus.getBlockSize());
        System.out.println(fileStatus.getReplication());
    }
    /**
     * 6、更改HDFS路径的名字
     */
    @Test
    public void rename() throws IOException {
        boolean rename = fileSystem.rename(new Path("/a.txt"), new Path("/b.txt"));
        System.out.println(rename);
    }
    /**
     * 7、获取某一个目录下所有的文件或者文件夹的方法
     */
    @Test
    public void list() throws IOException {
        FileStatus[] fileStatuses = fileSystem.listStatus(new Path("/"));
        for (FileStatus fileStatus : fileStatuses) {
            System.out.println(fileStatus.getPermission()+" "+fileStatus.getOwner()+" "+fileStatus.getGroup()+" "+fileStatus.getModificationTime()+" "+fileStatus.getPath());
        }
    }
    /**
     * 资源关闭
     */
    @After
    public void distory() throws IOException {
        fileSystem.close();
    }
}
```

## 配置文件对象设置有三种方式：
+ 1、直接通过配置文件对象的set方法设置   100M
+ 2、将HDFS的配置文件：core-site.xml和hdfs-site.xml文件复制到当前项目的resource目录下也行 64M
+ 3、直接使用HDFS自带的默认配置项   128M
+ 如果三个地方同时设置了同一个配置，那么代码配置永远优先生效

