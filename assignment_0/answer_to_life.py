
numb = [0]
i=1
j=1

while (numb[i-1]!=42) & (numb[i-1]>-100) & (numb[i-1]<100):
	numb.append(input())
	i+=1

while j<i-1:
	print numb[j]
	j+=1


