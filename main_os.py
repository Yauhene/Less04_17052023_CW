import os

print('======== Текущая папка ======')
currDir = os.getcwd()
print(os.getcwd())

os.chdir('D:/Jack')
print('======== Новая текущая папка ======')
print(os.getcwd())

os.chdir(currDir)
print('======== Возврат назад ======')
print(os.getcwd())

print()
# os.path.basename(path) - базовое имя пути
print(os.path.basename('D:/Jack/Java II/1_Незавершенка/Знакомство с языком программирования Python/Урок 4. Функции высшего порядка, работа с файлами/Less04_17052023_CW/main.py'))
print()
# os.path.abspath(path) - возвращает нормализованный абсолютный путь.
print(os.path.abspath('main.py'))
print()

