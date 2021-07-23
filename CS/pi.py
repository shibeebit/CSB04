from math import sqrt, pi

def basel(precision):
    x = 0
    n = 1
    while pi - sqrt(x*6) > precision:
        x += 1/(n ** 2)
        n += 1
    x = sqrt(x*6)
    return (x, n-1)

def taylor(precision):
    x = 0
    n = 0
    a = 1
    while abs(pi - 4*x) > precision:
        if (n%2==0):
            x += 1/a
        else:
            x -= 1/a
        a += 2
        n += 1
    x = 4 * x
    return (x, n)

def wallis(precision):
    x = 1
    n = 0
    a = 2
    while pi - 2*x > precision:
        x *= (a ** 2)/((a-1) * (a+1))
        a += 2
        n += 1
    x = 2 * x
    return (x, n)

def spigot(precision):
    x = 1
    n = 1
    a = 1
    b = 3
    while pi - 2*x > precision:
        a *= n/b 
        x += a
        b += 2
        n += 1
    x = 2 * x
    return (x, n)

def race(precision, algorithms):
    races = []
    for algo in algorithms:
        if algo == "basel":
            races.append(basel(precision))
        elif algo == "taylor":
            races.append(taylor(precision))
        elif algo == "wallis":
            races.append(wallis(precision))
        elif algo == "spigot":
            races.append(spigot(precision))
    for race in races:
        

def main():
    precision = float(input("Precision?"))
    choice = str(input("Choose spigot, wallis, taylor or basel?"))
    algorithms = []
    if "basel" in choice:
        algorithms.append("basel")
    elif "taylor" in choice:
        algorithms.append("taylor")
    elif "wallis" in choice:
        algorithms.append("wallis")
    elif "spigot" in choice:
        algorithms.append("spigot")
    print(race(precision, algorithms))

main()


