###################################################################
#																  #
#	Title			:	Finding the bridge						  #
#	Author			:	Alfred Ajay Aureate R					  #
#	Roll No			:	EE10B052								  #
#	Course			:	EE4371 - Data Structures and Algorithms	  #
#	Assignment No	:	7										  #
#																  #
###################################################################


import sys
from heapq import *
from collections import deque

# The following variables are used to keep track of the number of
# lines read and its limit

i = 0
offset = 0
v = 0
e = 0
graph = []

# This loop reads every line, from a given text file till
# the last line

for inp_str in sys.stdin.readlines():

	inp_str = inp_str.split()

	if (i<offset)&(i!=0):
		graph[int(inp_str[0])].append(int(inp_str[1]))
		graph[int(inp_str[1])].append(int(inp_str[0]))
	
	elif i==offset:	
		v = int(inp_str[0])	# no. of vertices
		e = int(inp_str[1])	# no. of edges

		#graph = [[flag,neighbour1,neighbour2,...],
		#		 [flag,neighbour1,neighbour2,...],...,similarly for n vertices]

		graph = []

		#spantree = [[parent node, node in prefix notation, (children+1), low prefix node, high prefix node, child1, child2,...],
		#			[parent node, node in prefix notation, (children+1), low prefix node, high prefix node, child1, child2,...],...,similarly for n vertices]

		spantree = []
		offset+=(e+1)
		l = 0
		while(l<v):
			spantree.append([0,0,0,0,0])
			graph.append([0])
			l+=1

	if (i==offset-1)&(len(graph)!=0)&(i!=0):
		srce = 0
		cur_ver = srce
		graph_temp = []
		m=0
		while (m<v):			
			k = 1
			while (k<len(graph[cur_ver])):
				if graph[graph[cur_ver][k]][0]==0:
					spantree[graph[cur_ver][k]][0] = cur_ver
					spantree[cur_ver].append(graph[cur_ver][k])
					graph_temp.append(graph[cur_ver][k])
					graph[graph[cur_ver][k]][0] = 1 # visited as a leaf but not yet as a root
				k+=1

			graph[cur_ver][0] = 2 # visited as a root. # not sure if required
			m+=1
			if (len(graph_temp)>0):
				cur_ver = graph_temp.pop()
			else:
				break

		spantreetemp = []
		spantreeprefix = [] # stores the actual spantree node corresponding to each node in prefix notation
		leaves = [] # the spantree nodes that are leaves are noted
		cur_ver = srce
		n=0
		spantree[cur_ver][1] = n
		while (n<v):
			l = 5
			if (len(spantree[cur_ver])==5):
				leaves.append(cur_ver)
			else:
				while (l<len(spantree[cur_ver])):
					spantreetemp.append(spantree[cur_ver][l])
					l+=1

			spantreeprefix.append(cur_ver)
			spantree[cur_ver][1] = n
			spantree[cur_ver][3] = n
			spantree[cur_ver][4] = n
			n+=1
			if (len(spantreetemp)>0):
				cur_ver = spantreetemp.pop()
			else:
				break
		
		low = 0
		high = v-1
		graphnode = v-1
		node = spantreeprefix[graphnode]
		while ((high - low)>=spantree[node][2]):		
			node = spantreeprefix[graphnode]
			low_of_p = []
			high_of_p = []
			spantree[node][2]+=1
			spantree[spantree[node][0]][2]+=spantree[node][2]
			heappush(low_of_p,(spantree[node][1],node))
			heappush(high_of_p,((v-1-spantree[node][1]),node))

			p = graphnode+spantree[node][2]-1
			while (p>graphnode):
				heappush(low_of_p,(spantree[spantreeprefix[p]][3],spantreeprefix[p]))
				heappush(high_of_p,((v-1-spantree[spantreeprefix[p]][4]),spantreeprefix[p]))
				p-=1

			q = 1
			while q<len(graph[node]):
				if spantree[node][0]!=graph[node][q]:
					heappush(low_of_p,(spantree[graph[node][q]][1],graph[node][q]))
					heappush(high_of_p,((v-1-spantree[graph[node][q]][1]),graph[node][q]))
				q+=1

			low_of_p_temp = heappop(low_of_p)
			spantree[node][3] = low_of_p_temp[0]
			low = low_of_p_temp[0]
			high_of_p_temp = heappop(high_of_p)
			spantree[node][4] = v-1-high_of_p_temp[0]
			high = v-1-high_of_p_temp[0]
			graphnode-=1

		if (node < spantree[node][0]):
			print node," ",spantree[node][0]
		elif (node > spantree[node][0]):
			print spantree[node][0]," ",node

	i+=1
