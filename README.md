# TCS_Hackathon_problems
tcsion hackathon python problems solution 

1.How to create a class

Question 1 :
Create a class Account with the below attributes:
int accntNo
String accntName
int accntBalance

Create a constructor which takes all parameters in the above sequence.


Create a class AccountDemo

Create a default constructor in the AccountDemo class as below

def __init__(self):
pass

Create a method depositAmnt which takes an Account object and amount to be deposited (amount) as input parameters. Update the balance i.e. Add the amount to the existing balance and return the updated balance

Create another method withdrawAmnt which takes an Account object and amount to be deposited (amount) as input parameters. Deduct the amount from the balance and return the updated balance. Minimum balance to be maintained is 1000. i.e if the balance is becoming less than 1000 when deducting the withdrawal amount, the operation need to be stopped with a message "No Adequate balance"


To test the code against your customized Input through console, the input data needs to be entered in the below order( as shown below in the sample input).

The first three lines in the below sample input represents the input for three variables of account object i.e account no. (accntNo),account name (accntName) and account balance (accntBalance), with which the object will be created.

The fourth line in the sample input is the input for the amount to be deposited in the account object and fifth line is the input for the amount to be withdrawn from the account object

Sample input:-
120
Rajesh
1500
1200
2000


Sample output for the above input:-
2700
No Adequate balance

Note:
For more details on
a. Input data entered from standard input
b. How this data is processed
c. The order of the input data

please refer the below main program.

Note:
Please request you to use the below main program to test/run your code and submit this main along with your solution.
Dont write separate main function again on your own.

if __name__ == '__main__':
acno=int(input())
acname=raw_input()
acntbal=int(input())
depamnt=int(input())
withamnt=int(input())
acnt=Account(acno,acname,acntbal)
acntdemoobj=AccountDemo()
print(acntdemoobj.depositAmnt(acnt,depamnt))
print(acntdemoobj.withdrawAmnt(acnt,withamnt))
_____________________________________________________________________________________

2.palindrome
Create a function with the name check_palindrome which takes a list of strings as input. The function checks each string of the list whether it is a palindrome or not and returns another list containing the palindrome from the input string.

Note:

i. A palindrome is a a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam
ii. The check for the string to be palindrome should be case-insensitive , e.g. madam and Madam both should be considered as palindrome.
You can use the below sample input and output to verify your solution.

Sample Input:
3
Hello
Malayalam
Radar

Output:

Malayalam
Radar

The first line in the sample input is the count of strings to be included in the list as the 1st input.
The strings are then provided one by one as the next lines of input.
For more details, please refer to the below main section of code
You can use the below sample main section to test your code.

Sample Main Method:
if __name__=='__main__': count=int(input()) inp_str=[] for i in range(count): inp_str.append(input()) output=check_palindrome(inp_str) if len(output)!=0: for i in output: print(i) else: print('No palindrome found')
______________________________________________________________________________________

3.def find_Novowels
Create a function with the name find_Novowels which takes a list of strings as input. The function checks each string of the list whether it has at least one vowel or not and returns another list containing the strings not having any vowel.

Note:
The check for the vowel should be case-insensitive .
You can use the below sample input and output to verify your solution.

Sample Input:

4
almost
vtyw
sound
prtwy

Output:
Strings without vowels:
vtyw
prtwy


The first line in the sample input is the count of strings to be included in the list to be passed to the method find_Novowels .
The strings are then provided one by one as the next lines of input.
For more details, please refer to the below main section of code
You can use the below sample main section to test your code.

Sample Main Method:
if __name__=='__main__': count=int(input()) inp_str=[] for i in range(count): inp_str.append(input()) output=find_Novowels(inp_str) if len(output)!=0: print('Strings without vowels:') for i in output: print(i) else: print('No string found')
_____________________________________________________________________________________
4.def  check_prime

create a function with the name check_prime which takes a number as input and checks if the given number is prime or composite. The function returns 1 if the number is prime,0 if the number is composite and 0 otherwise.

create another function with the name prime_composite_list which takes a list of numbers and checks whether the numbers in the list are prime or composite. Include all th prime numbers in one list and all the composite numbers in another list. Create a 3rd list and include the list of prime numbers and the list of composite numbers in the 3rd list and return the 3rd list from this function. The third list should be a list of lists.

Note : use the function check_prime to find whether the number is prime or composite.

To test the code against your customized Input through console, please refer to the below instructions

The first line in the sample input is the count of numbers to be provided in the input list
The next few lines are the numbers to be included in the list provided one by one

Sample Input :
4
11
7
90
44

Expected Output :

