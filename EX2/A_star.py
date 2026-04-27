import heapq
class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.node_names = set()
        self.is_directed = directed
    def build_graph(self):
        # 1. Define Nodes
        nodes_input = input("Enter node names (comma separated, e.g., A,B,C): ")
        self.node_names = {name.strip() for name in nodes_input.split(',')}
        self.graph = {name: [] for name in self.node_names}
        # 2. Define Connections (Replacing manual add_edge calls)
        print("\nEnter connections as 'Source, Destination, Weight' (Type 'done' to finish):")
        while True:
            entry = input("> ")
            if entry.lower() == 'done': break
            try:
                parts = [x.strip() for x in entry.split(',')]
                if len(parts) == 3:
                    u, v, w = parts[0], parts[1], float(parts[2])
                    if u in self.node_names and v in self.node_names:
                        self.graph[u].append((v, w))
                        if not self.is_directed:
                            self.graph[v].append((u, w))
                    else:
                        print("Error: One or both nodes not found in graph.")
            except ValueError:
                print("Invalid format. Use: Source, Destination, Weight")
    def display(self):
        print("\n--- Current Graph Structure ---")
        for n in sorted(self.graph.keys()):
            connections = [f"({neighbor}, {weight})" for neighbor, weight in self.graph[n]]
            print(f"{n} -> {', '.join(connections) if connections else 'None'}")
    def astar_search(self, start, goal):
        if start not in self.node_names or goal not in self.node_names:
            return print("Start or Goal node not found.")
        # Collect Heuristics
        print(f"\n--- Enter Heuristic values for Goal: {goal} ---")
        h = {}
        for node in sorted(list(self.node_names)):
            h[node] = float(input(f"  h({node}): "))
        fringe = []
        # (f_score, g_score, current_node, path)
        heapq.heappush(fringe, (h[start], 0, start, [start]))
        g_scores = {node: float('inf') for node in self.node_names}
        g_scores[start] = 0
        explored = []
        step = 1
        print(f"\n{'Step':<5} | {'Node':<5} | {'Intermediate Calculations & Neighbor Updates'}")
        print("-" * 90)
        while fringe:
            f_val, g_val, current, path = heapq.heappop(fringe)
            if current == goal:
                print(f"\nGoal Reached!")
                print(f"Path: {' -> '.join(path)}")
                print(f"Total Cost: {g_val}")
                return
            if current in explored: continue
            explored.append(current)
            print(f"{step:<5} | {current:<5} | Expanding {current}:")
            for neighbor, weight in self.graph[current]:
                if neighbor in explored:
                    print(f"{'':<13} | -- Skip {neighbor} (Already Explored)")
                    continue
                tentative_g = g_val + weight
                f_score = tentative_g + h[neighbor]
                # Intermediate Step Logging
                print(f"{'':<13} | -> Neighbor {neighbor}: g={g_val}+{weight}={tentative_g}, f={tentative_g}+{h[neighbor]}={f_score}")
                if tentative_g < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g
                    heapq.heappush(fringe, (f_score, tentative_g, neighbor, path + [neighbor]))
            # Show current fringe status for transparency
            fringe_view = [f"({n}:{f})" for f, g, n, p in sorted(fringe)]
            print(f"{'':<13} | Fringe Status: {', '.join(fringe_view)}")
            print("-" * 90)
            step += 1
        print("No path exists between these nodes.")
def main():
    print("--- Graph Search Tool ---")
    choice = input("1. Undirected\n2. Directed\nSelect: ")
    is_directed = True if choice == '2' else False
    g = Graph(directed=is_directed)
    g.build_graph()
    while True:
        print("\n1. Display Graph\n2. Run A* Search\n0. Exit")
        op = input("Choice: ")
        if op == '1':
            g.display()
        elif op == '2':
            s = input("Enter Start Node: ")
            target = input("Enter Goal Node: ")
            g.astar_search(s, target)
        elif op == '0':
            break
if __name__ == "__main__":
    main()
