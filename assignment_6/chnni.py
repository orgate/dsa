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
		srce = int(inp_str[1]) # bar is taken as source in both the graphs
		destch = int(inp_str[2]) # Charly's house is taken as the destination for the first graph
		destni = int(inp_str[3]) # Nito's house is taken as the destination for the second graph
		min_dist = 0
		cur_ver = srce
		l = 0

		if (v==-1)&(e==-1)&(srce==-1)&(destch==-1)&(destni==-1):
			break

#		heappush(graphdist, ('inf', 0))
		while(l<v):
			graph.append(['inf', 0])
			l+=1

	if (i==offset-1)&(len(graph)!=0):
		graph[srce-1][0] = 0 # distance from source is initialized to 0
#		graph[srce-1][2].append('ud') # previous node of source is initialized to undefined
		
#		graph_temp = [cur_ver]
		while (graph[destch-1][1]==0):			
			k = 2
#			print "it's here0 "

			min_dist_temp = 'inf'

			while (k<len(graph[cur_ver-1])):
				if graph[graph[cur_ver-1][k][0]-1][1]==0:
#					if (graph[cur_ver-1][0]!='inf'):
					if (graph[graph[cur_ver-1][k][0]-1][0] > (graph[cur_ver-1][0] + graph[cur_ver-1][k][1])):
						graph[graph[cur_ver-1][k][0]-1][0] = graph[cur_ver-1][0] + graph[cur_ver-1][k][1]
						heappush(graphdist, (graph[graph[cur_ver-1][k][0]-1][0], graph[cur_ver-1][k][0]))

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

		cur_ver = srce
		graphdistnito = []
		comver = srce
		comverflag = 0
		maxcomdist = 0
#		while (graph[destni-1][1]==0)|(graph[destni-1][1]==1):
		while graph[destni-1][1]!=2:
			k=2
#			print "it's here1 "

			while (k<len(graph[cur_ver-1])):
				if (graph[graph[cur_ver-1][k][0]-1][1]==0)|(graph[graph[cur_ver-1][k][0]-1][1]==1):
#					if (graph[cur_ver-1][0]!='inf'):
					if (graph[graph[cur_ver-1][k][0]-1][0] >= (graph[cur_ver-1][0] + graph[cur_ver-1][k][1])):
						graph[graph[cur_ver-1][k][0]-1][0] = graph[cur_ver-1][0] + graph[cur_ver-1][k][1]
						heappush(graphdistnito, (graph[graph[cur_ver-1][k][0]-1][0], graph[cur_ver-1][k][0]))
					
				elif (graph[graph[cur_ver-1][k][0]-1][1]!=0)|(graph[graph[cur_ver-1][k][0]-1][1]!=1):

#					print "it's here1 "
#					if (maxcomdist <= graph[graph[cur_ver-1][k][0]-1][0]):
#						comver = graph[cur_ver-1][k][0]
#						maxcomdist = graph[graph[cur_ver-1][k][0]-1][0]
					if (maxcomdist < graph[graph[cur_ver-1][k][0]-1][0]):
						comver = graph[cur_ver-1][k][0]
						maxcomdist = graph[graph[cur_ver-1][k][0]-1][0]

				k+=1
#					comver = graph[cur_ver-1][k][0]

			graph[cur_ver-1][1]=2 # marked as visited	
#			print cur_ver
#			print graphdistnito
#			print graph
##			next_var = cur_ver

			if (len(graphdistnito)>0):
				nextvartemp = heappop(graphdistnito)
				min_dist_temp = nextvartemp[0]
				cur_ver = nextvartemp[1]
			else:
				break

		print graph[comver-1][0],(graph[destch-1][0]-graph[comver-1][0]),(graph[destni-1][0]-graph[comver-1][0])


			

	i+=1

