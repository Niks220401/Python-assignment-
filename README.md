# Python-assignment-

As discussed please complete the below python assignments and point me to the github link for review.

 

Please make sure you send the execution output of all these assignments over email.

 

1) Input: matrix with A x B grid of single character. It can have number, alphabet, space or special characters (!,@,#,$,%,&).

Matrix has an additional first line which contains integers A (row) and B (column) having a space between them.

The first line specifies A & B of the matrix (8 by 5 in this case)

(Below is just an example. The program should work with any A x B matrix, with any combinations of special characters, space, alphanumeric letters. And not necessarily character dot would be the separator printing the later special characters)

(Note: The matrix will be declared in the code, do not read it from the user)

 

8 5

S   o v #

p T g t 

r e i # 

y c e   @

I h s L 

Q n @ t 

# o % d !

$ l P . #

 

Read test horizontally column by column

It will result to:

SpryIQ#$ Technologies@%Pvt# Ltd.#  @  !#

 

Desired output: Separate out words, and remove special characters between them. Keep special characters occurring after the last word.

Output:

SpryIQ Technologies Pvt Ltd.#  @  !#

 

(Program should also work with below example with the same code

9 3

O h r

p o a

e n m

n 5 m

* 7 i

% P n

P r g

y o @

t g !

 

Output: Open Python Programming@!

)

 

 

2. Given a list of files ["file1.txt", "file1.pdf", "file1.xlsx", "file1.xls", "file2.txt", "file3.pdf", "file4.mp4", "file2.ppt.txt"]

create dictionary with key representing the extension of file and value containing list of file names with that extension

e.g.

{

".txt": ["file1.txt", "file2.txt", "file2.ppt.txt"]

}

Note: .ppt.txt will be considered as .txt extension type. And list can have multiple file extension types.

 

 

3. Consider a list of strings ["random_2020-05-04 18:08_string", "random_string_2019-02-12 12:00", "string_random_2019-02-15 16:00", . . .]

   All the strings in the list have a common format "yyyy-mm-dd hh:mm".

   Write a program to extract the above common format and display it like: random_2020-05-04 18:08_string --> 2020-05-04 18:08

   Optimized code is expected here
