## 序列 列表，元组和字符串都是序列
## 序列最主要的特点是 索引操作符 和 切片操作符

shoplist = ['apple', 'mango', 'carrot', 'banana']

## indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

## slicing on a list
print 'Item 1 to 4 is', shoplist[1:4]
print 'Item 3 to end is', shoplist[3:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]