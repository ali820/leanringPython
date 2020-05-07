## week 6 组合数据类型
### 6.1 集合类型及其操作
### 6.2 序列类型及其操作
### 6.3 实例9：基本统计值计算
### 6.4 字典类型及操作
### 6.5 模块5：jieba库的使用
### 6.6 实例10：文本词频统计

### 6.1 集合类型及其操作
- 集合是多个元素的无序组合
    1. 集合类型和数学中集合概念一致
    2. 集合元素之间无序，每个元素唯一，不存在相同元素
    3. 集合元素不可更改，不能是可变数据类型
    4. 集合用`{}`表示，元素间用逗号分隔
    5. 建立集合类型用{}或者`set()`
    6. 建立空集合类型，必须用`set()`



```python
#使用{}建立集合,无序，不同
A = {'python',123,('python',123)}           #使用{}建立集合
print(A)
B = set('pypy123')                          #使用{}建立集合
print(B)
```

    {('python', 123), 123, 'python'}
    {'2', 'y', 'p', '1', '3'}
    

- 集合间操作
    1. S|T:返回一个新集合，包括在集合S和T中的所有元素（并）
    2. S-T:返回一个新集合，包括在集合S但不在T中的元素（差）
    3. S&T:返回一个新集合，包括同时在集合S和T中的元素（交）
    4. S^T:返回一个新集合，包括集合S和T中的非相同元素（补）
    5. S<=T或S<T:返回True/False，判断S和T的子集关系
    6. S>=T或S>T:返回True/False，判断S和T的包含关系
- 增强操作符
    1. S|=T：更新集合S，包括在集合S和T中的所有元素
    2. S-=T：更新集合S，包括在集合S但不在T中的元素
    3. S&=T：更新集合S，包括同时在集合S和T中的元素
    4. S^=T：更新集合S，包括集合S和T中的非相同元素


```python
#集合间操作
A={'p','y',123}
B=set('pypy123')
print(A-B,B-A,A&B,A|B,A^B)
```

    {123} {'1', '3', '2'} {'p', 'y'} {'2', 'y', 'p', '3', '1', 123} {'2', 123, '1', '3'}
    

- 集合处理方法
    1. S.add(x):如果x不在集合S中，将x增加到S
    2. S.discard(x)：移除S中元素x，如果x不在集合S中，不报错
    3. S.remove(x)：移除S中元素x，如果x不在集合S中,产生KeyError异常
    4. S.clear(x)：移除S中所有元素
    5. S.pop()：随机返回S的一个元素，并更新S，若S为空产生KeyError异常
    6. S.copy()：返回集合一个副本
    7. len(S)：返回集合S元素个数
    8. x in S：判断S中元素x，x在集合S中，返回Tue，否则返回False
    9. x not in S：判断S中元素x，x不在集合S中，返回Tue，否则返回False
    10. set(x)：将其他类型变量转换成为集合类型


```python
#集合处理方法
A = {'p','y',123}
for i in A:
    print(i,end=' ')
```

    123 y p


```python
try:
    A = {'p','y',123}
    while True:
        print(A.pop(),end=' ')
except:
    pass
```

    123 y p

- 集合类型应用场景
    - 最主要功能是数据去重：利用集合类型所有元素无重复的功能实现


```python
'p' in {'p','y',123}
```




    True




```python
{'p','y'}>={'p','y',123}
```




    False




```python
#数据去重
ls=['p','p','y','y',123]
s=set(ls)
ls=list(s)
print(s,ls)
```

    {123, 'y', 'p'} [123, 'y', 'p']
    

### 6.2 序列类型及其操作
- 序列：具有先后关系的一组元素，是一组一维元素向量，元素类型可以不同
    - 类似数学元素序列
    - 是一个基类类型
    - 字符串类型，元组类型，列表类型
    - 元素存在正向递增，反向递减
- 序列的通用操作符
    - `x in s`:x是序列s的元素，返回True，否则返回False
    - `x not in s`:如果x是序列s的元素，返回False，否则返回True
    - `s+t`:连接两个序列s和t
    - `s*n或n*s`:将序列s复制n次
    - `s[i]`:索引，返回s中的第i个元素,i是序号
    - `s[i:j]或s[i:j:k]`:切片，返回序列s中第i到j以k为步长的元素子序列


```python
#取反
ls=['python',123,'.io']
s='pythom123.o'
print(ls[::-1],s[::-1])
```

    ['.io', 123, 'python'] o.321mohtyp
    

- 函数和方法
    - `len(s)`:返回序列s的长度
    - `min(s)`:返回序列s最小元素，s中元素需要可比较
    - `max(s)`:返回序列s最大元素，s中元素需要可比较
    - `s.index(x)或s.index(x,i,j)`:返回序列s从i开始到j位置中第一次出现元素x的位置
    - `s.count(x)`:返回序列出现x的总次数


```python
ls=['python',123,'.io']
s='pythom123.o'
print(len(ls),max(s))
```

    3 y
    

- 元组是序列类型的一种拓展
    - 一种序列类型，一旦创建不可修改
    - 使用小括号()或tuple()创建，元素间用逗号分隔
    - 可以使用或者不使用小括号
    - 没有特殊操作


