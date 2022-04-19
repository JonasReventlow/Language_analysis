def repeat(word, number):
    """(str, int) -> str
    returns string repeated number of times;
    >>> 'hvilket ord skal gentages: abe
    >>> antal gentagelser: 2
    """

    return(word * number)

result = repeat(word, number)


word = input('hvad er dit ord:')
number = int(input('hvor mange gentagelser:'))

print (result)



