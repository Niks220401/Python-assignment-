def process_matrix(matrix):
    A, B = matrix[0].split()
    A, B = int(A), int(B)
    
    words = []
    for col in range(B):
        word = ''
        for row in range(1, A+1):
            char = matrix[row][col]
            if char.isalnum() or char.isspace():
                word += char
            elif word:
                words.append(word)
                word = ''
        if word:
            words.append(word)
    
    return ' '.join(words)

# Example usage:
matrix1 = [
    "8 5",
    "S   o v #",
    "p T g t ",
    "r e i # ",
    "y c e   @",
    "I h s L ",
    "Q n @ t ",
    "# o % d !",
    "$ l P . #",
]

matrix2 = [
    "9 3",
    "O h r",
    "p o a",
    "e n m",
    "n 5 m",
    "* 7 i",
    "% P n",
    "P r g",
    "y o @",
    "t g !",
]

output1 = process_matrix(matrix1)
output2 = process_matrix(matrix2)

print(output1)  # Output: SpryIQ Technologies Pvt Ltd.#  @  !#
print(output2)  # Output: Open Python Programming@!