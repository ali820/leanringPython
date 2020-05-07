### 第二周 Python基本图形绘制
#### 2.1 深入理解python语言
#### 2.2 实例2：python蟒蛇绘制
#### 2.3 模块1：turtle库的使用
#### 2.4 turtle程序语法元素分析

#### 2.1 深入理解python语言
计算机发展四个阶段：  
1946-1981：计算机系统结构时代，计算能力问题  
1981-2008：网络和视窗时代，人与计算机交互能力  
2008-2016：复杂系统时代，数据问题  
2017-    ：人工智能时代，人类的问题


不同编程语言 

|语言名称|学习内容|语言本质|解决问题|
|:---:|:---:|:---:|:---:|
|C|指针、内存、数据类型|理解计算机系统结构|性能|
|Java|对象、跨平台、运行时|理解主客体关系|跨平台|
|C++|对象、多态、继承|理解主客体关系|大规模程序|
|VB|对象、按钮、文本框|理解人机交互逻辑|桌面应用|
|Python|编辑逻辑、第三方库|理解问题、求解问题|各类问题|


深入理解python语言  
通用性：Python语言是一个通用语言，其通用性是其最大特点  
语法简介：Python语法具有强制可读性，有较少的底层语法元素，是C语言的代码量10%  
计算生态：Python具有大量的第三方库，有快速增长的第三方库，跨操作系统  

编程语言的种类
机器语言：二进制代码，与CPU型号相关  
汇编语言：二进制代码用助记符表示，与CPU型号相关  
高级语言：接近自然语言，编译器编译后运行，与CPU型号无关  
超级语言：接近自然语言，粘接已有程序，形成庞大生态，python是唯一超级语言

#### 2.2 实例2：python蟒蛇绘制
问题1：计算机绘图是什么原理？  
问题2：蟒蛇绘制应当从哪里开始？   
代码如下： 


```python
    #PythonDraw
    import turtle   #引入turtle库
    turtle.setup(650, 350, 200, 200)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    turtle.pensize(25)
    turtle.pencolor("gray")
    turtle.seth(-40)
    for i in range(4):
        turtle.circle(40, 80)
        turtle.circle(-40, 80)
    turtle.circle(40, 80/2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40 * 2/3)
    turtle.done()
```

#### 2.3 模块1：turtle库的使用
turtle库概述  
turtle绘图体系的Python实现，是python语言的标准库之一
>标准库：随解释器一起安装到操作系统的功能模块  
第三方库：需要经过安装才能使用的功能模块（库：Library、包：Package、模块：Module统称模块）  

turtle绘图窗体  
turtle种使用的单位是像素，窗体左上角是坐标原点


```python
turtle.setup(width,height,startx,starty)
#setup()设置窗体的大小及位置，4个参数后两个表示相对整个屏幕的位置
```

turtle空间坐标体系  
内部有一个绝对坐标系，中间为（0，0）点，可以从中点去往任意地方  
例如：goto


```python
import turtle
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(0,0)
```

海龟坐标：以海龟视角控制海龟的行走  

turtle的角度坐标系  
可以用`turtle.seth(angle)`来设置,例如`turtle.seth(45)`可以让海龟方向朝向45度  
也可以用`turtle.right(angle)``turtle.right(angle)`让海龟向左向右旋转  

例子：



```python
import turtle
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
ts.turtle.getscreen()
ts.getcanvas().postscript(file = 'z.eps')
```

turtle的色彩体系  
利用RGB的色彩，红绿蓝三色取0-255（或者0-1）数值来确定颜色  
可以用`turtle.colormode(mode)`改变整数（255）表示颜色或者小数（1）表示颜色  


#### 2.4 turtle语法元素分析
1. 库引用与import  
 库引用：扩充Python程序功能的一种方式
>库引用使用`import`保留字完成，采用`<a>.<b>()`的编码风格  
```        
          import<库名>    
         <库名>.<函数名>(<函数参数>)
```
>使用`form`和`import`保留字共同完成对库的引用
``` 
        form<库名>import<函数名>
        from<库名>import*
        <函数名>(<函数参数>)
```


```python
    #PythonDraw
    from turtle import*  #引入turtle库
    setup(650, 350, 200, 200)
    penup()
    fd(-250)
    pendown()
    pensize(25)
    pencolor("gray")
    seth(-40)
    for i in range(4):
        circle(40, 80)
        circle(-40, 80)
    circle(40, 80/2)
    fd(40)
    circle(16, 180)
    fd(40 * 2/3)
    done()
```

>或者为了防止名称冲突，可以使用`import `和`as`(建议)
```
    import<库名>as<库别名>
    <库别名>.<函数>(<函数参数>)
```



```python
#PythonDraw
import turtle as t   #引入turtle库
t.setup(650, 350, 200, 200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("gray")
t.seth(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80/2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2/3)
t.done()
```

2.turtle画笔控制函数  
>`turtle.penup()`或`turtle.pu()`，表示画笔抬起  
`turtle.pendown()`或`turtle.pd()`，表示画笔落下  
`turtle.pensize(width)`或`turtle.width()`，表示画笔宽度  
`turtle.pencolor(color)`，表示画笔颜色 

3.turtle运动控制函数  
>`turtle.forward(distance)`或`turtle.fd(distance)`，表示直线前行,可以是负数    
`turtle.circle(r,extent)`表示根据`r`画`excent`角度的弧形  
>>`r`默认在海龟左侧`r`处  
`extent`默认是360度整圆

4.turtle方向控制函数
>`turtle.setheading(angle)`或`turtle.seth(angle)`，表示角度改变  
>>`angle`改变的是绝对坐标度数,逆时针为正  

> `turtle.left(angle)`,`turtle.right(angle)`海龟视角左右
>>`angle`表示海龟前景视角上向左向右旋转的角度  
    




```python
for i in range(3,5):
    print(":)",i)
```

    :) 3
    :) 4
    

`range`函数产生循环技术序列
>`range(N)`产生0到N-1的整数序列  
`range(M,N)`产生M到N-1的整数序列,共N-M个数字



```python
    #PythonDraw
    import turtle as t   #引入turtle库
    t.setup(650, 350, 200, 200) #窗口大小为650*350,位置是窗口左上角距离屏幕左上角(200,200)处
    t.penup()                    #抬起画笔
    t.fd(-250)                   #向后行进250个像素,画布上没有任何痕迹
    t.pendown()                  #画笔落下
    #由原点变为左侧250
    t.pensize(25)                #设置笔的宽度为25
    t.pencolor("gray")           #颜色设置
    t.seth(-40)                  #方向设置为绝对坐标40度位置
    #准备工作完成
    for i in range(4):           
        t.circle(40, 80)
        t.circle(-40, 80)        #绘制身体部分
    t.circle(40, 80/2)              
    t.fd(40)
    t.circle(16, 180)
    t.fd(40 * 2/3)
    t.donet.done                #绘制完成不会不会自动退出,手动退出
```

#### turtle八边形绘制
‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬描述

使用turtle库，绘制一个八边形。


```python
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(100)
    t.left(45)
    t.done
```

#### turtle八角形绘制
‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬描述

使用turtle库，绘制一个八角形。


```python
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(150)
    t.left(135)
    #t.done
```