```python
#元组的使用
creature = 'cat','dog','tiger','human'
color=(0x001100,'blue',creature)
print(creature,color,creature[::-1],color[-1][2])
```

    ('cat', 'dog', 'tiger', 'human') (4352, 'blue', ('cat', 'dog', 'tiger', 'human')) ('human', 'tiger', 'dog', 'cat') tiger
    

- 列表是序列类型的一种扩展，十分常用
    - 列表是一种序列类型，创建后可以随便修改
    - 使用方括号[]或list()创建，元素间用`,`分隔
    - 列表中各元素类型可以不同，无长度限制


```python
#列表
ls=['cat', 'dog','tiger',1024]
lt=ls
lt
```




    ['cat', 'dog', 'tiger', 1024]



- 列表类型操作函数及方法
    - `ls[i]=x`:替换列表ls第i元素为x
    - `ls[i:j:k]=lt`:用列表lt替换切片后所对应元素子列表
    - `del ls[i]`:删除列表ls中第i元素
    - `del ls[i:j:k]`:删除列表ls中第i到第j以k为步长的元素
    - `ls+=lt`:更新列表ls，将lt元素增加到列表ls中
    - `ls*=n`:更新列表s，其元素重复n次


```python
#列表类型操作
ls=['cat', 'dog','tiger',1024]
ls[1:2]=[1,2,3,4]
print(ls)
del ls[::3]
print(ls)
ls*2
```

    ['cat', 1, 2, 3, 4, 'tiger', 1024]
    [1, 2, 4, 'tiger']
    




    [1, 2, 4, 'tiger', 1, 2, 4, 'tiger']



- 列表类型操作函数及方法
    - `ls.append(x)`:在ls最后增加一个元素x
    - `ls.clear()`:删除列表ls中所有元素
    - `ls.copy()`:生成一个新列表，赋值ls中所有元素
    - `ls.insert(i,x)`:在列表ls第i位置增加元素x
    - `ls.pop(i)`:将列表ls中第i位置元素取出并删除该元素
    - `ls.remove(x)`:将列表ls中出现的第一个元素x删除
    - `ls.reverse()`:将列表ls中的元素反转


```python
#列表类型操作
ls=['cat', 'dog','tiger',1024]
ls.append(1234)
print(ls)
ls.insert(3,'human')
print(ls)
ls.reverse()
print(ls)
```

    ['cat', 'dog', 'tiger', 1024, 1234]
    ['cat', 'dog', 'tiger', 'human', 1024, 1234]
    [1234, 1024, 'human', 'tiger', 'dog', 'cat']
    

- 序列类型应用场景
    - 元组用于元素不改变的应用场景，更多用于固定搭配
    - 列表更加灵活，它是最常用的数据类型
    - 最主要作用：表示一组有效数据，进而操作它们
    - 元素遍历
    - 元组可用于数据保护

### 6.3 实例9：基本统计值计算
- 问题分析
    - 需求：给出一组数据，对它们要有概要的理解
    - 总个数、求和、平均值、方差、中位数···



```python
#CalStatisticsV1
def getNum():
    nums=[]
    iNumStr=input('请输入数字（回车结束）：')
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr=input('请输入数字（回车结束）：')
    return nums
#计算平均值
def mean(numbers):
    s=0.0
    for num in numbers:
        s+=num
    return s/len(numbers)
#计算方差
def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev += (num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)
#计算中位数
def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med
#主函数
n = getNum()
print('源数据：{}\n平均值：{},方差：{:.2},中位数：{}'.format(n,mean(n),dev(n,mean(n)),median(n)))
```

    源数据：[1, 2, 3, 4, 5, 67, 7, 8, 9]
    平均值：11.777777777777779,方差：2.1e+01,中位数：5
    

### 6.4 字典类型及操作
- 映射：映射是一种键（索引）和值（数据）的对应
- 键值对：键是数据索引的拓展
- 字典是键值对的集合，键值对之间无序
- 一般采用大括号{}和dict()创建，键值对用冒号：表示
    - `{<键1>:<值1>,<键2>:<值2>,...,<键n>:<值n>}`
- 字典变量通过键获得值
    - `<字典变量>={<键1>:<值1>,...,<键n>:<值n>}`
    - `<值>=<字典变量>[<键>]`
    - `<字典变量>[<键>]=<值>`




```python
#字典例子
d = {'中国':'北京','美国':'华盛顿','法国':'巴黎'}
print(d['中国'])
de={}#生成空字典
type(de)#返回de类型
```

    北京
    




    dict



- 字典类型函数及方法
    - `del d[k]`：删除字典d中k对应数据值
    - `k in d`：判断键k是否在字典d中，如果在返回True，否则返回False
    - `d.keys()`：返回字典d中所有的键信息
    - `d.values()`：返回字典d中值的信息
    - `d.items()`：返回字典中所有键值对的信息
    - `d.get(k,<default>)`：键k存在，则返回相应值，不存在则返回<default\>值
    - `d.pop(k.<default>)`：键k存在，则取出相应值，不存在则返回<default\>值
    - `d.popitem()`：随机从字典d中取出一个键值对，以元组形式返回
    - `d.clear()`：删除所有键值对
    - `len(d)`：返回字典d中元素个数


