def get_fibonacci_number(index):
	return(
        index if index < 2 else
        (get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2))
    )

def get_fibonacci_sequence(length, seq=[0, 1]):
	return(
        seq[:length] if length <= 2 else
        get_fibonacci_sequence(length - 1) + [get_fibonacci_sequence(length - 1)[length - 2] + get_fibonacci_sequence(length - 1)[length - 3]]
    )

def get_sorted_dict_by_decimals(dict_arg):
	return {key: item for key, item in sorted(dict_arg.items(), key=lambda number: (number[1] * 10) % 10)}

def fibonacci_numbers(length):
    n1, n2 = 0, 1
    yield n1
    while length > 1:
        yield n2
        temp = n1 + n2
        n1 = n2
        n2 = temp
        length -= 1

def build_recursive_sequence_generator(liste, fonction, save=False):
    saved = liste[:]
    if save == True:
        def fonction1(index):
            yield saved[0]
            yield saved[1]
            while len(saved) < index:
                yield fonction(saved)
                saved.append(fonction(saved))
    else:
        def fonction1(index):
            i = 2
            yield saved[0]
            yield saved[1]
            while i < index:
                yield fonction(saved)
                saved.append(fonction(saved))
                del saved[0]
                i += 1
    return fonction1



if __name__ == "__main__":	
    num1 = [1, 3, 5, 7, 9, 10]
    num2 = [2, 4, 6, 8]
    num1[-1:] = num2
    print(num1)

