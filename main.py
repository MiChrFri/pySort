from sort import MergeSort

def main():
    nums = [4, 5, 2, 6, 1, 8, 7, 0, -1, -7, 43, 74]
    ms = MergeSort()
    sorted = ms.sort(nums)
    print(sorted)

if __name__ == '__main__':
    main()