#Day two of 2023 Advent - Owen 
endResult = 0

gameId = 0

latestBlue = 0
latestRed = 0
latestGreen = 0


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

f = open("DayTwo/dayTwoPT2.txt", "r")
output = 0

for i in f:
    notWork = False
    a = Convert(i)
    
    for b in range(len(a)):
        
        if(a[b] == 'blue'):
            if(int(a[b-1]) > latestBlue):
                latestBlue = int(a[b-1]) 
                
        if(a[b] == 'red'):
            if(int(a[b-1]) > latestRed):
                latestRed = int(a[b-1])
                
        if(a[b] == 'green'):
            if(int(a[b-1]) > latestGreen):
                latestGreen = int(a[b-1])
                
    output = (latestGreen * latestBlue * latestRed) + output
    latestBlue = 0
    latestRed = 0
    latestGreen = 0
    
    print(output)
        
print(output)

f.close()
quit() 