s=['2 A','1 B','4 C','1 A']

s.sort(key=lambda x:(x.split()[1:],x[0]))
print(s)