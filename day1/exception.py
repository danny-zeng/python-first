list=[1,2,3,4,5,5,6,7]
#for 循环与while 循环某些时候是可以相互转换的， for循环的相率月胜一筹
#遍历list
for i in list:
    print(i)

#与索引有关的遍历list之range()
for index in range(0,len(list)):
    if  index < 6:
        print(list[index])
#与索引有关的遍历list之enumerate()
for index ,item in enumerate(list):
    if index<6:
        print(item)

#异常
try:
    i=8/0
except(ZeroDivisionError,NameError) as error:
    print(error)
finally:
    print('永远执行')
