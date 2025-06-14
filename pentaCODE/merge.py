class Merge_Sorting():
    def __init__(self):
        self.list = []

    def add_data(self, data):
        self.list.append(data)

    def merge_sort(self, arr=None):
        if arr is None:
            arr = self.list

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        print(arr)
        right_half = arr[mid:]
        print(arr)

        sortedLeft = self.merge_sort(left_half)
        print(sortedLeft)
        sortedRight = self.merge_sort(right_half)
        print(sortedRight)
        
        self.list = self.merge(sortedLeft, sortedRight)
        return self.list
    
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        print(result)
        result.extend(right[j:])
        print(result)
        return result
