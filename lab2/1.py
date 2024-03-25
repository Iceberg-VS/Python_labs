import itertools
letter="ГЕПАРД"
count=0
for x in itertools.product(letter,repeat=5):
    ''.join(x)
    if (x.count('Г')==1 and x[0]!='A' and x[-1]!='E'):
        count=count+1
print(count)