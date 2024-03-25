def intersect(first_list,twist_list):
    result_list=set()
    for first_element in first_list:
        for twist_element in twist_list:
            if first_element==twist_element:
                result_list.add(first_element)
                break
    return list(result_list)

def rec_intersect(list1, list2):
    if not list1 or not list2:
        return []
    
    if list1[0] in list2:
        return [list1[0]] + rec_intersect(list1[1:], list2)
    
    return rec_intersect(list1[1:], list2)


print(intersect([1, 2,2,2, 3, 4], [2, 3, 4, 6, 8]))
print(intersect([5, 8, 2], [2, 9, 1]))
print(intersect([5, 8, 2], [7, 4]),'\n')

print(rec_intersect([1, 2,2,2, 3, 4], [2, 3, 4, 6, 8]))
print(rec_intersect([5, 8, 2], [2, 9, 1]))
print(rec_intersect([5, 8, 2], [7, 4]))

#терь корни

def sqrts(n):
    result=0.0
    first=3
    while (n!=0):
        result=(result+first)**0.5
        n=n-1
    return result

def rec_sqrts(n):
    if n == 0:
        return 0.0
    else:
        return (sqrts(n-1) + 3)**0.5

print(sqrts(0))
print(sqrts(1))
print(sqrts(2))
print(sqrts(3))

print(rec_sqrts(0))
print(rec_sqrts(1))
print(rec_sqrts(2))
print(rec_sqrts(3))