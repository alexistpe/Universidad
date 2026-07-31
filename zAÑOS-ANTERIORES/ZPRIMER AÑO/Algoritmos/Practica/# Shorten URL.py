# Shorten URL.
url = input() # Original URL.
t = len(url) # URL size/length.
b = "" # New string (shortened URL).
c = 0 # Loop counter.
while c < t: 
    if c < (t-1) and url[c] == "/" and url[c+1] == "/": # If it finds the protocol.
        for i in range(t - (c+2)): # Save text without protocol.
            if url[(c+2)+i] == "/": # Stop saving address.
                b = b + url[(c+2)+i]
                break
            b = b + url[(c+2)+i] # Part of what is after the protocol and address.
        c = (c+2) + i
    elif url[c] == "/" and c <= t-1:
        j = c + 1 # Starts from the character.
        while j < t-1 and url[j] != "/": # While it doesn't reach the end or finds /
            j = j + 1 # Traverse URL.

        if j < (t) and url[j] == "/": # If it found something valid.
            for i in range(j-c): # Iterate over valid text.
                b = b + url[c+i+1] # Saves the valid URL part.
        c = j # Continues at the next character after j.
    else:
        c = c + 1
print(b)