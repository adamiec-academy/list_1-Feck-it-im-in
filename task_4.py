def snowball(n, k):
    r = n / 2
    for i in range(n):
        for j in range(n):
            if ((i - r) ** 2 + (j - r) ** 2 <= r ** 2):
                print("#", end="")
            else:
                print (" ", end="")


def snowman(n):
    pass
