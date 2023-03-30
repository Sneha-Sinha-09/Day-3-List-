#LIST-->Ordered--default index

list1=[]
print(list1,type(list1))
list2=[10,20,30,40,50]
print(list2,type(list2))
list3=[10,20.10,30+3j,True,"Python"]
print(list3,type(list3))
list4=(list[100,200,300])
print(list4)
list5=[101,102,103,104]
print(list5)
list5.append(106)
print(list5)
list5.insert(0,51) #index,value
print(list5)
list5.insert(4,350) #index,value
print(list5)
list5.remove(101)
print(list5)
list5.pop() #pops the last value as default
print(list5)
list5.pop(3) #pops the content of given index value
print(list5)
del list5[1] #deletes the content of the given index value
print(list5)


#Q1 Calculate total numbers of characters and digits in a given string e
def count(string):
    char_count=0
    num_count=0
    for i in string:
        if i.isalpha():
            char_count+=1
        elif i.isdigit():
            num_count+=1
        else:
            continue
    return [char_count,num_count]

string=input("Enter a string: ")
print(count(string))


#Q2 Calculating the total number of pairs of numbers from a list to give a particular sum
def number_of_pairs(list,sum):
    num=0
    for i in list:
        index=list.index(i)+1
        for j in range(index,len(list)):
            if(i+list[j]==sum):
                num=num+1
    return num
list=[1,2,7,4,5,6,0,3]
print(number_of_pairs(list,6))


#Q3 Concatinating the first and last 2 characters of a string to form a new string
def func(str):
    a=""
    if(len(str)<2):
        a= "-1"
    elif(len(str)==2):
        a=str+str
    else:
        a=str[0:2:]+str[-2:]
    return a

str=input("Enter a string: ")
print(func(str))


#Q4 Add ly to a string of it ends with ing otherwise add ing
def ing(str):
    new=""
    if (len(str)<3):
        new=str
    elif (str[-3:]=="ing"): 
        new=str+"ly"
        
    else:
       new=str+"ing"
    return new
str=input("Enter a string: ")
print(ing(str))


#Q5 Checking if a nymbers and it's double contains the same digits or not
def check_double(number):
    double=2*number
    count=0
    for i in number:
        if i in double:
            count+=1
        else:
            return False
            break
    if count==len(number):
         return True

number=input()
print(check_double(number))



#Q6 Calculate the % of students having more than average marks, sorting the marks and generaing frequency
#sorted will always return a list
def more_than_average(marks):
    sum=0
    count=0
    for i in marks:
        sum+=i
        avg=sum/10
    for j in marks:
        if j>avg:
            count=count+1
            percent=(count/10)*100
    return percent

def sort(marks):
    marks=sorted(marks)
    return marks

def generate_frequency(marks):
    freq=[]
    for x in range(26):
        count=0
        for y in marks:
            if x==y:
                count+=1
        freq.append(count)
    return freq

marks=[12,18,25,24,2,5,18,20,20,21]
print(more_than_average(marks))
print(sort(marks))
print(generate_frequency(marks))


#Q7 Translating a sentence to some other language as per the provided dictionary
def translate(str1):
    dict1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
    list1=[]
    for i in str1:
        list1.append(dict1[i])
    return list1
str1=["merry","christmas"]
print(translate(str1))


#Q8 for loop version
def subarray(n1,n2):
    arr=[]
    for i in range(n1,n2+1):
        arr.append(i)
        print(arr)
        result=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            result.append(arr[i:j+1])
    return result
        
n1=int(input("Enter the starting num:"))
n2=int(input("Enter the ending num:"))
print(subarray(n1,n2))
       

       
#Q Printing odd numbers and square of even numbers within a particular range
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
#list comprehension version
print([i if i%2!=0 else i**2 for i in range(11)])


#Q9 for loop version
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop -- odd -->square it
#even -->cube it
arr1=[]
for i in mat:
    arr2=[]
    for j in i:
         if j%2!=0:
            arr2.append(j**2)
         else:
            arr2.append(j**3)
    arr1.append(arr2)
print(arr1)

#list comprehension version
print([j**2 if j%2!=0 else j**3
       for i in mat for j in i])

#for dynamic list
print([[j**2 if j%2!=0 else j**3 for j in i]
      for i in mat])


#Q10 for loop version
my_list=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
arr=[]
for i in list_b:
    for j in my_list:
        if i==j:
            b=(i,my_list.index(i))
            arr.append(b)
print(arr)

#alternate
result=[]
for i in list_b:
    result.append((i,my_list.index(i)))
print(arr)

res={}
for i in list_b:
    res[i]=my_list.index(i)
print(res)
    
#list comprehension
print([(i,my_list.index(i)) for i in list_b])
print({i:my_list.index(i) for i in list_b})


#Q11
sentences=["a new world record was set","in the holy city of ayodhya",
           "on the eve of diwali on tuesday","with over three lakh diya or earthen lamps",
           "it's up simultaneously on the banks of the sarayu river"]
stop_words=["for","a","of","the","and","to","in","on","with"]
sen=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stop_words:
            row_data.append(word)
    sen.append(row_data)
print(sen)

#using list comprehension
print([[word for word in sentence.split()
        if word not in stop_words]for sentence in sentences])


#Q12
array=list(map(int,input().split(",")))
num1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
num2=""
for i in l:
    num2+=str(i)
print(int(num2)+num1)


#Q13
s=input().split(",")
str1=[]
num=[]
for i in s:
    s1,n=i.split(":")
    str1.append(s1)
    num.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(str1[i],num[i]))


#Q14 Calculating nearest palindrome of a number
import sys
def nearest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(nearest_palindrome(99))
print(nearest_palindrome(1221))
    

    

        
        
        
        


    



























        
        
    
        


