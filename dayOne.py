import time

def decrypt():
    global endResult
    first = False
    firstNum = 0
    secondNum = 0
    
    print("enter code line :: q to exit and finish inputing lines")
    a = input()
    
    if (a == 'q'):
        print(endResult)
        time.sleep(5)
        quit()
        
    for i in range(len(a)):
        
        if(a[i].isnumeric() == True and first == False):
            firstNum = a[i]
            secondNum = a[i]
            first = True
            
        elif(a[i].isnumeric() == True):
            secondNum = a[i]
            
    output = int(firstNum + secondNum)
    endResult = endResult + output
    decrypt() 
decrypt()