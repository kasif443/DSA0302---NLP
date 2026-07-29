# DFA Simulator

# States
states = {"q0", "q1", "q2"}

# Input alphabet
alphabet = {"a", "b"}

# Transition table
transition = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",

    ("q1", "a"): "q1",
    ("q1", "b"): "q2",

    ("q2", "a"): "q1",
    ("q2", "b"): "q0"
}

# Initial state
initial_state = "q0"

# Final state(s)
final_states = {"q2"}

# Accept multiple strings
n = int(input("Enter number of input strings: "))

for i in range(n):
    string = input(f"Enter string {i+1}: ")

    current_state = initial_state
    path = [current_state]

    valid = True

    # Simulate DFA
    for symbol in string:
        if symbol not in alphabet:
            valid = False
            break

        current_state = transition[(current_state, symbol)]
        path.append(current_state)

    print("Transition Path:")
    print(" → ".join(path))

    if valid and current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")

    print()
