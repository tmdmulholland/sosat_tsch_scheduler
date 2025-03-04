import edge_colouring as ec
import scheduler as sc
import visualisation as vis

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

minimum_coloured_edges = ec.minimum_edge_colouring(graph)
strong_coloured_edges = ec.strong_edge_colouring(graph)

channels_required = max(strong_coloured_edges.values()) + 1
no_of_channels = 16

if channels_required > no_of_channels:
    print(f'Error: {channels_required} channels required, only {no_of_channels} available')
    exit()

schedule = sc.tsch_scheduler(no_of_channels, minimum_coloured_edges, strong_coloured_edges)

vis.schedule_table(schedule, no_of_channels)
vis.plot_graph(graph)