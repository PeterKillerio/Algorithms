input_array = [5,4,2,44,88,1,56,8186,11,486,48,2,45,5,4,6,8,4,8,684]

def buubleSort(array):
    for i in range(len(array)):
        for l in range(len(array)-i-1):
            if(array[l] > array[l+1]):
                array[l], array[l+1] = array[l+1], array[l]
    return array

print(buubleSort(input_array))