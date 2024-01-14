
count=0
with open('e.txt','r') as f:
    for line in f:
        for word in line.split():
            if word == "love":
                count+=1

    print('love word contain %d ',count)






