def nussinov(sequence):
    n = len(sequence)
    dp = [[0] * n for _ in range(n)]
    bt = [[None] * n for _ in range(n)]
    
    pair = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            
            dp[i][j] = dp[i + 1][j]
            bt[i][j] = (i + 1, j)

            if pair.get(sequence[i]) == sequence[j]:
                if dp[i + 1][j - 1] + 1 > dp[i][j]:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                    bt[i][j] = (i + 1, j - 1)

            for k in range(i, j):
                if dp[i][k] + dp[k + 1][j] > dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k + 1][j]
                    bt[i][j] = (i, k, k + 1, j)
    
    def backtrace(i, j, structure):
        if i >= j:
            return
        
        if bt[i][j] is None:
            return

        if len(bt[i][j]) == 2:
            ni, nj = bt[i][j]
            structure[i] = '('
            structure[j] = ')'
            backtrace(ni, nj, structure)
        elif len(bt[i][j]) == 4:
            i1, j1, i2, j2 = bt[i][j]
            backtrace(i1, j1, structure)
            backtrace(i2, j2, structure)
        else:
            ni, nj = bt[i][j]
            backtrace(ni, nj, structure)

    structure = ['.'] * n
    backtrace(0, n - 1, structure)
    return dp[0][n - 1], ''.join(structure)
