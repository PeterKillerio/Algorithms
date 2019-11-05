input_array = [5,3,2,44,88,1,56,8186,11,486,48,2,45,5,4,6,8,4,8,684]

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        flag = False
        while(j > 0):
            if(array[j-1] > array[i]):
                if((j-2) >= 0):
                    if(array[j-2] <= array[i]):
                        flag = True
                else:
                    flag = True
            if(flag):
                mem = array[i]
                print(array)
                for m in range(i, j - 2, -1):
                    array[m] = array[m - 1]
                array[j - 1] = mem
                break

            j -= 1
    return array

print(insertion_sort(input_array))