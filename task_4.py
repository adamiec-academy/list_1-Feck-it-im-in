def snowball(n, k):
    promien = n / 2
    for i in range(n):
        print(k * " ", end="")
        for j in range(n):
            if (i + 0.5 - promien) ** 2 + (j + 0.5 - promien) ** 2 <= promien ** 2:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def snowman(n):
    snowball(n, 2)
    snowball(n + 2, 1)
    snowball(n + 4, 0)
