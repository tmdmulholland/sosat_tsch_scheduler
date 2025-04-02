def tsch_scheduler (no_of_channels, minimum_list, strong_dict):
    
    schedule = [[[]] * no_of_channels for colour in range(len(minimum_list))]

    for timeslot in range(len(minimum_list)):
        current_timeslot = minimum_list[timeslot]
        schedule_timeslot = schedule[timeslot]
        
        for edge in range(len(current_timeslot)):
            current_edge = current_timeslot[edge]
            channel = strong_dict[current_edge]

            schedule_timeslot[channel] = schedule_timeslot[channel] + [current_edge]

    return schedule