## 第五周 函数和代码
### 5.1 函数的定义与使用
### 5.2 实例7：七段数码管绘制
### 5.3 代码复用与函数递归
### 5.4 模块4：PyInstaller库的使用
### 5.5 科赫雪花小包裹



### 5.1 函数的定义与使用
- 函数的理解与定义
    - 函数是一段代码的表示，是具有一定功能的、可重复使用的语句组，是一种功能的抽象
    - 两个作用：
        - 降低编程难度
        - 代码复用
    - ```
        def<函数名>(<参数（0个或者多个）>):
            <函数体>
            return <返回值>
        ```
    - 函数定义时，所指定的参数是一种占位符
    - 函数定义后，如果不经过调用，不会被执行
    - 函数定义时，参数是输入、函数体是处理、结果是输出（IPO）
    



```python
#计算n！
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

n = input()
b=fact(int(n))
print(b)
```

    3628800
    

- 函数的使用及调用过程
    - 函数只有被调用，才会被执行

- 函数的参数传递
    - 无论函数有没有参数，都要保留括号
    - 可选参数：函数定义时可以为某些参数指定默认值，构成可选参数
        -  ```
        def<函数名>(<非可选参数（必选参数）>，<可选参数>):
            <函数体>
            return <返回值>
        ```
        - 可选参数一定要在必选参数后面
    - 可变参数的传递：函数定义时可以设计可变数量参数，既不确定参数总数量
        -  ```
        def<函数名>(<参数>，*b):
            <函数体>
            return <返回值>
        ```
    - 函数调用时，参数可以按照位置或名称方式传递



```python
#可选参数：计算n！//m
def fact(n,m=1):  #m是可选参数
    s=1
    for i in range(1,n+1):
        s*=i
    return s//m
b=fact(10,5)    #位置传递
c=fact(m=5,n=10) #名称传递
print(b,c)

```

    725760 725760
    


```python
#可变参数：计算n！//m
def fact(n,*b):  #*b为可变参数
    s=1
    for i in range(1,n+1):
        s*=i
    for item in b:
        s*=item
    return s
print(fact(3))
print(fact(3,4,6))
print(fact(3,10,9,10))
```

    6
    144
    5400
    

- 函数的返回值
    - 函数可以返回0或者多个结果，也可以不返回



```python
#可选参数：计算n！//m
def fact(n,m=1):  #m是可选参数
    s=1
    for i in range(1,n+1):
        s*=i
    return s,m,s//m  #返回三个值

b=fact(10,5)    #位置传递
c=fact(m=5,n=10) #名称传递

x,y,z = fact(10,5) #返回的三个值分别赋给xyz

print(b,c)
print(x,y,z)
```

    (3628800, 5, 725760) (3628800, 5, 725760)
    3628800 5 725760
    

- 局部变量和全局变量
    - 局部变量是函数内部使用的变量




1. 局部变量和全局变量是不同变量
- 局部变量是函数内部的占位符，可以与全局变量重名但是不相同
- 函数运算结束后，局部变量被释放
- 可以使用`global`保留字在函数内部使用全局变量


```python
n,s=10,100 #此处n，s是全局变量
def fact(n):        #fact函数中的n，s是局部变量
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(fact(n),s)  #n,s是全局变量
```

    3628800 100
    


```python
n,s=10,100 #此处n，s是全局变量
def fact(n):        #fact函数中的n，s是局部变量
    global s   #声明是全局变量
    for i in range(1,n+1):
        s*=i
    return s
print(fact(n),s)  #n,s是全局变量
```

    362880000 362880000
    

2. 局部变量为组合数据类型且未创建，等同于全局变量


```python
ls=['F','f'] #创建全局变量s
def func(a):
    ls.append(a) #此处ls是列表类型，未真实创建则等同于全局变量
    return
func('C') #全局变量ls被修改
print(ls)
```

    ['F', 'f', 'C']
    


```python
ls=['F','f'] #创建全局变量s
def func(a):
    ls = []     #此处ls是列表类型，真实创建ls是局部变量，函数运行完成就被释放
    ls.append(a) 
    return
func('C') #局部变量ls被修改
print(ls)
```

    ['F', 'f']
    

- lambda函数
    - lambda函数返回函数名作为结果
         1. lambda函数是一种匿名函数，即没有名字的函数
         2. 使用lambda保留字定义，函数名是返回结果
         3. lambda函数用于定义简单的、能够在一行内表示的函数
         ```
         <函数名>=lambda<参数>:<表达式>
         ```
    - 谨慎使用lambda函数
        - lambda函数主要用作一些特定函数或方法的参数
        - lambda函数有固定的使用方式


```python
#
f = lambda x,y:x+y
print(f(10,15))
```

    25
    

### 5.2 实例7：七段数码管绘制
- 交通灯的显示等
    1. 绘制三个数字的数码管
        - 七段数码管由7个基本线条组成
        - 七段数码管可以有固定顺序
        - 不同数字显示不同的线条
    2. 获得一串数字，绘制对应数码管
    3. 获得当前时间，绘制对应数码管



```python
#SevenDigitsDrawV1.py
import turtle as t

def drawLine(draw):                                                             #绘制单段数码管
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)

def drawDigit(digit):                                                        #根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)                                                             #为后续数字确定位置
    t.penup()                                                               #为后续数字确定位置
    t.fd(20)                                                                #为后续数字确定位置

def drawDate(date): 
    for i in date:
        drawDigit(eval(i))                                                   #通过eval（）函数将数字变为整数

def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate('20200317')
    t.hideturtle()
    t.done
main()
```