[[11, 7], [90, 44]]


Please use the below main program code to implement and to test/run your code and submit the complete code along with this main code.

if __name__=='__main__':
inp=[]
count=int(input())
for i in range(count):
inp.append(int(input()))
print(check_prime(inp[1]))
result=prime_composite_list(inp)
print(result)

Note: Request you to very carefully check the indentation of your code in the console before submitting. Some times while pesting the code copied from the debugger gets distorted in the console. In that case you have to modify the indentation as per Python syntax.
_____________________________________________________________________________________
5.def occ(l,e)

Write a Python program to find the position of the second occurrence of a given number in a given list of numbers.
Function will take as input a list of numbers as first argument and a numeric variable as second argument . This function should return the index where the given variable value occurs in the list for the second time

Function signature:
getIndex(listOfIntegers,NumericVariable):

In the above function signature, First argument represents list of integer values and
Second argument represents a number, whose second occurred position(index) to be returned.
The function should return the index of the number(supplied as second argument), occurred for the second time in the list.

If the number does not occur for the second time in the input list or If the number does not exist in the list then the function should return 0.

Develop a main program , with below sequence of actions:

a. Create an empty list .
b. Read the size of the list from standard input
c. Based on the size of the list read above, repeat reading and adding the elements to the list created.
d. Read the number, whose index is to be searched for its second occurrence .
e. Then call getIndex function by supplying the input list as first argument and numeric value ( whose index is to be searched for its second occurrence) as second argument.
Function should return the index of the second occurrence of the number(whose value supplied as second argument to the main program through numeric variable)
Finally print the returned value of the function.

Look at the Sample testcase below for more clarity to write the input and output statements in the main section.

1.Sample Testcase1#:
Let us assume to create a list with 5 elements (3,4,3,7,4) and
to search for the index of the second occurrence of 3 in the list

Input :

5
3
4
3
7
4
3

Output:
2

Desctription:
In the above Input, the first line content(5) represents the number of elements in the list, to be created
From Second line to 6th line represents the 5 elements as below and to be added to the list created.
3
4
3
7
4

The last line content (3) represents the number to search for its second occurance position(Index)
in the input list

Output is 2 means, the element 3 is found second time at the index value 2 , in the given input list.


2.Sample Testcase#2:
Input:
4
2
3
4
5
5
Output:
0

Desctription:
In the above Sample Input, the first line content(4) represents the number of elements in the list, to be created
From Second line to 5th line represents the 4 elements as below and to be added to the list created.
2
3
4
5
The last line content (5) represents the number to search for its second occurance position(Index) in the input list

Output is 0 means, the element 5 is not found second time in the input list .
_____________________________________________________________________________________

6.#During the COVID19 pandemic, the status of beds availability is to be tracked

Create a class City with the below attributes:
city_id of type Number
state_name of type String
city_name of type String
covidbeds of type Number
avlblcovbeds of type Number
ventilbeds of type Number
avlblventilbeds of type Number


Attribute description:
city_id represents Unique ID for the city
state_name represents the state name
city_name represents the city name
'101', 'Delhi', 'Delhi', '100000', '20000', '5000', '2000', 
'102', 'Telangana', 'Hyderabad', '200000', '40000', '1000', '500',
'103', 'Telangana', 'Warangal', '100000', '30000', '2000', '1000',
'104', 'AndhraPradesh', 'Vijayawada', '800000', '300000', '30000', '2500',
'105', 'AndhraPradesh','Vizag','500000','100000','6000','1000','AndhraPradesh'


question :
During the COVID19 pandemic, the status of beds availability is to be tracked

Create a class City with the below attributes:
city_id of type Number
state_name of type String
city_name of type String
covidbeds of type Number
avlblcovbeds of type Number
ventilbeds of type Number
avlblventilbeds of type Number


Attribute description:
city_id represents Unique ID for the city
state_name represents the state name
city_name represents the city name

covidbeds represents the total covid beds in the city
avlblcovbeds represents the total available covid beds in the city
ventilbeds represents the total ventilator beds in the city
avlblventilbeds represents the total available ventilator beds in the city


Create the __init__ method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values .

Create another class CovBedsAnalysis with the below attributes:
analysis_name of type String
city_list of type List having city objects

Create the __init__ method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values inside the method.

Create another method inside the class with the name get_StateWiseAvlblBedStats

This method is used to find the state wise available covid beds and available ventilator beds and returns a list of tuples with State name,total available covid beds and total available ventilator beds for each state, sorted by state name.


