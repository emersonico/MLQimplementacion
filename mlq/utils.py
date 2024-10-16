from process import Process

def read_input(file_name):
    processes = []
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("#") or line.strip() == "":
                continue
            label, bt, at, q, pr = line.strip().split(";")
            processes.append(Process(label.strip(), int(bt), int(at), int(q), int(pr)))
    return processes
