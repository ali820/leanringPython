## Week8 程序设计方法
### 8.1 实例13：体育竞技分析
### 8.2 python程序设计思维
### 8.3 python第三方库安装
### 8.4 模块7：os库的使用
### 8.5 实例14：第三方库自动安装脚本


### 8.1 实例13：体育竞技分析
- 问题分析：毫厘是多少？如何科学分析体育竞技比赛
- 输入：球员水平
- 输出：可预测比赛成绩
- 计算思维：抽象+自动化
    - 模拟：抽象比赛过程+自动化执行N场比赛
    - N越大，比赛结果分析越科学
- 规则：
    - 双人击球：A&B，回合制，5局3胜
    - 开始时一方先发球，直至判分，接下来胜者发球
    - 球员只能在发球局得分，15分胜一局
- 自顶向下（设计）：
    - 将一个总问题表达为若干小问题的组成形式
    - 使用同样的方法进一步分解小问题
    - 直至，小问题可以用计算机简单明了解决
- 自底向上（执行）：
    - 分单元测试，逐步组装
    - 按照自顶向下的相反路径操作
    - 直至系统各部分组装的思路都经过测试和验证

- 程序总体框及步骤：
    - 步骤1：打印程序的介绍性信息式
    - 步骤2：获得程序运行参数：proA，proB，n
    - 步骤3：利用球员A和B的能力值，模拟n局比赛
    - 步骤4：输出球员A和B获胜的场次及概率
- 四个函数完成四个步骤


```python
#Sport
from random import random

#主函数
def main():
    printIntro()
    probA,probB,n=getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)

#打印介绍信息
def printIntro():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0到1之间的小数表示）')

#获取输入
def getInputs():
    a = eval(input('请输入选手A的能力值（0-1）：'))
    b = eval(input('请输入选手B的能力值（0-1）：'))
    n = eval(input('请输入比赛的场次：'))
    return a,b,n

#模拟n场比赛
def simNGames(n,probA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

#模拟一场比赛
def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = 'A'
    while not gameOver(scoreA,scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if serving == 'B':
                if random() < probB:
                    scoreB += 1
                else:
                    serving = 'A'
    return scoreA,scoreB

#判断比赛是否结束
def gameOver(a,b):
    return a == 15 or b == 15

            
#表示模拟结果
def printSummary(winsA,winsB):
    n = winsA + winsB
    print('竞技分析开始，共进行{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(winsA,winsA/n))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(winsB,winsB/n))

main()
```

    这个程序模拟两个选手A和B的某种竞技比赛
    程序运行需要A和B的能力值（以0到1之间的小数表示）
    竞技分析开始，共进行10000场比赛
    选手A获胜10000场比赛，占比100.0%
    选手B获胜0场比赛，占比0.0%
    

### 8.2 python程序设计思维
- 三大思维：
    - 逻辑思维：推理和演绎，数学为代表
    - 实证思维：实验和验证，物理为代表
    - 计算思维：设计和构造，计算机为代表
- 计算思维：抽象和自动化
    - 抽象问题的计算过程，利用计算机自动化求解
- 例子：
- 计数求和，1-100的和：
    - 逻辑思维：求和公式
    - 计算思维：代码直接累加求和
- 圆周率：
    - 逻辑思维：求公式，画多边形逼近
    - 计算思维：蒙特卡洛方法
- 天气预报：
    - 实证思维：从历史数据推理未来
    - 计算思维：建立模型训练预报
- 量化分析：
    - 实证+逻辑：自己猜
    - 计算思维：使用机器学习来自动购买
- 计算思维:关注过程，关注设计和构造，而非因果
- 编程是将计算思维变成现实的手段
- 计算生态：竞争发展、相互依存、迅速更迭
- python的生态
    - 大量第三方库：野蛮生长和自然选择
    - 库之间的相互依存普遍
- 从应用需求到软件产品
    1. 产品定义：对应用需求充分理解和明确定义
    2. 系统架构：以系统方式思考产品技术的实现
    3. 设计与实现：结合架构完成关键设计及系统实现
    4. 用户体验：从用户角度思考应用的效果

