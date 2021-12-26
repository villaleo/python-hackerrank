if __name__ == '__main__':
    """
    You are given two sets, A and B. 
    Your job is to find whether set A is a subset of set B.
    
    If set A is subset of set B, print True.
    If set A is not a subset of set B, print False.
    
    Further details are provided in the info.pdf file provided within this directory.
    """
    amount_test_cases = int (input ())
    sets = []
    results = []
    for _ in range (amount_test_cases):
        size_of_set_a = int (input ())
        set_a = {int (x) for x in input ().split ()}
        sets.append (set_a)

        size_of_set_b = int (input ())
        set_b = {int (x) for x in input ().split ()}
        sets.append (set_b)

        results.append(set_a.issubset(set_b))

    for val in results:
        print (val)
