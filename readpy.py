
def string_key():
    with open('foo.txt') as f:
        lines = f.readlines()

    return str(lines)