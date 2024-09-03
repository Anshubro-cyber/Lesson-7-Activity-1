lst = ['Apple','Guava','Mango','Banana','Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Update List:", lst)

lst.remove('Guava')
print("Update List:", lst)

lst.sort()
print("Sorted List:", lst)

lst.reverse()
print("Reversed List:", lst)
print("Multiplication on List :", lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Update List :", lst)