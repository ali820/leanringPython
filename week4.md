## 第四周 程序的控制结构
### 4.1 程序的分支结构
### 4.2 实例5：身体质量指数BMI
### 4.3 程序的循环结构
### 4.4 模块3：ramdom库的使用
### 4.5 实例6：圆周率的计算

### 4.1 程序的分支结构
- 1. 单分支结构
    - 根据判断条件结果选择不同前进路径的运行方式
        - ```python
        if<条件>:
            <语句块1>
        ```
    - 见到`if ture: `后面的语句一定被执行
    - 见到`if not ture:`后面的语句一定不会被执行
- 2. 二分支结构
    - 根据判断条件结果选择不同前进路径的运行方式
        - ```python
        if<条件>:
            <语句块>
        else:
            <语句块2>
        ```
        - 紧凑形式：`<表达式1> if <条件> else <表达式2>`
            - 对应输出不是语句，而是表达式


```python
#猜数字
guess = eval(input())
print('猜{}了'.format('对'if guess == 99 else '错'))
```

- 3. 多分支结构
     - ```python
        if<条件>:
            <语句块1>
        elif<条件>:
             <语句块1>
          ···
        else:
            <语句块n>
        ```
    - 应当注意语句之间的逻辑包含关系


```python
#不同成绩分级
score = eval(input())
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
print('输入成绩属于级别{}'.format(grade))
```

- 4. 条件判断及组合
    - and：与，or:或，not：非
- 5. 程序的异常处理 
    - 异常处理的基本使用：
        - ```
        try:
            <语句块1>
        except:
            <语句块2>
        ```
    - 进一步了解异常类型：
        - ```
        try:
            <语句块1>
        except<异常类型>:
            <语句块2>
        ```
        高级应用：
         - ``` python
        try:
            <语句块1>
        except:
            <语句块2>
        else：
            <语句块3>  #不发生异常时执行
        finally：
            <语句块4>  #一定执行
        ``` 


```python
# #平方操作
# #未加异常处理
# num = eval(input('请输入一个整数：'))
# print(pow(num,2))

#添加异常处理
try:
    num = eval(input('请输入一个整数：'))
    print(pow(num,2))
except NameError:
    print('输入不是整数')
```

### 4.2 实例5：身体质量指数BMI


```python
#CalBMIv1.py
height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
who = ""
if bmi < 18.5:
    who = "偏瘦"
elif 18.5 <= bmi < 25:
    who = "正常"
elif 25 <= bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"
print("BMI 指标为:国际'{0}'".format(who))
```


```python
#CalBMIv2.py
height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
nat = ""
if bmi < 18.5:
    nat = "偏瘦"
elif 18.5 <= bmi < 24:
    nat = "正常"
elif 24 <= bmi < 28:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI 指标为:国内'{0}'".format(nat))
```


```python
#CalBMIv3.py
height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI 指标为:国际'{0}', 国内'{1}'".format(who, nat))
```

### 4.3 程序的循环结构
- 遍历某个结构形成的循环运行方式
    - ```
    for <循环变量> in <遍历结构>:
        <语句块>
    ```
    - 由保留字fo和in组成，完整遍历所有元素后结束
    - 每次循环，所获得元素放入循环变量，并执行一次语句块  
     - 计数循环（N次） 
        - ```
        for <循环变量> in range(N):
            <语句块>
        for <循环变量> in range(M,N,K):
            <语句块>
        ```



```python

```


```python
for i in range(1,6,2):
    print('hello',i)
```


```python
#字符串遍历循环
for c in 'python123':
    print(c,end =',')
```


```python
#列表遍历循环
for item in [123,'py',456]:
    print(item,end=',')
```

- 文件遍历循环
  - ```
  for line in fi:
    <语句块>
    
 ```
fi是一个文件标识符，遍历其每行，产生循环
- 无线循环：由条件控制的循环运行方式
    - ```
        while<条件>:
            <语句块>
    ```


```python
#例子
a=3
while a>0:
    a-=1
    print(a)
```

    2
    1
    0
    

- 循环控制保留字
- `break`和`continue`
    - break跳出并结束当前整个循环，执行循环后的语句
    - continue结束当次循环，继续执行后续次数循环
    - breaki和 continue可以与for和 while循环搭配使用



```python
#例子
for c in 'python':
    if c == 't':
        continue
    print(c,end=',')
```

    p,y,h,o,n,


```python
#例子
for c in 'python':
    if c == 't':
        break
    print(c,end=',')
```

    p,y,


```python
#例子
s='python'
while s != '':
    for c in s:
        print(c,end=",")
    s=s[:-1]
    print('\n')
```

    p,y,t,h,o,n,
    
    p,y,t,h,o,
    
    p,y,t,h,
    
    p,y,t,
    
    p,y,
    
    p,
    
    


