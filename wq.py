def ConvertTolower(readstring):
    newstring = readstring.lower()
    newlist = list(newstring)
    return newlist

def removecharacters(stringchara):
    special = [" ",",","?","!","/",".",";"]
    for character in special:
        if character in stringchara:
            stringchara.remove(character)
    return stringchara

def palcheck(stringpal):
    rev = stringpal[::-1]
    if rev == stringpal:
        return "palindrome"
    else:
        return "not palindrome"
    
def main():
    inputstring=input("\nenter a string:")
    llist = ConvertTolower(inputstring)
    clist = removecharacters(llist)
    print (palcheck(clist))
main()

