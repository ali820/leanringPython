## 第三周 基本数据类型
### 3.1 数据类型及操作
### 3.2 实例3:天天向上的力量
### 3.3 字符串类型及其操作
### 3.4 模块2：time库使用
### 3.5 实例4：文本进度条

### 3.1 数据类型及操作
>整数类型:与数学中整数的概念一致,可正可负，没有取值范围限制   

- pow（x y）函数：计算$x^y$，想算多大算多大  

四种进制表示形式：
- 十进制：1010，99，-217等
- 二进制，以0b或者0B开头：0b010，-0B10
- 八进制，以00或0O开头：00123，-00456
- 十六进制，以0x或0X开头：0x9a2，-0X89


```python
pow(2,10) #pow函数
```




    1024



>浮点数：带有小数点的数，与数学中概念一直，范围$-10^{308}$~$10^{308}$,精度$10^{-16}$

- 浮点数的尾数存在不确定尾数，不是bug  
- round（x，d）：对x四舍五入，d是小数截取位数  
浮点数间运算及比较用round0函数辅助
- 浮点数可以采用科学计数法表示  
使用字母e或E作为幂的符号，以10为基数，格式如下
<a>e<b>表示a*10b
例如：4.3e-3值为000439.6E5值为960000.0


```python
0.1+0.2  #不确定尾数
```




    0.30000000000000004




```python
0.1+0.2==0.3
```




    False




```python
round(0.1+0.2,3)==0.3
```




    True




```python
7.8e-1
```




    0.78



>复数类型：与数学中复数一致




```python
z=1.23e-4+5.6e+89j
#z.imag
z.real
```




    0.000123



>数值运算操作符


+，-，*，/，//：加，减，乘，除，整数除
- +x：x本身
- -y：y的负值
- x%y：y对x取余
- x**y：幂运算

- 增强运算符：x op= y，即x = x op y



```python
4**0.5
```




    2.0




```python
x=2
x*=3
print(x)
```

    6
    

>数值运算函数:一些以函数形式提供数值运算的功能


```python
abs(-10.00001) #绝对值函数abs（x）
```




    10.00001




```python
divmod(10,3) #商余，（x//y，x%y）
```




    (3, 1)




```python
pow(4,pow(2,1),10) #幂余，（x*y）%z，[]表示参数z可省路
```




    6




```python
round(10.12345,3) #四舍五入，d是保留小数位数，默认值为0
```




    10.123




```python
max(1,3,5,6,7,8,9,10,0b11111111111111111111111111111110101010) #最大值
```




    274877906858




```python
min(1,3,4,5,6,7,87,8,8,-0x123a27365) #最小数
```




    -4892816229




```python
int(123.3456) #将数变成整数，舍弃小数部分
```




    123




```python
float(10) #将数变成浮点数，增加小数部分
```




    10.0




```python
complex(-10e2) #将整变成复数，增加虚数部分
```




    (-1080+0j)



### 3.2 实例3:天天向上的力量
>问题1：千分之一的历力量
- 每天进步0.001，一年累计进步多少？
- 每天退步0.001，一年累计退步多少？


```python
#DayDayUpQ1
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print('向上：{:.2f},向下：{:.2f}'.format(dayup,daydown))
```

    向上：1.44,向下：0.69
    

问题2：改为百分之一或者千分之五  
在代码里加变量，更改变量即可


```python
#DayDayUpQ2
dayfactor = 0.01
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print('向上：{:.2f},向下：{:.2f}'.format(dayup,daydown))
```

    向上：37.78,向下：0.03
    

问题3：5个工作日进步1%，2个休息日退步1%


```python
#DayDayUpQ3
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup *= (1 - dayfactor)
    else:
        dayup *= (1 + dayfactor)
print('进步：{:.2f}'.format(dayup))
```

    进步：4.63
    

问题4：工作日努力程度多少时，才能与每天努力1%相同（休息两天下降1%不变）


```python
#DayDayUpQ4
def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup

dayfactor = 0.01
while dayUp(dayfactor) < round(pow(1.01,365),2):
    dayfactor += 0.001
 
print('工作日的努力程度：{:.3f}'.format(dayfactor))
```

    工作日的努力程度：0.019
    

### 3.3 字符串类型及其操作
>由0个或多个字符组成的有序字符序列

