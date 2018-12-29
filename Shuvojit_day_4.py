
'''
#question no 7

x=input("enter the number")
sum=0
for i in range(len(x)):
    sum+=int(x[i])
print(sum)


#question no 23

string=input("enter the string")
count=0
for i in string:
    count=count+1
print("length of string is ", count)
list=string.split(" ")
list.reverse()
print(string[::-1])
string1=input("enter the string")
s3=string+string1
print(s3)
if(string=string1)
    print("they are equal")
else:
    print("they are not equal")
if(string1=string):
    exit()
else:
    print(string1)


#question no 15

x=int(input("1st number"))
y=int(input("2nd number"))
z=int(input("3rd number"))
p=1
for i in range(y+z):
    p*=x
print(p)



#question number 18

x=int(input("first number"))
y=int(input("enter the power"))
p=1
for i in range(y):
    p*=x
print(p)


#question number 12

str35="he is a good boy"
list35=str35.split(" ")
list35.reverse()
print(' '.join(list35))



#question no 24

num = 10

# To take input from the user
# num = int(input("Display multiplication table of? "))

# use for loop to iterate 10 times
for i in range(1, 11):
   print(num,'x',i,'=',num*i)



#question number 26

salary=int(input("enter your salary"))
if salary>=5000:
    hra=salary*0.15
    da=salary*1.5
    gross_salary=hra+da+salary
    print("gross salary",gross_salary)

else:
    hra=salary*0.10
    da=salary*1.1
    gross_salary=hra+da+salary
    print("gross salary",gross_salary)


#question number 20

wow= lambda s:s.replace("a","#").upper()
print(wow("He is a good boy"))


#question number 2

list=[55,44,22,10,6,100,600,7]
print(max(list))
print(min(list))
'''

