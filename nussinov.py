def nussinov(sequence):
    n = len(sequence)
    dp = [[0] * n for _ in range(n)]
    bt = [[None] * n for _ in range(n)]
    
    pairs = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            
            dp[i][j] = dp[i + 1][j]
            bt[i][j] = (i + 1, j)
            if dp[i][j-1] > dp[i][j]:
                dp[i][j] = dp[i][j-1]
                bt[i][j] = (i, j-1)

            if pairs[sequence[i]] == sequence[j]:
                dp[i][j] = dp[i + 1][j - 1] + 1
                bt[i][j] = (i + 1, j - 1)

            for x in range(i, j):
                if dp[i][x] + dp[x + 1][j] > dp[i][j]:
                    dp[i][j] = dp[i][x] + dp[x + 1][j]
                    bt[i][j] = (i, x, x + 1, j)

    soln = traceback(sequence, dp)

    structure = ['.'] * n
    for (i, j) in soln:
        structure[i] = '('
        structure[j] = ')'
    return dp[0][-1], ''.join(structure)


def traceback(sequence, dp):
    n = len(sequence)
    stack = [(0,n-1)]
    soln = []
    while len(stack) > 0:
        i,j = stack.pop()
        if i >= j:
            continue
        elif dp[i+1][j] == dp[i][j]:
            stack.append((i+1, j))
        elif dp[i][j-1] == dp[i][j]:
            stack.append((i, j-1))
        elif dp[i+1][j-1] +1 == dp[i][j]:
            soln.append((i, j))
            stack.append((i+1, j-1))
        else:
            for k in range(i+1, j):
                if dp[i][k] + dp[k+1][j] == dp[i][j]:
                    stack.append((k+1, j))
                    stack.append((i, k))
                    break

    return soln