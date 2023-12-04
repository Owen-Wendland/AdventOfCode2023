#Day two of 2023 Advent - Owen 
endResult = 0

gameId = 0

redLimit = 12
greenLimit = 13
blueLimit = 14

red = 0
green = 0
blue = 0

def Convert(string):
    string = string.replace(';', ':')
    string = string.replace(' ', ':')
    string = string.replace('\n', ':')
    string = string.replace(',', ':')
    li = list(string.split(":"))
    return li

f = open("DayTwo/dayTwo.txt", "r")
output = 0

for i in f:
    notWork = False
    a = Convert(i)
    
    for b in range(len(a)):
        if(notWork == False):
            if(a[b] == 'blue'):
                if(int(a[b-1]) > blueLimit):
                    notWork = True
                    
            elif(a[b] == 'red'):
                if(int(a[b-1]) > redLimit):
                    notWork = True
                    
            elif(a[b] == 'green'):
                if(int(a[b-1]) > greenLimit):
                    notWork = True
                    
    if(notWork == False):
        output = int(a[1]) + output
        
print(output)

f.close()
quit() 