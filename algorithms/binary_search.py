array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

item = int(input('type the target: '))

def binarySearch(array, target, start=0, end=None):
    if end is None:
        end = len(array)-1

    if start <= end: # enquanto se tem uma sublista válida
        mid = (start + end)//2

        if target == array[mid]:
            return mid

        elif target > array[mid]:
            return binarySearch(array, target, mid+1, end)

        elif target < array[mid]:
            return binarySearch(array, target, start, mid-1)

    return None 

print(binarySearch(array, item))
