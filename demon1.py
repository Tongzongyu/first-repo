import random
#print('duima')
a=123
the_name="name"
s1=12
s2=input("请输入：")
s3=float(s2)
s4=random.randint(1,100)
s5=random.uniform(1,100)
a1=[1,2,3]
b={2,5,8}
c=(1,3,8)
d={'n':1,'b':2}
print(a1)
print(f"变量\t值\n为：{s1}")
s6=s4*s3
print("changing key: %d" % s6)
s7=s3%2
s8=s7==0
if s3 <=20:
    print("o数")
elif s3<=40 :
    print("i数")
else:
    print("z数")

'''注释
while s3>10:
    s3/=2
    print(s3)
    if s3>50:
        break
'''
'''
s9="ABCDEF"
for i in s9:
    print(i)
'''
s9="ABCDEF"
s10=s9[:4]
print(s10)
s9=s9.replace("CDE","PIG")
print(s9)
arr=s9.split("B")
print(arr)
arr2="-".join(arr)
print(arr2)
