#non - pre-emptive scheduling
#process :[arrival time,burst time,priority,pid]

def priority_scheduling(process_list):
    t = 0
    gantt = []
    completed = {}
    process_list.sort(key=lambda x: (x[0], x[2]))
    total_tat = 0
    total_wt = 0

    while process_list :
        available_processes = [p for p in process_list if p[0] <=t]
        if not available_processes:
            gantt.append("idle")
            t += 1
            continue
        else:
            available_processes.sort(key=lambda x: x[2])
            at, bt, priority, pid = available_processes.pop(0)
            process_list.remove((at, bt, priority, pid))
            gantt.append(pid)
            t += bt
            ct = t
            tat = ct - at
            wt = tat - bt
            completed[pid] = [at, bt,priority,ct,tat,wt]
            total_tat += tat
            total_wt += wt

    # Calculate averages
    num_processes = len(completed)
    avg_tat = total_tat / num_processes
    avg_wt = total_wt / num_processes


     # Print the Gantt chart
    print("Gantt Chart:", gantt)

    # Print process statistics in a simpler format
    print("\nPID\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for pid, stats in completed.items():
          print(f"{pid}\t{stats[0]}\t{stats[1]}\t{stats[2]}\t\t{stats[3]}\t\t{stats[4]}\t\t{stats[5]}")

    # Print average TAT and WT
    print("Average Turnaround Time:",avg_tat)
    print("Average Waiting Time:",avg_wt)


# Example usage
if __name__ == "__main__":
    process_list = [(0,8,3, "p1"), (1,2,4, "p2"), (3,4,4 ,"p3"), (4,1,5, "p4"), (5,6,2 ,"p5"),(6,5,6,"p6"),(10,1,1,"p7")]
    priority_scheduling(process_list)


