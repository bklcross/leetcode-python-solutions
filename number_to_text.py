def number_to_text(sequence):
    result = ""
    keys = [" ", ".,?!'", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

    # function to find how many repeats
    def count_repeat(val, sequence):
        count = 0
        for j, jal in enumerate(sequence):
            if val == jal:
                count += 1
            else:
                break
        return count

    i = 0

    while i < len(sequence):
        if sequence[i] == ' ':
            count = 0
            i += 1
        
        # get number of repeats
        count = count_repeat(sequence[i], sequence[i::])

        # find key group [][]
        key = keys[int(sequence[i])]

        # convert string to array and get letter using count as index []
        letter = list(key)[count -1]

        # skip repeat index
        i += count
        
        result += letter

    
    return result

sequence = "4433555 555666096667775553"
print(number_to_text(sequence)) 