#There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

#A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

#As a simplification, you may assume that no letter occurs more than once in the secret string.

#You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

# recoverSecret.py


def recoverSecret(triplets):

    secretWord = []
    bufferList = []
    secretStringLen = 0

    # Find the 1st char
    for t in triplets:
        if t[0] not in secretWord: secretWord.append(t[0])
        if t[1] not in bufferList: bufferList.append(t[1])
        if t[2] not in bufferList: bufferList.append(t[2])
    
    # Get the string length 
    secretStringLen = len(bufferList)+1
    
    for validItem in secretWord:
        if validItem not in bufferList: 
            secretWord = []
            secretWord.append(validItem)
            bufferList = []
            break


    # Find the rest of the char by the 1st char    
    while len(secretWord) < secretStringLen:
        for t in triplets:
            if secretWord[-1] in t and secretWord[-1] != t[-1]:
                if t[t.index(secretWord[-1])+1] not in bufferList: bufferList.append(t[t.index(secretWord[-1])+1])
            
        if len(bufferList) == 1: 
            secretWord.append(bufferList[-1])
            bufferList = []   
        else:
            tempList = bufferList[:]
            for nextChar in bufferList:
                for n in triplets:
                    if nextChar in n and nextChar != n[0]:
                        if nextChar == n[2]:
                            if n[1] not in secretWord or n[0] not in secretWord:
                                tempList.remove(nextChar)
                                break
                        if nextChar == n[1]:
                            if n[0] not in secretWord:
                                 tempList.remove(nextChar)
                                 break

            if len(tempList) == 1: 
                secretWord.append(tempList[0])
                bufferList = []
        
    return ''.join(secretWord)
