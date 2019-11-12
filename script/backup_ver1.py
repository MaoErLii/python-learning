## backup
import os
import time

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