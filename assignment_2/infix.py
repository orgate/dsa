#############################################################################################################
#																											#
#	Title			:	Infix notation to RPN or postfix notation											#
#	Author			:	Alfred Ajay Aureate R																#
#	Roll No			:	EE10B052																			#
#	Course			:	EE4371 - Data Structures and Algorithms												#
#	Assignment No	:	2																					#
#																											#
#############################################################################################################


import sys

# Class used for stack related operations
class stackclass:

	# The actual stack used is initiated
	# below

	stack = []


	# This function initializes the stack
	# when class is initiated
	# The syntax is in-built in Python

	def __init__(self):
		self.stack = []


	# This function gives the length of the
	# stack when length of class is called
	# The syntax is in-built in Python

	def __len__(self):
		return len(self.stack)


	# This function gets a particular item
	# from the stack based on the index given
	# The syntax is in-built in Python

#	def __getitem__(self,index):
#		return self.stack[index]


	# This function pushes an element to the
	# top or the end of stack

	def stack_push(self,element):
		self.stack.append(element)
		return self.stack


	# This function pops the top or the last
	# element from the stack

	def stack_pop(self):	
		return self.stack.pop()


# This function checks whether the given string
# could be converted to a floating point number
# or not

def float_check(value):
		try:
			float(value)
			return True
		except ValueError:
			return False











def in2post(input_list,k):

	# This declares the stack class

	stck = stackclass()

	outputlist = []

	err_flag = 0

	# This loop runs for all the parsed symbols
	# or numbers stored in stck_list until all
	# of them are read or until it finds an error

#	print k," ",input_list

#	while ((k<len(input_list))&(input_list[k]!=')')):
	while k<len(input_list):
#		print "inside while "
#		print "len of stck",len(stck)
#		print "input_list[k] is ",input_list[k]
		if (input_list[k]==')'):
			if len(outputlist)==0:
				err_flag=1
			else:
				while len(stck)>0:
					outputlist.append(stck.stack_pop())
				return outputlist,k
		elif (input_list[k]=='('):
			in2post_out = in2post(input_list,k+1)
			l=0
			temp = []
			while l<len(in2post_out[0]):
				temp.append(in2post_out[0][l])
				l+=1
			m=0
			while m<len(temp):
				outputlist.append(temp[m])
				m+=1
#			outputlist.append()
			k = in2post_out[1]
		elif (len(stck)==0)&((input_list[k]=='+')|(input_list[k]=='-')|(input_list[k]=='*')|(input_list[k]=='/')|(input_list[k]=='^')|(input_list[k]=='sqrt')|(input_list[k]=='u-')|(input_list[k][0]=='-')):
#			print "why else "
			if ((input_list[k]=='-')|(input_list[k][0]=='-'))&(k==0):
				stck.stack_push('u-')
			else:
				stck.stack_push(input_list[k])
#			print "+ is pushed ",input_list[k]
		elif input_list[k]=='+':

#			temp = stck.stack_pop()			

