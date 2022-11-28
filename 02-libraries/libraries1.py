import sys
import time

# seconds = int(sys.argv[1])
# time.sleep(seconds)
# print('\a')


seconds = int(sys.argv[1])
for second in range(seconds):
    time.sleep(1)
    print(second)

print('\a')
