def ispalindrome(s):
    return s == s[::-1]


s = input("Enter the word: ")
ans = ispalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
