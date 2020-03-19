###################################################################
#																  #
#	Title			:	Island capitals							  #
#	Author			:	Alfred Ajay Aureate R					  #
#	Roll No			:	EE10B052								  #
#	Course			:	EE4371 - Data Structures and Algorithms	  #
#	Assignment 		:	Final exam								  #
#																  #
###################################################################


import sys
from heapq import *

# The following variables are used to keep track of the number of
# lines read and its limit

i = 0
#cases = 0
#offset = 1
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


#	if (cases!=0)&(i<offset)&(i!=0):
	if i<offset:
		if not(towns.has_key(inp_str[0])):
			towns[inp_str[0]] = t		#town_name  --->  number
			townlist[t] = inp_str[0]	#number     --->  town_name
			townslistdyn[t] = inp_str[0]	#number     --->  town_name
			t+=1

		if not(towns.has_key(inp_str[1])):
			towns[inp_str[1]] = t		#town_name  --->  number
			townlist[t] = inp_str[1]	#number     --->  town_name
			townslistdyn[t] = inp_str[1]	#number     --->  town_name
			t+=1

		graph[towns[inp_str[0]]].append([towns[inp_str[1]], int(inp_str[2])])
		graph[towns[inp_str[1]]].append([towns[inp_str[0]], int(inp_str[2])])

	
	elif i==offset:	
		v = int(inp_str[0])	# no. of vertices
		e = int(inp_str[1])	# no. of edges
		graph = []
#		graphfirst = []
		towns = {}
		townlist = ['']*v
		townslistdyn = ['']*v
		t = 0
		graphdist = []
		graphcapt = []
		offset+=(e+1)
#		srce = int(inp_str[2])
#		dest = int(inp_str[3])
		min_dist = 0
#		cur_ver = srce
		l = 0
		heappush(graphdist, ('inf', -1))
#		heappush(graphcapt, ('inf', 0)) #not sure if it's required
		while(l<v):
			graph.append(['inf', 0])
#			graph.append([0])
#			graphfirst.append('inf')
#			graph.append(['inf']*v)
#			graph[l].append(0)

			l+=1

#	if (i==offset-1)&(len(graph)!=0)&(i!=0):
	if (i==offset-1)&(len(graph)!=0):


#		print graph
#		print towns
		capitals = []

#		townslistdyn = townlist		
#		print townslistdyn
#		startisland = 0
#		m=0
		for town in townslistdyn:

#			if (startisland==0):
				
			srce = towns[town]
			graph[srce][0] = 0 # distance from source is initialized to 0

			cur_ver = srce
			tot_dist = 0
		
#			graph_temp = [cur_ver]


			m=0
#			while(graph[dest-1][1]==0):			
			while(m<v):
				k = 2	

#			min_dist_temp = 'inf'
				while (k<len(graph[cur_ver])):	
					if graph[graph[cur_ver][k][0]][1]==0:
						if (graph[cur_ver][0]!='inf'):
							if (graph[graph[cur_ver][k][0]][0] > (graph[cur_ver][0] + graph[cur_ver][k][1])):
								graph[graph[cur_ver][k][0]][0] = graph[cur_ver][0] + graph[cur_ver][k][1]
								heappush(graphdist, (graph[graph[cur_ver][k][0]][0], graph[cur_ver][k][0]))
					k+=1

				graph[cur_ver][1] = 1 # marked as visited	
				m+=1

				if (len(graphdist)>0):
					nextvartemp = heappop(graphdist)
#				min_dist_temp = nextvartemp[0]
					cur_ver = nextvartemp[1]
				else:
					break


			ver = 0
			tot_dist = 0
			islandtowns = 1
			graph[srce][1] = 0
			island = [graph[srce]]
			islandlist = [srce]
			graph[srce][0] = 'inf'
			islandmat = [[town]]
			townslistdyn.remove(townlist[srce])
			islanddist = []
			heappush(islanddist, ('inf', 0))
			while (ver<v):
				if (graph[ver][0]!='inf')&(ver!=srce):
