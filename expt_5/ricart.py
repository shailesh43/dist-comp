import time

class Process:

    def __init__(self, pid, total):
        self.pid = pid
        self.total = total
        self.clock = 0
        self.reply_count = 0

    def request_cs(self):

        self.clock += 1

        print(f"Process {self.pid} requests CS at time {self.clock}")

        return self.clock

    def receive_request(self, timestamp, pid):

        self.clock = max(self.clock, timestamp) + 1

        print(f"Process {self.pid} received request from P{pid}")

        self.send_reply(pid)

    def send_reply(self, pid):

        print(f"Process {self.pid} sends REPLY to P{pid}")

    def receive_reply(self):

        self.reply_count += 1

    def enter_cs(self):

        if self.reply_count == self.total - 1:

            print(f"Process {self.pid} ENTERS critical section")

            time.sleep(1)

            print(f"Process {self.pid} EXITS critical section\n")



processes = [Process(i,3) for i in range(3)]

timestamps = []

for p in processes:
    timestamps.append(p.request_cs())

for i in range(3):
    for j in range(3):
        if i != j:
            processes[j].receive_request(timestamps[i], i)

for p in processes:
    for _ in range(2):
        p.receive_reply()

for p in processes:
    p.enter_cs()