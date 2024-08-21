from math import floor
import random


def one_dim_algo(arr):
    for i in range(len(arr)):
        left = arr[i-1] if i-1 >= 0 else float('-inf')
        right = arr[i+1] if i+1 < len(arr) else float('-inf')
        cur = arr[i]
        
        if cur >= left and cur >= right:
            return cur
            
    return None

def one_dim_divide_algo(arr):
    def algo(arr, s, e):
        idx_mid = floor((s + e) / 2)
        
        mid = arr[idx_mid]
        left = arr[idx_mid - 1] if idx_mid - 1 >= 0 else float('-inf')
        right = arr[idx_mid + 1] if idx_mid + 1 < len(arr) else float('-inf')
        
        if mid < left:
            return algo(arr, s, idx_mid-1)
        elif mid < right:
            return algo(arr, idx_mid+1, e)
        else:
            return mid
        
    return algo(arr, 0, len(arr)-1)

def two_dim_algo(arr, i=0, j=0):
    def greatest_dir(i, j):
        nonlocal m, n, arr
        
        pt = arr[i][j]
        left = arr[i][j-1] if j-1 >= 0 else float('-inf')
        right = arr[i][j+1] if j+1 < n else float('-inf')
        up = arr[i-1][j] if i-1 >= 0 else float('-inf')
        down = arr[i+1][j] if i+1 < m else float('-inf')
        
        greatest = max(pt, left, right, up, down)
        
        if greatest == pt:
            return (i, j)
        elif greatest == left:
            return (i, j-1)
        elif greatest == right:
            return (i, j+1)
        elif greatest == up:
            return (i-1, j)
        else:
            return (i+1, j)
        
    m, n = len(arr), len(arr[0])
    
    new_i, new_j = greatest_dir(i, j)
    while not (new_i == i and new_j == j):
        i, j = new_i, new_j
        new_i, new_j = greatest_dir(i, j)
    
    return arr[i][j]

def two_dim_divide_algo(arr):
    def find_max_idx(arr, col):
        mx = float('-inf')
        idx = -1

        for i, row in enumerate(arr):
            v = row[col]
            if v > mx:
                mx = v
                idx = i
                
        return idx
    
    def algo(arr, m_s, m_e, n_s, n_e):
        m, n = m_e - m_s + 1, n_e - n_s + 1
        j = floor((n_s + n_e) / 2)
        i = find_max_idx(arr, j)
        
        pt = arr[i][j]
        left = arr[i][j-1] if j-1 >= 0 else float('-inf')
        right = arr[i][j+1] if j+1 < n else float('-inf')
        
        if left > pt:
            new_arr = [row[:j] for row in arr]
            return algo(new_arr, 0, len(new_arr)-1, 0, len(new_arr[0])-1)
        elif right > pt:
            new_arr = [row[j+1:] for row in arr]
            return algo(new_arr, 0, len(new_arr)-1, 0, len(new_arr[0])-1)
        else:
            return pt
    
    return algo(arr, 0, len(arr)-1, 0, len(arr[0])-1)

if __name__ == "__main__":
    one_dim_arr = [random.randint(0, 100) for _ in range(10)]
    two_dim_arr = [[random.randint(0, 100) for _ in range(10)] for _ in range(5)]
    
    # gives the first peak it finds
    one_dim_peak_1 = one_dim_algo(one_dim_arr)
    # gives the first peak it finds start from middle
    one_dim_peak_2 = one_dim_divide_algo(one_dim_arr)
    
    # these may give local peaks
    two_dim_peak_1 = two_dim_algo(two_dim_arr)
    two_dim_peak_2 = two_dim_divide_algo(two_dim_arr)

    print('1D Array:\n', one_dim_arr)
    print('\n2D Array:\n')
    for row in two_dim_arr:
        print(row)

    print(f'1D Peaks: {one_dim_peak_1}, {one_dim_peak_2}')
    print(f'2D Peaks: {two_dim_peak_1}, {two_dim_peak_2}')

