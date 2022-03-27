def find_Novowels(inp_str):
    result=[]
    b='aeiou'
    for i in inp_str:
        j=i.lower()
        if len(set(j)&set(b))==0:
            result.append(i)
    return result
    
  
   

if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
    output=find_Novowels(inp_str)
    if len(output)!=0:
        print('Strings without vowels:')
        for i in output:
            print(i)
    else:
        print('No string found')
# inp_str= [ 'almost',
# 'vtyw',
# 'sound',
# 'prtwy'];
# output=find_Novowels(inp_str)
# if len(output)!=0:
#     print('Strings without vowels:')
#     for i in output:
#         print(i)
# else:
#     print('No string found')