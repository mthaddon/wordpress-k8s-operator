# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Module for commonly used internal types in WordPress charm."""

from typing import Any, NamedTuple, Optional, Union


class CommandExecResult(NamedTuple):
    """Result of executed command from WordPress container.

    Attrs:
        return_code: exit code from executed command.
        stdout: standard output from the executed command.
        stderr: standard error output from the executed command.
    """

    return_code: int
    stdout: Union[str, bytes]
    stderr: Union[str, bytes, None]


class ExecResult(NamedTuple):
    """Wrapper for executed command result from WordPress container.

    Attrs:
        success: True if command successful, else False.
        result: returned value from execution command, parsed in desired format.
        message: error message output of executed command.
    """

    success: bool
    result: Any
    message: str


class DatabaseConfig(NamedTuple):
    """Configuration values required to connect to database.

    Attrs:
        hostname: The hostname under which the database is being served.
        database: The name of the database to connect to.
        username: The username to use to authenticate to the database.
        password: The password to use to authenticat to the database.
    """

    hostname: Optional[str]
    database: Optional[str]
    username: Optional[str]
    password: Optional[str]
