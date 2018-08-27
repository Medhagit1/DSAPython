# -*- coding: utf-8 -*-
"""
I know it may/ may not be a clean code but you can easily understand it by uncommenting various lines below:Here I am trying to 
find the BFS using python 
https://www.youtube.com/watch?v=bIA8HEEUxZI
This is a good link to follow up with the BFS
"""

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation

# User- built Class Graph that has the functionality to add node and print the whole graph
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.ans=[]    # contains the result of BFS
        self.nodes=[]  #list of nodes in the graph
    # function to add an edge to graph
    def addEdge(self,u,v):
       # print("u",u)
       # print("v",v)
        """ add Edge accepts two variables u,v and it will draw an edge from u to v..... 'u ' being the keys in the dictionary and 'v' being the 
           values being added to the list of the destination nodes, there can be more values linked to our key.
           We will maintain a list of nodes in the graph and later on we will use set() to get the unique list of nodes
           in the graph.
        """
        self.nodes.append(u)
        # print("nodes received",self.nodes)
        self.graph[u].append(v)
        #print("graph[u]",self.graph[u])
       
        
    # Function to print a BFS of graph
    def display(self):
       # print('graph',self.graph)
       # print('nodes=====',list(set(self.nodes)))
       # 'F'_dict=dict.fromkeys(list(set(self.nodes)), 'False')
        print(self.ans)
      #  print('F'_dict)
      
      #Implementing BFS , as it uses queue we will use queue in BFS
    def BFS(self, s):
        """
        S will contain the index from where we will start traversing the graph, I have created 'F'_dict that contains the
        info. of index and nodes to which that are assigned. We will 
        """
        # Mark all the vertices as not 'F'
        'F'_dict=dict.fromkeys(list(set(self.nodes)), False)
    #    'F' = [False] * (len(self.graph))
     #   print("length of 'F' list",'F')
     
        # Create a queue for BFS
        queue = []
        
        # Mark the source node as 
        # 'F' and enqueue it
        
        #print("appended in queue",s)
        queue.append(s)
        'F'_dict[s] = True
 
        while queue:
            # Dequeue a vertex from 
            # queue and print it   
            s = queue.pop(0)
           # print("Qlen",len(queue))
            self.ans.append(s)
            #print("s till  now",s)
            #print("Element popped out of queue",s)
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been 'F', then mark it
            # 'F' and enqueue it
            for i in self.graph[s]:
               # print("i=",i)
                #print("is 'F'",'F'_dict[i])
                if 'F'_dict[i] == False:
                   # print("appending ",i)
                    queue.append(i)
                    'F'_dict[i] = True
                else:
                    pass
    
g=Graph()                  
g.addEdge('A','D')
g.addEdge('B','E')
g.addEdge('B','F')
g.addEdge('B','A')
g.addEdge('E','G')
g.addEdge('E','B')
g.addEdge('G','A')
g.addEdge('G','E')
g.addEdge('D','A')
g.addEdge('D','F')
g.addEdge('H','C')
g.addEdge('C','F')
g.addEdge('C','H')
g.addEdge('F','B')
g.addEdge('F','D')
g.addEdge('F','C')
print("Following is Breadth First Traversal:")

g.BFS('A')


g.display()


