# Slice function

trial = "reverse this string"
new_trial = trial[::-1]
print(new_trial)


# Recursion

def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:]) + str[0]


str = "reverse me"
reverse = string_reversal(str)
print(reverse)
