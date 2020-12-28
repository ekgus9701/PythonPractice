    
def ms(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = ms(leftList)
    rightList = ms(rightList)
    return merge(leftList, rightList)  

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

n=int(input(""))
arr=[]
leftList =[]
rightList=[]
arr=list(map(int,input("").split()))

k=int(input(""))
ms(arr)

List=leftList+rightList
print( " ".join( repr(e) for e in List ) )
    
