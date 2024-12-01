def ft_filter(function, iterable):
    result = []
    try:

        for item in iterable:
            if  function(item):
                    result.append(item)
        print(filter.__doc__)
        return(result)
    except Exception as e:
        print(f"{e}")