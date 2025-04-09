import graph_tools as gt
import scheduler as sc
import visualisation as vis
import create_config as cc

# network = {
#     1: [2, 5],
#     2: [1, 3, 4],
#     3: [2, 5],
#     4: [2, 7],
#     5: [1, 3, 6],
#     6: [5],
#     7: [4, 8],
#     8: [7]
# }

# network = {
#     1: [2, 3, 4],
#     2: [1, 5, 6],
#     3: [1, 7, 8],
#     4: [1, 9, 10],
#     5: [2, 11, 12],
#     6: [2, 13, 14],
#     7: [3, 15, 16],
#     8: [3, 17],
#     9: [4, 18],
#     10: [4, 19, 20],
#     11: [5],
#     12: [5],
#     13: [6],
#     14: [6],
#     15: [7],
#     16: [7],
#     17: [8, 21, 22],
#     18: [9, 23],
#     19: [10],
#     20: [10],
#     21: [17],
#     22: [17],
#     23: [18, 24],
#     24: [23, 25],
#     25: [24]
# }

network = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1, 7, 8],
    4: [1, 9],
    5: [2, 10, 11],
    6: [2, 12],
    7: [3, 13],
    8: [3, 14],
    9: [4, 15],
    10: [5],
    11: [5],
    12: [6],
    13: [7],
    14: [8],
    15: [9, 16],
    16: [15]
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