class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def addVertex(self, value):
        if value not in self.gdict:
            self.gdict[value] = []

    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            if vrtx2 not in self.gdict[vrtx1]:
                self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

        if vrtx2 in self.gdict:
            if vrtx1 not in self.gdict[vrtx2]:
                self.gdict[vrtx2].append(vrtx1)
        else:
            self.gdict[vrtx2] = [vrtx1]




graph_elements = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['e'],
    'e': ['d']
}

g = Graph(graph_elements)
print(g.getVertices())
print(g.edges())
g.addVertex('f')
print(g.getVertices())
g.addEdge({'a','e'})
g.addEdge({'f','z'})
print(g.edges())
