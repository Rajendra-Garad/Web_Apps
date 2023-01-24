def F_read():
    with open("Text2.txt", 'r') as file:
        data = file.readlines()
    return data


def F_write(args):
    with open("Text2.txt", 'w') as file:
        file.writelines(args)


