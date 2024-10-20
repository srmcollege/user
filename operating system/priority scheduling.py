from time import sleep
mylist_1 = [["p1", 3, 0, 8], ["p2", 4, 1, 2], ["p3", 4, 3, 4], ["p4", 5, 4, 1], ["p5", 2, 5, 6], ["p6", 6, 6, 5], ["p7", 7, 10, 1]]
print("Initial List:")
print(mylist_1)
sleep(0.5)
mylist_2 = sorted(mylist_1, key=lambda x: x[1])
print("Sorted by priority:")
print(mylist_2)
sleep(0.5)
current_time = 0
for i in range(len(mylist_2)):
    arrival_time = mylist_2[i][2]
    burst_time = mylist_2[i][3]
    if current_time < arrival_time:
        current_time = arrival_time
    completion_time = current_time + burst_time
    mylist_2[i].append(completion_time)
    current_time = completion_time
    print(f"Process {mylist_2[i][0]}: Completion Time = {completion_time}")
    sleep(0.5)
print("After calculating completion times:")
print(mylist_2)
sleep(0.5)
for i in range(len(mylist_2)):
    turnaround_time = mylist_2[i][4] - mylist_2[i][2]
    mylist_2[i].append(turnaround_time)
    print(f"Process {mylist_2[i][0]}: Turnaround Time = {turnaround_time}")
    sleep(0.5)
print("After calculating turnaround times:")
print(mylist_2)
sleep(0.5)
for i in range(len(mylist_2)):
    waiting_time = mylist_2[i][5] - mylist_2[i][3]
    mylist_2[i].append(waiting_time)
    print(f"Process {mylist_2[i][0]}: Waiting Time = {waiting_time}")
    sleep(0.5)

print("After calculating waiting times:")
print(mylist_2)
sleep(1)
print("id\tpriority\tarrival_time\tburst_time\tcompletion_time\tturnaround_time\twaiting_time")
for i in range(len(mylist_2)):
    print(f"{mylist_2[i][0]}\t{mylist_2[i][1]}\t{mylist_2[i][2]}\t{mylist_2[i][3]}\t{mylist_2[i][4]}\t{mylist_2[i][5]}\t{mylist_2[i][6]}")
    
print("Your Non-Preemptive Priority Scheduling Algorithm Is Completed")
