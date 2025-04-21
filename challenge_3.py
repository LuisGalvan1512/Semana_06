from collections import deque
import random

class TrafficLane:
    def __init__(self, name):
        self.name = name
        self.queue = deque()
        self.wait_times = []
        self.max_length = 0

    def add_vehicle(self, arrival_time):
        self.queue.append(arrival_time)
        self.max_length = max(self.max_length, len(self.queue))

    def pass_vehicle(self, current_time):
        if self.queue:
            arrival = self.queue.popleft()
            wait_time = current_time - arrival
            self.wait_times.append(wait_time)
            print(f"{self.name}: Vehicle passed after waiting {wait_time} time units")

    def get_average_wait(self):
        if not self.wait_times:
            return 0
        return sum(self.wait_times) / len(self.wait_times)

    def get_max_length(self):
        return self.max_length

class TrafficLightSimulation:
    def __init__(self, green_duration, total_time):
        self.north_south = TrafficLane("North-South")
        self.east_west = TrafficLane("East-West")
        self.green_duration = green_duration
        self.total_time = total_time

    def simulate(self):
        for time in range(self.total_time):
            print(f"\n⏱️ Time: {time}")

            if random.random() < 0.5:
                self.north_south.add_vehicle(time)
                print("🚗 Vehicle arrived at North-South")

            if random.random() < 0.5:
                self.east_west.add_vehicle(time)
                print("🚕 Vehicle arrived at East-West")

            if (time // self.green_duration) % 2 == 0:
                print("🟢 Green light: North-South")
                self.north_south.pass_vehicle(time)
            else:
                print("🟢 Green light: East-West")
                self.east_west.pass_vehicle(time)

        # Final statistics
        print("\n📊 Simulation Results:")
        print(f"North-South - Avg Wait: {self.north_south.get_average_wait():.2f}, Max Queue Length: {self.north_south.get_max_length()}")
        print(f"East-West   - Avg Wait: {self.east_west.get_average_wait():.2f}, Max Queue Length: {self.east_west.get_max_length()}")


#TEST

# Run the simulation
sim = TrafficLightSimulation(green_duration=3, total_time=4)
sim.simulate()


