file_name = open('reversed.txt','rb')

file_read=file_name.read()
a=file_read[::-1]

f=open('rev.txt','w+b')
f.write(a)
f.close()
print(open('rev.txt','r').read()[::-1])
