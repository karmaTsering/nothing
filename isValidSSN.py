
def isValidSSN(tmp):
    

    if len(tmp)==11 and tmp[0:3].isdigit() and tmp[3]=='-' and tmp[4:6].isdigit() and tmp[6]=='-' and tmp[7:12].isdigit():
        return True
    else:
        return False
