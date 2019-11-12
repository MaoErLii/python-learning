## 字符串方法
name = 'Aqua'

if name.startswith('Aq'):
  print 'Yes, the string starts with "Aq"'

if 'a' in name:
  print 'Yes, it contains the string "a"'

if name.find('war') != -1:
  print 'Yes, it contains the string "ua"'

delimiter = '_*_'
mylist = ['Aqua', 'Mea', 'Fubiki', 'Monika']
print delimiter.join(mylist)