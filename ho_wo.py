#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = input('Привет, как тебя зовут?')
print('Здравствуй,' , name)
age = int(input("Сколько тебе лет?"))
print(name,',ты такая взрослая')
school = int(input("В каком ты классе ты учишься?"))
school_5 = int(school +5)
old = int(input('В какой класс ты перейдешь через 5 лет?'))
while old != school_5:
    if old == school_5:
        print('Правильно. Будешь в', school_5)
        break
    old = int(input('А если подумать?'))
else:
    print('Верно.Ты будешь в',school_5)
check = int(input('Сколько будет 8 * 9:'))
while check != 72:
    if check == 72:
        print('Это правильный ответ')
        break
    check = int(input('А если подумать?'))
else: 
    print('Верно,72')
dog = input('У тебя есть собака?')
if dog == 'да':
    name_dog = input('Как её зовут?')
    print('Красивое имя')
else:
    print('Жаль.Животное дома это радость')
rain = input('За окном идет дождь?')
if rain == 'нет':
    print('Это хорошо!')
else:
    print('Деревню гадюкино смыло')
stroll =  input('Пойдем в лес гулять?')
if stroll == 'нет':
    print('Очень жаль.Тогда я пойду гулять с',name_dog)
    
else:
    print('Вау!Ты супер ребенок')


# In[ ]:


name = input('Привет, как тебя зовут?')
print('Здравствуй' , name)
age = int(input("Сколько тебе лет?"))
print(name ,'такая взрослая')
school = int(input("В каком ты классе?"))
check = int(input('Сколько будет 3 * 8: '))
while check != 24:
    print('Поробуй еще раз',int(input('Сколько будет 3 * 8: ')))
    break
else:
    print('Верно, 24')


# In[ ]:


x = int(input())
h = int(input())
m = int(input())
print((h*60+x)//60)
print((x+h*60+m) % 60)


# In[3]:


X = int(input())
H = int(input())
M = int(input())
c = (H*60 + M) + X
print(c//60)
print(c%60)


# In[11]:



((a and b) or ((not a) and (not b)))


# In[12]:


x = 5
y = 10
y > x * x or y >= 2 * x and x < y


# In[13]:


a = True
b = False
a and b or not a and not b


# In[2]:


school = int(input('В каком ты классе учишься?'))
school_5 = int(school +5)
old = int(input('В какой класс ты перейдешь через 5 лет?'))
while old != school_5:
    if old == school_5:
        print('Правильно. Будешь в', school_5)
        break
    old = int(input('А если подумать?'))
else:
    print('Верно.Ты будешь в',school_5)


# In[8]:


check = int(input('Сколько будет 8 * 9:'))
while check != 72:
    if check == 72:
        print('Это правильный ответ')
        break
    check = int(input('А если подумать?'))
else: 
    print('Верно,72')


# In[3]:


dog = input('У тебя есть собака?')
if dog == 'да':
    name_dog = input('Как её зовут?')
    print('Красивое имя')
else:
    print('Жаль.Животное дома это радость')
rain = input('За окном идет дождь?')
if rain == 'нет':
    print('Это хорошо!')
else:
    print('Деревню Гадюкино смыло')
stroll =  input('Пойдем в лес гулять?')
if stroll == 'нет' and dog == 'да':
    print('Очень жаль.Тогда я пойду гулять с',name_dog)
elif stroll == 'нет' and dog != 'да':
    print('Очень жаль.Придется идти одному')
else:
    print('Вау!Ты супер ребенок')


# In[6]:


a = int(input('AB'))
b = int(input('CD'))
c = b - a
AB_2 = b - c
CD_2 = a + c
OF = AB_2 + CD_2
print(OF)


# In[7]:


a = str(input())
b = str(20)
c = a + b
print(c)


# In[12]:


A = int(input())
B = int(input())
H = int(input())
if A <= H <= B :
    print('Это нормально')
elif H <= A:
    print('Недосып')
else:
    print('Пересып')


# In[ ]:




