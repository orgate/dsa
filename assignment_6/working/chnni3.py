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

	if i<offset:
		graph[int(inp_str[0])-1].append([int(inp_str[1]), int(inp_str[2])])
		graph[int(inp_str[1])-1].append([int(inp_str[0]), int(inp_str[2])])
	
	elif i==offset:	
		v = int(inp_str[0])	# no. of vertices
		e = int(inp_str[4])	# no. of edges
		graph = []
		graphdist = []
		graphdistsrce = []
		offset+=(e+1)
		srce = int(inp_str[1])
		destch = int(inp_str[2])
		destni = int(inp_str[3])
		cur_ver = srce
		l = 0

		if (v==-1)&(e==-1)&(srce==-1)&(destch==-1)&(destni==-1):
			break

		while(l<v):
			graph.append(['inf', 'inf', 'inf', 0])
			l+=1

	if (i==offset-1)&(len(graph)!=0):
		graph[srce-1][0] = 0 # distance from source is initialized to 0

		graphdist = []
		while ((graph[destch-1][3]!=1) | (graph[destni-1][3]!=1)):			
			k = 4
			while (k<len(graph[cur_ver-1])):
				if graph[graph[cur_ver-1][k][0]-1][3]!=1:
					if (graph[cur_ver-1][0]!='inf'):
						if (graph[graph[cur_ver-1][k][0]-1][0] > (graph[cur_ver-1][0] + graph[cur_ver-1][k][1])):
							graph[graph[cur_ver-1][k][0]-1][0] = graph[cur_ver-1][0] + graph[cur_ver-1][k][1]
							heappush(graphdist, (graph[graph[cur_ver-1][k][0]-1][0], graph[cur_ver-1][k][0]))
				k+=1

			graph[cur_ver-1][3] = 1 # marked as visited
			graphdistsrce.append(cur_ver)	

			if (len(graphdist)>0):
				nextvartemp = heappop(graphdist)
				min_dist_temp = nextvartemp[0]
				cur_ver = nextvartemp[1]
			else:
				break

		chsrce = destch
		chdest1 = srce
		chdest2 = destni
		graphdist = []
		cur_ver = chsrce
		graph[chsrce-1][1] = 0 # distance from source is initialized to 0
		while ((graph[chdest1-1][3]!=2) | (graph[chdest2-1][3]!=2)):			
			k = 4
			while (k<len(graph[cur_ver-1])):
				if graph[graph[cur_ver-1][k][0]-1][3]!=2:
					if (graph[cur_ver-1][1]!='inf'):
						if (graph[graph[cur_ver-1][k][0]-1][1] > (graph[cur_ver-1][1] + graph[cur_ver-1][k][1])):
							graph[graph[cur_ver-1][k][0]-1][1] = graph[cur_ver-1][1] + graph[cur_ver-1][k][1]
							heappush(graphdist, (graph[graph[cur_ver-1][k][0]-1][1], graph[cur_ver-1][k][0]))
				k+=1

			graph[cur_ver-1][3] = 2 # marked as visited	

			if (len(graphdist)>0):
				nextvartemp = heappop(graphdist)
				min_dist_temp = nextvartemp[0]
				cur_ver = nextvartemp[1]
			else:
				break

		nisrce = destni
		nidest1 = srce
		nidest2 = destch
		graphdist = []
		cur_ver = nisrce
		graph[nisrce-1][2] = 0 # distance from source is initialized to 0
		while ((graph[nidest1-1][3]!=3) | (graph[nidest2-1][3]!=3)):			
			k = 4
			while (k<len(graph[cur_ver-1])):
				if graph[graph[cur_ver-1][k][0]-1][3]!=3:
					if (graph[cur_ver-1][2]!='inf'):
						if (graph[graph[cur_ver-1][k][0]-1][2] > (graph[cur_ver-1][2] + graph[cur_ver-1][k][1])):
							graph[graph[cur_ver-1][k][0]-1][2] = graph[cur_ver-1][2] + graph[cur_ver-1][k][1]
							heappush(graphdist, (graph[graph[cur_ver-1][k][0]-1][2], graph[cur_ver-1][k][0]))
				k+=1

			graph[cur_ver-1][3] = 3 # marked as visited	

			if (len(graphdist)>0):
				nextvartemp = heappop(graphdist)
				min_dist_temp = nextvartemp[0]
				cur_ver = nextvartemp[1]
			else:
				break

		maxcomver = 0
		comver = srce
		for ver in graphdistsrce:
			if (graph[ver-1][0]!='inf')&(graph[ver-1][1]!='inf')&(graph[ver-1][2]!='inf'):
				if (graph[ver-1][0]+graph[ver-1][1]<=graph[destch-1][0]):
					if (graph[ver-1][0]+graph[ver-1][2]<=graph[destni-1][0]):
						if (maxcomver < graph[ver-1][0]):
							maxcomver = graph[ver-1][0]
							comver = ver

		print graph[comver-1][0],(graph[destch-1][0]-graph[comver-1][0]),(graph[destni-1][0]-graph[comver-1][0])

	i+=1
