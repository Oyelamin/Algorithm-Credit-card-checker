

def luhn(card):
   
    second = 0
    first = 0
    nonTag = 0
    cardObj = card.split()

    for n in cardObj:
        nonTag += (int(n[-1]) + int(n[-3]))
        if len(n) == 4:
            one = int(n[-2]) * 2 #-2
            two = int(n[-4]) * 2  #-4
            
            if one >= 10:
                one = str(one)
                firstVal = int(one[0]) + int(one[1])
                first += firstVal
            elif one <= 9:
                first += one

            if two >= 10:
                two = str(two)
                secondVal = int(two[0]) + int(two[1])
                second += secondVal
              
            elif two <= 9:
                second += two
        else:
            return False

    ftotal = first + second
    total = ftotal + nonTag
    total = str(int(total))
    
    if total[-1] == "0":
        return True
    else:
        return False

#Give value in 4 unit numbers seperated with a whitespace
luhn("1566 5666 6663 6639")
