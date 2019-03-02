N = int(input('Write a number to define a range: '))
for i in range(1, N+1):
    if i % 15 == 0:
        i = 'FizzBuzz'
    elif i % 5 == 0:
        i = 'Buzz'
    elif i % 3 == 0:
        i = 'Fizz'
    print(i)
