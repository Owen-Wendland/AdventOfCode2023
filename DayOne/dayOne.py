#Day one of 2023 Advent - Owen 
endResult = 0
first = False
firstNum = 0
secondNum = 0

f = open("DayOne/dayOne.txt", "r")

for a in f:
    for i in range(len(a)):  
        if(a[i].isnumeric() == True and first == False):
            firstNum = a[i]
            secondNum = firstNum
            first = True
        
        elif(a[i].isnumeric()):
            secondNum = a[i]
    
    output = int(firstNum + secondNum)
    endResult = endResult + output
    first = False
    
print(endResult)

f.close()
quit() 