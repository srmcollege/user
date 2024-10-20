process=["p0","p1","p2","p3","p4"]
allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
maximum = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
remaining_time = []
for i in range (len(process)):
    row = []
    for j in range(3):
        a = maximum[i][j] - allocation[i] [j]
        row.append(a)
    remaining_time.append(row)
print(remaining_time)
for i in remaining_time:
    print(i)
