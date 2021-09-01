import socket

from threading import Thread

host = "127.0.0.1"

class Process:
    def __init__(self, i, port_range, cs_port, N=None, K=None, S=0, L=0, require_access=0):
        self.i              = i + 1          # This process id
        self.port_range     = port_range     # Port range, i.e. 40000, 50000, etc
        self.cs_port        = cs_port        # Critical section port
        self.N              = N              # Number of processes
        self.K              = K              # Constant number
        self.S              = S              # This process status
        self.L              = L              # Last process status
        self.require_access = require_access # If process require access to a shared resource        
        self.this_port      = self.port_range + self.i # This socket port

    # Send message to a process or shared resource
    def send_message(self, host, port, message):
        client_socket = socket.socket()
        client_socket.connect((host, port))
        client_socket.send(str.encode(message))
        server_response = client_socket.recv(1024)
        print(server_response.decode("utf-8"))
        client_socket.close()

    # Receive message from previus process
    def receive_message(self, port):
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.bind(("", port))
        socket_server.listen(1)
        sc, addr = socket_server.accept()
        message_receive = sc.recv(1024).decode("utf-8")
        sc.close()
        socket_server.close()

    """
    Dijkstra algorithm for mutual process exclusion
    """

    def subprocess_1(self):
        self.send_message(host, self.this_port) # Send S to (i + 1 mod k);

    def subprocess_2(self):
        if self.i == 0:                                 # If (i = 0) then
            self.receive_message(self.this_port+self.N) #    Receive L from N
        else:                                           # Else
            self.receive_message(self.this_port-1)      #    Receive L from i-1
                                                        # EndIf

    def subprocess_3(self, L, lap_number):
        # If require_Access == 0 or True
        if self.require_access == 0:                       # When need_access_to_critical_section Do
            if self.i == 1:                                #    If (i = 0) then
                if L == self.S:                            #        When ( L = S ) Do
                    print("\nP: {} IN CS".format(self.i))  #            go_to_critical_section();
                    message = "Process {} of {} accessed the critical section on lap {}" \
                        .format(self.i, self.K, lap_number)#            go_to_critical_section();
                    thread = self.send_message(host, self.cs_port, message) # go_to_critical_section();
                    Thread(target=thread).start()          #            go_to_critical_section();
                    self.S = (L + 1) % self.K              #            S = (L + 1) mod K;
                    self.L = L                             #            (custom implementation)
                                                           #         EndWhen
            else:                                          #    Else
                if L != self.S:                            #        When ( L <> S ) Do
                    print("\nP: {} IN CS".format(self.i))  #            go_to_critical_section();
                    message = "Process {} of {} accessed the critical section on lap {}" \
                        .format(self.i, self.K, lap_number)#            go_to_critical_section();
                    thread = self.send_message(host, self.cs_port, message) # go_to_critical_section();
                    Thread(target=thread).start()          #            go_to_critical_section();
                    self.S = L                             #            S = L;
                    self.L = L                             #            (custom implementation)
                                                           #        EndWhen
                                                           #    EndIf
                                                           # EndWhen
    """
    End Dijkstra algorithm for mutual process exclusion
    """

    # Dijkstra algorithm for mutual process exclusion
    def run_dijkstra_alg(self, L, lap_number):
        """
        # Sub process 1
        thread_1 = self.subprocess_1(self.i, self.K)
        #self.subprocess_1(self.i, self.K)

        # Sub process 2
        thread_2 = self.subprocess_2(self.i, self.N)
        #self.subprocess_2(self.i, self.N)
        """

        # Sub process 3
        self.subprocess_3(L, lap_number)
        """
        thread_3 = self.subprocess_3( \
            self.i, \
            self.S, \
            self.L, \
            self.require_access(), \
            self.K
        )
        """
        # Run the three subprocess simultaneously
        """
        Thread(target=thread_1).start()
        Thread(target=thread_2).start()
        Thread(target=thread_3).start()
        """
