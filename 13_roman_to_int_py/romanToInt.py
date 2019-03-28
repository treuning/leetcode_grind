
def romanToInt(s: str) -> int:
    d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    arr = list(s)
    print (arr)
    value = 0
    
    if (len(arr) == 1):
        value = d[arr[0]]
        return value
    else:
        for i in range(len(arr)):
            if (i==0):
                value += d[arr[i]]
            elif (d[arr[i]] < d[arr[i-1]]):
                value += d[arr[i]]
            elif (d[arr[i]] > d[arr[i-1]]):
                value += d[arr[i]] - (d[arr[i-1]]*2) 
            elif (d[arr[i]] == d[arr[i-1]]):
                value += d[arr[i]]
        return abs(value)

i1 = "IIII","IX","XIX","XXI","IV","VII","MMMDCCXXIV",'MCMXCIV'

for i in i1:
    print(romanToInt(i))