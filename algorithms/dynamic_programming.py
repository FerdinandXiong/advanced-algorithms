def max_money(A):
    for i in range (len(A) - 1):
        A[i + 1][0] += A[i][0]
        A[0][i + 1] += A[0][i]
    
    for i in range (len(A) - 1):
        for j in range (len(A) - 1):
            A [i + 1][j + 1] += A[i + 1][j] if A[i + 1][j] > A[i][j + 1] else A[i][j + 1]
    
    return A[len(A) - 1][len(A) - 1]

def path_max_money(A):
    n = len(A)
    path_arr = [[None] * n for _ in range(n)]
    for i in range(n - 1):
        A[i + 1][0] += A[i][0]
        A[0][i + 1] += A[0][i]
        
        path_arr[i + 1][0] = (i, 0)
        path_arr[0][i + 1] = (0, i)
    
    for i in range (n - 1):
        for j in range (n - 1):
            if A[i + 1][j] > A[i][j + 1]:
                A [i + 1][j + 1] += A[i + 1][j]
                path_arr[i + 1][j + 1] = (i + 1, j)
            else:
                A [i + 1][j + 1] += A[i][j + 1]
                path_arr[i + 1][j + 1] = (i, j + 1)
    
    path = [None]*(n * 2 - 1)
    print (len(path))
    path [(n * 2) - 2] = (n - 1, n - 1)
    for i in range ((n * 2) - 3, -1, -1):
        (x, y) = path[i + 1]
        path[i] = path_arr[x][y]   
    print(path)
    return A[n - 1][n - 1]

def weight_sum_possible(weight_set, target_weight):
    iterative_weight_set = set()
    for s in weight_set:
        for e in list(iterative_weight_set):
            iterative_weight_set.add(s + e)
        iterative_weight_set.add(s)
    print(iterative_weight_set)
    return target_weight in iterative_weight_set
    