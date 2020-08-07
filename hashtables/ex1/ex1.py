def get_indices_of_item_weights(weights, length, limit):
    # Prep hash table
    hash_table = {}
    # Loop through list the size of length
    for i in range(length):
        # Find the target weights by subtracting individual weights from limit
        target = limit - weights[i]
        # print(target)
        # Check if the target weight is in the hash table
        if target in hash_table:
            # If it is, instantiate target weight from the hash table
            tw = hash_table[target]
            # Instaniate list to hold corresponding keys
            target_list = [i, tw]
            return target_list
        # If target weight is not in hash table
        else:
            # Save the weight to the hash table; {weight, index}
            hash_table[weights[i]] = i
    return None

if __name__ == "__main__":
    # weights_3 = [4, 6, 10, 15, 16]
    # print(get_indices_of_item_weights(weights_3, 5, 21))

    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    print(get_indices_of_item_weights(weights_4, 9, 7))