Note: A state contains multiple cities. Total number of available beds for a respective category (covid or ventilator beds) in a state is the sum of the available beds of all the cities in that state for the respective category(covid or ventilator). Refer testcase output for more clarity.


Create another method with the name get_CiitesWithMoreThanAvgOccupiedbeds, which takes state as argument and returns the dictionary with city as the key and tuple of occupied covid beds and occupied ventilator beds as value, where number of covid beds occupied and ventilator beds occupied are more than the state average for the respective category of beds .


i.e. the City(cities) in the given state to be recorded/resulted( with the data mentioned), should satisfy the below conditions:

Whose occupied covid beds count is more than the "average of Occupied covid beds of all the cities of the given state" and the respective City should also contain the Occupied ventilator beds count more than the "average of occupied ventilator beds of all cities of the given state".

For more clarity , please refer the Sample test case Input and Output in below section

If no city is found with the occupied beds more than state average as mentioned above, then return None and display ‘No city available' (Without quotes) in main function.


Please note that the search operations(if any as per the requirement ..) should be case insensitive.

Instructions to write main function:

Instructions to write main section of the code
a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence.
c. Create the respective objects(City and CovBedsAnalysis ) with the given sequence of arguments to fulfill the __init__ method requirement defined in the respective classes referring to the below instructions.

i. Create a City object after reading the data related to it and add the object to the list of city objects which will be provided to the CovBedsAnalysis object while creation.
This point repeats for the number of city objects(considered in the first line of input data) .

