
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
            #add the first numeral to value
            if (i==0):
                value += d[arr[i]]
            
            #if the current numeral is less than the previous, add current to total value
            elif (d[arr[i]] < d[arr[i-1]]):
                value += d[arr[i]]

            #if the current numeral is greater than the preceding numeral, multiply the previous value
            # by 2, subtract it from the current value, then add to total value    
            elif (d[arr[i]] > d[arr[i-1]]):
                value += d[arr[i]] - (d[arr[i-1]]*2) 

            #if the current numeral is equal to the previous, add current to total value
            elif (d[arr[i]] == d[arr[i-1]]):
                value += d[arr[i]]
        
        return value

i1 = "IIII","IX","XIX","XXI","IV","VII","MMMDCCXXIV",'MCMXCIV','IIIIV','IIX'

for i in i1:
    print(romanToInt(i))