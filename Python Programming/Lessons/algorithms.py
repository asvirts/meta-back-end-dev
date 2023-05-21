# Algorithm for a palindrome checker

def is_Palindrome(pd):
    startOfIndex = 0
    endOfIndex = len(pd) - 1

    for i in pd:
        if pd[startOfIndex] != pd[endOfIndex]:
            return False
        return True


print(is_Palindrome('racecar'))
