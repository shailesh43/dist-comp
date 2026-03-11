import threading
import queue
import time

# Create separate message queues for each client
client_queues = {
    "student1": queue.Queue(),
    "student2": queue.Queue(),
    "student3": queue.Queue()
}

# Multicast group
multicast_group = ["student1", "student3"]


# Server function
def server():
    time.sleep(1)
    print("\nServer Started...\n")

    # Unicast message
    client_queues["student1"].put("Unicast: Assignment reminder for Student1")

    # Multicast message
    for student in multicast_group:
        client_queues[student].put("Multicast: Project meeting for selected students")

    # Broadcast message
    for student in client_queues:
        client_queues[student].put("Broadcast: Class cancelled tomorrow")

    print("Messages sent by server.\n")


# Client function
def client(name):
    print(f"{name} started and waiting for messages...")

    while True:
        try:
            message = client_queues[name].get(timeout=5)
            print(f"{name} received: {message}")

        except queue.Empty:
            break


# Threads
server_thread = threading.Thread(target=server)

student1_thread = threading.Thread(target=client, args=("student1",))
student2_thread = threading.Thread(target=client, args=("student2",))
student3_thread = threading.Thread(target=client, args=("student3",))


# Start threads
student1_thread.start()
student2_thread.start()
student3_thread.start()
server_thread.start()


# Wait for completion
server_thread.join()
student1_thread.join()
student2_thread.join()
student3_thread.join()

print("\nGroup Communication Simulation Complete.")