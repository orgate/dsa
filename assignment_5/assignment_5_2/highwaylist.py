###################################################################
#																  #
#	Title			:	Highways (shortest route)				  #
#	Author			:	Alfred Ajay Aureate R					  #
#	Roll No			:	EE10B052								  #
#	Course			:	EE4371 - Data Structures and Algorithms	  #
#	Assignment No	:	5.2										  #
#																  #
###################################################################


import sys


# The following variables are used to keep track of the number of
# lines read and its limit

i = 0
cases = 0
offset = 1
v = 0
e = 0
graph = []

# This loop reads every line, from a given text file till
# the last line

for inp_str in sys.stdin.readlines():

	inp_str = inp_str.split()

	if i==0:
		cases = int(inp_str[0])


	if (cases!=0)&(i<offset)&(i!=0):
		graph[int(inp_str[0])-1].append([int(inp_str[1]), int(inp_str[2])])
		graph[int(inp_str[1])-1].append([int(inp_str[0]), int(inp_str[2])])
	
	elif i==offset:	
		v = int(inp_str[0])	# no. of vertices
		e = int(inp_str[1])	# no. of edges
		graph = []
		offset+=(e+1)
		srce = int(inp_str[2])
		dest = int(inp_str[3])
		min_dist = 0
		cur_ver = srce
		l = 0
		while(l<v):
			graph.append(['inf', 0])
			l+=1

	if (i==offset-1)&(len(graph)!=0)&(i!=0):
		graph[srce-1][0] = 0 # distance from source is initialized to 0
		graph_temp = [cur_ver]
		while(graph[dest-1][1]==0):			
			k = 2
			min_dist_temp = 'inf'
			while (k<len(graph[cur_ver-1])):
				if graph[graph[cur_ver-1][k][0]-1][1]==0:
					if (graph[graph[cur_ver-1][k][0]-1][0] > (graph[cur_ver-1][0] + graph[cur_ver-1][k][1])):
						graph[graph[cur_ver-1][k][0]-1][0] = graph[cur_ver-1][0] + graph[cur_ver-1][k][1]
						graph_temp.append(graph[cur_ver-1][k][0])
				k+=1

			graph[cur_ver-1][1] = 1 # marked as visited	

			next_ver = cur_ver
			for ver in graph_temp:
				if (graph[ver-1][1]==0)&(graph[ver-1][0]!='inf'):
					if (min_dist_temp > graph[ver-1][0]):
						min_dist_temp = graph[ver-1][0]
						next_ver = ver

#			print graph_temp

			if (cur_ver==next_ver):
				break
			elif(len(graph_temp)!=0):
				graph_temp.remove(cur_ver)
			cur_ver = next_ver
		
		if (graph[dest-1][0]=='inf'):
			print "NONE"
		else:
			print graph[dest-1][0]

	i+=1

