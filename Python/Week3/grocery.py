dict = {}
while True:
    try:
        item = input().upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    except EOFError:
        print()
        keys = list(dict.keys())
        keys.sort()
        new_dict ={i: dict[i] for i in keys}
        for item in new_dict:
            print(new_dict[item], item)
        break