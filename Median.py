# to find the median of the given array
if __name__ == '__main__':

    salaries = [1250, 1200, 813, 1046, 1046, 806, 952, 927, 915, 861, 850, 814, 813, 809, 808, 806, 792, 778, 757, 755, 813, 752, 750]
def median(salaries):
    salaries.sort()
    if len(salaries) % 2 != 0:
        median = salaries[int(len(salaries)/2)]
    else:
        median = salaries[(int(len(salaries)/2)) - 1] + salaries[int(len(salaries)/2)]
        median = median/2
    return median
print("the median of the given array is:", median(salaries))

