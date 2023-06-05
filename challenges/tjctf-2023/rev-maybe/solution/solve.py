from z3 import *
# pip install z3-solver

solver = Solver()
encoded = [0x12, 0x11, 0x00, 0x15, 0x0b, 0x48, 0x3c, 0x12, 0x0c, 0x44, 0x00, 0x10, 0x51, 0x19, 0x2e, 0x16, 0x03, 0x1c, 0x42, 0x11, 0x0a, 0x4a, 0x72, 0x56, 0x0d, 0x7a, 0x74, 0x4f, 0x00]
user_input = [BitVec(f'user_input{i}', 8) for i in range(33)]

# Add constraints
for i in range(32):
    if i >= 4:
        solver.add((user_input[i] ^ user_input[i - 4]) == encoded[i - 4])
solver.add(user_input[0] == ord("t"))
solver.add(user_input[1] == ord("j"))
solver.add(user_input[2] == ord("c"))
solver.add(user_input[3] == ord("t"))
solver.add(user_input[32] == 0x0)

# Get solution
if solver.check() == sat:
    model = solver.model()
    decoded = [model.evaluate(user_input[i]).as_long() for i in range(33)]
    print("".join([chr(val) for val in decoded]))
else:
    print("No solution found.")
