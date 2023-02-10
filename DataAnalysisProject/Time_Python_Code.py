import time
from datetime import datetime

script_start_time=datetime.now()
start_time = time.time()

for i in range(10000):
    j= 10+i

end_time=time.time()
script_end_time=datetime.now()

final_time=end_time-start_time
script_time=script_end_time-script_start_time

print(final_time)
print(script_time)