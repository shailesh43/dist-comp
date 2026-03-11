import time
import heapq

class Process:

    def __init__(self, pid, total):
        self.pid = pid
        self.total = total
        self.clock = 0
        self.queue = []
        self.reply_count = 0

    def request_cs(self):

        self.clock += 1
        timestamp = self.clock

        print(f"Process {self.pid} requesting CS at time {timestamp}")

        heapq.heappush(self.queue, (timestamp, self.pid))

        return timestamp

    def receive_request(self, timestamp, pid):

        self.clock = max(self.clock, timestamp) + 1

        print(f"Process {self.pid} received request from P{pid}")

        heapq.heappush(self.queue, (timestamp, pid))

    def send_reply(self, pid):

        print(f"Process {self.pid} sends REPLY to P{pid}")

    def receive_reply(self):

        self.reply_count += 1

    def enter_cs(self):

        if self.reply_count == self.total - 1:

            print(f"Process {self.pid} ENTERS critical section")

            time.sleep(1)

            print(f"Process {self.pid} EXITS critical section\n")

            heapq.heappop(self.queue)



processes = [Process(i,3) for i in range(3)]

timestamps = []

for p in processes:
    timestamps.append(p.request_cs())

for i in range(3):
    for j in range(3):
        if i != j:
            processes[j].receive_request(timestamps[i], i)
            processes[j].send_reply(i)

for p in processes:
    for _ in range(2):
        p.receive_reply()

for p in processes:
    p.enter_cs()