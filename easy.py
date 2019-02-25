
# coding: utf-8

# In[ ]:


# 1. Перейти в папку

import os 
import pandas as pd
import shutil

def change_dir():

    for i in os.listdir(os.getcwd()):
        if  os.path.isdir(i) == True:
            print(i,'\n')    
    try:
        folder = input('Выберите папку из списка выше:\n\n ')

        path = os.getcwd() + '\\' + folder
        os.chdir(path)
        print('\n Успешно перешел\n \n')

    except FileNotFoundError:
        print('Такой папки не существует. Повторите ввод, используя название одной из папок из списка выше.\n \n')

def files_in_cd():
    print('Файлы текущей папки: ', os.listdir(os.getcwd()))

def del_folder():
    for i in os.listdir(os.getcwd()):
        if  os.path.isdir(i) == True:
            print(i,'\n')
                    
    try:
        folder = input('Выберите папку для удаления из списка выше:\n\n ')

        path = os.getcwd() + '\\' + folder

        shutil.rmtree(path)

        print('\n Папка успешно удалена\n \n')

    except FileNotFoundError:
         print('Такой папки не существует. Повторите ввод, используя название одной из папок из списка выше.\n \n')
    except PermissionError:
         print('Данная папка или ее содержимое не доступно для удаления, необходимо снять ограничения. \n \n')
    
def create_folder():
    folder_name = input('Введите название новой папки:')
    try:
        os.mkdir(os.path.join(os.getcwd(), folder_name))
        print('\nПапка успешно создана\n')
    except FileExistsError:        
        print('\nТакая директория уже существует\n')     