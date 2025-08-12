class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, signal_name):
        """Add a signal to the circular queue."""
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full — cannot enqueue")
        elif self.front == -1:  # Queue is empty
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = signal_name
            print(f"{signal_name} added to queue")
        else:  # Normal case
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = signal_name
            print(f"{signal_name} added to queue")

    def dequeue(self):
        """Remove a signal from the circular queue."""
        if self.front == -1:
            print("Queue is empty — cannot dequeue")
        elif self.front == self.rear:  # Only one element
            print(f"{self.queue[self.front]} removed from queue")
            self.front = -1
            self.rear = -1
        else:
            print(f"{self.queue[self.front]} Turned Green")
            self.front = (self.front + 1) % self.size

    def display(self):
        """Display all signals in the queue."""
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Traffic signals in queue:")
            i = self.front
            while True:
                print(self.queue[i], end="  ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print("\n")


class TrafficSignalSystem:
    def __init__(self):
        size = int(input("Enter the number of signals in the system: "))
        self.queue = CircularQueue(size)

    def menu(self):
        while True:
            print("\nTraffic Signal Management")
            print("1. enqueue signal")
            print("2. dequeue signal")
            print("3. Display Signals")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                signal_name = input("Enter signal name to add: ")
                self.queue.enqueue(signal_name)
            elif choice == "2":
                self.queue.dequeue()
            elif choice == "3":
                self.queue.display()
            elif choice == "4":
                print("Exiting Traffic Signal System...")
                break
            else:
                print("Invalid choice. Try again.")


# Run the program
TrafficSignalSystem().menu()
