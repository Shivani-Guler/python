#def leftrotate(s, d):
#	n = s[d : ] + s[0 : d]
#	return n


#def rightrotate(s, d):
#	return leftrotate(s, len(s) - d)

#str1 = "abcde"
#print(leftrotate(str1, 1))

#str2 = "abcde"
#print(rightrotate(str2, 1))

######
def rotateOnceLeft(s):
    return s[-1]+s[:-1]
#print(rotateOnceLeft("abcde"))

def rotateOnceRight(s):
    return s[1:]+s[0]
#print(rotateOnceRight("abcde"))

# def rotate(s,direction,times):
    
#         if direction=='L':
#             return s[-times:]+s[:-times]
#         elif direction=='R':
#             return s[times:]+s[:times]
    
# print(rotate("abcde",'L',2))
# print(rotate("abcde",'R',2))


# def rotate(s,direction,times):
#     for i in range(times):
#         if direction=='L':
#             s= rotateOnceLeft(s)
#         elif direction=='R':
#             s=rotateOnceRight(s)
#     return s
# print(rotate("abcde",'L',2))
# print(rotate("abcde",'R',2))

def rotate(s,direction,times):
    f=rotateOnceRight if direction=='L' else rotateOnceLeft
    for i in range(times):
        s=f(s)
    return s
print(rotate("abcde",'L',3))
print(rotate("abcde",'R',3))