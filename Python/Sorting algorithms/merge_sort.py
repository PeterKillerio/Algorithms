input_array = [5,3,2,44,88,1,56,8186,11,486,48,2,45,5,4,6,8,4,8,684]

def merge_sort(array):
    c_new = []
    idxA = 0
    idxB = 0

    a = array[:round(len(array) / 2)]
    if (len(a) > 1): a = merge_sort(a)

    b = array[round(len(array) / 2):]
    if (len(b) > 1): b = merge_sort(b)

    while True:
        if(idxA >= len(a) and idxB >= len(b)):
            break
        elif(idxA >= len(a)):
            while(idxB < len(b)):
                c_new.append(b[idxB])
                idxB += 1
            continue
        elif(idxB >= len(b)):
            while(idxA < len(a)):
                c_new.append(a[idxA])
                idxA += 1
            continue

        if(a[idxA] <= b[idxB]):
            c_new.append(a[idxA])
            idxA += 1
        else:
            c_new.append(b[idxB])
            idxB += 1

    return c_new

print(merge_sort(input_array))