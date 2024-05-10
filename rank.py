"""
برنامه گرفتن 4 نمره 4 درس هر نفر و تعیین رتبه و معدل وی(برای 5 دانش اموز) 
"""
name =[]
score=[]
mean =[]
rank = []
for i in range(0,5):
    i=input("please enter name =")
    name.append(i)
for j in range(0,len(name)):
    print(name[j])
    a = float(input("please enter score a ="))
    score.append(a)
    b = float(input("please enter score b ="))
    score.append(b)
    c = float(input("please enter score c ="))
    score.append(c)
    d = float(input("please enter score d ="))
    score.append(d)
    m = (a+b+c+d)/4
    mean.append(m)
    rank.append(m)
print("name =",name)
print("score =",score)
print("mean =",mean)
for k in range(0,len(rank)):
    for z in range(0,len(rank)-k-1):
        if rank[z]<rank[z+1]:
            j = rank[z]
            rank[z]=rank[z+1]
            rank[z+1]=j
print('rank is ',rank)
while (1):
    c = input("please enter name?")
    print(c)
    b = name.index(c)
    for q in range (b*4,(b*4)+4):
        print(score[q])
    print("mean is",mean[b])
    h = mean[b]
    print("rank is", rank.index(h)+1)