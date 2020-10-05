from paramiko import (
        SSHClient,
        AutoAddPolicy,
        ssh_exception)


def set_ssh_password_login(enable=True):
    '''Enable or disable ssh password login.

    Parameters
    ---
    enable: bool, wheather to enable or disable the password login
    '''

    print(f'setting ssh password login to {enable}')
    newlines = []
    with open('/etc/ssh/sshd_config') as ssh_config:
        for line in ssh_config.readlines():
            if line.startswith('PasswordAuthentication'):
                continue
            newlines.append(line)
    if enable:
        newlines.append('PasswordAuthentication yes')
    else:
        newlines.append('PasswordAuthentication no')
    with open('/etc/ssh/sshd_config', 'w') as ssh_config:
        ssh_config.writelines(newlines)


def test_ssh_login(username, password, host='localhost', port=22):
    '''Verify that a user can be logged in via ssh.

    Parameters
    ---
    username: str, the name of the user
    password: str, the password of the user
    host: str, the host to connect to
    port: int, the ssh port
    '''

    print(f'trying to login to {host} on port {port} as {username}')
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        client.connect(
                host,
                port,
                username,
                password,
                allow_agent=False,
                look_for_keys=False)
        client.close()
    except ssh_exception.AuthenticationException:
        return False
    return True


def test_ssh_command(command, username, password, host='localhost', port=22):
    ''' login a user and execute the specified command

    Parameters
    ---
    command: string, the command to execute, with options and arguments
    username: str, the name of the user
    password: str, the password of the user
    host: str, the host to connect to
    port: int, the ssh port
    '''

    print(f'trying to login to {host} on port {port} as {username} and execute $ {command}')
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        client.connect(
            host,
            port,
            username,
            password,
            allow_agent=False,
            look_for_keys=False)
        stdin, stdout, stderr = client.exec_command(command)
        stdout = stdout.readlines()
        stderr = stderr.readlines()
        client.close()
    except (ssh_exception.AuthenticationException, ssh_exception.SSHException) as e:
        return (False, stderr)
    return (True, stdout)
