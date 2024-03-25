def find_divisors(n):
    divisors = []
    for i in range(2, n):
        if n % i ==  0:
            divisors.append(i)
    divisors.sort()
    return divisors

count=0
for i in range(500001,1000000):
    variable=find_divisors(i)   
    for j in variable:
        if j!=8 and j%10==8:
            print(i,j)
            count+=1
            break
    if count==5:
        break
