

def threeConsecutiveOdds(arr):
    count = 0
    for i in arr:
        if i % 2 == 1:
            count +=1
        elif count == 3:
            return True
        else:
            count = 0
    return count >= 3

print(threeConsecutiveOdds([424,915,193,591,923]))