"""
    Python standard library for binary search tree is bisection method,
    which module named bisect
"""
import bisect

def binary_search_tree(sortedlist, target):
    if not sortedlist:
        return None

    left = 0
    right = len(sortedlist)-1

    """
        1. 首先判断能不能进while loop, 如果只有一个元素在list里面, so, 我需要left <= right
        2. right = mid-1, not right = mid.  因为如果我们只有一个元素在list里面，这个元素并不等于target,
           那while loop会陷入死循环.
    """
    while left <= right:
        mid = left + (right - left)//2
        if sortedlist[mid] == target:
            return mid
        if sortedlist[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo


def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: lo = mid+1
        else: hi = mid
    return lo



def binary_search(sarray, target):
    if not sarray and isinstance(target, int):
        raise 'sarray none'
    
    left = 0
    right = len(sarray) -1
    while left<= right: # only < miss one element
        mid = left + (right - left)//2
        if sarray[mid] == target:
            return mid
        elif sarray[mid] < target:
            right = mid -1
        else:
            left = mid + 1
    
def search_in_sorted_matrix(array, target):
    print(array)
    if not array or len(array[0]) == 0:
        return 'NOT 2D ARRAY'
    
    rows = len(array)
    cols = len(array[0])
    right = rows * cols -1
    left = 0
    
    while left  <= right:
        mid = left + (right - left)//2
        r = mid // cols
        c = mid % cols
        if array[r][c]  == target:
            print(r,c)
            return r, c
        elif array[r][c] > target:
            right = mid -1
        else:
            left = mid+1
    
def binary_searh_2(array, target):
    if not array:
        return none
    
    left = 0
    right = len(array) -1
    while  left < right-1: # if 左边界 == 右边界-1就相邻了, terminates
        mid = left + (right - left)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid  #if mid + 1 就错过了后面的值
        else:
            right = mid
    
    #post processing: 不同的提议，稍微不一样
    if abs(array[left] -target) < abs(array[right]-target):
        return left
    else:
        return right
    
    
def binary_search_1st_Occur(array, target):
    '''
     return the index of the first occurrence of an element, say 5? 
    '''
    left = 0
    right = len(array) - 1
    while left < right -1:
        mid = left + (right - left)//2
        if array[mid] == target:
            right = mid # = mid -1 wrong: [4,5,5], right = mid -1 => right =4, miss掉了index=1的5， 不能把此target排除为非1st target! do not stop here, keeping track the left.
        elif array[mid] < target:
            mid = left + 1
        else:
            mid = right - 1
    
    # post processing
    if array[left] == target:
        return left
    elif array[right]  == target:
        return right
    

def k_closest_in_sorted_array(array, target, k):
    if not isinstance(k, int) or not array:
        return 'not valid input'
    
    left = 0
    right = len(array) -1
        # find largets smaller or equal target element 's index in the array
    while left < right-1:
        mid = left +(right - left) //2
        if array[mid] <= target:
            left = mid
        else:
            right = mid
    
    i = 0
    kclosest = []
    while i < k:
        if right >= len(array) or left >= 0 and abs(array[left] -target) < abs(array[right]-target):
            kclosest.append(left)
            left -= 1
        else:
            kclosest.append(right)
            right +=1
        i +=1
    return kclosest
    
def test():
    # sortedList = [7, 8, 9, 10, 11, 12]
    # target_po = binary_search(sortedList, 12)
    # print(target_po)

    # arr2D = [[3,5],[6,7],[8,9],[10,11],[21,23]]
    # r,c = search_in_sorted_matrix(arr2D, 23)
    
    
    # arr_1stocc =[4, 5,5]
    # index = binary_search_1st_Occur(arr_1stocc, 5)
    # print(index)
    
    array = [1, 2, 3, 8,9 ]
    kclosests = k_closest_in_sorted_array(array, 4, 2)
    print(f'kcloests: {kclosests}')
    
if __name__ == "__main__":
    test()