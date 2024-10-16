class Process:
    def __init__(self, label, burst_time, arrival_time, queue_id, priority):
        self.label = label
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.queue_id = queue_id
        self.priority = priority
        self.remaining_time = burst_time
        self.start_time = -1
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1

    def __str__(self):
        return (f"{self.label}; {self.burst_time}; {self.arrival_time}; {self.queue_id}; "
                f"{self.priority}; {self.waiting_time}; {self.completion_time}; "
                f"{self.response_time}; {self.turnaround_time}")
