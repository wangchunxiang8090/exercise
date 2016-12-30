import time
import os
date = time.strftime('%Y-%m-%d')
month = time.strftime('%m')
path = 'C:\Users\djn1\Desktop'
directory = os.path.join(path,month,date)
if not os.path.exists(directory):
    os.makedirs(directory)