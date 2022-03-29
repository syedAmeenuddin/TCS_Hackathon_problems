def occ(l,e):
    count = 0
    index = -1
    for i in l:
        index+=1
        if e == i:
            count+=1
        if count ==2:
            return index
    return 0




if __name__=='__main__': 
  lenoflist = int(input())
  li=[]
  intocc=[]
  for i in range(0,lenoflist+1):
      li.append(input())
  for i in range(len(li)):
      intocc.append(int(li[i]))
  ex = intocc[-1]
  intocc=intocc[0:-1]
  out = occ(intocc,ex)
  print(out)