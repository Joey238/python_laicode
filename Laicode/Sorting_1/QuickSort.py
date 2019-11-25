


def partition_sort(array, pivot):
    if not array and pivot >= len(array):
        raise "not valid"

    pivot_value = array[pivot]
    i = 0
    rightIndex = len(array) -1
    array[rightIndex], array[pivot] = pivot_value, array[rightIndex]
    j = rightIndex-1

    while i <= j:
        if array[i] < pivot_value:
            i += 1
        elif array[j] > pivot_value:
            j -= 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    array[i], array[rightIndex] = array[rightIndex], array[i]
    return array, i


def Rainbow_Sort(array):
    ''''
    aaaabbbccc
    '''
    if not array:
        return

    i = 0
    j = 0
    k = len(array) -1

    while j <= k:
        if array[i] == 'a':
            i += 1
            j += 1
        elif array[j] == 'b':
            j += 1
            print(i, j)
        elif array[k]  == 'c':
            k -= 1
        elif array[j] == 'a':
            array[i], array[j] = array[j], array[i]
            i += 1
            j += 1
        else:
            array[j], array[k] = array[k], array[j]
            k -= 1
    return array



def move_all_0(array):
    '''Given an array with integers, move all “0s” to the right-end of the array
       [0, i) : i的左侧不包含i 为非0
       [i, j]: unknown area
       [j, n-1):  j 的右侧不包含i 为‘0'.
       
    '''
    if array and isinstance(array, str):
        array = [i for i in array]
    
    i = 0
    j = len(array) -1
    while i <= j:
        if array[i] != '0':
            i +=1
        elif array[j] == '0':
            j -= 1
        else:
            array[i], array[j] = array[j],array[i]
            i += 1
            j -= 1
    return array

if __name__=="__main__":
    # array = [1, 9, 8, 5, 3]
    # pivot = 3
    # result, i = partition_sort(array, pivot)
    # print(result, i)


    # array2 = 'aaccbaaccbbbca'
    # array2 = [i for i in array2]
    # sorted2 = Rainbow_Sort(array2)
    # print(sorted2)
    
    reslut0 = move_all_0('asd000sdf00asd0f0w')
    print(reslut0)
    