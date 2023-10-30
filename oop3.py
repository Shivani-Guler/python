# def palindrommableV1(s):      #--efficiency slow----
#     seen=[]
#     for letter in s:
#         if letter in seen:
#             seen.remove(letter)
#         else:
#             seen.append(letter)
#     return len(seen ) in (0,1)
# print(palindrommableV1("aadgg")) 

def getCounts(s):
    d={}
    for letter in s:
        d[letter]=d.get(letter,0)+1
    return d

def palindrommableV2(s):
    countsDict=getCounts(s)
    #print(countsDict)
    odds_count=0
    for letter in countsDict:
        if countsDict[letter]%2:
            odds_count+=1
            if odds_count>1:
                return False
    return True
print(palindrommableV2("aadgg")) 