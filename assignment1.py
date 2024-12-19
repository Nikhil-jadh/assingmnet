#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple'''
string="String"
lis=[1,2,5,'Nikhil']
Float=29.40
Tuple=(1,2,5,4,6)


# In[5]:


'''Q2. Given are some following variables containing data:
(i) var1 = ‘ ‘
(ii) var2 = ‘[ DS , ML , Python]’
(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
(iv) var4 = 1.
What will be the data type of the above given variable.'''
var1=''
var2='[ds,ml,python]'
var3=['ds','ml','python']
var4=1
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


# In[9]:


'''Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **'''
# "/"is use to division of two oprand
a=10
b=20
print("Division",a/b)
# "%" it is modules oprator use to find mode of oprand
print("modules",a%b)
# "//" is use to floor division
print("floor division",a//b)
# "**" is a Exponentiation oprator use to find the exponentiation
print("Exponentiation",a**b)


# In[10]:


'''Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.'''
l=[1,2,'john','ram',30.50,(1,2,4)]
for i in l:
    print(i)


# In[12]:


'''Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.'''
a=int(input("Enter a number"))
b=int(input("Enter b number"))
count=0;
while(a%b==0):
    a//=b
    count+=1
if(count>0):
    print("The number is divisible times:",count)
else:
    print("number is not divisible")


# In[33]:


'''Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.'''
numbers=list(range(0,26))
for num in numbers:
    if(num%3==0):
        print("Numbers divisible by 3:",num)
    else:
        print("Number no divisible by 3:",num)


# In[ ]:


'''Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.'''
'''mutable=its provide a flexibility.you can perform many opration on it.example list dictonary,sttring'''
'''inmutable=it does not provide flexibility.only some opration perform on it.example set,tuple'''


# In[ ]:




