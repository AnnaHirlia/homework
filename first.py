array = [560, 711, 237, 472, 24, 133, 879, 767, 983, 401, 731, 553, 347, 951, 15]

for i in range(len(array)): # bubbles
    for j in range(len(array) - 1):
        if array[j]>array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print("sorted by bubbles: ")
print(array)

array = [735, 85, 524, 551, 333, 313, 953, 446, 510, 434, 174, 238, 747, 494, 473]

for i in range(len(array)): # insertion
    j = i - 1
    temp = array[i]
    while array[j] > temp and j >= 0:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = temp

print("\nsorted by insertion: ")
print(array)

array = [559, 248, 874, 703, 235, 885, 658, 101, 34, 98, 613, 253, 699, 363, 128]

for i in range(len(array) - 1): # selection
    min = i
    for j in range(i+1,15):
        if array[j] < array[min]:
            min = j
    if min != i:
        temp = array[min]
        array[min] = array[i]
        array[i] = temp

print("\nsorted by selection: ")
print(array)
