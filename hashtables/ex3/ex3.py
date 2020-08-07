def intersection(arrays):
    # Prep hash table
    hash_table = {}
    # Loop through arrays
    for array in arrays:
        # Loop through each item in the array
        for i in array:
            # Check if each item is in the hash table
            if i in hash_table:
                # If it is, increment its value
                hash_table[i] += 1
            else:
                # If not, set to 1 to start a running count 
                hash_table[i] = 1
    # Instantiate items with value equal to # of arrays
    results = [i for i in hash_table if hash_table[i]==len(arrays)]
    
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
