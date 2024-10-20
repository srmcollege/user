List of tasks with their processing times
tasks = [["p1", 4], ["p2", 5], ["p3", 7], ["p4", 6]]
print("Initial tasks:", tasks)
time_quantum = 3
queue = tasks.copy()
scheduled_tasks = []
while queue:
    task = queue.pop(0)  
    task_name, remaining_time = task
    print(f"Processing {task_name} with remaining time {remaining_time}")
    if remaining_time > time_quantum:
        remaining_time -= time_quantum
        queue.append([task_name, remaining_time])
    scheduled_tasks.append((task_name, remaining_time))
print("Remaining tasks after scheduling:", scheduled_tasks)
