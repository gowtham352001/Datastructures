def palindrome(str,n,i):
    if i >= n/2:
        return True
    if str[i] != str[n-i-1]:
        return False
    i = i+1
    return palindrome(str,n,i+1)
string = "MADAMA"
length = len(string)
result = palindrome(string,length,0)
print(result)

    
    