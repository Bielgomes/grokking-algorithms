def regression(i: int) -> None:
    print(i)

    if i <= 1:
        return

    regression(i - 1)


def fat(i: int) -> int:
    if i == 1:
        return 1

    return i * fat(i - 1)


regression(3)
print("---------------")
print(fat(10))
