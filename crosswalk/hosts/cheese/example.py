
# ------------------------------------------------------------------------------
def mul(count):
    """
    This is a re-implementation of the function declared in the
    Standard API of crosswalk. 

    :param count: Number of cycles to multiply by

    :return: Value of multiplication 
    """
    print('Running from cheese')
    counter = 0
    for i in range(count):
        counter *= i
    return counter


# ------------------------------------------------------------------------------
def taste():
    """
    Note - this function is NOT declared in the Standard API. Therefore
    it would not be considered a 'normal' function to call through a 
    cross-api library. However, the dynamic re-routing allows for this
    to be called in a natural way (crosswalk.example.bespoke_mul), but
    care is required if you're copy/pasting code between different 
    interpreters which may not utilise the same host implementation.

    :param count: 
    :return: 
    """
    print('running a function implemented only in cheese')
    return None

