# findingn the mean of the array

salaries = [4, 6, 7, 8, 10, 15, 20]
def mean(salaries):
    sum = 0
    for i in salaries:
        sum +=i
        mean = sum/len(salaries)
    return mean
print("The mean of the given array is:",mean(salaries))



