def fizzbuzz(n):
    s = ''
    if n % 3 == 0:
        s += 'Fizz'
    if n % 5 == 0:
        s += 'Buzz'
    if len(s) > 1:
        return s
    return str(n)