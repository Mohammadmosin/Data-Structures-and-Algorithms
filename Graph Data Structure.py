#To find Shortest Distance from a given vertex to all other vetices in Graph

class Vertex:
    def __init__(self,n):
        self.name=n

class Graph():
    def __init__(self):
        self.vertices={}
        self.edges=[]
        self.edge_indices= {}
        self.shortest_distance=[]
        self.previos_vertex=[]
        self.vertex_list=[]
        self.vertex_visited=[]
        self.visited_vertex=[]
        self.r = []
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.edge_indices[vertex.name] = len(self.edges)
            self.vertices[vertex.name]=vertex
            self.vertex_list.append(vertex.name)
            self.previos_vertex.append(None)
            self.shortest_distance.append(1000)
            for i in self.edges:
                i.append(0)
            self.edges.append([0]*(len(self.edges)+1))
            return True
        else:
            return False
    def add_edge(self,u,v,weight=1):
        if u in self.vertices and v in self.vertices:
            pass
            self.edges[self.edge_indices[v]][self.edge_indices[u]]=weight
            self.edges[self.edge_indices[u]][self.edge_indices[v]] =weight
        else:
            return False
    def print_graph(self):
        print("***Adjacency matrix of given Graph***")
        for key,value in self.edge_indices.items():
            v=key+' '
            k=(self.edges[value])
            for i in k:
                v=v+str(i)
            print(v)
    def store(self,u,v):
        print(u,v)
    def vertex_visited(self,k):
        if k in self.vertex_visited:
            return False
        else:
            return True

        pass
    def find_short_path(self,u):
        k=self.vertex_list.index(u)
        #print(self.shortest_distance)
        #print(self.previos_vertex)
        if(min(self.shortest_distance)!=0):
            self.shortest_distance[k]=0
        s = self.shortest_distance[k]
        n=[]
        l=10000
        for i in range(0,len(self.edges)):
            if(self.edges[k][i]!=0):
                j = self.shortest_distance[i]
                if(self.edges[k][i]+s<=j ):
                    self.shortest_distance[i]=self.edges[k][i]+s
                    self.previos_vertex[i]=self.vertex_list[k]
                    n.append(self.edges[k][i]+s)
                    #print(self.shortest_distance)
                    self.r.append(i)
                    if(self.edges[k][i]+s<l):
                        l=i
        self.visited_vertex.append(u)
        pr=self.visited_vertex[len(self.visited_vertex)-1]
        if  l!=10000:
            self.find_short_path(self.vertex_list[l])
        if (len(self.visited_vertex)<len(self.vertex_list)):
            for i in self.vertex_list:
                if i not in self.visited_vertex:
                    self.find_short_path(i)
                    #break
        return self.shortest_distance



l=Vertex('A')
m=Vertex('B')
n=Vertex('C')
o=Vertex('D')
p=Vertex('E')
q=Graph()
q.add_vertex(l)
q.add_vertex(m)
q.add_vertex(n)
q.add_vertex(o)
q.add_vertex(p)
edges=['AB','AD','BC','BD','CD','CE','DE']
li=[2,9,3,1,1,3,4]
for i  in range(0,len(edges)):
    u=edges[i]
    q.add_edge(u[:1], u[1:],li[i])
q.print_graph()
given_vertex='A'
s=(q.find_short_path(given_vertex))
print('shortest distance from given vertex '+given_vertex)
for i in range(len(s)):
    print(given_vertex+' to '+q.vertex_list[i]+' is',q.shortest_distance[i])
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI',IF]
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.print_graph()
given_vertex='G'
s=(g.find_short_path(given_vertex))
print('shortest distance from given vertex '+given_vertex)
for i in range(len(s)):
    print(given_vertex+' to '+g.vertex_list[i]+' is',g.shortest_distance[i])


