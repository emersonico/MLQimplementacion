from queue_scheduler import QueueScheduler
from process import Process

class MLQScheduler:
    def __init__(self, queue_config):
        self.queues = [QueueScheduler(policy, time_quantum) for policy, time_quantum in queue_config]
        self.processes = []

    def add_process(self, process):
        self.queues[process.queue_id - 1].add_process(process)
        self.processes.append(process)

    def run(self):
        current_time = 0
        iteration_count = 0
        max_iterations = 10000

        while any(not q.process_queue.empty() for q in self.queues) and iteration_count < max_iterations:
            for queue in self.queues:
                if not queue.process_queue.empty():
                    process, new_time = queue.execute_process(current_time)
                    if process:
                        current_time = new_time
                        self._calculate_times(process, current_time)
                        break
            iteration_count += 1

        if iteration_count >= max_iterations:
            print("Se alcanzó el número máximo de iteraciones.")

    def _calculate_times(self, process, current_time):
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        if process.response_time == -1:
            process.response_time = process.start_time - process.arrival_time

    def print_results(self, file_name):
        with open(file_name, 'w') as file:
            for process in self.processes:
                file.write(str(process) + '\n')
            avg_wt = sum(p.waiting_time for p in self.processes) / len(self.processes)
            avg_ct = sum(p.completion_time for p in self.processes) / len(self.processes)
            avg_rt = sum(p.response_time for p in self.processes) / len(self.processes)
            avg_tat = sum(p.turnaround_time for p in self.processes) / len(self.processes)
            file.write(f"WT={avg_wt:.2f}; CT={avg_ct:.2f}; RT={avg_rt:.2f}; TAT={avg_tat:.2f};\n")