#			if len(stck)>=1:
#				temp = stck.stack_pop()			
#			else:
#				temp = ''
			temp = stck.stack_pop()			
			outputlist.append(temp)
			if (temp=='+')|(temp=='-'):
				stck.stack_push(outputlist.pop())
				stck.stack_push('+')
			else:
				stck.stack_push('+')
				while (temp!='+')&(temp!='-')&(len(stck)>=1):
					temp = stck.stack_pop()
					outputlist.append(temp)
				stck.stack_push(outputlist.pop())

		elif (input_list[k]=='-')&(input_list[k-1]!='+')&(input_list[k-1]!='-')&(input_list[k-1]!='*')&(input_list[k-1]!='/')&(input_list[k-1]!='^')&(input_list[k-1]!='sqrt')&(input_list[k-1]!='u-')&(k>0):
			temp = stck.stack_pop()			
			outputlist.append(temp)
			if (temp=='+')|(temp=='-'):
				stck.stack_push(outputlist.pop())
				stck.stack_push('-')
			else:
				stck.stack_push('-')
				while (temp!='+')&(temp!='-')&(len(stck)>=1):
					temp = stck.stack_pop()
					outputlist.append(temp)
				stck.stack_push(outputlist.pop())

		elif input_list[k]=='*':
			temp = stck.stack_pop()			
			outputlist.append(temp)
			if (temp=='+')|(temp=='-')|(temp=='*')|(temp=='/'):
				stck.stack_push(outputlist.pop())
				stck.stack_push('*')
			else:
				stck.stack_push('*')
				while (temp!='+')&(temp!='-')&(temp!='*')&(temp!='/')&(len(stck)>=1):
					temp = stck.stack_pop()
					outputlist.append(temp)
				stck.stack_push(outputlist.pop())

		elif input_list[k]=='/':
			temp = stck.stack_pop()			
			outputlist.append(temp)
			if (temp=='+')|(temp=='-')|(temp=='*')|(temp=='/'):
				stck.stack_push(outputlist.pop())
				stck.stack_push('/')
			else:
				stck.stack_push('/')
				while (temp!='+')&(temp!='-')&(temp!='*')&(temp!='/')&(len(stck)>=1):
					temp = stck.stack_pop()
					outputlist.append(temp)
				stck.stack_push(outputlist.pop())

		elif input_list[k]=='^':
			temp = stck.stack_pop()			
			outputlist.append(temp)
			if (temp=='+')|(temp=='-')|(temp=='*')|(temp=='/')|(temp=='^'):
				stck.stack_push(outputlist.pop())
				stck.stack_push('^')
			else:
				stck.stack_push('^')
				while (temp!='+')&(temp!='-')&(temp!='*')&(temp!='/')&(temp!='^')&(len(stck)>=1):
					temp = stck.stack_pop()
					outputlist.append(temp)
				stck.stack_push(outputlist.pop())

		elif input_list[k]=='sqrt':
			temp = stck.stack_pop()			
			outputlist.append(temp)
			if (temp=='+')|(temp=='-')|(temp=='*')|(temp=='/')|(temp=='^')|(temp=='sqrt')|(temp=='u-'):
				stck.stack_push(outputlist.pop())
				stck.stack_push('sqrt')
			else:
				stck.stack_push('sqrt')
				while (temp!='+')&(temp!='-')&(temp!='*')&(temp!='/')&(temp!='^')&(temp!='sqrt')&(temp!='u-')&(len(stck)>=1):
					temp = stck.stack_pop()
					outputlist.append(temp)
				stck.stack_push(outputlist.pop())

		elif (input_list[k][0]=='-')|(input_list[k]=='u-')|(input_list[k]=='-'):
			temp = stck.stack_pop()			
			outputlist.append(temp)
			if (temp=='+')|(temp=='-')|(temp=='*')|(temp=='/')|(temp=='^')|(temp=='sqrt')|(temp=='u-'):
				stck.stack_push(outputlist.pop())
				stck.stack_push('u-')
			else:
				stck.stack_push('u-')
				while (temp!='+')&(temp!='-')&(temp!='*')&(temp!='/')&(temp!='^')&(temp!='sqrt')&(temp!='u-')&(len(stck)>=1):
					temp = stck.stack_pop()
					outputlist.append(temp)
				stck.stack_push(outputlist.pop())
		
		else:
			outputlist.append(input_list[k])
		
#		print outputlist,k

		k+=1
	while len(stck)>0:
		outputlist.append(stck.stack_pop())
	return outputlist,k








# This loop reads every line, from a given text
# file till the last line

for expr in sys.stdin.readlines():


	# This parses a line removing all spaces
	# and stores the whole set of symbols or
	# numbers belonging to a line

	input_list = expr.split()

	outputlist = []
	
	err_flag = 0
	
	k=0

	output = in2post(input_list,k)	
	outputlist = output[0]


	
#	print outputlist

	if err_flag==1:
		print "ERROR"
	else:
		print ''.join(a + ' ' for a in outputlist)
