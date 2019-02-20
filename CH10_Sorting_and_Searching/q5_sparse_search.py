def sparse_search(list,target):

    start = 0
    end = len(list)-1
    print(binary_search(list,start,end,target))

def binary_search(list,start,end,target):

    left = right = 0

    while start <= end:
        mid = (start+end)//2

        if list[mid] == "":
            left = mid - 1
            right = mid + 1
            while True:
                if left < start and right > end:
                    return -1
                if left >= start and list[left] != "":
                    mid = left
                    break
                if right <= end and list[right] != "":
                    mid = right
                    break
                left -= 1
                right += 1
        if list[mid] == target:
            return mid

        if list[mid] > target:
            end = mid - 1
            continue
        start = mid + 1
    return -1


list = ["at", "ball", "", "", "", "", "car",
           "dad", "", "", "", ""]

target = "dad"
sparse_search(list,target)