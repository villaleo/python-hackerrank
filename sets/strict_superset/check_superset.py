if __name__ == '__main__':
    """
    You are given a set A and n other sets. 
    Your job is to find whether set A is a strict superset of each of the n sets.
    Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
    A strict superset has at least one element that does not exist in its subset.
    
    Further details are provided in the info.pdf file provided within this directory.
    """


    def is_strict_superset (source: set, other_set: set) -> bool:
        for item in other_set:
            if item not in source:
                return False
        return source != other_set


    set_a = {int (x) for x in input ().split ()}
    amount_other_sets = int (input ())
    other_sets = []

    for _ in range (amount_other_sets):
        other_sets.append ({int (x) for x in input ().split ()})

    result = True
    for data in other_sets:
        if not is_strict_superset (source=set_a, other_set=data):
            result = False
            break

    print (result)
