def NULL_not_found(object: any) -> int:
    if object == 0  and type(object) == int :
        print("Zero:", object, type(object))
    elif isinstance(object, float) and object != object :
        print("Cheese:", object, type(object))
    elif object == '' :
        print("Empty:", object, type(object))
    elif object == False :
        print("Fake:", object, type(object))
    elif object == None :
        print("Nothing:", object, type(object))
    else :
        print("Type not found")
        return (1)
    return (0)