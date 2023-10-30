plant_height=0
days=0
climb_rate=10
slide_rate=5
pos=0
#while pos<=plant_height:
   # days+=1
   # pos+=climb_rate
    #if pos>=plant_height:
     #   break
    #pos-=slide_rate
#print(days)

#while True:
 #   days+=1
  #  pos+=climb_rate
   # if pos>=plant_height:
    #    break
    #pos-=slide_rate
#print(days)

top_reached=False
while not top_reached:
    days+=1
    pos+=climb_rate
    if pos>=plant_height:
        top_reached=True
    pos-=slide_rate
print(days) 