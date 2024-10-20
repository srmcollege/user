def RoundRobin(process_list, time_quantum):
    t = 0
    gantt = []
    queue = process_list[:]
    completion_times = {}
    
    while queue:
        brust_time, pid = queue.pop(0)
        if brust_time > time_quantum:
            gantt.append(pid)
            t += time_quantum
            queue.append((brust_time - time_quantum, pid))
        else:
            gantt.append(pid)
            t += brust_time
            completion_times[pid] = t
    
    print("Gantt chart\n", gantt)
    print("Completion Times\n:")
    for pid, completion_time in completion_times.items():
        print(f"{pid}: {completion_time}")
process_list = [(8, "p1"), (2, "p2"), (7, "p3"), (3, "p4"), (5, "p5")]
time_quantum = 3
RoundRobin(process_list, time_quantum)