### 8.3 python第三方库安装
- 三种方法安装第三方库
    1. 使用pip命令
    2. 集成安装方法
    3. 文件安装方法
- 使用python自带的pip工具安装
    - `pip install <第三方库>`：安装第三方库
    - `pip install -U<第三方库>`：更新第三方库
    - `pip unstall <第三方库>`:卸载指定第三方库
    - `pip downlooad<第三方库>`:下载不安装第三方库
    - `pip show<第三方库>`：列出指定第三方库的详细信息
    - `pip search<关键字>`：根据关键字在名称和介绍中搜索第三方库
    - `pip list`:列出已经安装好的库
- 集成安装：anaconda，下载一个第三方库就有了800多个包
- 文件安装:编译安装，可以使用网站进行安装

### 8.4 模块7：os库的使用
- os库提供了通用的、基本的操作系统交互功能
- 常用路径操作、进程管理、环境参数等几类
    - 路径操作：os.path子库，处理文件路径及信息
    - 进程管理：启动系统中其他程序
    - 环境参数：获得系统中软件信息等环境参数
- os库的路径操作
    - `os.path.abspath(path)`：返回path在当前系统中的绝对路径
    - `os.path.normpath(path)`:归一化path的表示形式，统一用\\分隔路径
    - `os.path.relpath(path)`：返回当前程序与文件之间的相对路径（relative path）
    - `os.path.dirname(path)`:返回path中目录名称
    - `os.path.basename`:返回path中最后文件名称
    - `os.path.join(path,*paths)`：组合path与paths，返回一个路径字符串
    - `os.path.exists(path)`：判断path对应文件路径或者目录是否存在，返回True或False
    - `os.path.isfile(path)`：判断path对应文件是否为已存在文件，返回True或者False
    - `os.path.isdir(path)`：判断path所对应是否为已存在的目录，返回True或者False
    - `os.path.getatime(path)`:返回path对应文件或目录的上一次访问时间
    - `os.path.getmtime(path)`:返回path对应文件目录最近一次修改时间
    - `os.path.getctime(path)`:返回path对应文件或目录的创建时间
    - `os.path.size(file)`：判断path所存在文件大小
- 进程管理：使用python调用其他程序
    - `os.system(程序路径)`
- 换境参数：获取或改变系统环境信息
    - `os.chdir(path)`:修改当前程序的操作路径
    - `os.getcwd()`:获得当前路径
    - `os.getloginin()`:获得当前登录用户名
    - `os.cpu_count()`获得当前cpu数量
    - `os.urandom(n)`:获得n个字节长度的随机字符串，通常用于加解密运算


```python
import os
print(os.getcwd())
print(os.getlogin())
print(os.cpu_count())
print(os.urandom(4))
```

    f:\Users\Administrator\Documents\笔记\记录笔记\北理python\jupyter note\基础
    Administrator
    12
    b'V\x81\x9dq'
    

### 8.5 实例14：第三方库自动安装脚本
- 需求：自动安装批量第三方库
    - 自动用pip安装


```python
#BatchInstall
import os
libs={"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system('pip install'+lib)
    print('successful')
except:
    print('failed somehow')
```

    successful
    

### 英文字符的鲁棒输入
描述  
获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。


```python
#英文字符的鲁棒输入
s=input()
for i in s:
    if i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        print(i,end='')
```

    abce


```python
#参考答案
alpha = []
for i in range(26):
    alpha.append(chr(ord('a') + i))
    alpha.append(chr(ord('A') + i))
s = input()
for c in s:
    if c in alpha:
        print(c, end="")
```

### 数字的鲁棒输入

描述  
获得用户输入的一个数字，可能是浮点数或复数，如果是整数仅接收十进制形式，且只能是数字。对输入数字进行平方运算，输出结果。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

要求：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

（1）无论用户输入何种内容，程序无错误；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

（2）如果输入有误，请输出"输入有误"。



```python
#数字的鲁棒输入
s = input()
try:
    if complex(s)==complex(eval(s)):
        print(pow(eval(s),2))
except:
    print('输入有误')
```

    输入有误
    


```python

```
