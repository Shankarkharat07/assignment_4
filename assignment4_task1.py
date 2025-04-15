try:
    File_1=open('sample.txt','r')
    ReadFile=File_1.read()
    print(ReadFile)
except FileNotFoundError:
    print("The file 'sample.txt' was not found")