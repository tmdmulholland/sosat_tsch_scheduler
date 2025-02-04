def strong_edge_colouring(graph):
    edges = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if (neighbor, node) not in edges:
                edges.add((node, neighbor))

    edge_list = list(edges)
    edge_sets = []

    while edge_list:
        current_set = set()
        remaining_edges = []
        used_nodes = set()
        
        for edge in edge_list:
            x, y = edge
            if not ({x, y} & used_nodes):
                current_set.add(edge)
                used_nodes.update(graph[x] + graph[y])
            else:
                remaining_edges.append(edge)
        
        edge_sets.append(current_set)
        edge_list = remaining_edges

    return edge_sets

graph = {
    1: [2, 5],
    2: [1, 3, 4],
    3: [2, 5],
    4: [2, 7],
    5: [1, 3, 6],
    6: [5],
    7: [4, 8],
    8: [7]
}

coloured_edges = strong_edge_colouring(graph)
for i, edge_set in enumerate(coloured_edges):
    print(f"Set {i+1}: {edge_set}")