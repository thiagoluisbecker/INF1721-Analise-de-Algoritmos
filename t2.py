rows = 3
columns = 3

def create_matrix(rows, columns):
    cfg = []
    for y in range(columns):
        col = []
        for x in range(rows):
            if (1 + x + y * rows) != 9:
                col.append(1 + x + y * rows)
            else:
                col.append(0)

        cfg.append(col)
    return cfg
class Node:
    def __init__(self, degree, config, id):
        self.deg = degree
        self.cfg = config
        self.id = id

    def print_config(self):
        for column in self.cfg:
            print(column)



def create_graph():
    initial_config = create_matrix(rows, columns)
    for column in initial_config:
        pass



x = Node()
x.print_config()