﻿# Режим a

colors = ['red', 'green', 'blue']
data = open('file_1.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

# ● data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление
# в существующий файл, а не перезапись файлов.
# Ещё один способ записи данных в файл:

with open('file_2.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

# Режим r
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

# 3. Режим w
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()