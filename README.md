# Dijkstra algorithm for mutual exclusion

## Execution
1. Open a terminal and run ***server_critical_section.py***
2. Then open another terminal and run ***client_processes.py***

## Background

This is an implementation of Stable Algorithm for Mutual Exclusion (processes concurrence) in a distributed system, proposed by **Edsger W. Dijkstra** in 1974.

This implementation does not link processes trough socket, for this demonstration, processes are stored in a simple list.

## Algorithm resume

	When need_access_to_critical_section Do
		If (i = 0) then
			When ( L = S ) Do
				go_to_critical_section();
				S = (L + 1) mod K;
			EndWhen
		Else
			When ( L <> S ) Do
				go_to_critical_section();
				S = L;
			EndWhen
		EndIf
	EndWhen
	
Since processes are stored in a list, we can skip a some steps.

## Algorithm details
- Synchronus comunication
- Ring logic topology
- Solution consider **N processes**, ranged from **0 to N - 1**

**Variables used:**

- i = Process id
- S = Status of process i
- L = Last process status
- K = Constant bigger or iqual to N

## Notes
In the source code, some variables and methods are defined but not used, they remains for future implementations and changes.

## Credits
- [Socket Server with Multiple Clients | Multithreading | Python](https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/) 
- [Python Multithreading Example: Create Socket Server with Multiple Clients](https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/) 
- [Socket Programming with Multi-threading in Python](https://www.geeksforgeeks.org/socket-programming-multi-threading-python/) 
- [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/#handling-multiple-connections) 
- [Real Python](https://github.com/realpython/materials/tree/master/python-sockets-tutorial) 
- [Self-Stabilizing Mutual Exclusion Dijkstra Algorithm](https://www.youtube.com/watch?v=7wEakmGYMqw&pp=ugMICgJlcxABGAE%3D) 
- [Proof of Self-Stabilizing Mutual Exclusion Dijkstra Algorithm](https://www.youtube.com/watch?v=cWSmOqVMesg) 