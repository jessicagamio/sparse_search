def sparse(word, str_list, s=0,f=0):
    """return index of word in a list of strings

    >>> str_list=['at','','','ball','','bob','']
    >>> word = 'bob'
    >>> sparse(word, str_list, s=0, f=0)
    5
    """


    # find the length of the list
    list_length= len(str_list)
    f=list_length-1

    # if list has only two items left evaluate items
    if list_length==2:
        if word in str_list[0]:
            return list_length - s

        return (list_length - s) + 1
    # get mid point by dividing list in half
    
    # print('stringlist===>', str_list)
    mid = list_length//2
    # print('mid===>',mid, 'string of mid===>', str_list[mid])


    # check if mid is equal to word
    if str_list[mid] == word:
        print('f-mid  ====>', f-mid)
        return f-mid

    # if not equal to word split to left and right
    else:
        left=str_list[s:mid]
        right=str_list[mid:f+1]

        if word in left:
            sparse(word,left,s,f)

        else:
            s=mid
            sparse(word,right,s,f)






if __name__=="__main__":
    from doctest import testmod
    if testmod().failed==0:
        print("*****Success****")


