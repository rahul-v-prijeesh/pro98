file1=input("enter !stfiles name: ")
file2=input("enter 2ndfiles name: ")

def swapfiledata(file1,file2): 
    with open(file1,'r') as a1:
        data_a=a1.read()
    with open(file2,'r') as b1:
        data_b=b1.read()

    with open(file1,'w') as a1:
        a1.write(data_b)
    with open(file2,'w') as b1:
        b1.write(data_a)

   
swapfiledata(file1,file2)   