#Tower of Hanoi

def tower_of_hanoi(n,source,helper,destination):
    if n==1:
        print("Move dist 1 from",source,"to",destination)
        return
    tower_of_hanoi(n-1,source,destination,helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1,helper,source,destination)

#Number of disk

n=int(input("Enter number of disks: "))
#Solve Tower of Hanoi
tower_of_hanoi(n,"A","B","C")

#Total number of moves
print("Total moves: " ,(2**n)-1)
