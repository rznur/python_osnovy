# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.



# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <directory name> - создание директории")
    print("ping - тестовый ключ")
    print("dublicate <file name> - копировать файл") 
    print("remove <file name> - удалить файл")
    print("cd <full_path or relative_path> - поменять текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not arg_2nd:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), arg_2nd)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(arg_2nd))
    except FileExistsError:
        print('директория {} уже существует'.format(arg_2nd))


def ping():
    print("pong")
    
def cp(): #copy file
    #print('Файлы текущей папки: ', os.listdir(os.getcwd()))
    
    #shutil.copy(arg_2nd,'copy_'+arg_2nd)
    if not arg_2nd:
        print("Необходимо указать имя файла вторым параметром")
        return    
    shutil.copy(arg_2nd,'copy_'+arg_2nd)
def rm():# remove file
    if not arg_2nd:
        print("Необходимо указать имя файла вторым параметром")
        return    
    if arg_2nd:
        print("Вы хотите удалить файл: {} ? Для выбора введите: да или нет ?".format(arg_2nd))
        user_answer = input()
        if user_answer == 'да':
            try:
                os.remove(arg_2nd)
            except OSError as e:  ## if failed, report it back to the user ##
                print ("Error: %s - %s." % (e.filename, e.strerror))
        else:
            return
    # CAN'T MAKE IT CHANGE DIRECTORY - when working from shell
def cd():#change current dir
    ##if not arg_2nd:
     #   print("Необходимо указать путь директории, в которую Вы хотите перейти, вторым параметром")
     #   return     
        
    try:
        path = input('path here:')
        os.chdir(path)
        print('\n Успешно перешел\n \n')
            
    except FileNotFoundError:
        print('Такой папки не существует. Повторите ввод.\n \n')
         
def ls(): #list full path for current directory      
    print('Путь текущей директории:\n', os.getcwd())  
        
do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "dublicate": cp,
    "remove": rm,
    'cd': cd,
     'ls':ls
}

try:
    arg_2nd = sys.argv[2]
except IndexError:
    arg_2nd = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")