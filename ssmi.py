from subprocess import Popen, PIPE

MAX_ITERS = 1000

def nvidia_smi():
    proc = Popen(['nvidia-smi'],stdout=PIPE,encoding='utf-8')
    stdout, _ = proc.communicate()
    return stdout

def ssmi():
    print_gpu_info = True
    print_proc_info = True

    nvidia_smi_output = nvidia_smi()
    nvidia_smi_output.strip()
    lines = iter(nvidia_smi_output.split('\n'))
    try:
        next(lines)
        for _ in range(3):
            line = next(lines)
            if print_gpu_info:
                print(line)

        while True:
            line = next(lines)

            if line[0] == ' ':
                break
            if print_gpu_info:
                print(line[:6],end='')
            line = next(lines)
            if print_gpu_info:
                print(line[1:12]+line[13:19]+line[23:])

            next(lines)
            line = next(lines)
            if print_gpu_info:
                print(line)

        # next(lines)
        line = next(lines)
        if not print_gpu_info and print_proc_info:
            print(line)

        next(lines)
        line = next(lines)
        if print_proc_info:
            print(line)
        next(lines)
        line = next(lines)
        if print_proc_info:
            print(line)
        while True:
            line = next(lines)
            if print_proc_info:
                print(line)

    except StopIteration:
        pass

ssmi()