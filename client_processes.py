import time

from random import randint

from library.process import Process

# Generate up to 10 processes
processes = list()
for i in range(randint(5, 10)):
    processes.append(Process(i=i, port_range=60000, cs_port=61000))

N = len(processes) - 1 # Number of processes
K = N + 1

# Add current number of processes, K constant and previus process to each process
for i in range(len(processes)):
    processes[i].N = N
    processes[i].K = K

# Display generated processes
print("\n{} processes\n".format(len(processes)))
for i in processes:
    print(
        "id: {}, S: {}, L: {}, N: {}, K: {}, this port: {}"
        .format(i.i, i.S, i.L, i.N, i.K, i.this_port)
    )
print()

if __name__ == "__main__":
    count = 0
    top   = 3 # Max number of laps
    while count != top:
        print("\n########## Lap {} ##########\n".format(count+1))
        
        for i in range(len(processes)):
            processes[i].require_access = randint(0, 1) # Random "require access" for each process

            L = processes[i-1].S # Set last status
            if i == len(processes)-1: # If this is the last process
                L = processes[0].S    # Last status = status of first process
            
            processes[i].run_dijkstra_alg(L, count+1) # Run Dijkstra algorithm
            
            print(
                "id: {}, S: {}, L: {}, N: {}, K: {}, this port: {}"
                .format(
                    processes[i].i,
                    processes[i].S,
                    processes[i].L,
                    processes[i].N,
                    processes[i].K,
                    processes[i].this_port
                )
            )
            
            time.sleep(0.5)
        count += 1
