 def countWordsFromFile():
    fileName = input("Enter the file name:- ")
    fileName2 = input("Enter file name")
    with open(fileName, 'r') as a:
    data_a = a.read()
    with open(fileName2, 'r') as a:
    data_b = b.read()
    with open(fileName, 'w') as a:
    a.write(data_b)
    with open(fileName2, 'w') as a:
    b.write(data_a)
countWordsFromFile()