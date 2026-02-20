def compress(chars):
    counter_arr = []  # List to store the compressed characters and counts
    if len(chars) == 1:
        # If only one character, return 1 (no compression needed)
        return 1
    else:
        count = 0  # Counter for consecutive repeating characters
        i = 0  # Index for iterating through chars
        # Loop through the list, stopping at the second-to-last character
        while i <= len(chars) - 2:
            if chars[i] == chars[i + 1]:
                # If current and next character are the same, increment count
                count += 1
                i += 1
                # If at the last character, handle the final group
                if i == len(chars) - 1:
                    if count > 9:
                        # If count is more than 9, split into digits
                        count += 1
                        y = [int(d) for d in str(count)]
                        counter_arr.append(chars[i])
                        counter_arr.append(y[0])
                        counter_arr.append(y[1])
                    else:
                        # For count <= 9, just append count+1
                        counter_arr.append(chars[i])
                        counter_arr.append(count + 1)
                        i += 1
            elif count > 0:
                # If a group of repeating characters just ended
                if count > 9:
                    count += 1
                    y = [int(d) for d in str(count)]
                    counter_arr.append(chars[i])
                    counter_arr.append(y)
                    counter_arr.append(y[0])
                    counter_arr.append(y[1])
                else:
                    counter_arr.append(chars[i])
                    counter_arr.append(count + 1)
                    i += 1
                    count = 0  # Reset count for next group
            elif chars[i] != chars[i + 1]:
                # If current and next character are different, move to next
                i += 1
        if not counter_arr:
            # If no compression was possible, return original length
            return len(chars)
    return len(counter_arr)  # Return the length of the compressed array
        

# Example usage
x = ["x", "x", "x", "y", "y", "z", "z", "z", "z", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]
ans = compress(x)
print(ans)  # Output the result of compression