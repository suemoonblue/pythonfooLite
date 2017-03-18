<<<<<<< HEAD
=======
#!/usr/bin/env python3

>>>>>>> c1c3a1b0d7aba895b6471068c4cb0b29bded37a3
# Generatoren und yield
>> > def gen(s):
... for char in s:
... yield char
...
...
>> > for x in gen("abcdef"):
... print(x)

# Dekoratoren
>> > def f(x):
... return x**2
...
>> > f(2)
4
>> > f(3)
9

>> > def dec(func):
... def inner_func(*args):
... print(args)
...         r = func(*args)
... print("Return: {}".format(r))
... return r
... return inner_func
...
>> > @dec
... def f(x):
... return x**2
...
>> > f(2)
(2,)
Return:
    4
4