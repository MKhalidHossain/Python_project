s1 = 'I love python'
s2 = 'I love Java'

list1 = s1.split()
list2 = s2.split()

common = set(list1).intersection( set(list2) )

print("The common word of those two string are ", common)
