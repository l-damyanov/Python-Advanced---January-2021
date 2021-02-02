from fibonacci_sequence.fibonacci_seq.sequence import create_sequence, locate

line = input()

while line != "Stop":
    command = line.split()
    seq = []
    if command[0] == "Create":
        seq = create_sequence(int(command[-1]))
        print(' '.join([str(el) for el in seq]))
    elif command[0] == "Locate":
        located_num = locate(int(command[-1]))
        if located_num != None:
            print(f"The number - {int(command[-1])} is at index {located_num}")
        else:
            print(f"The number {int(command[-1])} is not in the sequence")

    line = input()