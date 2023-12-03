import sys
import time

seconds = int(sys.argv[-1])

for i in range(seconds):
    print(seconds - i, "seconds left")
    time.sleep(1)
print("Finish")
