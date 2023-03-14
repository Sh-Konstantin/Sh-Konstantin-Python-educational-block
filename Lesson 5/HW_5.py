# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

Text_Convert_Beefore= "АБВ какой то текст котороый надо конвертировать обработать в данном случаи убрать АБВ и получить текст без АБВ "
print (f'\n текст до \n {Text_Convert_Beefore}\n')
def delete (Text_Cnvert):
    Text_Convert_After = list(filter(lambda x: 'АБВ' not in x, Text_Convert_Beefore.split()))
    return " ".join(Text_Convert_After)

Text_Convert = delete(Text_Convert_Beefore)
print (f'\n текст после \n {Text_Convert} \n ')