# It returns True if pattern is found in the text, otherwise False.
def naive(text, pattern, length_text, length_pattern):
    if length_text<length_pattern:
        return False
    for i in range(length_text-length_pattern):
        x = i
        for j in range(length_pattern):
            if pattern[j]==text[x]:
                x+=1
            else:
                break
        if x-i==length_pattern:
            return True
    return False

# It returns the index number where the pattern is found, otherwise -1.
def naive_index(text, pattern, length_text, length_pattern):
    if length_text<length_pattern:
        return -1
    for i in range(length_text-length_pattern):
        x = i
        for j in range(length_pattern):
            if pattern[j]==text[x]:
                x+=1
            else:
                break
        if x-i==length_pattern:
            return i
    return -1
        
# It returns the number of times the pattern is present in the text.
def naive_times(text, pattern, length_text, length_pattern):
    if length_text<length_pattern:
        return 0
    count = 0
    for i in range(length_text-length_pattern):
        x = i
        for j in range(length_pattern):
            if pattern[j]==text[x]:
                x+=1
            else:
                break
        if x-i==length_pattern:
            count+=1
    return count

# It returns the number of times the pattern is present in the text.
def rabin_karp(text, pattern, length_text, length_pattern):
    mod = 11
    if length_text<length_pattern:
        return 0
    p = int(psttern)%mod
    for i in range(length_text - length_pattern):
        if int(text[i:i+length_pattern])%mod == p:
            flag = 1
            for j in range(length_pattern):
                if text[i+j] != pattern[j]:
                    flag = -1
                    break
            if flag==1:
                return i
    return -1

#It returns index number if pattern is found, otherwise returns -1.
def boyer_moore(text, pattern, length_text, length_pattern):
    lookup = [0]*150

    for i in range(length_pattern-1, -1, -1):
        lookup[ord(pattern[i])] = max(lookup[ord(pattern[i])], i)

    for j in range(length_text-1, -1, -1):
        if lookup[ord(text[j])] == 0:
            lookup[ord(text[j])] = -1

    i = j = length_pattern - 1

    while i<length_text:
        if pattern[j] == text[i]:
            if j==0:
                return i
            else:
                i-=1
                j-=1
        else:
            i = i + length_pattern - min(j, 1+lookup([ord(text[i])]))
            j = length_pattern - 1
    return -1




























    
