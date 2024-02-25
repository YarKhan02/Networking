file_path = 'memory_storage.txt'

class Memory():
    def __init__(self):
        self.buffer_storage = []
        self.capacity = 10

    def write(self, w):
        with open(file_path, 'r') as file:
            current_capacity = sum(1 for line in file)

        if current_capacity < self.capacity:
            with open(file_path, 'a') as file:
                file.write(w + '\n')
                file.close()
        else:
            raise BufferError('Memory capacity reached')

    def read(self):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                file.close()
            return content
        except FileNotFoundError:
            return None 

memory = Memory()