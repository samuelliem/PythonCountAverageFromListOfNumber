#Program to input number in a list and know the average of the list
#Making a list
numberList = list()

#Iterate for input a value (number) in a list
while True:
    stillWant = input ("Want insert number? (y/n) = ")
    if stillWant == "y":
        insertnum = input("Insert number = ")
        value = float(insertnum)
        numberList.append(value)
    #User input n to stop inserting number
    else:
        break

#Use try-except to avoid an error that make program crash
#Count average from a list
try:
    average = sum(numberList) / len(numberList)
    print("Average from list ", numberList, " is = ", average)
except Exception as e:
    print("Error = ", e)
