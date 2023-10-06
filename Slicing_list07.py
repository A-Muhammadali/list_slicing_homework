def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    if n>0:
        return list1[0]+list1[n::n]
    else:
        return list1[n::n]
print(main(['a', 1, 'b', 2, 'c', 3, 'd', 4],2))