MAX_SIZE = 3
queue = []

def is_empty():
    return len(queue) == 0

def is_full():
    return len(queue) == MAX_SIZE

def enqueue():
    if is_full():
        print("⚠️ Queue is full. Cannot add more calls.")
    else:
        call = input("Enter customer ID (e.g., C4): ")
        queue.append(call)
        print(f"✅ Call from {call} added to the queue.")

def dequeue():
    if is_empty():
        print("⚠️ Queue is empty. No calls to attend.")
    else:
        removed = queue.pop(0)  # shifts elements left
        print(f"📞 Attended call from {removed}.")

def peek():
    if is_empty():
        print("⚠️ Queue is empty. No front element.")
    else:
        print(f"👀 Front of queue: {queue[0]}")

def display():
    if is_empty():
        print("📭 Queue is empty.")
    else:
        print("📋 Queue status:")
        for i, val in enumerate(queue, 1):
            print(f" {i}. {val}")

def show_menu():
    print("\n--- Customer Support Queue ---")
    print("1. Add new call (Enqueue)")
    print("2. Attend next call (Dequeue)")
    print("3. Show front call (Peek)")
    print("4. Display full queue")
    print("5. Exit")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("🔚 Exiting support center simulation.")
        break
    else:
        print("❌ Invalid choice. Try again.")