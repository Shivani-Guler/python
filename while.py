#i=0
#while i<50:
 #   print(i)
  #  i+=1

num=int(input("Enter a num"))
end=int(input("Enter end num"))
i=0
while i<end:
    print(f"{num}x{i:>3}={num*i:>5}")
    i+=1