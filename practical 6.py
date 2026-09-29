def matrix_chain_multiplication(p):
    n = len(p) - 1

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # length = chain length
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1

            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


# Main program
p = [10, 30, 5, 60]

result = matrix_chain_multiplication(p)

print("Minimum number of scalar multiplications:", result)