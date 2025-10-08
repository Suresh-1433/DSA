def get_reversed_string(string,length,s):
    if length < 0:
        return s
    s=s+string[length]
    return get_reversed_string(string,length-1,s)
    
string = input()
s=""
resultant_string = get_reversed_string(string,len(string)-1,s)
print(resultant_string)