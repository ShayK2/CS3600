def quickSort(list):
    if len(list) < 2:
        return list

    less = [i for i in list[1:] if i < list[0]];
    greater = [i for i in list[1:] if i >= list[0]];
    return quickSort(less) + [list[0]] + quickSort(greater);

if __name__ == '__main__':
    lst = [2,4,5,1]
    print quickSort(lst)