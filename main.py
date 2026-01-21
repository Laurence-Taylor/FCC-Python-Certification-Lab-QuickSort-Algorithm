def quick_sort(int_list):
    # Stop Sorting
    if int_list == []:
        return []
    if len(int_list) == 1:
        return int_list
    
    # Declare and Initialize new variables.
    pivot = int_list[0]
    list_less_pivot = []
    list_great_pivot = []
    list_eq_pivot = []
    
    # Create the new 3 list
    for i in range(len(int_list)):
        if pivot < int_list[i]:
            list_great_pivot.append(int_list[i])
        elif pivot > int_list[i]:
            list_less_pivot.append(int_list[i])
        else:
            list_eq_pivot.append(int_list[i])

    # Recursive Call
    less_soted = quick_sort(list_less_pivot)
    great_sorted = quick_sort(list_great_pivot)
    
    #Return ordered List
    return less_soted + list_eq_pivot + great_sorted

if __name__ == '__main__':
    print(quick_sort([20, 3, 14, 1, 5]))