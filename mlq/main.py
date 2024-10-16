from mlq_scheduler import MLQScheduler
from utils import read_input

queue_config = [
    ('RR', 1),
    ('RR', 3),
    ('SJF', None)
]

if __name__ == "__main__":
    mlq_scheduler = MLQScheduler(queue_config)
    process_list = read_input('mlq003.txt')
    for process in process_list:
        mlq_scheduler.add_process(process)

    mlq_scheduler.run()
    mlq_scheduler.print_results('mlq001_output.txt')
