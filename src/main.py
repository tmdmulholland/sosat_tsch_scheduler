import graph_tools as gt
import scheduler as sc
import visualisation as vis
import create_config as cc

network = {
    1: [2, 5],
    2: [1, 3, 4],
    3: [2, 5],
    4: [2, 7],
    5: [1, 3, 6],
    6: [5],
    7: [4, 8],
    8: [7]
}

minimum_coloured_edges = gt.minimum_edge_colouring(network)
strong_coloured_edges = gt.strong_edge_colouring(network)

no_of_nodes = len(network)
channels_required = max(strong_coloured_edges.values()) + 1
no_of_channels = 16

if channels_required > no_of_channels:
    print(f'Error: {channels_required} channels required, only {no_of_channels} available')
    exit()

schedule = sc.tsch_scheduler(no_of_channels, minimum_coloured_edges, strong_coloured_edges)
# print(schedule)

slotframe_length = len(schedule)
next_hop_to_1 = gt.breadth_first_search(network, 1)
duration = 500
seed = 50
num_runs = 10
app_packet_period_sec = 0.5
cc.create_config_json(network, schedule, no_of_nodes, slotframe_length, duration, seed, num_runs, app_packet_period_sec)

vis.schedule_table(schedule, no_of_channels)
vis.plot_graph(network)