```python
#类型操作
d = {'中国':'北京','美国':'华盛顿','法国':'巴黎'}
'中国'in d
print(d.keys(),d.values(),d.get('中国','伊斯兰堡'),d.get('巴基斯坦','伊斯兰堡'),d.popitem())
```

    dict_keys(['中国', '美国']) dict_values(['北京', '华盛顿']) 北京 伊斯兰堡 ('法国', '巴黎')
    


```python
d={} #定义空字典d
d['a']=1;d['b']=2 #向d中新增两个键值对
d['b']=2 #修改赋值时的第二个元素
'c' in d #判断c是否在d中
len(d) #d的长度
d.clear() #清空d
```

- 字典应用类型
    - 映射无处不在，键值对无处不在
    - 例子：统计数据出现次数，数据是键，次数是值
    - 最主要作用：表达键值对数据，进而操作他它们
    - 应用键来对字典遍历

### 6.5 模块5：jieba库的使用
- 中文文本需要通过分词获得单个词语
- jieba是优秀的中文分词第三方库
- jieba库提供三种分词模式，最简单的只需掌握一个函数
- 利用中文词库确定汉字之间的关联概率
- 三种模式
    - 精确模式：文本精确切分开，没有冗余单词
    - 全模式：把文中所有可能的词语扫描出来，有冗余
    - 搜索引擎模式：在精确模式基础上，对长词语再次切分
- 四个函数：
    - `jieba.lcut(s)`：精确模式，返回一个列表类型的分词结果
    - `jieba.lcut(s,cut_all=True)`：全模式，返回一个列表类型的分词结果
    - `jieba.lcut_for_search(s)`：搜索引擎模式，返回一个列表类型的分分词结果
    - `jieba.add_word(w)`：向分词词典种添加新词


```python
#jieba库的函数
import jieba
s='中国是一个伟大的国家'
print(jieba.lcut(s),'\n',jieba.lcut(s,cut_all=True),'\n',jieba.lcut_for_search(s),'\n',jieba.add_word('python'))

```

    ['中国', '是', '一个', '伟大', '的', '国家'] 
     ['中国', '国是', '一个', '伟大', '的', '国家'] 
     ['中国', '是', '一个', '伟大', '的', '国家'] 
     None
    

### 6.6 实例10：文本词频统计
- 需求，分析文章出现哪些次，哪些词出现的最多（中文和英文）
- 英文：Hamlet  
- 中文：三国演义

- 英文：噪音处理，归一化，提取单一单词作为第一步骤



```python
#CalHamletV
#归一化文本
def getText():
    txt = open('Hamlet.txt','r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch,' ') #将文本中字符替换为空格
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
for i in range(10):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))
```

    the        1138
    and         965
    to          754
    of          669
    you         550
    i           542
    a           542
    my          514
    hamlet      462
    in          436
    

- 三国演义：jieba分词，无特殊符号等


```python
#CalThreeKingdomsV1
import jieba as j
txt = open('三国演义.txt','r',encoding='utf-8').read()
words = j.lcut(txt)
counts={}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
for i in range(15):
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))
```

    曹操          953
    孔明          836
    将军          772
    却说          656
    玄德          585
    关公          510
    丞相          491
    二人          469
    不可          440
    荆州          425
    玄德曰         390
    孔明曰         390
    不能          384
    如此          378
    张飞          358
    


```python
#CalThreeKingdoms
import jieba
excludes = {"将军","却说","荆州","二人","不可","不能","如此","军马","军士","左右"}
txt = open("三国演义.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
```

    曹操         1451
    孔明         1383
    刘备         1252
    关羽          784
    张飞          358
    商议          344
    如何          338
    主公          331
    吕布          300
    赵云          278
    


```python
d= {'a': 1, 'b': 2, 'b': '3'}
print(d['b'])
```

    3
    


### 数字不同数之和
描述
获得用户输入的一个整数N，输出N中所出现不同数字的和。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭

例如：用户输入 123123123，其中所出现的不同数字为：1、2、3，这几个数字和为6。


```python
#数字不同数之和
s = input()
s = set(s)
sum=0
for i in s:
    sum += int(i)
print(sum)

```

    6
    

### 人名最多数统计


描述
编程模板中给出了一个字符串，其中包含了含有重复的人名，请直接输出出现最多的人名。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬输入输出示例
这里是个示例，展示输出格式，不是结果。


```python
#输出字符串最多的值
s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''
ls=s.split()
counts={}
for i in ls:
    counts[i]=counts.get(i,0)+1
max_name,max_cnt='',0
for name in counts:
    if counts[name]>max_cnt:
        max_name,max_cnt = i,counts[i]
print(max_name)
```

    赵敏
    


```python
s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''
ls = s.split()
d = {}
for i in ls:
    d[i] = d.get(i, 0) + 1
max_name, max_cnt = "", 0
for k in d:
    if d[k] > max_cnt:
        max_name, max_cnt = k, d[k]
print(max_name)
```

    赵敏
    
