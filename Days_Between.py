def day_per_Month(year):
    if (year%4 == 0 and year%100 != 0) or year %400 ==0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days(date2):
    dayDiff = 0
    date1 = (1, 1, 1)
    dayPerMonth = day_per_Month(date2[0])
    print(dayPerMonth)

    if date2[1] > date1[1]:
        dayDiff += sum(dayPerMonth[date1[1]:date2[1]-1])
        dayDiff += dayPerMonth[date1[1]-1] - date1[2]
        print(dayPerMonth[date1[1]-1])
        dayDiff += date2[2]
    else:
        dayDiff = date2[2] - date1[2]

    dayDiff += int((date2[0]-date1[0])*365) + int((date2[0]-date1[0])/4) - int((date2[0]-date1[0])/100) + int((date2[0]-date1[0])/400)

    return dayDiff

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """

    return abs(days(date1)-days(date2))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    #assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    #assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print(days_diff((7410,4,9), (9884,3,16)))
