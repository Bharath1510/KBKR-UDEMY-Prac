def read_file(file_name):
    file = open(file_name,'r')
    print("contents:\n" + file.read())
    file.close()

#write
file = open("newfile.txt","w")
file.write('this is a new file')
file.close()
#read
file = open('newfile.txt','r')
print("contents:\n" + file.read())
file.close()
#append
file = open('newfile.txt','a')
file.write('\n but not now')
file.close()
read_file('newfile.txt')
