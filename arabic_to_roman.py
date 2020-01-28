def arabic2roman(num):
    #String Builder
    ans = ''

    #Error Check
    if (type(num) != int):
        print('Please use an integer')
        return ans

    if(num == 0 or num > 3999):
        print('Please use a number between 1 - 3999')
        return ans

    # Numeral KV pairs
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    #Pointer starting at first index
    i = 0

    while(num > 0):
        if(num - value[i] >= 0):
            ans += roman[i]
            num = num - value[i]
        else:
            i+=1    

    return ans

