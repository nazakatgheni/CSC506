from data_structures import Stack, Queue, Deque, LinkedList

# --- Problem Solving Algorithms ---

def is_balanced_parentheses(string):
    """Algorithm using Stack: Check for balanced parentheses."""
    s = Stack()
    for char in string:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.isEmpty():
                return False
            s.pop()
    return s.isEmpty()

def hot_potato_simulation(name_list, num):
    """Algorithm using Queue: Hot Potato game simulation."""
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
        
    while len(sim_queue.items) > 1:
        for _ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue() # Remove the person holding the potato
    return sim_queue.dequeue()

def is_palindrome(string):
    """Algorithm using Deque: Palindrome checker."""
    char_deque = Deque()
    for char in string:
        char_deque.addRear(char)
        
    while len(char_deque.items) > 1:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            return False
    return True

# --- Test Program & Validation ---

def run_tests():
    print("="*50)
    print("  DATA STRUCTURES TESTING & VALIDATION")
    print("="*50)

    print("\n--- 1. Testing Stack (Last-In-First-Out) ---")
    st = Stack()
    print("Action: Push 10 onto the stack")
    st.push(10)
    print(f"Current Stack state: {st.items}")
    
    print("Action: Push 20 onto the stack")
    st.push(20)
    print(f"Current Stack state: {st.items}")
    
    print("Action: Peek (View the top item without removing it)")
    print(f"Result: {st.peek()} (Expected: 20)")
    
    print("Action: Pop (Remove the top item)")
    print(f"Result: {st.pop()} (Expected: 20)")
    print(f"Current Stack state after pop: {st.items}")
    
    print("Algorithm Demonstration: Balanced Parentheses")
    print("Checking string: '(())'")
    print(f"Result: {is_balanced_parentheses('(())')} (Expected: True)")

    print("\n--- 2. Testing Queue (First-In-First-Out) ---")
    q = Queue()
    print("Action: Enqueue 'Task1' into the queue")
    q.enqueue("Task1")
    print(f"Current Queue state (Rear -> Front): {q.items}")
    
    print("Action: Enqueue 'Task2' into the queue")
    q.enqueue("Task2")
    print(f"Current Queue state (Rear -> Front): {q.items}")
    
    print("Action: View the Front item")
    print(f"Result: {q.front()} (Expected: Task1)")
    
    print("Action: Dequeue (Remove the Front item)")
    print(f"Result: {q.dequeue()} (Expected: Task1)")
    print(f"Current Queue state after dequeue: {q.items}")

    print("\nAlgorithm Demonstration: Hot Potato Simulation")
    names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
    print(f"Players: {names}, Passes per round: 7")
    print(f"Winner: {hot_potato_simulation(names, 7)} (Expected: Susan)")

    print("\n--- 3. Testing Deque (Double-Ended Queue) ---")
    dq = Deque()
    print("Action: Add 'Front1' to the Front")
    dq.addFront("Front1")
    print(f"Current Deque state: {dq.items}")
    
    print("Action: Add 'Rear1' to the Rear")
    dq.addRear("Rear1")
    print(f"Current Deque state: {dq.items}")
    
    print("Action: Remove from the Front")
    print(f"Result: {dq.removeFront()} (Expected: Front1)")
    print(f"Current Deque state after removal: {dq.items}")

    print("\nAlgorithm Demonstration: Palindrome Checker")
    print("Checking string: 'radar'")
    print(f"Result: {is_palindrome('radar')} (Expected: True)")

    print("\n--- 4. Testing LinkedList ---")
    ll = LinkedList()
    print("Action: Insert elements 5, 10, 15")
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    print(f"Current List state: {ll.display()} (Expected: [5, 10, 15])")
    
    print("Action: Search for the number 10")
    print(f"Result: {ll.search(10)} (Expected: True)")
    
    print("Action: Delete the number 10")
    ll.delete(10)
    print(f"Current List state after deletion: {ll.display()} (Expected: [5, 15])")

if __name__ == "__main__":
    run_tests()