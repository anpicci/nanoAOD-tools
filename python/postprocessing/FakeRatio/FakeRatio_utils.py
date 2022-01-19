import array

def pytocpptypes(typ):
    if type(typ) == int:
        return "/I"
    elif type(typ) == float:
        return "/F"
    elif type(typ) == str:
        return "/C"
    elif type(typ) == array.array:
        single = pytocpptypes(typ[0])
        return "[" + str(len(typ)) + "]" + single