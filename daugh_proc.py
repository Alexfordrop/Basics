import os

pid = os.fork()

if pid == 0:
    # дочерний процесс
    print(f'Process {os.getpid()} was created bt {os.getppid()}.')

else:
    # родительский процесс
    print(f'Process {os.getpid()} just created {pid}.')