- 字符串由一对单引号或一对双引号表示  
字符串是字符的有序序列，可以对其中的字符进行索引
- 字符串有2类共4种表示方法
由一对单引号或双引号表示，仅表示单行字符串  
由一对三单引号或三双引号表示，可表示多行字符串
- 如果希望在字符串中包含双引号或单引号呢？  
需要哪种引号就不把那种引号作为字符串的标记
- 同时存在正向递增（从0开始）、反向递减（从-1开始）
- 索引：返回字符串中单个字符:<字符串>\[M]  
切片：返回字符串中一段字符子串:<字符串>\[M：N]，M缺失表示至开头，N缺失表示全培尾  
<字符串>M：N：K]，根据步长K对字符串切片
- 转义符：\ 可以表示字符的本意  
转义符形成一些组合，表达一些不可打印的含义:"\b"回退,"\n"换行（光标移动到下行首）,"\r"回车（光标移动到本行首）
>由0个或多个字符组成的有序字符序列

- x+y:连接两个字符串  
n\*x或x*n：复制n次字符串x  
 x in s：如果x是s的子串，返回True，否则返回 False  




```python
#WeekNamePrintV1
weekStr = '星期一星期二星期三星期四星期五星期六星期日'
weekId = eval(input('请输入星期数字（1-7）：'))
pos = (weekId - 1)*3
print(weekStr[pos:pos+3])

```

    星期二
    


```python
#WeekNamePrintV1
weekStr = '一二三四五六日'
weekId = eval(input('请输入星期数字（1-7）：'))
print('星期'+weekStr[weekId-1])
```

    星期日
    

>字符串处理函数


```python
len('1yi一') #字符串长度
```




    4




```python
str(1234) #将任意类型变成字符串
```




    '1234'




```python
hex(234) #将整数变成16进制
```




    '0xea'




```python
oct(234) #将整数变成8进制
```




    '0o352'




```python
chr(1234) #Unicode编码返回其对应的字符
```




    'Ӓ'




```python
ord('A') #字符，返回其对应的 Unicode编码
```




    65




```python
#输出星座字符
for i in range (12):
    print(chr(9800+i),end = '')
```

    ♈♉♊♋♌♍♎♏♐♑♒♓

>方法"在编程中是一个专有名词  
- "方法"特指`<a>.<b>()`风格中的函数`<b>()`  
方法本身也是函数，但与`<a>`有关，`<a>.<b>()`风格使用  
字符串及变量也是`<a>`，存在一些方法




```python
'ABDHSUwwbdja'.lower() #全部字符小写 
```




    'abdhsuwwbdja'




```python
'ASJIJIHDqhsudhausbc'.upper() #全部字符大写
```




    'ASJIJIHDQHSUDHAUSBC'




```python
'A<BAB<G'.split('<') #按照给定符号将一个字符串拆解成为列表
```




    ['A', 'BAB', 'G']




```python
'an apple a day'.count('a') #查字符串中的出现数目 
```




    4




```python
'python'.replace('n','n123.io') #替换字符串中某些元素
```




    'python123.io'




```python
'python'.center(20,'~') #根据20的宽度用~填充居中字符
```




    '~~~~~~~python~~~~~~~'




```python
'= python ='.strip(' =np') #去除左右两端的字符
```




    'ytho'




```python
'-'.join('我是谁？') #用于字符串分隔
```




    '我-是-谁-？'



>字符串类型的格式化
- 槽：一种用于字符串的占位信息符


```python
'{}:计算机{}的CPU占用率：{}%'.format('2018-10-10','C',pow(2,5)) #槽机制+format方法
```




    '2018-10-10:计算机C的CPU占用率：32%'




```python
'{:=^50}'.format('python') #=填充，居中对齐，宽度50
```




    '======================python======================'




```python
'{:,.2f}'.format(12345.678947) #千位分隔，精度为2，浮点数类型
```




    '12,345.68'



### 3.4 模块2：time库使用
>time库：Python中处理时间的标准库 
计算机时间的表达  
提供获取系统时间并格式化输出功能  
提供系统级精确计时功能，用于程序性能分析  

- 包括三类函数
    - 时间获取：`time()`,`ctime()`,`gmtime()`
    - 时间格式化：`strftime()`,`strptime()`
    - 程序计时：`sleep()`,`perf_time()`


```python
import time as t

#时间获取
t.time() #1970/1/1 0.0.0 至今的秒数,计算机内部时间
```




    1583509138.1986494




```python
t.ctime() #获取当前时间并以易读方式表示，返回字符串
```




    'Fri Mar  6 23:38:53 2020'




