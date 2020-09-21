def fizzBuzz(n: int):
    result = []
    for i in range(n):
        key = i + 1
        if key % 15 is 0:
            result.append("FizzBuzz")
            continue
        if key % 5 is 0:
            result.append("Buzz")
            continue
        if key % 3 is 0:
            result.append("Fizz")
            continue
        result.append("{}".format(key))

    return result

fizzBuzz(1)