```python
#SevenDigitsDrawV2.py
import turtle as t
import time as ti

def drawGap():                                                                  #绘制数码管间隔
    t.penup()
    t.fd(5)

def drawLine(draw):
    drawGap()                                                             #绘制单段数码管
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)

def drawDigit(digit):                                                        #根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)                                                             #为后续数字确定位置
    t.penup()                                                               #为后续数字确定位置
    t.fd(20)                                                                #为后续数字确定位置


#遇到-是年，遇到=是月，遇到+是日
def drawDate(date): 
    t.pencolor('red')                                                        #date为日期，格式为‰Y-‰m=%d+
    for i in date:
        if i == '-':
            t.write('年',font = ('Arial',18,'normal'))                                                   
            t.pencolor('green')
            t.fd(40)
        elif i == '=':
            t.write('月',font = ('Arial',18,'normal'))
            t.pencolor('blue')
        elif i == '+':
            t.write('日',font = ('Arial',18,'normal'))
        else:
            drawDigit(eval(i))

def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(ti.strftime('%Y-%m=%d+',ti.gmtime()))
    t.hideturtle()
    t.done
main()
```

### 5.3 代码复用与函数递归
- 把代码当作资源进行抽象：
    - 代码资源化：程序代码是一种用来表达计算的“资源”
    - 代码抽象化：使用函数等方法对代码赋予更高级别的定义
    - 代码复用：同一份代码在需要时可以被重复使用
- 函数和对象是代码复用的两种主要形式
    - 函数：将代码命名，在代码层面建立了初步抽象
    - 对象：通过属性和方法`<a>.<b>`和`<a>.<b>()`，在函数之上再次组织进行抽象
- 模块化设计：分而治之
    - 通过函数或对象封装将程序划分为模块及模块间的表达
    - 具体包括：主程序、子程序和子程序间的关系
    - 是一中分而治之、分层抽象、体系化设计的思想

- 紧耦合：两个部分之间交流很多，无法独立存在
- 松耦合：两个部分之间交流很少，可以独立存在，由清晰独立的接口
- 在模块内部尽可能紧耦合、模块之间尽可能松耦合

- 函数递归：函数中调用函数自身的方式，类似数学归纳法
    - 链条：计算过程存在递归链条
    - 基例：存在一个人或者多个不需要再次递归的基例
    - 递归本身是一个函数，需要通过函数定义方式描述
    - 函数内部，采用分支语句对输入参数进行判断
    - 基例和链条，分别编写对应代码


```python
#n！计算
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=10
print(fact(n))

```

    3628800
    


```python
#字符串反转-递归

# s=input()
# s[::-1]

def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:])+s[0]

s = 'sdf'
rvs(s)

```




    'fds'




```python
#斐波那契数列
def f(n):
    if n ==1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)

n=10
f(n)
```




    55




```python
#汉诺塔
from time import perf_counter 
st = perf_counter()
count = 0
def hanoi(n,src,dst,mid):
#n是圆盘数，src是源柱子，dst是目标柱子，mid是中间柱子
    global count 
    if n == 1:
        print('{}:{}->{}'.format(1,src,dst))
        count +=1
    else:
        hanoi(n-1,src,mid,dst)
        print('{}:{}->{}'.format(n,src,dst))
        count+=1
        hanoi(n-1,mid,dst,src)

n = 3
hanoi(n,'a','c','b')
print(count,perf_counter()-st)


```

    1:a->c
    2:a->b
    1:c->b
    3:a->c
    1:b->a
    2:b->c
    1:a->c
    7 0.00025690000256872736
    

### 5.4 模块4：PyInstaller库的使用
- PyInstaller可以将.py源代码文件封装成为可执行文件
    - pyinstaller -h:查看帮助
    - pyinstaller --clean：清理打包过程的临时文件
    - -D,--online:默认值，生成dist文件夹
    - -F，--onefile：在dist文件夹中只生成独立打包文件
    - -i<图标文件名>指定打包程序使用的图标（icon）文件


### 5.5 科赫雪花小包裹
- 科赫曲线：一种迭代的自相似曲线


```python
#KochDrawV1
import turtle as t
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)

def main():
    t.setup(800,400)
    t.penup()
    t.goto(-300,-50)
    t.pendown()
    t.pensize(2)
    koch(600,3)
    t.hideturtle()
    t.done
main()
```


```python
#KochDrawV2
import turtle as t
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)

def main():
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    level=int(input())
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
    t.done
main()
```


### 随机密码生成
描述
补充编程模板中代码，完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬
以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密码，密码的每位是一个数字。每个密码单独一行输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

产生密码采用random.randint()函数。


```python
import random

def genpwd(length):
    return random.randint(pow(10,length-1),pow(10,length))


length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))

```

    634
    524
    926
    

### 连续质数计算
描述
补充编程模板中代码，完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。


```python
def prime(m):
    count = 1
    while(count<=5):
        isprime = 1
        for i in range(2,m):
            if m%i == 0:
                isprime = 0
        if isprime == 1:
            if count == 5:
                print(m,end='')
            else:
                print(m,end=',')
            count+=1
        m+=1

n = eval(input())
prime(int(n))
```

    13,17,19,23,29


```python
#参考代码
def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1 
    n_ += 1
```

    13,17,19,23,29


```python

```
