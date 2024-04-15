"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/description/

"""

# v1
def lcs_length(X, Y):
    m = len(X)  # get the # of symbols in X
    n = len(Y)  # get the # of symbols in Y
    # c will be the array to hold the lengths of LCS; adding 1 for the base case 0 values
    c = [[0 for j in range(n+1)] for i in range(m+1)]
    # Building the matrix in bottom-up fashion
    for i in range(1, m+1):  # for all X[i]
        for j in range(1, n+1):  # for all Y[j]
            if X[i-1] == Y[j-1]:  # Indexes of i and j in X and Y should be i-1 and j-1
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    # The bottom-right element will have the length of the LCS
    return c[m][n]

# Example strings
x = "abcde"
y = "ace"

# Get the length of the LCS
print('lcs len:', lcs_length(x, y))

# v2
def lcs_length_and_solution(X, Y):
    m = len(X)
    n = len(Y)
    # c is the table for the length of the LCS
    c = [[0] * (n + 1) for _ in range(m + 1)]
    # b is the table to remember the choices (directions to reconstruct the LCS)
    b = [[""] * (n + 1) for _ in range(m + 1)]
    
    # Fill the tables c and b
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "↖"  # Indicates a match
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "↑"  # Indicates to move up
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"  # Indicates to move left
                
    return c, b

def print_lcs(b, X, i, j):
    # Helper function to print LCS using table b
    if i == 0 or j == 0:
        return ""
    if b[i][j] == "↖":
        return print_lcs(b, X, i - 1, j - 1) + X[i - 1]
    elif b[i][j] == "↑":
        return print_lcs(b, X, i - 1, j)
    else:
        return print_lcs(b, X, i, j - 1)

# Example strings
x = "abcde"
y = "ace"

# Get the length of the LCS and the solution table
c, b = lcs_length_and_solution(x, y)

# Print the length of the LCS
lcs_length = c[len(x)][len(y)]
lcs_sequence = print_lcs(b, x, len(x), len(y))

print('lcs len:',lcs_length, 'lcs seq:', lcs_sequence)
