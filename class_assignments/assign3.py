l = str(input("Enter the elements in list...\n"))
l = l.split()
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
