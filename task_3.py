def envelope(n):
    for i in range(1):
        print ((2 * n + 1) * "*")
    for i in range(n - 1):
        print ("*" + i * " " + "*" + (2 * n - 3 - 2 * i) * " " + "*" + i * " " + "*")
    for i in range(1):
        print ("*" + (n - 1) * " " + "*" + (n - 1) * " " + "*")
    for i in range(n - 1):
        print("*" + (n - 2 - i) * " " + "*" + (2 * i + 1) * " " + "*" + (n - 2 - i) * " " + "*")
    for i in range(1):
        print((2 * n + 1) * "*")

envelope(n)
