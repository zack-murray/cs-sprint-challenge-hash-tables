def has_negatives(a):
    # Prep hash table and empty list to store results
    hash_table = {}
    result = []

    # Loop through items in array
    for i in a:
        # Keep running count; {item, count}
        hash_table[i] = 1

        # If items count doesn't equal zero and it's negative counter-part
        # exists in the hash table
        if i != 0 and -i in hash_table:
            # Append positive items to result list
            result.append(abs(i))
            

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
