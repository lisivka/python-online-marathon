"""
Это простое упражнение (а заодно и распространённый пример) на использование распаковок.
На вход подаётся строка, содержащая некоторое количество (не больше сотни) записанных через пробел целых чисел.
Распечатайте каждое целое число, приведённое к типу float, на отдельной строке в том же порядке, в котором они были переданы.
Sample Input:

0 1 1 2 3 5 8 13 21 34
Sample Output:

0.0
1.0
1.0
2.0
3.0
5.0
8.0
13.0
21.0
34.0
"""


s = input("Введите числа через пробел: ").split()

for num in s:
    print(float(num))

