Overview of all shared util functions
===

io
---

Contains functions for common file operations.

| function name | arguments                                             | return type | description                                                                    |
|---------------|-------------------------------------------------------|-------------|--------------------------------------------------------------------------------|
| is_file       | str, filepath                                         | bool        | Returns true if a given file exists                                            |
| is_dir        | str, dirpath                                          | bool        | Returns true if a given directory exists                                       |
| write_to_file | str, filepath - str/list(str), content - bool, append | None        | Writes "content" to "filepath". If append is true, append instead of overwrite |
| move_file     | str, oldpath - str, newpath                           | None        | Move file from "oldpath" to "newpath"                                          |
| delete_file   | str, filepath                                         | None        | Delete a file                                                                  |
| delete_dir    | str, dirpath                                          | None        | Delete a directory and all of its contents                                     |

shell
---

Provides access to shell operations.

| function name | arguments                 | return type          | description                                                               |
|---------------|---------------------------|----------------------|---------------------------------------------------------------------------|
| run_in_shell  | str or list(str), command | tuple(int, list(str) | Run a command in a shell and return the returncode and the command output |

ssh
---

Common operations concerning ssh.

| function name          | arguments                                                           | return type      | description                                               |
|------------------------|---------------------------------------------------------------------|------------------|-----------------------------------------------------------|
| set_ssh_password_login | bool, enable                                                        | None             | enables or disables ssh login with a password             |
| test_ssh_login         | str, username - str, password - str, host - int, port               | bool             | return if an ssh login was successful                     |
| test_ssh_command       | str, comman - str, username - str, password - str, host - int, port | tuple(bool, str) | return a tuple of bool and the output of a remote command |

systemd
---

Orchestrate systemd services and query their status.

| function name                  | arguments         | return type | description                                                             |
|--------------------------------|-------------------|-------------|-------------------------------------------------------------------------|
| is_service_running             | str, service_name | bool        | Returns true if a systemd service is running                            |
| is_service_enabled             | str, service_name | bool        | Returns true if a systemd service is enabled                            |
| is_service_running_and_enabled | str, service_name | bool        | Combination of the first two functions                                  |
| start_service                  | str, service_name | bool        | Start a systemd service and return true if the start was successful     |
| start_service                  | str, service_name | bool        | Restart a systemd service and return true if the restart was successful |
| stop_service                   | str, service_name | bool        | Stop a systemd service and return true if the stop was successful       |
| service_status                 | str, service_name | str         | Get the service status output as a string                               |
| service_trigger_status         | str, service_name | bool        | TODO                                                                    |

user
---

Perform unix user and group operations.

| function name     | arguments                                                         | return type | description                                                               |
|-------------------|-------------------------------------------------------------------|-------------|---------------------------------------------------------------------------|
| add_group         | str, group                                                        | bool        | Add a unix group to the system. Returns true if command was successful    |
| remove_group      | str, group                                                        | bool        | Remove unix group and return true if successful                           |
| add_user          | str, username - str, userpass - str, usergroup - bool, createhome | bool        | Add a unix user with given parameters. Usergroup == username if not given |
| add_user_to_group | str, username - str/list(str), usergroups - bool, append_groups   | bool        | Add or append groups to a unix user                                       |
| remove_user       | str, username - bool, force - bool, remove_home                   | bool        | Remove unix user, force if logged in                                      |
