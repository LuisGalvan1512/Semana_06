from collections import deque

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.remaining_time = burst_time
        self.total_time = 0
        self.waiting_time = 0

    def __str__(self):
        return f"Process {self.pid}"

class RoundRobinScheduler:
    def __init__(self, time_quantum):
        self.time_quantum = time_quantum
        self.queue = deque()
        self.current_time = 0
        self.completed_processes = []

    def add_process(self, pid, burst_time):
        self.queue.append(Process(pid, burst_time))

    def run(self):
        while self.queue:
            process = self.queue.popleft()

            execution_time = min(self.time_quantum, process.remaining_time)
            self.current_time += execution_time
            process.remaining_time -= execution_time
            process.total_time = self.current_time

            print(f"{process} executed for {execution_time} units, remaining: {process.remaining_time}")

            # If not finished, put it back in the queue
            if process.remaining_time > 0:
                self.queue.append(process)
            else:
                process.waiting_time = process.total_time - (process.remaining_time + execution_time)
                self.completed_processes.append(process)

    def print_stats(self):
        print("\n📊 Scheduling Results:")
        for p in self.completed_processes:
            print(f"{p} - Turnaround Time: {p.total_time}, Waiting Time: {p.waiting_time}")
        avg_turnaround = sum(p.total_time for p in self.completed_processes) / len(self.completed_processes)
        avg_waiting = sum(p.waiting_time for p in self.completed_processes) / len(self.completed_processes)
        print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
        print(f"Average Waiting Time: {avg_waiting:.2f}")

#TEST

# Test with 3 processes and quantum of 4
scheduler = RoundRobinScheduler(time_quantum=4)
scheduler.add_process("P1", 10)
scheduler.add_process("P2", 4)
scheduler.add_process("P3", 6)

scheduler.run()
scheduler.print_stats()
