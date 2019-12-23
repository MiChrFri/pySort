class MergeSort:

    def get_mid(self, lower, upper):
        return lower + int((upper - lower)/2)

    def merge(self, left, right):
        merged = []
        l_index = 0
        l_len = len(left)
        r_index = 0
        r_len = len(right)

        while l_index < l_len and r_index < r_len:
            if left[l_index] < right[r_index]:
                merged.append(left[l_index])
                l_index += 1
            else:
                merged.append(right[r_index])
                r_index += 1

        while l_index < l_len:
            merged.append(left[l_index])
            l_index += 1

        while r_index < r_len:
            merged.append(right[r_index])
            r_index += 1
        
        return merged
        

    def merge_sort(self, numbers, lower, upper):
        if upper-lower == 1:
            return numbers[lower:upper]

        mid = self.get_mid(lower, upper)
        left = self.merge_sort(numbers, lower, mid)
        right = self.merge_sort(numbers, mid, upper)

        return self.merge(left, right)


    def sort(self, numbers):
        return self.merge_sort(numbers, 0, len(numbers))