#						tot_dist = 'inf'
#						break
###					temp = towns.pop(townlist[ver])
##					islandmat.append([townlist[towns.pop(townlist[ver])]])
#					print "townslistdyn is ",townslistdyn
#					print "townlist is ",townlist
					townslistdyn.remove(townlist[ver])
					graph[ver][1] = 0
					island.append(graph[ver])						
					islandlist.append(ver)
					tot_dist+=graph[ver][0]

					graph[ver][0] = 'inf'
					islandtowns+=1
				else:
					graph[ver][1] = 0
#						tot_dist+=graph[ver][srce]
				ver+=1
			
#			print "island is ",island
#			print "islandlist is ",islandlist

##			twn = 0
			islandcaptdist = []
			heappush(islandcaptdist, ('inf', 'Alfred'))
##			while(twn<islandtowns):
#					islandmat[twn].append(''*islandtowns)
##				islandmat[twn].append(island[twn][0])
##				twn+=1
			heappush(islandcaptdist, (tot_dist, town))
#			startisland = 1






#			else:

			itwns = 1
			while (itwns<islandtowns):
				srce = islandlist[itwns]
				graph[srce][0] = 0 # distance from source is initialized to 0
	
				cur_ver = srce
#					tot_dist = 0
			
#			graph_temp = [cur_ver]



				m=0
#			while(graph[dest-1][1]==0):			
				while(m<islandtowns):
					k = 2	

#			min_dist_temp = 'inf'
					while (k<len(graph[cur_ver])):	
						if graph[graph[cur_ver][k][0]][1]==0:
							if (graph[cur_ver][0]!='inf'):
								if (graph[graph[cur_ver][k][0]][0] > (graph[cur_ver][0] + graph[cur_ver][k][1])):
									graph[graph[cur_ver][k][0]][0] = graph[cur_ver][0] + graph[cur_ver][k][1]
									heappush(islanddist, (graph[graph[cur_ver][k][0]][0], graph[cur_ver][k][0]))
						k+=1
	
					graph[cur_ver][1] = 1 # marked as visited	
					m+=1
	
					if (len(islanddist)>0):
						nextvartemp = heappop(islanddist)
#				min_dist_temp = nextvartemp[0]
						cur_ver = nextvartemp[1]
					else:

						break
	
				ver = 0
				tot_dist = 0
#				print "Now, graph is ",graph
				while (ver<islandtowns):
#						tot_dist = 'inf'
#						break
					graph[islandlist[ver]][1] = 0
#					islandmat[ver].append(island[ver][0])
					tot_dist+= graph[islandlist[ver]][0]
					graph[islandlist[ver]][0] = 'inf'
#						tot_dist+=graph[ver][srce]
					ver+=1
#				heappush(islandcaptdist, (tot_dist, islandmat[itwns][0]))
				heappush(islandcaptdist, (tot_dist, townlist[islandlist[itwns]]))
		
				itwns+=1	

#				startisland+=1
				
#				if (startisland == islandtowns):
#					startisland=0




#			print "islandcaptdist is ",islandcaptdist
			islandcapt = []
			capttemp1 = heappop(islandcaptdist)
			capttemp2 = heappop(islandcaptdist)

			if (capttemp1[0]==capttemp2[0])&(capttemp1[1]>capttemp2[1]):
				heappush(islandcapt,capttemp2[1])						
			else:
				heappush(islandcapt,capttemp1[1])						

			while(capttemp1[0]==capttemp2[0])&(len(islandcaptdist)>0):
				capttemp2 = heappop(islandcaptdist)
				if (capttemp1[0]==capttemp2[0])&(capttemp1[1]>capttemp2[1]):
					heappush(islandcapt,capttemp2[1])						

			heappush(capitals,heappop(islandcapt))


		while (len(capitals)>0):
			print heappop(capitals)










	
#			heappush(graphcapt,(tot_dist,srce))	
		
#		capt = heappop(graphcapt)
#		print townlist[capt[1]]



#		if (graph[dest-1][0]=='inf'):
#			print "NONE"
#		else:
#			print graph[dest-1][0]

	i+=1

