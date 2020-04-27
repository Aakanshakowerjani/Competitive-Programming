n = int(input())
s = input()
x = int(input())
s1 = ''
x=x%26
for i in s:
    if i.isupper():
        i=i.lower()
        if ord(i) > 122 - x and ord(i) < 123:
            s1 += chr(96 + (ord(i) - (122 - x))).upper()
        elif ord(i) > 96 and ord(i) <= 122 - x:
            s1 += chr(ord(i) + x).upper()
        else:
            s1 += i
    else:
        if ord(i) > 122 - x and ord(i) < 123:
            s1 += chr(96 + (ord(i) - (122 - x)))
        elif ord(i) > 96 and ord(i) <= 122 - x:
            s1 += chr(ord(i) + x)
        else:
            s1 += i
print(s1)
