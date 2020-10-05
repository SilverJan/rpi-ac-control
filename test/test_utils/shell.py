from subprocess import run, PIPE


def run_in_shell(command):
    '''Runs a given command in a shell subprocess.

    Parameters
    ---
    command: str/list(str), the command to execute

    Returns
    ---
    (return_code, command_output): int, list(str)
    '''

    if type(command) is str:
        cmdline = command.split(' ')
    elif type(command) is list:
        cmdline = command
    else:
        assert False, 'command parameter is not type list or str'

    print(f'Running {cmdline} in a subprocess')
    result = run(cmdline, stdout=PIPE)
    output = result.stdout.decode('utf8').split('\n')[:-1]
    return (result.returncode, output)
