[TOC]
# Map集合体系
	Map集合是一个双列结合，本身也是一个接口，代表每条数据都是由key和value两部分组成的

	Map集合中，每一条数据的key值底层是用一个set集合存储的，每一条数据的value值底层使用一个Collection集合存储的。Map集合中key值不允许重复，value数据可以重复的。

	Map集合中keyvalue称之为一个映射关系，map集合中可以根据key值找到集合中与之对应的唯一的一个value值

##	Map集合常用的几个实现类

		HashMap：存放的元素无序的

		LinkedHashMap：存放元素有序（加入）

		HashTable->Properties：存放的数据无序的，读取配置文件
        
		TreeMap：存放元素有序的（按照key值的大小有序，要求key值必须实现了比较器）

key值不允许重复，value可以重复的 