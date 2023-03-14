
from os.path import getctime
import datetime

print("""\n            Приветствую мой друг -    
            это твоя маленькая записная кинжка, 
            мы можем написать заметку, а затем ее прочитать,
            или если она тебе не понравится удалить\n          """)

print(datetime.datetime.fromtimestamp(getctime('intermediate_certification/123.csv')).strftime('%H:%M:%S'))