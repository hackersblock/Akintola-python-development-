from datetime import datetime

#print the current time and task name
def print_time (task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Akintola'
print_time('first naame assigned')

for x in range(0,10):
    print_time(x)
print_time('loop completed')