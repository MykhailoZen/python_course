def funk_1(t):
    if not t.isdigit():
        raise TypeError("не тот тип")


def funk_2(t: str) -> str:
    """
    dvxcgv xdg
    @param t: fdsfsdfb sdfgs
    @return: fsfdfsf dfsdf
    """
    return type(type(t))


if __name__ == '__main__':
    t = "4053453ffd"
    print(funk_2(4))

