from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print(f"Node '{node}' added")
        else:
            print(f"Node '{node}' already exists")

    def add_edge(self, u, v, cost=0):
        if u in self.graph and v in self.graph:
            if (v, cost) in self.graph[u]:
                print(f"Edge from '{u}' to '{v}' already exists")
            else:
                self.graph[u].append((v, cost))
                self.graph[v].append((u, cost))
                print(f"Edge from '{u}' to '{v}' added")
        else:
            print("Add nodes first")

    def delete_node(self, node):
        if node in self.graph:
            self.graph.pop(node)
            for n in self.graph:
                self.graph[n] = [(x, c) for x, c in self.graph[n] if x != node]
            print(f"Node '{node}' deleted")
        else:
            print(f"Node '{node}' not found")

    def delete_edge(self, u, v):
        if u in self.graph:
            initial_count = len(self.graph[u])
            self.graph[u] = [(x, c) for x, c in self.graph[u] if x != v]
            self.graph[v] = [(x, c) for x, c in self.graph[v] if x != u]
            if len(self.graph[u]) < initial_count:
                print(f"Edge from '{u}' to '{v}' deleted")
            else:
                print(f"Edge from '{u}' to '{v}' not found")
        else:
            print(f"Edge from '{u}' to '{v}' not found")

    def display(self):
        print("\nGraph:")
        for node in self.graph:
            print(node, "-", self.graph[node])

    def display_adj_list(self, node):
        if node in self.graph:
            print(node, "-", self.graph[node])
        else:
            print("Node not found")

    def bfs_lr(self, start, goal_node=None):
        explored = set()
        fringe = deque([(start, [start])])
        found_goal = False
        iteration = 0

        print("BFS (L-R):")
        while fringe:
            iteration += 1
            node, path = fringe.popleft()
            if node not in explored:
                explored.add(node)
                print(f"Iteration {iteration}: Fringe: {list(fringe)}, Explored: {explored}")
                if node == goal_node:
                    found_goal = True
                    print(f"Goal node '{goal_node}' reached! Path: {' -> '.join(path)}")
                    break
                for neigh, _ in self.graph[node]:
                    if neigh not in explored:
                        new_path = list(path)
                        new_path.append(neigh)
                        fringe.append((neigh, new_path))
        print()
        if goal_node and not found_goal:
            print(f"Goal node '{goal_node}' not found in traversal.")

    def bfs_rl(self, start, goal_node=None):
        explored = set()
        fringe = deque([(start, [start])])
        found_goal = False
        iteration = 0

        print("BFS (R-L):")
        while fringe:
            iteration += 1
            node, path = fringe.popleft()
            if node not in explored:
                explored.add(node)
                print(f"Iteration {iteration}: Fringe: {list(fringe)}, Explored: {explored}")
                if node == goal_node:
                    found_goal = True
                    print(f"Goal node '{goal_node}' reached! Path: {' -> '.join(path)}")
                    break
                for neigh, _ in reversed(self.graph[node]):
                    if neigh not in explored:
                        new_path = list(path)
                        new_path.append(neigh)
                        fringe.append((neigh, new_path))
        print()
        if goal_node and not found_goal:
            print(f"Goal node '{goal_node}' not found in traversal.")

    def dfs_lr(self, start, goal_node=None):
        explored = set()
        fringe = [(start, [start])]
        found_goal = False
        iteration = 0

        print("DFS (L-R):")
        while fringe:
            iteration += 1
            node, path = fringe.pop()
            if node not in explored:
                explored.add(node)
                print(f"Iteration {iteration}: Fringe: {fringe}, Explored: {explored}")
                if node == goal_node:
                    found_goal = True
                    print(f"Goal node '{goal_node}' reached! Path: {' -> '.join(path)}")
                    break
                for neigh, _ in reversed(self.graph[node]):
                    if neigh not in explored:
                        new_path = list(path)
                        new_path.append(neigh)
                        fringe.append((neigh, new_path))
        print()
        if goal_node and not found_goal:
            print(f"Goal node '{goal_node}' not found in traversal.")

    def dfs_rl(self, start, goal_node=None):
        explored = set()
        fringe = [(start, [start])]
        found_goal = False
        iteration = 0

        print("DFS (R-L):")
        while fringe:
            iteration += 1
            node, path = fringe.pop()
            if node not in explored:
                explored.add(node)
                print(f"Iteration {iteration}: Fringe: {fringe}, Explored: {explored}")
                if node == goal_node:
                    found_goal = True
                    print(f"Goal node '{goal_node}' reached! Path: {' -> '.join(path)}")
                    break
                for neigh, _ in self.graph[node]:
                    if neigh not in explored:
                        new_path = list(path)
                        new_path.append(neigh)
                        fringe.append((neigh, new_path))
        print()
        if goal_node and not found_goal:
            print(f"Goal node '{goal_node}' not found in traversal.")

g = Graph()
while True:
    print("\nMENU")
    print("1 Add Nodes")
    print("2 Add Edges")
    print("3 Delete Node")
    print("4 Delete Edge")
    print("5 Display Graph")
    print("6 Display Adjacency List")
    print("7 BFS Left to Right ")
    print("8 BFS Right to Left ")
    print("9 DFS Left to Right ")
    print("10 DFS Right to Left ")
    print("11 Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        count = int(input("How many nodes to add? "))
        for _ in range(count):
            node = input("Node: ")
            g.add_node(node)
    elif ch == 2:
        count = int(input("How many edges to add? "))
        for _ in range(count):
            u = input("From: ")
            v = input("To: ")
            cost = int(input("Cost (0 if none): "))
            g.add_edge(u, v, cost)
    elif ch == 3:
        node_to_delete = input("Node: ")
        g.delete_node(node_to_delete)
    elif ch == 4:
        u = input("From: ")
        v = input("To: ")
        g.delete_edge(u, v)
    elif ch == 5:
        g.display()
    elif ch == 6:
        g.display_adj_list(input("Node: "))
    elif ch == 7:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node: ")
        goal_node = goal_input if goal_input else None
        g.bfs_lr(start_node, goal_node)
    elif ch == 8:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node: ")
        goal_node = goal_input if goal_input else None
        g.bfs_rl(start_node, goal_node)
    elif ch == 9:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node: ")
        goal_node = goal_input if goal_input else None
        g.dfs_lr(start_node, goal_node)
    elif ch == 10:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node: ")
        goal_node = goal_input if goal_input else None
        g.dfs_rl(start_node, goal_node)
    elif ch == 11:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
