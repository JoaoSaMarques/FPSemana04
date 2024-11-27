file = open("lorem.txt", "rt")

first_line = file.readlines()

for line in first_line:
    print(line.strip())


file.close()

#Modos de abertura
#r, w, a, t, b

file2 = open("log.txt", "wt")

for i in range(0, 10):
    txt = ("Line" + str(i))
    file2.write(txt)
    
file2.close()