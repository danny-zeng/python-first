#函数学习

#函数是一个公共代码块的集合，主要功能是增强代码复用

#yeild的使用,yeild 相当于return
#...yeild 与return de 区别
#...return:返回值，返回完代表程序执行结束
#...yeild:返回值，程序执行不会结束，sososo,类似一个值生成器
def foo(param):
    if param==1:
        print('this is medo')
        re=yield 1
        print(re)
g=foo(1)

#定义函数
def sum_this(a,b):
    return a+b

def jian_this(a,b):
    return a-b
f=sum_this(1,2)

# 定义一个函数嵌套函数
def deal_whith(a=0,b=0):  #a=0当参数不传时默认参数值为0
    if a>1:
        return sum_this(a,b)
    return jian_this(a,b)

j=deal_whith(1)

#嵌套函数定义
def for_un():
    print('this is first')
    def do():
        print('this is second')
    do()
for_un()

#局部变量只能局部访问，局部可以访问全局变量，函数内不能随意更改全局变量，内部函数也不能更改外部函数的变量
#主要原因是当更改时会默认为局部变量，局部变量不能不初始化。所以更改时需要定义为global
#MAX_VALUE=1
#def test():
#global  MAX_VALUE+=1
#test()

#内部函数可以访问外部函数定义的变量，但是无法修改，若要修改，必须加上nonlocal这个关键字：
#如果不加上nonlocal这个关键字，而内部函数的变量又和外部函数变量同名，那么同样的，内部函数变量会覆盖外部函数的变量。


#闭包
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是exponent_of函数
square = nth_power(2) # 计算⼀个数的平⽅
cube = nth_power(3) # 计算⼀个数的⽴⽅
print(square)
print(square(2))