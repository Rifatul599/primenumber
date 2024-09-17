def checkprime (num):
    if num<=1:
        return 'not prime'
    for i in range (2,int(num**0.5 + 1)):
        if num % i == 0:
            return 'not prime'
    else:
        return 'prime'

print(checkprime(9))