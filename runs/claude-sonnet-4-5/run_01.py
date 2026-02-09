
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    
    # Create pairs and sort by aura value, then by index
    pairs = [(a[i], i) for i in range(n)]
    pairs.sort()
    
    # Extract sorted values
    v = [p[0] for p in pairs]
    
    # DP table: dp[L][R] = max score for interval [L, R]
    dp = [[0] * n for _ in range(n)]
    
    # Fill DP table by increasing interval length
    for length in range(2, n + 1):
        for L in range(n - length + 1):
            R = L + length - 1
            step = R - L + 1  # Current step number (1-indexed)
            weight = w[step - 1]  # Weight for this step
            contribution = weight * (v[R] - v[L])
            
            # Take max of extending from left or right
            dp[L][R] = max(dp[L + 1][R], dp[L][R - 1]) + contribution
    
    return dp[0][n - 1]

t = int(input())
for _ in range(t):
    print(solve())
