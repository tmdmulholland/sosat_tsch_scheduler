import json
import graph_tools as gt

def create_config_json(network, schedule, no_of_nodes, slotframe_length, duration, seed, num_runs, app_packet_period_sec):

# run with GUI
    # header = """{
    #     "WEB_ENABLED": true,
    #     "NODE_TYPES": [
    #         {
    #             "NAME": "node",
    #             "START_ID": 1,
    #             "APP_PACKETS": {"TO_ID": 1}
    #         }
    #     ]
    # }"""

# run in terminal
    header = """{
        "NODE_TYPES": [
            {
                "NAME": "node",
                "START_ID": 1,
                "APP_PACKETS": {"TO_ID": 1}
            }
        ]
    }"""

    base_json = json.loads(header)
    base_json.update({
        "SIMULATION_DURATION_SEC": duration,
        "SIMULATION_SEED": seed,
        "SIMULATION_NUM_RUNS": num_runs,
        "CONNECTIONS": create_connections(network)
    })
    base_json["NODE_TYPES"][0].update({
        "COUNT": no_of_nodes,
        "APP_PACKETS": {"APP_PACKET_PERIOD_SEC": app_packet_period_sec, "TO_ID": 1}
    })

    custom_json = base_json.copy()
    next_hops = gt.breadth_first_search(network, 1)
    schedule_dict = create_schedule_entry(schedule, next_hops)
    custom_json.update({"SCHEDULE": schedule_dict})
    
    custom_json["SCHEDULING_ALGORITHM"] =  "customSchedule"
    custom_json["ROUTING_ALGORITHM"] = "NullRouting"
    custom_json["TSCH_SCHEDULE_CONF_DEFAULT_LENGTH"] = slotframe_length
    custom_json["NEXT_HOP"] = next_hops

    with open('outputs/config_custom.json', 'w') as outfile:
        outfile.write(json.dumps(custom_json, indent=4))


    orch_json = base_json.copy()
    orch_json["SCHEDULING_ALGORITHM"] =  "Orchestra"    

    with open('outputs/config_orch.json', 'w') as outfile:
        outfile.write(json.dumps(orch_json, indent=4))



def create_connections(network):
    connections = []
    for from_id, to_ids in network.items():
        for to_id in to_ids:
            connections.append({"FROM_ID": from_id, "TO_ID": to_id})

    return connections



def create_schedule_entry(schedule, next_hops):
    schedule_dict = {}

    for ts, timeslot in enumerate(schedule):
        for co, channel_offset in enumerate(timeslot):
            for node1, node2 in channel_offset:
                schedule_dict.setdefault(node1, {}).setdefault(node2, {})
                schedule_dict.setdefault(node2, {}).setdefault(node1, {})

                if next_hops.get(str(node1)) >= node2:
                    type1, type2 = 1, 2
                else:
                    type1, type2 = 2, 1
                
                schedule_dict[node1][node2] = {"ts": ts, "co": co, "type": type1}
                schedule_dict[node2][node1] = {"ts": ts, "co": co, "type": type2}

    return schedule_dict