def longest_palindrome(s):

    # Reverse the string
    r_s = s[::-1]

    l = len(r_s)
    matches = []

    for i in range(l):
        for j in range(i+1, l):
            if r_s[i:j] in s:
                print(r_s[i:j], len(r_s[i:j]))
                matches.append(len(r_s[i:j]))

    return matches


print(longest_palindrome("a"))
