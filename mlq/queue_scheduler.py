import queue
from process import Process

class QueueScheduler:
    def __init__(self, policy, time_quantum=None):
        self.policy = policy
        self.time_quantum = time_quantum
        self.process_queue = queue.Queue()

    def add_process(self, process):
        self.process_queue.put(process)

    def execute_process(self, current_time):
        if self.process_queue.empty():
            return None, current_time
        if self.policy == 'RR':
            return self._round_robin(current_time)
        elif self.policy == 'SJF':
            return self._shortest_job_first(current_time)
        elif self.policy == 'FCFS':
            return self._first_come_first_served(current_time)
        elif self.policy == 'STCF':
            return self._shortest_time_to_completion(current_time)

    def _round_robin(self, current_time):
        if self.process_queue.empty():
            return None, current_time
        process = self.process_queue.get()
        print(f"Ejecutando {process.label} con RR (restante: {process.remaining_time})")

        # Si si es la primera vez que se ejecuta  registra el tiempo de inicio
        if process.start_time == -1:
            process.start_time = current_time

        # actualiza el tiempo de respuesta si es la primera vez que se ejecuta
        if process.response_time == -1:
            process.response_time = current_time - process.arrival_time

        # ejecución del proceso según el quantum
        execution_time = min(process.remaining_time, self.time_quantum)
        process.remaining_time -= execution_time
        current_time += execution_time

        if process.remaining_time > 0:
            self.process_queue.put(process)  # VOlver a colocar en la cola si no ha terminado
        else:
            process.completion_time = current_time

        print(f"Proceso {process.label} completado: {process.completion_time}, restante: {process.remaining_time}")
        return process, current_time
        ...

    def _shortest_job_first(self, current_time):
        if self.process_queue.empty():
            return None, current_time
        # Encontrar el proceso con el menor burst time
        shortest_process = min(self.process_queue.queue, key=lambda p: p.burst_time)
        self.process_queue.queue.remove(shortest_process)

        if shortest_process.start_time == -1:
            shortest_process.start_time = current_time

        execution_time = shortest_process.burst_time
        shortest_process.remaining_time = 0
        current_time += execution_time
        shortest_process.completion_time = current_time

        print(f"Ejecutando {shortest_process.label} con SJF, completado a: {shortest_process.completion_time}")
        return shortest_process, current_time
      

    def _first_come_first_served(self, current_time):
        if self.process_queue.empty():
            return None, current_time
        process = self.process_queue.get()
        print(f"Ejecutando {process.label} con FCFS (restante: {process.remaining_time})")
        
        if process.start_time == -1:
            process.start_time = current_time

        execution_time = process.remaining_time
        process.remaining_time = 0
        current_time += execution_time
        process.completion_time = current_time

        print(f"Proceso {process.label} completado: {process.completion_time}")
        return process, current_time
        ...

    def _shortest_time_to_completion(self, current_time):
        if self.process_queue.empty():
            return None, current_time
        # Encontrar el proceso con el menor tiempo restante
        stcf_process = min(self.process_queue.queue, key=lambda p: p.remaining_time)
        self.process_queue.queue.remove(stcf_process)

        print(f"Ejecutando {stcf_process.label} con STCF (restante: {stcf_process.remaining_time})")

        if stcf_process.start_time == -1:
            stcf_process.start_time = current_time

        execution_time = stcf_process.remaining_time
        stcf_process.remaining_time = 0
        current_time += execution_time
        stcf_process.completion_time = current_time

        print(f"Proceso {stcf_process.label} completado: {stcf_process.completion_time}")
        return stcf_process, current_time

