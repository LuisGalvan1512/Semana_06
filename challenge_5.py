class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.max_size = size
        self.start = 0
        self.count = 0

    def add(self, value):
        index = (self.start + self.count) % self.max_size
        if self.count == self.max_size:
            # Overwrite the oldest data
            self.start = (self.start + 1) % self.max_size
        else:
            self.count += 1
        self.buffer[index] = value

    def get_latest(self):
        result = []
        for i in range(self.count):
            index = (self.start + i) % self.max_size
            result.append(self.buffer[index])
        return result

    def calculate_average(self):
        if self.count == 0:
            return 0
        return sum(filter(None, self.get_latest())) / self.count

#TEST

cb = CircularBuffer(5)
cb.add(10)
cb.add(20)
cb.add(30)
print(cb.get_latest())           # [10, 20, 30]
print(cb.calculate_average())    # 20.0

cb.add(40)
cb.add(50)
cb.add(60)  # This overwrites 10
print(cb.get_latest())           # [20, 30, 40, 50, 60]
print(cb.calculate_average())    # 40.0
