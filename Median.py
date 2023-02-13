# to find the median of the given array
salaries = [41, 52, 85, 10, 15, 20, 25, 30, 35, 40]
def median(salaries):
    salaries.sort()
    if len(salaries) % 2 != 0:
        median = salaries[int(len(salaries)/2)]
    else:
        median = salaries[(int(len(salaries)/2)) - 1] + salaries[int(len(salaries)/2)]
        median = median/2
    return median
print("the median of the given array is:", median(salaries))