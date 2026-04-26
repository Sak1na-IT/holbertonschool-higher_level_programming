#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(list_length):
        result = 0
        try:
            l1 = my_list_1[i]
            l2 = my_list_2[i]
            result = l1 / l2
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
