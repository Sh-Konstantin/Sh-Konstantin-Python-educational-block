"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet



LST_PING = ['ping', 'yndex.ru', 'youtube.com']
MY_PING = subprocess.Popen(LST_PING,stdout=subprocess.PIPE)
print (MY_PING.stdout)
for line in MY_PING.stdout:
    result = chardet.detect(line)
    print (result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
