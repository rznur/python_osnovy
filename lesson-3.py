
# coding: utf-8

# # LESSON 3 EASY

# In[1]:


# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    return round(number,ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# In[2]:



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6: return ('Wrong ticket number')
    else:
        if int(str(ticket_number)[0]) +int(str(ticket_number)[1]) == int(str(ticket_number)[4]) +int(str(ticket_number)[5]): return True 
        else:
            return False



print(lucky_ticket(426741))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


# # LESSON 3 NORMAL
# 

# In[3]:


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    ryad=[1]
    a=1
    b=1

    
    for i in range(m):
        ryad.append(b)
        a,b = b,a+b
    return ryad[n:m]
    
    

fibonacci(5,10)


# In[4]:


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sorted_list=[]
    while len(origin_list):
        for item in origin_list:
            if item == min(origin_list):
                sorted_list.append(item)
                origin_list.remove(item)
    
    return sorted_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# In[5]:


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(some_function,some_object): #not working with strings!
        
    new_object = [item for item in some_object if some_function(item)]
    filtered=new_object
    return filtered

my_filter(lambda x: x%2, [1,23,45,6,7,8])


# In[6]:


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math
# A1
x1=1
y1=3
#A2
x2=4
y2=7
#A3
x3=2
y3=8
#A4
x4=-1
y4=4

A1A2=math.sqrt((x2-x1)**2+(y2-y1)**2)
A2A3=math.sqrt((x3-x2)**2+(y3-y2)**2)
A3A4=math.sqrt((x4-x3)**2+(y4-y3)**2)
A4A1=math.sqrt((x1-x4)**2+(y1-y4)**2)
if A1A2 == A3A4 and A2A3 == A4A1:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки НЕ являются вершинами параллелограмма')


# In[8]:


#вариант для ввода с клавы

# A1
x1=int(input('x1 = '))
y1=int(input('y1 = '))
#A2
x2=int(input('x2 = '))
y2=int(input('y2 = '))
#A3
x3=int(input('x3 = '))
y3=int(input('y3 = '))
#A4
x4=int(input('x4 = '))
y4=int(input('y4 = '))

A1A2=math.sqrt((x2-x1)**2+(y2-y1)**2)
A2A3=math.sqrt((x3-x2)**2+(y3-y2)**2)
A3A4=math.sqrt((x4-x3)**2+(y4-y3)**2)
A4A1=math.sqrt((x1-x4)**2+(y1-y4)**2)
if A1A2 == A3A4 and A2A3 == A4A1:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки НЕ являются вершинами параллелограмма')


# # LESSON 3 HARD

# ## #1

# In[10]:


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# reshala svoim sposobom, vyshlo gromozdko, ne ponravilos, nije pokrasivee reshenie iz google,razobrala ot i do, perepisala koe-chto
import re

def NOD(m,n):
    while m != 0 and n != 0:
        if m > n:
            m = m % n
        else:
            n = n % m
    return m + n

def NOK(m, n):
#Наименьшее общее кратное (НОК) двух целых чисел m и n есть наименьшее натуральное число, которое делится на m и n без остатка.
#Зная наибольший общий делитель (НОД) двух целых чисел m и n, их наименьшее общее кратное можно вычислить по такой формуле:
#НОК = m * n / НОД (m, n)
    return m * n / NOD(m, n)

def diff(lst):
#getting difference between list elements
    difference = lst[0]
    for x in range(len(lst)):
        if x:
            difference = difference - lst[x]
    return difference

def get_fract(value, NOK):
    if value > NOK:
        whole = value // NOK
        new_val = value % NOK
        if new_val !=0:
            result = '{0:.0f} {1:.0f}/{2:.0f}'.format(whole, new_val, NOK)
        else:
            result=whole
    else:
        result = '{0:.0f}/{1:.0f}'.format(value, NOK)
    return result
       
      
expres = input("Введите выражение в формате, как в примере: 5/6 + 4/7 ")
# получаем все дроби из строки
fractions = re.findall(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', expres)
# получаем список содержащий оператор
signs = re.split(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', expres)

numerators = []
denumerators = []
i = 0
for frac in fractions:
    temp = frac.split('/')
    numerators.append(int(temp[0]))
    if len(temp) > 1:
        denumerators.append(int(temp[1]))
    else:
        denumerators.append(1)


for s in signs:
    # определяем оператор действия с дробями
    if s:
        sign = s.strip()
        break
        
get_NOK = NOK(denumerators[0], denumerators[1])

for n in numerators:
    # вычисляем новые числители по найденному НОК
    numerators[i] = n * get_NOK / denumerators[i]
    i += 1

print('Результат вычисления ' + expres + ':')
if sign == '+':
    print(get_fract(sum(numerators), get_NOK))
    
elif sign == '-':
    print(get_fract(diff(numerators), get_NOK))
else:
    print('Действие не определено, программа выполняет только сложение и вычитание')


# ## #2

# In[11]:


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import pandas as pd
import numpy as np

workers = pd.read_excel('workers.xlsx')
hours_of = pd.read_excel('hours_of.xlsx')

workers['за1час'] = round(workers['Зарплата']/workers['Норма_часов'])

df =  pd.merge(workers,hours_of, how='inner',left_on='Фамилия', right_on='Фамилия')
# df=pd.merge(energy,gdp,how='inner',left_on='Country', right_on='Country')
df.drop(['Имя_y'], axis = 1, inplace = True)

overtime = (-df.loc[:,'Норма_часов'] + df.loc[:,'Отработано часов'])*df.loc[:,'за1час']*2  + df.loc[:,'за1час']*df.loc[:,'Норма_часов']
df['Финал.оклад'] = np.where(df.loc[:,'Отработано часов'] <= df.loc[:,'Норма_часов'], df.loc[:,'за1час']*df.loc[:,'Отработано часов'] , overtime)

df


# ## #3

# In[12]:



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


import pandas as pd
import numpy as np

df = pd.read_csv('fruits.txt', encoding = 'utf8', names = ['Фрукты'])
df['first_letter'] = df['Фрукты'].astype(str).str[0]
gp = df.groupby('first_letter')

gp.apply(lambda x: x.to_csv('Фрукты' + str(x.name) + '.txt'))

