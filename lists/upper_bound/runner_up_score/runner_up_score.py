def solution ():
    """
    Given the participants' score-sheet for your University Sports Day, you are required
    to find the runner-up score. You are given n scores. Store them in a list and find
    the score of the runner-up.
    
    Note: The first line contains n. The second line contains an array A[] of n integers
    each separated by a space.
    
    Further details are provided in the info.pdf file provided within this directory.
    """
    n = int (input ())
    arr = list (map (int, input ().split ()))
    arr.sort ()
    arr.reverse ()

    i = 0
    current = arr[0]
    while arr[i] == current:
        i += 1
    print (arr[i])
