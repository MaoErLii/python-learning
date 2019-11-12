# 字典 类似于你通过联系人名字查找地址和联系人详细情况的地址薄（键(key)值(value)对）

ab = { 'Monika': 'monika@maoerli.com',
  'Aqua': 'aqua@minato.com',
  'fubiki': 'fubiki@hemi.com',
  'mea': 'mea@kagura.com'
 }

print "Monika's address is %s" %ab['Monika']
print "please tell me aqua's address %s" %ab['Aqua']

ab['guohongjian'] = 'guohongjian@debu.com'
print 'the new dic length is now', len(ab)

del ab['guohongjian']
print 'the new dic length is now %d' %len(ab)

for (name, address) in ab.items():
  print 'Contact %s at %s' %(name, address)

if 'test' in ab:
  print "test's address is %s" %ab['test']
else:
  print 'There is no test in ab'