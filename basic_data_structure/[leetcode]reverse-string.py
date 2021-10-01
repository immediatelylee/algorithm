# s = list("hello")
s = ["H","a","n","n","a","h"]

#1  two pointer
left,right =0,len(s)-1
while left < right:
    s[left],s[right] =s[right],s[left]
    left += 1
    right -= 1

#2 reverse()

s = ["H","a","n","n","a","h"]

s.reverse()

#3 slice list

s[:] = s[::-1]