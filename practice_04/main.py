x = 13

def show():
    x = 3
    print(x)

show()
print(x)

# внутри функции x = 3, вне функции x = 13

def total(*args):
    return sum(args)
    pass


print(total(3, 4, 5))


def person(**kwargs):
    name = 'Олег'
    age = 19
    return name, age

print(person())

def increase(x):
    return x + 3  # Число из варианта

def apply(func, value):
    res = func(value)
    return res
    pass

print(apply(increase, 4))


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(4)

