from prettytable import PrettyTable
import networkx as nx
import matplotlib.pyplot as plt

def schedule_table(schedule, no_of_channels):
    schedule_table = PrettyTable()

    headers = [f'Slot {i}' for i in range(len(schedule))]
    schedule_table.add_column('Channel Offset', list(range(no_of_channels))) 

    for column in range(len(schedule)):
        current_column = schedule[column]
        formatted_row = [str(cell) if cell else '-' for cell in current_column]
        schedule_table.add_column(headers[column], formatted_row)

    schedule_txt = open('outputs/schedule.txt', 'w')
    schedule_txt.write(str(schedule_table))
    schedule_txt.close()
    # print(schedule_table)
    


def plot_graph(graph):
    graph_visual = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            graph_visual.add_edge(node, neighbor)

    plt.figure(figsize=(10, 6))
    
    pos = nx.spring_layout(graph_visual)
    colors = ['orangered' if node_name == 1 else 'lightblue' for node_name in list(graph_visual.nodes)]
    nx.draw(graph_visual, pos=pos, with_labels=True, node_color=colors, edge_color='gray', node_size=750, font_size=12)

    plt.savefig("outputs/graph.png")
    # plt.show()