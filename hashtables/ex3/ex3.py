def intersection(arrays):
    """
    YOUR CODE HERE
    """
    length = len(arrays)
    nest = {y: {x:0 for x in arrays[y]} for y in range(length)}
    result = {}
    for x in range(length-1):
        temp = nest[x]
        temp = dict(temp.items() & nest[x+1].items())
        result.update(temp.items())

    return list(result.keys())


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
