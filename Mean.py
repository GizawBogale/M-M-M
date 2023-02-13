# findingn the mean of the array

salaries = [1250, 1200, 813, 1046, 1046, 806, 952, 927, 915, 861, 850, 814, 813, 809, 808, 806, 792, 778, 757, 755, 813, 752, 750]
def mean(salaries):
    sum = 0
    for i in salaries:
        sum +=i
        mean = sum/len(salaries)
    return mean
print("The mean of the given array is:",mean(salaries))



