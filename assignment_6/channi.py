###################################################################
#																  #
#	Title			:	Charly and Nito							  #
#	Author			:	Alfred Ajay Aureate R					  #
#	Roll No			:	EE10B052								  #
#	Course			:	EE4371 - Data Structures and Algorithms	  #
#	Assignment No	:	6										  #
#																  #
###################################################################


import sys
from heapq import *

# The following variables are used to keep track of the number of
# lines read and its limit

i = 0
#cases = 0
offset = 0
v = 0
e = 0
graph = []

# This loop reads every line, from a given text file till
# the last line

for inp_str in sys.stdin.readlines():

	inp_str = inp_str.split()

#	if i==0:
#		cases = int(inp_str[0])


	if i<offset:
		graph[int(inp_str[0])-1].append([int(inp_str[1]), int(inp_str[2])])
		graph[int(inp_str[1])-1].append([int(inp_str[0]), int(inp_str[2])])
	
	elif i==offset:	
		v = int(inp_str[0])	# no. of vertices
		e = int(inp_str[4])	# no. of edges
		graph = []
		graphdist = []
		offset+=(e+1)
		srce = int(inp_str[1])
		destch = int(inp_str[2])
		destni = int(inp_str[3])
		min_dist = 0
		cur_ver = srce
		l = 0

		if (v==-1)&(e==-1)&(srce==-1)&(destch==-1)&(destni==-1):
			break

#		heappush(graphdist, ('inf', 0))
		while(l<v):
			graph.append(['inf', 0, []])
			l+=1

	if (i==offset-1)&(len(graph)!=0):
		graph[srce-1][0] = 0 # distance from source is initialized to 0
		graph[srce-1][2].append('ud') # previous node of source is initialized to undefined

		
#		graph_temp = [cur_ver]
		while ((graph[destch-1][1]==0) | (graph[destni-1][1]==0)):			
			k = 3

			min_dist_temp = 'inf'

			while (k<len(graph[cur_ver-1])):
				if graph[graph[cur_ver-1][k][0]-1][1]==0:
					if (graph[cur_ver-1][0]!='inf'):
						if (graph[graph[cur_ver-1][k][0]-1][0] > (graph[cur_ver-1][0] + graph[cur_ver-1][k][1])):
#						if (graph[graph[cur_ver-1][k][0]-1][0] > (graph[cur_ver-1][0] + graph[cur_ver-1][k][1]))&(cur_ver not in graph[graph[cur_ver-1][k][0]-1][2]):
							graph[graph[cur_ver-1][k][0]-1][0] = graph[cur_ver-1][0] + graph[cur_ver-1][k][1]
							graph[graph[cur_ver-1][k][0]-1][2] = [cur_ver]
							heappush(graphdist, (graph[graph[cur_ver-1][k][0]-1][0], graph[cur_ver-1][k][0]))
						elif (graph[graph[cur_ver-1][k][0]-1][0] == (graph[cur_ver-1][0] + graph[cur_ver-1][k][1]))&(cur_ver not in graph[graph[cur_ver-1][k][0]-1][2]):
##							graph[graph[cur_ver-1][k][0]-1][0] = graph[cur_ver-1][0] + graph[cur_ver-1][k][1]
							graph[graph[cur_ver-1][k][0]-1][2].append(cur_ver)
##							heappush(graphdist, (graph[graph[cur_ver-1][k][0]-1][0], graph[cur_ver-1][k][0]))
#				else:
#							graph[cur_ver-1][2].append(graph[cur_ver-1][k][0]-1)

				k+=1

			graph[cur_ver-1][1] = 1 # marked as visited	
#			print cur_ver
#			print graphdist

##			next_var = cur_ver



			if (len(graphdist)>0):
				nextvartemp = heappop(graphdist)
				min_dist_temp = nextvartemp[0]
				cur_ver = nextvartemp[1]
			else:
				break
##			while (next_var == cur_ver)&(len(graphdist)>0):
#				if (len(graphdist)>0):
#				nextvartemp = heappop(graphdist)
##				min_dist_temp = nextvartemp[0]
##				cur_ver = nextvartemp[1]
#				else:
#					break

#			print "now "
#			print graphdist
				
#		print min_dist_temp
#		print graph



		pathch = [[destch]]
#		cur_ver = destch

		l=0
#		while (cur_ver!=srce):
		while (pathch[l]!=[srce]):
			pathch.append([])
			m=0
			while m<len(pathch[l]):
				cur_ver = pathch[l][m]
				n=0
				if (cur_ver!=srce):
					while n<len(graph[cur_ver-1][2]):
#					pathni[l].append(graph[cur_ver-1][2][k])
						if graph[cur_ver-1][2][n] not in pathch[l+1]:
							pathch[l+1].append(graph[cur_ver-1][2][n])
						n+=1
				m+=1
#			print pathch
##			cur_ver = pathch[l+1][0]
			l+=1



		pathni = [[destni]]
#		cur_ver = destni

		l=0
#		while (cur_ver!=srce):
		while (pathni[l]!=[srce]):
			pathni.append([])
			m=0
			while m<len(pathni[l]):
				cur_ver = pathni[l][m]
				n=0
				if (cur_ver!=srce):
					while n<len(graph[cur_ver-1][2]):
#					pathni[l].append(graph[cur_ver-1][2][k])
						if graph[cur_ver-1][2][n] not in pathni[l+1]:
							pathni[l+1].append(graph[cur_ver-1][2][n])
						n+=1
				m+=1
#			print pathch
##			cur_ver = pathni[l+1][0]
			l+=1



#		print graph
#		print pathch
#		print pathni


		lench = len(pathch)
		lenni = len(pathni)
		comver = srce
		maxcomdist=0
		pathverch = []
		pathverni = []

		l=0
		while l<lench:
			k=0
			while (k<len(pathch[l])):
				pathverch.append(pathch[l][k])
				k+=1
			l+=1

		l=0
		while l<lenni:
			k=0
			while (k<len(pathni[l])):
				pathverni.append(pathni[l][k])
				k+=1
			l+=1
		
		l=0
		while (l<lench):
			if (pathverch[l] in pathverni)&(maxcomdist < graph[pathverch[l]-1][0]):
				comver = pathverch[l]
				maxcomdist = graph[pathverch[l]-1][0]
			l+=1

##		while (l<lench)&(l<lenni):
##			verch = pathch.pop()
##			verni = pathni.pop()
##			k=0
##			comverflag=0
#/			maxcomdist=0
##			while (k<len(verch)):
##				if (verch[k] in verni)&(maxcomdist<=graph[verch[k]-1][0]):
##					comver = verch[k]
##					maxcomdist = graph[verch[k]-1][0]
##					comverflag = 1
#				elif (verch[k] in verni)&(mincomdist==graph[verch[k]-1][0]):
#					comver = verch[k]
#					mincomdist = graph[verch[k]-1][0]
#					comverflag = 1
##				k+=1
##			if comverflag==0:
##				break	
##			l+=1


#		print pathch
#		print pathverch
#		print pathni
#		print pathverni

		print graph[comver-1][0],(graph[destch-1][0]-graph[comver-1][0]),(graph[destni-1][0]-graph[comver-1][0])


##		if (graph[dest-1][0]=='inf'):
##			print "NONE"
##		else:
##			print graph[dest-1][0]

	i+=1

