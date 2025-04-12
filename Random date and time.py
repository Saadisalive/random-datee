import random
import time

def getRandomDate(starDate, endDate):
    print("Printing random date between",starDate, "and",endDate)
    randomGenerater = random.random()
    dateFormate = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(starDate, dateFormate))
    endTime = time.mktime(time.strptime(endDate, dateFormate))

    randomTime = startTime + randomGenerater * (endTime - startTime)
    randomDate = time.strftime(dateFormate, time.localtime(randomTime))
    return randomDate
#display rsult
print("Random Date = ",getRandomDate("1/1/2016","12/12/2018"))
