## backup
import os
import platform
import time
import re

osPlatform = re.findall('Windows', platform.platform())[0]

print 'os is %s' %osPlatform

source = [r'E:/my_github/test']

target_dir = "E:/backup/"

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

command = 'rar a %s %s' %(target, ' '.join(source))

print command

zip_command = command

if os.system(zip_command) == 0:
  print 'Successful backup to', target
else:
  print 'Backup Failed'