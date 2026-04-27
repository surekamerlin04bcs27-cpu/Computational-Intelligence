import heapq
from collections import deque
class Graph:
    def __init__(self):
        # Stores graph as an adjacency list: {node: [(neighbor, cost), ...]}
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
                print(f"Edge ({u}, {v}) already exists")
            else:
                self.graph[u].append((v, cost))
                self.graph[v].append((u, cost)) # Assuming an undirected graph
                print(f"Edge ({u}, {v}) with cost {cost} added")
        else:
            print("Add nodes first")
    def delete_node(self, node):
        if node in self.graph:
            self.graph.pop(node)
            for n in self.graph:
                self.graph = [(x, c) for x, c in self.graph if x != node]
            print(f"Node '{node}' deleted")
        else:
            print("Node not found")
    def delete_edge(self, u, v):
        if u in self.graph:
            initial_count = len(self.graph[u])
            self.graph[u] = [(x, c) for x, c in self.graph[u] if x != v]
            self.graph[v] = [(x, c) for x, c in self.graph[v] if x != u]
            if len(self.graph[u]) < initial_count:
                print("Edge deleted")
            else:
                print("Edge not found")
        else:
            print("Edge not found")
    def display(self):
        print("\nGraph:")
        for node in self.graph:
            print(node, "-", self.graph[node])
    def display_adj_list(self, node):
        if node in self.graph:
            print(node, "-", self.graph[node])
        else:
            print("Node not found")
    def _print_step(self, iteration, fringe_items, explored):
        # Helper to print the current state of search for BFS/DFS
        fringe_str = str([item[0] for item in fringe_items])
        explored_str = str(sorted(list(explored)))
        print(f"{iteration:<10} | {fringe_str:<30} | {explored_str}")
    # BFS and DFS methods from your original code (omitted for brevity)
    # ...
    def ucs(self, start, goal):
        """
        Implements Uniform Cost Search (UCS) using a priority queue (heapq).
        """
        if start not in self.graph or goal not in self.graph:
            print("Start or goal node not found in graph.")
            return None
        # The frontier is a priority queue: (cost, node, path)
        frontier = [(0, start, [start])]
        heapq.heapify(frontier) # Initialize as a min-heap
        explored = set()
        iteration = 1
        print(f"\n{'Iter':<10} | {'Fringe (Priority Queue)':<30} | {'Explored Set'}")
        print("-" * 70)
        while frontier:
            # Pop the node with the lowest cumulative cost (priority)
            current_cost, current_node, path = heapq.heappop(frontier)
            # Print state for tracing (using helper function adapted for UCS tuple format)
            # Note: The fringe visualization here is tricky with a heap,
            # so we just show the popped node in the iteration count for simplicity in tracing
            print(f"{iteration:<10} | {str([item[1] for item in frontier] + [current_node]):<30} | {str(sorted(list(explored)))}")
            iteration += 1
            if current_node == goal:
                print(f"\nGoal node '{goal}' reached!")
                print(f"Optimal Path: {' -> '.join(path)}")
                print(f"Total Cost: {current_cost}")
                return path, current_cost
            if current_node not in explored:
                explored.add(current_node)
                # Explore neighbors
                for neighbor, step_cost in self.graph[current_node]:
                    if neighbor not in explored:
                        new_cost = current_cost + step_cost
                        new_path = path + [neighbor]
                        # Push neighbor to frontier as (new_cost, neighbor, new_path)
                        heapq.heappush(frontier, (new_cost, neighbor, new_path))
                        # The heapq automatically handles keeping the lowest cost item at the top
                        # If a shorter path is found later, it will be processed first due to priority
        print(f"\nGoal node '{goal}' not found.")
        return None
g = Graph()
while True:
    print("\nMENU")
    print("1 Add Node")
    print("2 Add Edge")
    print("3 Delete Node")
    print("4 Delete Edge")
    print("5 Display Graph")
    print("6 Display Adjacency List")
    print("7 BFS Left to Right ")
    print("8 BFS Right to Left ")
    print("9 DFS Left to Right ")
    print("10 DFS Right to Left ")
    print("11 Uniform Cost Search (UCS)") # Added UCS menu option
    print("12 Exit") # Updated Exit option
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if ch == 1:
        count = int(input("How many nodes do you want to add? "))
        for _ in range(count):
            node = input("Node: ")
            g.add_node(node)
    elif ch == 2:
        count = int(input("How many edges do you want to add? "))
        for _ in range(count):
            u = input("From: ")
            v = input("To: ")
            cost = int(input("Cost (0 if none): "))
            g.add_edge(u, v, cost)
    elif ch == 3:
        g.delete_node(input("Node: "))
    elif ch == 4:
        u = input("From: ")
        v = input("To: ")
        g.delete_edge(u, v)
    elif ch == 5:
        g.display()
    elif ch == 6:
        g.display_adj_list(input("Node: "))
    elif ch == 7:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.bfs_lr(s, gl if gl else None)
    elif ch == 8:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.bfs_rl(s, gl if gl else None)
    elif ch == 9:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.dfs_lr(s, gl if gl else None)
    elif ch == 10:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.dfs_rl(s, gl if gl else None)
    elif ch == 11: # Handle UCS
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.ucs(s, gl)
    elif ch == 12: # Handle Exit
        print("Program terminated")
        break
    else:
        print("Invalid choice")
