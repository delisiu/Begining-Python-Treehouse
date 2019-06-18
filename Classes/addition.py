def combiner(list):
    num = 0
    str = []
    for item in list: 
        if isinstance(item, int):
           num += item
        elif isinstance(item, float):
            num += item
        else: 
            str.append(item)

    return "{}{}".format("".join(str), num)
