from subprocess import Popen, PIPE

MAX_ITERS = 1000

def nvidia_smi():
    proc = Popen(['nvidia-smi'],stdout=PIPE,encoding='utf-8')
    stdout, _ = proc.communicate()
    return stdout

def ssmi():
    nvidia_smi_output = nvidia_smi()
    nvidia_smi_output.strip()
    lines = iter(nvidia_smi_output.split('\n'))
    try:
        next(lines)
        for _ in range(3):
            print(next(lines))

        while True:
            line = next(lines)

            if line[0] == ' ':
                break

            print(line[:6],end='')
            line = next(lines)
            print(line[1:12]+line[13:19]+line[23:])

            next(lines)
            line = next(lines)
            print(line)

        print(next(lines))

        next(lines)
        print(next(lines))
        next(lines)
        print(next(lines))
        while True:
            print(next(lines))

    except StopIteration:
        pass

ssmi()