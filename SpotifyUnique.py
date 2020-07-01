arr="If you want to jumpstart the process of talking to us about this role, here’s a little challenge: write a program that outputs the largest unique set of characters that can be removed from this paragraph without letting its length drop below 50."
count=0
arr2=set()
for a in arr:
    if a not in arr2:
        count=+1
    arr2.add(a)
if len(arr2)<50:
    arr4=list(arr2)
    for i in range (0,50-len(arr2)):
        arr4.append(" ")
    print(arr4)
    print(len(arr4))
    print("Unique String: "+"\""+''.join(arr4)+"\"")
