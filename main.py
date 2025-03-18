def max_min_select(arr, low, high):
   
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]
    
    mid = (low + high) // 2
    
    left_max, left_min = max_min_select(arr, low, mid)
    right_max, right_min = max_min_select(arr, mid + 1, high)
    
    overall_max = max(left_max, right_max)
    overall_min = min(left_min, right_min)  
    
    return overall_max, overall_min

if __name__ == "__main__":
    arr = [3, 5, 1, 7, 9, 2, 8, 4, 6]
    n = len(arr)
    max_val, min_val = max_min_select(arr, 0, n - 1)
    print(f"Maior elemento: {max_val}")
    print(f"Menor elemento: {min_val}")