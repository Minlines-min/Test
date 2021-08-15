## ***python基础语法***
**多行注释可以使用'''或者"""**  
**基本面数据类型**：Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Set（集合）、Dictionary（字典）可以为多个变量连续赋值   
**Number**：混合运算时整数变为浮点数，支持复数（complex(a,b)表示(a,b均为浮点数))，可以使用del来对变量进行删除  
**String**；使用'或者"，'\'来进行转义，可以使用 a[x:b]来进行截取，使用+来连接，*来复制  
**List**：a[]，可以使用 a[x:b]来进行截取，使用a[x:b:c]来设置步长截取，内部元素可以变化，可以被索引和切片，使用+拼接，list内置函数（待学习）  
**Tuple**：a()，内部元素不能进行修改，具体方法和列表类似，空元组使用()，单一元素元组使用(x,)    
**Se**t：a{}。可以使用set()函数建立  
**Dictionary**：a{key:value},key的值必须是唯一的且使用不可改变类型，可以使用dict()建立   
**算术运算符**：+、-、*、/、%取模、//取整（特殊）  
**比较运算符（返回值为布尔类型）**：==、!=、>、<、>=、<=  
**赋值运算符**：=、+=、-=、*=、/=、%=、**=、//=、:=海象运算符（需重新学习）  
**逻辑运算符**：and、or、not  
**位运算符（一般用于二进制运算）**：&、|、^、~、<<、>>  
**成员运算符（需重新学习）**：in、not in  
**身份运算符（需重新学习）**：is、not is_

### ***代码示例***
    String

    str = 'Runoob'  
    print(str)  # 输出字符串
    print(str[0:-1])  # 输出第一个到倒数第二个的所有字符  
    print(str[0])  # 输出字符串第一个字符  
    print(str[2:5])  # 输出从第三个开始到第五个的字符  
    print(str[2:])  # 输出从第三个开始的后的所有字符  
    print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)  
    print(str + "TEST", '\n')  # 连接字符串`

    List

    list = ['abcd', 786, 2.23, 'runoob', 70.2]  
    tinylist = [123, 'runoob']  
    print(list)  # 输出完整列表  
    print(list[0])  # 输出列表第一个元素  
    print(list[1:3])  # 从第二个开始输出到第三个元素  
    print(list[2:])  # 输出从第三个元素开始的所有元素  
    print(tinylist * 2)  # 输出两次列表  
    print(list + tinylist, '\n')  # 连接列表

    Tuple

    tuple = ('abcd', 786, 2.23, 'runoob', 70.2)  
    tinytuple = (123, 'runoob')  
    print(tuple)  # 输出完整元组   
    print(tuple[0])  # 输出元组的第一个元素  
    print(tuple[1:3])  # 输出从第二个元素开始到第三个元素  
    print(tuple[2:])  # 输出从第三个元素开始的所有元素  
    print(tinytuple * 2)  # 输出两次元组  
    print(tuple + tinytuple, '\n')  # 连接元组

    Set

    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}  
    print(sites)  # 输出集合，重复的元素被自动去掉

    成员测试

    if 'Runoob' in sites:  
        print('Runoob 在集合中')  
    else:  
        print('Runoob 不在集合中')

    set可以进行集合运算

    a = set('abracadabra')  
    b = set('alacazam')  
    print(a)  
    print(a - b)  # a 和 b 的差集  
    print(a | b)  # a 和 b 的并集  
    print(a & b)  # a 和 b 的交集  
    print(a ^ b, '\n')  # a 和 b 中不同时存在的元素

    Dictionary

    dict = {'one': "1 - 菜鸟教程", 2: "2 - 菜鸟工具"}  
    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}  
    print(dict['one'])  # 输出键为 'one' 的值  
    print(dict[2])  # 输出键为 2 的值  
    print(tinydict)  # 输出完整的字典  
    print(tinydict.keys())  # 输出所有键  
    print(tinydict.values(), '\n')  # 输出所有值_

