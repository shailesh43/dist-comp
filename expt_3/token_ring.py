import threading
import time

MAX_ROUNDS = 8
current_round = 0


class Node:

    def __init__(self, node_id):
        self.node_id = node_id
        self.next_node = None
        self.has_token = False

    def set_next_node(self, node):
        self.next_node = node

    def receive_token(self):
        self.has_token = True

    def process(self):

        global current_round

        while current_round < MAX_ROUNDS:

            if self.has_token:

                print(f"Node {self.node_id} is using the token")

                time.sleep(1)

                print(f"Node {self.node_id} passing token to Node {self.next_node.node_id}")

                self.has_token = False
                self.next_node.receive_token()

                current_round += 1

            time.sleep(0.5)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.set_next_node(node2)
node2.set_next_node(node3)
node3.set_next_node(node4)
node4.set_next_node(node1)

node1.has_token = True

threads = []

for node in [node1, node2, node3, node4]:
    t = threading.Thread(target=node.process)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nToken Ring Simulation Finished")