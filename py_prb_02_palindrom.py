def check_palindrome(int_str):
	result=[]
	for i in int_str:
		j=i;
		if type(i)!=int:
			j=i.lower()

		if j==j[::-1]:
			result.append(i)
	return result

#Sample main section.  

#Do not remove the below portion of code.  

if __name__=='__main__': 

        count=int(input()) 

        inp_str=[] 

        for i in range(count):
			
                inp_str.append(input()) 
output=check_palindrome(inp_str) 

if len(output)!=0: 
    for i in output: 
        print(i) 

    else: 

        print('No palindrome found')