# list differences

def list_diff(list1: str, list2: str) -> dict:
    """This function takes two lists and returns a dictionary containing the unique elements of list1, the unique elements of list2, and the common elements between list1 and list2.
    
    Args:
        list1 (list): the first list to compare
        list2 (list): the second list to compare

    Returns:
        Dictionary: a dictionary containing the unique elements of list1, the unique elements of list2, and the common elements between list1 and list2
    """
    
    if not isinstance(list1, list):
        raise TypeError("list1 must be a list")
    if not isinstance(list2, list):
        raise TypeError("list2 must be a list")
    
    unq_list1 = list(set(list1) - set(list2))
    unq_list2 = list(set(list2) - set(list1))
    common = list(set(list1).intersection(set(list2)))
    
    return {"list1Unq": unq_list1, "list2Unq": unq_list2, "common": common}


