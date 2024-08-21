calls = 0


def count_calls(calls_1):
    global calls
    calls = calls_1
    return calls


count_calls(4)


def string_info(string):
    str_1 = len(string), string.upper(), string.lower()

    return str_1


result = string_info('Homework')
result_1 = string_info('marshmallow')
print(result)
print(result_1)


def is_contains(string, list_to_search):
    if string in list_to_search:
        print(True)
    else:
        print(False)
        return


print(is_contains('Homework', ['Home', 'HoMeWoRk', 'Homework']))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(calls)
