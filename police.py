def countThieves(s):
    caught,not_caught=0,0
    for i,c in enumerate(s):
        if c=='T':
            if s[i-1]=='P' or s[i+1]=='P':
                caught+=1
            else:
                not_caught+=1
    return caught,not_caught

print(countThieves('PPTPTTPPTPPTTTP'))


