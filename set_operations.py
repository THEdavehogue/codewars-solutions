def process_2arrays(arr1, arr2):
    set1, set2 = set(arr1), set(arr2)
    return[len(set1.intersection(set2)), len(set1.symmetric_difference(set2)),
           len(set1.difference(set2)), len(set2.difference(set1))]
