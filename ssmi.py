import argparse
from subprocess import Popen, PIPE

MAX_ITERS = 1000


def parse_args():
    parser = argparse.ArgumentParser(
        description='Displays a simplified version of the output from the `nvidia-smi` command.\n'
                    'When no options are provided, it displays both GPU details and process information.')
    parser.add_argument('-g', '--gpus', action='store_true', help='display GPU details')
    parser.add_argument('-p', '--procs', action='store_true', help='display process details')

    args = parser.parse_args()

    if not (args.gpus or args.procs):
        args.gpus = args.procs = True

    return args


def nvidia_smi():
    proc = Popen(['nvidia-smi'], stdout=PIPE, encoding='utf-8')
    stdout, _ = proc.communicate()
    return stdout


def ssmi():
    args = parse_args()
    print_gpu_info = args.gpus
    print_proc_info = args.procs

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
                print(line[:6], end='')
            line = next(lines)
            if print_gpu_info:
                print(line[1:12] + line[13:19] + line[23:])

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


if __name__ == '__main__':
    ssmi()
