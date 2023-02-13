# To find the mode of the array
salaries = [1250, 1200, 813, 1046, 1046, 806, 952, 927, 915, 861, 850, 814, 813, 809, 808, 806, 792, 778, 757, 755, 813, 752, 750]

def mode(salaries):
    counter = 0
    num = salaries[0]

    for i in salaries:
        current_frequency = salaries.count(i)
        if (current_frequency > counter):
            counter = current_frequency
            num = i
    return num
    return counter
print("the mode of the given array is:", mode(salaries))


