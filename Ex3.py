'''
3. Backtracking y Recursión
a) N Reinas
Dado un tablero de ajedrez N x N, encuentra todas las formas de colocar N reinas sin que se ataquen entre sí.

b) Generar Combinaciones de Paréntesis
Dado un número n, genera todas las combinaciones válidas de n pares de paréntesis.


Input: 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
'''

def n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(i - row) == abs(board[i] - col):
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(list(board))
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

print(n_queens(4))

def generate_parenthesis(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result

print(generate_parenthesis(3))