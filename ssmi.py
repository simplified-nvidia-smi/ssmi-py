#!/usr/bin/env python3
import argparse
import sys
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


def command_erored():
    print('ERROR: Failed to run command', file=sys.stderr)
    exit(1)


def nvidia_smi():
    try:
        proc = Popen(['nvidia-smi'], stdout=PIPE)
    except FileNotFoundError:
        command_erored()

    stdout, _ = proc.communicate()

    if proc.returncode != 0:
        command_erored()

    return stdout.decode('utf-8')


def ssmi():
    # get run flags from CLI
    args = parse_args()
    print_gpu_info = args.gpus
    print_proc_info = args.procs

    # Execute the nvidia-smi command and open a stream to read its output
    nvidia_smi_output = nvidia_smi()

    # split the output by lines and create an iterator
    lines = iter(nvidia_smi_output.split('\n'))

    # The execution runs in a try/except structure to catch the StopIteration error that liens will throw when
    # it has been fully consumed
    try:
        # consume but do not print the time and date
        next(lines)

        # Read the next three lines of the command's output and print each if not NULL
        # +---------------------------------------------------------------------------------------+
        # | NVIDIA-SMI 535.154.05             Driver Version: 535.154.05   CUDA Version: 12.2     |
        # |-----------------------------------------+----------------------+----------------------+
        for _ in range(3):
            line = next(lines)
            if print_gpu_info:
                print(line)

        # Loops once per GPU on system
        while True:

            # if the line starts with a space that means there are no more gpus to be processed
            line = next(lines)
            if len(line.strip()) == 0:
                break

            if print_gpu_info:
                print(line[:6], end='')  # prints "| GPU "

            line = next(lines)

            # prints " Fan  Temp " + " Perf " + "      Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |"
            if print_gpu_info:
                print(line[1:12] + line[13:19] + line[23:])

            # skip blank line
            next(lines)

            # prints block seperator "...-----..."
            line = next(lines)
            if print_gpu_info:
                print(line)

        # since the while loop consumes one line before it exits there is no need to handle the blank
        # line following the gpu table

        # if the gpu details were not printed out print the header for the process table
        line = next(lines)
        if not print_gpu_info and print_proc_info:
            print(line)

        # dump the line that just says processes
        # "| Processes:
        next(lines)

        # print the process table column headers
        # "|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |"
        line = next(lines)
        if print_proc_info:
            print(line)

        # dump the line that has overflow text from the headers
        # "|        ID   ID                                                             Usage      |"
        next(lines)

        # print out the rest of the process table
        while True:
            line = next(lines)
            if print_proc_info:
                print(line)

    except StopIteration:
        pass


if __name__ == '__main__':
    ssmi()
