# To find the mode of the array
salaries = [45, 14, 15, 12, 14, 15, 15, 18]

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


