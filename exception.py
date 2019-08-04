try:
    a=2/0
except ZeroDivisionError:
    print("cannot divide by zero")

else:
    print(a)
finally:
    print("finally block")


try:
    a=[1,2,3,4]
    print(a[10])
except IndexError:
    print("index out")
finally:
    print("index final")