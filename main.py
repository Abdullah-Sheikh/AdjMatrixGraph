class Graph(object):

    # Init the matrix
    def __init__(self, size):
        self.adjMatrix = []
        self.nodes = Nodes
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # this function will add Add edges
    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1


    # Print the matrix
    def print_matrix(self):
          print ('\nthe vertical col shows row\n')
          a= 'A'
          for  row in self.adjMatrix:

            for val in row:
                 print(a ,':' ,val)
            print ('\n')
            a= chr(ord(a) + 1)


Nodes=["A","B","C","D","E"]  # init the nodes

obj = Graph(5)  # create a object of class Graph "5" means the number of vertices is 5


obj.add_edge(0, 1)
obj.add_edge(0, 2)
obj.add_edge(1, 2)
obj.add_edge(2, 0)
obj.add_edge(2, 3)

obj.print_matrix()

