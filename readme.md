Python3 练习题 100例
====================


## [题目 1](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_1.py) ##

有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

> 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。


## [题目 2](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_2.py) ##

企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

> 请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。


## [题目 3](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_3.py) ##

一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

> 在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。


## [题目 4](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_4.py) ##

输入某年某月某日，判断这一天是这一年的第几天？

> 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天。


## [题目 5](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_5.py) ##

输入三个整数x,y,z，请把这三个数由小到大输出。

> 我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。


## [题目 6](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_6.py) ##

斐波那契数列。

> 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。


## [题目 7](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_7.py) ##

将一个列表的数据复制到另一个列表中。

> 使用列表[:]。


## [题目 8](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_8.py) ##

输出 9*9 乘法口诀表。

> 分行与列考虑，共9行9列，i控制行，j控制列。


## [题目 9](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_9.py) ##

模拟Linux用户登录。

> 验证账号和密码，若失败则延迟三秒输出错误信息。


## [题目 10](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_00/sub_10.py) ##

格式化输出当前时间。

> 使用 time 模块，格式为 yyyy-mm-dd HH:mm:ss。


## [题目 11](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_11.py) ##

古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

> 兔子的规律为数列1,1,2,3,5,8,13,21....


## [题目 12](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_12.py) ##

判断101-200之间有多少个素数，并输出所有素数。

> 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 


## [题目 13](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_13.py) ##

打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

> 利用for循环控制100-999个数，每个数分解出个位，十位，百位。


## [题目 14](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_14.py) ##

将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

> 对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
> (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
> (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
> (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。


## [题目 15](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_15.py) ##

利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

> 程序分析：(a>b)?a:b这是条件运算符的基本例子。


## [题目 16](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_16.py) ##

输出指定格式的日期。

> 使用 datetime 模块。


## [题目 17](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_17.py) ##

输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

> 利用while语句,条件为输入的字符不为'\n'。


## [题目 18](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_18.py) ##

求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

> 关键是计算出每一项的值。


## [题目 19](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_19.py) ##

一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

> 请参照程序Python 练习实例14。


## [题目 20](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_10/sub_20.py) ##

一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

> 利用循环计算每一次小球落地的高度。


## [题目 21](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_21.py) ##

猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

> 采取逆向思维的方法，从后往前推断。


## [题目 22](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_22.py) ##

两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。 

> 先进行排列组合，再挑选符合要求的组合。


## [题目 23](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_23.py) ##

利用循环打印菱形

> 先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。


## [题目 24](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_24.py) ##

有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

> 请抓住分子与分母的变化规律。 


## [题目 25](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_25.py) ##

求1+2!+3!+...+20!的和。

> 此程序只是把累加变成了累乘。 


## [题目 26](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_26.py) ##

利用递归方法求5!。

> 递归公式：fn=fn_1*4!
 
 
## [题目 27](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_27.py) ##

利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

> 递归实际上是一种函数堆栈。


## [题目 28](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_28.py) ##

有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

> 利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。


## [题目 29](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_29.py) ##

给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

> 学会分解出每一位数。


## [题目 30](https://github.com/HongShen-Z/PythonExercise/blob/patch-1/case_20/sub_30.py) ##

一个5位数，判断它是不是回文数。

> 回文数，个位与万位相同，十位与千位相同。
