# Threshold t1 and t2 Load Balancing Algorithm

# Example initial server loads
servers = [2, 4, 6, 3]

# Taking thresholds as input
threshold1 = int(input("Enter Threshold t1 (Normal limit): "))
threshold2 = int(input("Enter Threshold t2 (Critical limit): "))

def assign_request_to_server(request_id):

    for i in range(len(servers)):

        # Case 1: Server under normal load
        if servers[i] < threshold1:
            servers[i] += 1
            print(f"Request {request_id} assigned to Server {i}")
            print(f"Current Load: {servers[i]} (Below Threshold1)\n")
            return

        # Case 2: Server busy but still acceptable
        elif threshold1 <= servers[i] < threshold2:
            servers[i] += 1
            print(f"Server {i} is busy but accepting request {request_id}")
            print(f"Current Load: {servers[i]} (Between Threshold1 and Threshold2)\n")
            return

        # Case 3: Server overloaded
        else:
            print(f"Server {i} overloaded (Load = {servers[i]})")

    print("All servers overloaded. Request rejected.\n")


print("Initial Server Loads:", servers)
print()

# Simulate requests
for req in range(1, 6):
    assign_request_to_server(req)

print("Final Server Loads:", servers)
