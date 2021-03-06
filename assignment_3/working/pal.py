###################################################################
#																  #
#	Title			:	Finding the next least palindrome number  #
#	Author			:	Alfred Ajay Aureate R					  #
#	Roll No			:	EE10B052								  #
#	Course			:	EE4371 - Data Structures and Algorithms	  #
#	Assignment No	:	3										  #
#																  #
###################################################################


import sys


# The following variables are used to keep track of the number of
# lines read and its limit

i=0
count = 0


# This loop reads every line, from a given text file till
# the last line

for numb_str in sys.stdin.readlines():


	# The last EOF (say,'\n') are removed from the given string

	numb_str = numb_str.strip()


	# The first line is noted as the number of strings to be read
	# or rather number of palindrome string to be made

	if i==0:
		count = int(numb_str)
	

	# The program stops after reading "count" number of strings

	if (i==count+1):
		break

	l = len(numb_str)
	j=0


	# This part is for strings with even length

	if (l%2==0)&(i!=0):

		half_len = (l/2)


		# This keeps track of no. of 9's that has to be made
		# zeros in the palindrome string

		zeros = 0


		# This is the element of the string where the increment
		# happens. Initially, it is the last element of the
		# first half of the string.

		pal_elm = numb_str[half_len-1]


		# This part is executed if the given string is less than
		# or equal to the string, which is created by copying
		# the reversed version of the first half string and
		# making it the second half

		if numb_str[(half_len-1)::-1]<=numb_str[half_len:]:
			while j<half_len:


				# This condition increments the zeros for every
				# '9', and continues in the while loop

				if(numb_str[half_len-j-1]=='9'):
					zeros+=2

				# This now means that the element where the
				# increment should happen has been encountered.
				# It is usually the last element of the first
				# half or the first element to the left of all
				# the 9's. It then breaks the while loop, with
				# "j" being the no. of 9's in the first half of
				# the string
 
				else:
					pal_elm = str(int(numb_str[half_len-j-1])+1)
					break

				j+=1


		# The following part prints the next palindrome
			
		# This is for printing next palindrome string for all
		# other possibilities (other than the following conditions)

		if (l!=2)&(j!=half_len)&(j!=half_len-1):
			print numb_str[0:(half_len-j-1)] + pal_elm + '0'*zeros + pal_elm + numb_str[(half_len-2-j)::-1]


		# This condition is for printing 2 digit next palindrome
		# string for strings less than '99'. Ex: '34'

		elif (l==2)&(numb_str!='99'):			
			print pal_elm + '0'*zeros + pal_elm


		# This condition is for exclusively printing the next
		# palindrome of '99' which is '101'

		elif l==2:
			print '101'

		# This condition is to make sure, that if nothing is
		# there, then print nothing, rather than stopping with
		# error

		elif l==0:
			print ''


		# This condition is for strings with only 9's. Ex:'9999'
		elif j==half_len:
			print '1' + '0'*(zeros-1) + '1'


		# This condition is for strings with all the elements
		# of the first half of the string being '9' except the
		# first element. Ex: '1991' or '499996'

		elif j==half_len-1:
			print pal_elm + '0'*zeros + pal_elm


	# This part is for the strings with odd length

	elif (i!=0):

		half_len = ((l-1)/2)


		# This keeps track of no. of 9's that has to be made
		# zeros in the palindrome string

		zeros = 0

		# This stores the middle element

		mid_elm = numb_str[half_len]

		# This is used, if the increment does not happen in
		# the middle element i.e. when the middle element
		# is '9'. It is the first element to the left of all
		# the 9's.

		pal_elm = ''


		# This part is executed if the given string is less
		# than or equal to the string, which is created by
		# copying the reversed version of the first half
		# string and making it the second half (middle
		# element is part of neither halves)

		if numb_str[(half_len-1)::-1]<=numb_str[(half_len+1):]:

			while j<=half_len:


				# This condition increments the zeros for
				# every '9', and continues in the while
				# loop. It makes sure the middle element of
				# the next palindrome is zero if the middle
				# element of the given string is '9'

				if(numb_str[half_len-j]=='9'):
					if j!=0:
						zeros+=2
					else:
						mid_elm = '0'


				# This now means that the element where the
				# increment should happen has been encountered.
				# It is usually the last element of the first
				# half or the first element to the left of all
				# the 9's. It then breaks the while loop, with
				# "j" being the no. of 9's in the first half of
				# the string. This also makes sure that the
				# middle element is incremented, provided it
				# is not '9'

				else:
					if j!=0:
						pal_elm = str(int(numb_str[half_len-j])+1)
					else:
						mid_elm = str(int(numb_str[half_len-j])+1)
					break
				j+=1



		# The following part prints the next palindrome
			
		# This is for printing next palindrome string for all
		# other possibilities (other than the following conditions)

		if (l!=1)&(j!=half_len+1)&(j!=half_len):
			print numb_str[0:(half_len-j)] + pal_elm + '0'*(zeros-1) + mid_elm + '0'*(zeros-1) + pal_elm + numb_str[(half_len-j-1)::-1]


		# This condition is for printing 1 digit next palindrome
		# string for strings less than '9'. Ex: '3'

		elif (l==1)&(mid_elm!='9'):
			print str(int(mid_elm)+1)


		# This condition is for exclusively printing the next
		# palindrome of '9' which is '11'

		elif l==1:
			print '11'


		# This condition is for strings with only 9's. Ex: '999'

		elif j==half_len+1:
			print '1' + '0'*zeros + '1'


		# This condition is for strings with all the elements of
		# the first half of the string being '9' except the
		# first element. Ex: '191' or '49996'

		elif j==half_len:
			print pal_elm + '0'*(zeros/2) + mid_elm + '0'*(zeros/2) + pal_elm


	i+=1

# THE END
