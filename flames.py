p1=input("\nEnter the first player name:")
p2=input("\nEnter the second player name:")
p3=p2
p2=list(p2)
count=0
for i in p1:
    if i in p2:
        count+=1
        p2.remove(i)

round=len(p1)+len(p2)-count

list=['F','L','A','M','E','S']
id=0
number=len(list)
while len(list)>1:
    for i in range(round):
        id+=1
        if id >len(list):
            id=1
    list.remove(list[id-1])
    id-=1


if list[0]=='F':
    print(f"\n{p1} and {p3} relationship status is Friend!!!\n")
if list[0]=='L':
    print(f"\n{p1} and {p3} Your relationship status is Love!!!\n")
if list[0]=='A':
    print(f"\n{p1} and {p3} Your relationship status is Affectionate!!!\n")
if list[0]=='M':
    print(f"\n{p1} and {p3} Your relationship status is Marriage!!!\n")
if list[0]=='E':
    print(f"\n{p1} and {p3} Your relationship status is Enemy!!!\n")
if list[0]=='S':
    print(f"\n{p1} and {p3} Your relationship status is Sister!!!\n")


