# CELL 1
from google.colab import files

uploaded = files.upload()

# CELL 2
import time

# List of uploaded files
file_list = list(uploaded.keys())

print("Files in DFS:", file_list)
print()

# Display content one by one
for file in file_list:
    print("Content of:", file)
    print("----------------------------------")
    
    content = uploaded[file].decode("utf-8")
    print(content)
    
    print("\n==================================\n")
    time.sleep(2)
