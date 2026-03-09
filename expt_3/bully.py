class Process:

    def __init__(self, pid):
        self.pid = pid
        self.alive = True


def bully_election(processes, initiator):

    print(f"\nProcess {initiator.pid} starts the election")

    higher = [p for p in processes if p.pid > initiator.pid and p.alive]

    if not higher:
        print(f"Process {initiator.pid} becomes the new coordinator")
        return initiator

    for p in higher:
        print(f"Process {initiator.pid} sends election message to Process {p.pid}")

    new_initiator = max(higher, key=lambda x: x.pid)

    return bully_election(processes, new_initiator)


# Creating processes
processes = [
    Process(1),
    Process(2),
    Process(3),
    Process(4),
    Process(5)
]

# Simulating leader failure
processes[-1].alive = False

# Starting election
leader = bully_election(processes, processes[1])

print(f"\nLeader elected: Process {leader.pid}")
