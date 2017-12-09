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
