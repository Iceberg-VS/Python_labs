variable = 5**36 + 5**24 - 25
count=0
while variable>0:
    if variable%5==4:
        count=count+1
    variable = variable // 5
print(count)