ii. Create CovBedsAnalysis object by passing the CovBedsAnalysis name(you can hard-code any name you want) and List of city objects ( created as mentioned in above
point# c.i ) as the arguments.
d. Take a string value as input depicting the state which is passed to the get_CiitesWithMoreThanAvgOccupiedbeds
e. Call the method get_StateWiseAvlblBedStats mentioned above from the main section.
f. Display the State,total available covid beds and total available ventilator beds received from the method, with a single space in between as shown in sample testcase output,
g. Call the method get_CiitesWithMoreThanAvgOccupiedbeds mentioned above from the main section
h. Display the city name, occupied covid beds and occupied ventilator beds with a single space in between as shown in the sample testcase output.
I. If None is returned by the method get_CiitesWithMoreThanAvgOccupiedbeds, display the message ‘No city available' (excluding the quotes).


You can use/refer the below given sample input and output to verify your solution using ' Test against Custom Input ' option in Hackerrank.


Input format for Custom Testing:

a.The 1st input taken in the main section is the number of city objects to be added to the list of cities.
b.The next set of inputs are the values for the attribtes: city_id,state_name,city_name, covidbeds,avlblcovbeds,ventilbeds,avlblventilbeds respectively for each city taken one after other and is repeated for number of objects given in the first line of testcase input
c.The last line of input refers the state name which is passed to the function: get_CiitesWithMoreThanAvgOccupiedbeds



____________________________________________________________________________________________________________________________________________________


7. Question 1 :
Blood Bank – Donate blood and Save life

Problem statement:

Many of us know the importance of blood availaibility at critical condictions in case of an accident or long run diseases. To keep track of blood donors , blood group wise , an NGO want to go automate the donor identification process with an application with the below requirements


Develop a class Donor with the below attributes

ID of numeric type
Name of string type
Contact Number of numeric type of 10 digits
Bloodgroup of String type
PrevDonatedMon of string type of 3 characters(first 3 characters of the month name) , which represents the month in which the donor donated the blood recently.

AwayFrom of type Numberic representing distance in KM from the centralized point of the city from where the application/program is running.

Note:

Assume that the input month to be recorded for the attribute: PrevDonatedMon ,should fall into the range of Jan to Nov of current year (2020) only.

Implement a __init__ method to initialize the attributes from the main function

Develop BloodBank class with the below attributes
Name of string type
ListOfDonors of list of Donor objects
Implement a __init__ method to initialize the attributes from the main function

Implement a function: getListofAvailableDonors():

Which will return a sorted dictionary of Bloodgroup wise counts in the ascending order of blood group

i.e. BloodGroup and Count as the key:value pairs based on the Donors in the ListOfDonors ,who satisfied with the below two conditions:

The conditions for a Donor, to be considered as available:

1. For any Donor , If there is a minimum of 4 months gap between the 'previously donated month' and current month.
2. The Donor should be with in 50 kms range(AwayFrom attribute represents this value) from the centralized point of the city from where the application/program is running.


Two conditions,above should be satisfied for a Donor to consider as available for donating.


The above two conditions section referred multiple places in the Question. To avoid repetitive statements, we mentioned the conditions at one place, i.e. here above and referred the same in couple of places below. Please make a note of it.


Note2: Please note that to fulfill the requirement, this function would be called twice, before and after calling the function : getAndUpdateDonor (from main),

to know the status of available donors,bloodgroup wise before and after fulfilling the donors request.

Refer the Sample testcase input for any input or attributes format and output or output format for more clarity.

Implement another function : getAndUpdateDonor() which takes two parameters i.e. blood group and required donor count and return a True or False as per the below requirements:


Case1. For the given blood group,

If the required donor count more than the available count of donors( who satisfies the conditions mentioned in the above section: " The conditions for a Donor, to be considered as available") , then the method will update the PrevDonatedMon of all the available Donors of the given blood group with the current month in the list of donor objects (of BloodBank ) and rerutns False


Case2. For the given blood group,

If the required donor count is less than or equals to the available count of donors( who satisfies the conditions mentioned in the above section: " The conditions for a Donor, to be considered as available" ), then this method considers the first available donors of the given blood group from the input ListOfDonors (of Bloodbank class) for donation and update the PrevDonatedMon attribute of the donors , considered for donation with current month and returns True.


'i.e. If 5 donors are available with the given conditions(mentoned above # a, b), and the required donors are only 3, then the method will consider the first 3 donors as per the input order from the ListOfDonors and update their previous Donated month with the current month

Instructions to write main section of the code

Instructions to write main:

a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence.
c. Create the respective objects( Donor and BloodBank) with the given sequence of arguments to fulfill the __init__ method requirement defined in the respective classes referring to the below instructions.

i. Create a Donor object after reading the data related to it and add the object to the list of Donor objects which will be provided to the BloodBank object. This point repeats for the number of Donor objects(considered in the first line of testcase input) .

ii. Create BloodBank object by passing the BloodBank name(you can hard-code any name you want)and List of Donor objects ( created as mentioned in above point# c.i ) as the arguments.

d. Take a string value for blood group parameter and integer for required donor count, which are to be passed to getAndUpdateDonor function.
e. Call the method getListofAvailableDonors from the main section and Display the Blood group and "count of donors available for the respective bloodgroup" from the resultant dictionary(returned by the getListofAvailableDonors ) with a single space between them.
f. Call the method getAndUpdateDonor with the blood group and count of required donors ,read in point#d from the main section.
h. Display the message "Donor count available" (excluding the quotes) . If the method getAndUpdateDonor returns True and

If False is returned , then display the message ‘Donor count not available' (excluding the quotes).

j. Call the getListofAvailableDonors method again to get the updated available list of donors(satisfies the conditions mentioned for a donor to consider as available)
k. Display the Blood group and "count of donors available for the respective bloodgroup" from the resultant dictionary(returned by the getListofAvailableDonors )

with a single space between them.


Note: Refer testcase input and output for more clarity on input/ouput and their formats.

You can use/refer the below given sample input and output to verify your solution using ' Test against Custom Input ' option in Hackerrank.



Input Format for Custom Testing

a.The 1st input taken in the main section is the number of Donor objects to be added to the list of donors.
b.The next set of inputs are the

DonorID
DonorName
DonorContactNumber
DonorBloodgroup
PrevDonatedMon

AwayFrom

and these input values repeated for number of objects given in the first line of test case input.

c. The last but one and last input of inputs are Bloodgroup and required count of Donors which are to be passed to the getAndUpdateDonor


Sample Testcase 1:

Input:
5
101
AAA
9010101010
A-Positive
May
5
102
BBB
9011101010
B-Positive
Jun
45
103
CCC
9111101010
O-Positive
Jul
49
104
DDD
9111101110
O-Positive
Jan
43
105
DDD
9111101110
AB-Negative
Nov
65
O-Positive
2
Testcase Output:

A-Positive 1
AB-Negative 0
B-Positive 1
O-Positive 2
Donor count available
A-Positive 1
AB-Negative 0
B-Positive 1
O-Positive 0


Explanation:

a.The first four lines represents blood group wise available count of donors (who satisfies the conditions mentioned in the section: " The conditions for a Donor, to be considered as available" in the Question text ,above)

b. 5th line represents the count of donors required is less than the available count of donors(who satisfies the conditions mentioned in the section: " The conditions for a Donor, to be considered as available" in the Question text ,above)

c. 6th to 9th line represents the updated current available donors count , bloodgroup wise after considering the donors request for "2 in count for O-Positive" .

Hence current O-Positive counts is 0 after donating the O-Positive blood, for 2 in count and remaining bloodgroup donor counts remains intact.


____________________________________________________________________________________________________________________________________________________

8.