```python
#例子
s='python'
while s != '':
    for c in s:
        if c=='t':
            break
        print(c,end=",")
    s=s[:-1]
    print('\n')
```

    p,y,
    
    p,y,
    
    p,y,
    
    p,y,
    
    p,y,
    
    p,
    
    


```python
#例子
s='python'
while s != '':
    for c in s:
        if c=='t':
            continue
        print(c,end=",")
    s=s[:-1]
    print('\n')
```

    p,y,h,o,n,
    
    p,y,h,o,
    
    p,y,h,
    
    p,y,
    
    p,y,
    
    p,
    
    

- 循环的高级用法
    - 循环与else
        - 当循环没有被break语句退出时，执行else语句块
        - 这里else的用法与异常处理中else用法相似


```python
#循环与else
for c in 'python':
    if c == 't':
        continue
    print(c,end='')
else:
    print('正常退出')
```

    pyhon正常退出
    


```python
#循环与else
for c in 'python':
    if c == 't':
        break
    print(c,end='')
else:
    print('正常退出')
```

    py

### 4.4 模块3：ramdom库的使用
- random库是使用随机数的Python标准库
- 基本随机数函数
    - 随机数种子通过梅森旋转算法产生随机序列，序列中每一个数都是随机数
    - `seed()`:初始化给定的随机数种子，默认为当前系统时间,使用种子可以再现随机过程
    - `random()`:生成一个[0.0，1.0）之间的随机小数


```python
import random as r
r.seed(0)
print(r.random())
print(r.random())
```

    0.8444218515250481
    0.7579544029403025
    

- 扩展随机数函数
- 六个常用


```python
r.randint(10,100)  #生成一个两数之间的随机数
```




    63




```python
r.randrange(10,100,5) #10到100之间随机选取一个以5为步长的整数
```




    15




```python
r.getrandbits(16) #生成一个16比特长的随机整数
```




    16968




```python
r.uniform(10,100) #生成一个10到100之间的随机小数
```




    96.89183977257255




```python
r.choice([1,2,3,4,5,6,67,8])  #从列表里随街选择一个数
```




    8




```python
s=[1,2,3,3,5,6,7,8,9,9,0,5]
r.shuffle(s) #打乱序列顺序
print(s)
```

    [8, 6, 2, 1, 3, 5, 9, 5, 7, 0, 3, 9]
    

能力要求：
- 能够利用随机数种子产生"确定"伪随机数
- 能够产生随机整数
- 能够对序列类型进行随机操作

### 4.5 实例6：圆周率的计算
- 蒙特卡罗方法计算圆周率
- 公式$\pi=\sum_{k=0}^\infty[\frac{1}{16^k}(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6})]$


```python
#CalPiV1,公式
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print('圆周率的值是：{}'.format(pi))
```

    圆周率的值是：3.141592653589793
    


```python
#CalPiV1,蒙特卡洛方法
from random import random
from time import perf_counter
darts = 1000*1000*10
hits = 0.0
start = perf_counter()
for i in range (1,darts+1):
    x,y = random(),random() #x,y是在（0，1）之间的随机数
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0:
        hits +=1
pi = 4*(hits/darts)
print('圆周率的值是：{}\n运行时间是：{:.5f}'.format(pi,perf_counter()-start))
```

    圆周率的值是：3.1419168
    运行时间是：6.87932
    

### 四位玫瑰数 
   ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬四位玫瑰数是4位数的自幂数。自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。  

   ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‪‬‪‬‪‬‮‬‭‬‪例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数，3位数的自幂数被称为水仙花数。

‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬请输出所有4位数的四位玫瑰数，按照从小到大顺序，每个数字一行。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬


```python
from time import perf_counter as p
#start = p()
for i in range(1000,10000):
    i = str(i)
    if eval(i) == pow(eval(i[0]),4)+pow(eval(i[1]),4)+pow(eval(i[2]),4)+pow(eval(i[3]),4):
        print(i)
#print(p()-start)
```

    1634
    8208
    9474
    

### 100以内素数之和

求100以内所有素数之和并输出。 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

素数指从大于1，且仅能被1和自己整除的整数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

提示：可以逐一判断100以内每个数是否为素数，然后求和。


```python
sum = 0
for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        #print(i)
        sum+=i
print(sum)      
```

    1060
    


```python
sum = 0
for i in range(2,100):
    for k in range(2,i):
        if i % k == 0:
            break
    else:                      #是正常退出的都是素数，然后都求和就可以了
            sum += i
print(sum)
```

    1060
    
