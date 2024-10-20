def no_preemption():
    processes = []
    n = int(input("enter a number: "))
    for i in range(n):
        pid = f'p{i+1}'
        priority = int(input(f"enter the priority for {pid}: "))
        arrival_time = int(input(f"enter arrival time for {pid}: "))
        brust_time = int(input(f"enter brust time for {pid}: "))
        processes.append({'pid': pid, 'priority': priority, 'arrival_time': arrival_time, 'brust_time': brust_time})
    processes.sort(key=lambda x: x['priority'])
    current_time = 0
    for process in processes:
        if current_time < process['arrival_time']:
            print(f"for idle {process['arrival_time'] - current_time} units")
            current_time = process['arrival_time']
        waiting_time = current_time - process['arrival_time']
        completion_time = current_time + process['brust_time']
        turnaround_time = completion_time - process['arrival_time'] 
        response_time = waiting_time
        print(f"Process {process['pid']}: Waiting Time = {waiting_time}, Completion Time = {completion_time}, Turnaround Time = {turnaround_time}, Response Time = {response_time}") 
        current_time = completion_time
no_preemption()
