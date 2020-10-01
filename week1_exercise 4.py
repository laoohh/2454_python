fullName      = "Bob Jones"
spacePosition = fullName.find(" ")
startPosition = spacePosition
endPosition   = len(fullName)
lastName     = fullName[startPosition:endPosition]
print(lastName)
