

def bubble(my_list):
    for j in range(len(my_list) - 1):
        for i in range(len(my_list) - j - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list

