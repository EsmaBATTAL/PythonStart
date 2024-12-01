def ft_filter(function, iterable):
    result = [item for item in iterable if (function(item) if function else item)]
    print(filter.__doc__)
    return(result)