```python
t.gmtime() #获取当前时间，表示为计算机可处理的时间格式
```




    time.struct_time(tm_year=2020, tm_mon=3, tm_mday=6, tm_hour=15, tm_min=39, tm_sec=3, tm_wday=4, tm_yday=66, tm_isdst=0)




```python
#时间格式化：类似字符申格式化，需要有展示模板，展示模板由特定的格式化控制符组成

Time = t.gmtime() #获取计算机可读的时间
t.strftime('%Y-%m-%B-%b-%d  %H（%I）:%M:%S  %A-%a  %p',Time) #按照定义的模板输出时间类型变量，%B表示英文十二个月全名称，其余看示例
```




    '2020-03-March-Mar-06  15（03）:41:40  Friday-Fri  PM'




```python
#读取字符串里的时间为计算机可识别的
timeStr = '2020-03-06  23:46:34'
t.strptime(timeStr,'%Y-%m-%d  %H:%M:%S')
```




    time.struct_time(tm_year=2020, tm_mon=3, tm_mday=6, tm_hour=23, tm_min=46, tm_sec=34, tm_wday=4, tm_yday=66, tm_isdst=-1)




```python
#程序计时：测量起止动作所经历时间的过程，分测量时间和产生时间
start = t.perf_counter()#测量时间,差值才有意义
end = t.perf_counter()
end - start
```




    2.6000000161729986e-05




```python
def wait():
    t.sleep(3.3)
wait()#程序等待3.3s后继续
```

### 3.5 实例4：文本进度条


```python
#TextProBarV1
import time as t #引入库
scale = 10
print('------执行开始------') #开始标签
for i in range(scale+1): #产生循环，每一个循环产生时间和打印进度条
    a = "*"*i
    b = '.'*(scale - i) #字符串与整数的乘积表示字符串复制的次数
    c = (i/scale)*100
    print('{:^3.0f}%[{}->{}]'.format(c,a,b))
    t.sleep(0.3)
print('-------执行结束------') #结束标签
```

    ------执行开始------
     0 %[->..........]
    10 %[*->.........]
    20 %[**->........]
    30 %[***->.......]
    40 %[****->......]
    50 %[*****->.....]
    60 %[******->....]
    70 %[*******->...]
    80 %[********->..]
    90 %[*********->.]
    100%[**********->]
    -------执行结束------
    


```python
#TextProBarV1 单行刷新
#刷新的本质是用后打印的字符覆盖前面的字符
#需要控制print函数，防止其自动换行
import time as t
for i in range(101):
    print('\r{:3}%'.format(i),end = '')
    t.sleep(0.1)
```

    100%


```python
#TextProBarV3
import time as t #引入库
import math as m 
scale = 50
print('执行开始'.center(scale//2,'-')) #开始标签
start = t.perf_counter()
for i in range(scale+1): #产生循环，每一个循环产生时间和打印进度条
    a = "*"*i
    b = '.'*(scale - i) #字符串与整数的乘积表示字符串复制的次数
    #c = (i/scale)*100  #线性记录进度
    c = round((m.sin(i/scale*0.5*(m.pi))),3)*100
    dur = t.perf_counter()-start
    print('\r{:^3.0f}%[{}->{}] [{:.2f}s]'.format(c,a,b,dur),end = '')
    t.sleep(0.1)
print('\n'+'执行结束'.center(scale//2,'-')) #结束标签
```

    -----------执行开始----------
    100%[**************************************************->] [5.03s]
    -----------执行结束----------
    

- 进度条是人机交互的较好的表现形式


```python
val = pow(2,1000)
len(str(val))
```




    302




```python
s='PYTHON'
print("{0:3}".format(s))
```

    PYTHON
    

#### 平方根格式化

获得用户输入的一个整数a，计算a的平方根，保留小数点后3位，并打印输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

输出结果采用宽度30个字符、右对齐输出、多余字符采用加号(+)填充。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

如果结果超过30个字符，则以结果宽度为准。


```python
zhengshu = input()
print('{:+>30.3f}'.format(pow(eval(zhengshu),0.5)))
```

    ++++++++++++++++++0.000+3.162j
    

#### 字符串分段组合

获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。


```python
zifu = input()
ZiFu = zifu.split('-')
print('{}+{}'.format(ZiFu[0],ZiFu[-1])) 
```

    Alice+Flurry
    
