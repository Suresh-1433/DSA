def is_palindrome(string,s,length):
    if length < 0:
        return s
    x = string[length].lower() 
    s = s+ x
    return is_palindrome(string,s,length-1)

string = input()
s = ""
is_true = is_palindrome(string,s,len(string)-1)
if is_true == string.lower():
    print(True)
else:
    print(False)
