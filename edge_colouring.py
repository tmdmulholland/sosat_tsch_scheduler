def find_edges(graph):
    edges = []
    seen_edges = set()
    for u, neighbors in graph.items():
        for v in neighbors:
            if (u, v) not in seen_edges and (v, u) not in seen_edges:
                edges.append((u, v))
                seen_edges.add((u, v))

    return edges



def strong_edge_colouring(graph):
    edges = find_edges(graph)

    edge_sets= {}
    channel_offset = 0

    while edges:
        current_set = set()
        remaining_edges = []
        used_nodes = set()
        
        for edge in edges:
            x, y = edge
            if not ({x, y} & used_nodes):
                current_set.add(edge)
                used_nodes.update(graph[x] + graph[y])
            else:
                remaining_edges.append(edge)
        
        for edge in current_set:
            edge_sets[edge] = channel_offset
        
        channel_offset += 1
        edges = remaining_edges

    return edge_sets



def minimum_edge_colouring(graph):
    edges = find_edges(graph)

    max_degree = 0
    for neighbors in graph.values():
        if len(neighbors) > max_degree:
            max_degree = len(neighbors)

    colour_groups = [[] for colour in range(max_degree + 1)]
    node_colours = {}
    
    node_colours = graph.copy()
    node_colours.update((key, set()) for key in node_colours)

    for u, v in edges:
        for colour in range(0, max_degree + 1):
            if colour not in node_colours[u] and colour not in node_colours[v]:
                colour_groups[colour].append((u, v))
                node_colours[u].add(colour)
                node_colours[v].add(colour)
                break

    colour_groups = [x for x in colour_groups if x != []]
    
    return colour_groups