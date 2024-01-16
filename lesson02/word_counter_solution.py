word = 'the'
s = 'thethethe the the thexthex'
count = 0

# your code here
for i in range(len(s)):
    # we'll calculate the first and last character to match.
    last = i + len(word)
    if s[i:last] == word:
        # we found one! increment the counter.
        count += 1

print('The word "%s" occurs %s times.' % (word, count))
