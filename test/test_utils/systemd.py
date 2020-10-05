from subprocess import run, PIPE


def is_service_running(service_name):
    '''Checks if a given systemd service is running.

    Parameters
    ---
    service_name: str, the name of the service
    '''

    print(f'checking if {service_name} is running')
    result = run(['systemctl', 'is-active', service_name], stdout=PIPE)
    return result.stdout == b'active\n'


def is_service_enabled(service_name):
    '''Checks if a given systemd service is enabled.

    Parameters
    ---
    service_name: str, the name of the service
    '''

    print(f'checking if {service_name} is enabled')
    result = run(['systemctl', 'is-enabled', service_name], stdout=PIPE)
    return result.stdout == b'enabled\n'


def is_service_running_and_enabled(service_name):
    '''Checks if a given systemd service is running and enabled.

    Parameters
    ---
    service_name: str, the name of the service
    '''

    print(f'checking if {service_name} is running and enabled')
    return (
            is_service_running(service_name)
            and is_service_enabled(service_name))


def start_service(service_name):
    '''Start a systemd service.

    Parameters
    ---
    service_name: str, the name of the service
    '''

    print(f'starting {service_name}')
    result = run(['systemctl', 'start', service_name])
    return result.returncode == 0


def restart_service(service_name):
    '''Restart a systemd service.

    Parameters
    ---
    service_name: str, the name of the service
    '''

    print(f'restarting {service_name}')
    result = run(['systemctl', 'restart', service_name])
    return result.returncode == 0


def stop_service(service_name):
    '''Stop a systemd service.

    Parameters
    ---
    service_name: str, the name of the service
    '''

    print(f'stopping {service_name}')
    result = run(['systemctl', 'stop', service_name])
    return result.returncode == 0


def service_status(service_name):
    '''This will run the command 'systemctl status {service}'.

    Parameters
    ---
    service_name: str, the name of the service

    :return: str, the output of the command
    '''

    print(f'get logs of {service_name}')
    result = run(["systemctl", "status", service_name], stdout=PIPE)
    return result.decode('utf-8')


# TODO what exactely is this supposed to do? Currently it is equivalent to
# return True, as the return code of the command seems to always be 0
def service_trigger_status(service_name):
    '''Function to check for last trigger status of a systemd service or timer.
    This will simply run a command 'systemctl list-unit-files {service}'.  It
    will return the exit status of the command as boolean.

    Parameters
    ---
    service_name: str, the name of the service

    :return: boolean, status code of the command
    '''

    print(f'get trigger status of {service_name}')
    result = run(["systemctl", "list-unit-files", service_name])
    return result.returncode == 0
