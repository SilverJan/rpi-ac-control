from subprocess import run


def add_group(group):
    '''Adds a unix user-group to the system.

    Parameters
    ---
    group: str, the group to add
    '''

    print(f'adding {group}')
    result = run(['groupadd', group])
    print(result)
    return result.returncode == 0


def remove_group(group):
    '''Remove a unix user-group

    Parameters
    ---
    group: str, the group to remove
    '''

    print(f'removing {group}')
    result = run(['groupdel', group])
    print(result)
    return result.returncode == 0


def add_user(username, userpass=None, usergroup=None, createhome=True):
    '''This function will add an unix user.

    Parameters
    ---
    username: str, the name of the user
    userpass: str, the password of the user
    usergroup: str, the primary group of the user (default is the username)
    createhome: bool, create /home/<username> directory
    '''

    print(f'adding {username}')
    params = ['useradd']
    if createhome:
        params.append('-m')
    if userpass:
        params.append('-p')
        params.append(userpass)
    if usergroup:
        params.append('-g')
        params.append(usergroup)
    params.append(username)
    result = run(params)
    print(result)
    return result.returncode == 0


def add_user_to_group(username, usergroups, append_groups=True):
    '''Add a user to a group.

    Parameters
    ---
    username: str, the user
    usergroup: list/str, the usergroup or usergroups
    append_groups: bool, do not remove groups the user is currently part of
    '''

    groups_to_add = None
    if type(usergroups) == str:
        groups_to_add = usergroups
    elif type(usergroups) == list:
        groups_to_add = usergroups.join(',')
    else:
        raise TypeError('usergroups must be a str or a list')
    print(f'adding {username} to group(s) {usergroups}')

    params = ['usermod', '-G']
    if append_groups:
        params.append('-a')
    params.append(groups_to_add)
    params.append(username)
    result = run(params)
    print(result)
    return result.returncode == 0


def remove_user(username, force=True, remove_home=True):
    '''Remove a user from the system.

    Parameters
    ---
    username: str, the name of the user account
    force: bool, force removal of the user, even if logged in
    remove_home: bool, remove the home directory
    '''

    print(f'removing {username}')
    params = ['userdel']
    if force:
        params.append('-f')
    if remove_home:
        params.append('-r')
    params.append(username)
    result = run(params)
    print(result)
    return result.returncode == 0
