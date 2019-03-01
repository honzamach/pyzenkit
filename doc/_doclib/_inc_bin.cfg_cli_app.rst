``--help``
    Display help and usage description and exit (*flag*).

``--debug``
    Run in debug mode (*flag*).

    Input various status information to ``stderr``.

    *Type:* ``boolean``, *default:* ``False``

``--quiet``
    Run in quiet mode (*flag*).

    Do not write anything to ``stdout`` or ``stderr``.

    *Type:* ``boolean``, *default:* ``False``

``--verbose``
    Increase application output verbosity (*flag*, *repeatable*).

    *Type:* ``boolean``, *default:* ``False``

``--name alternative-name``
    Alternative name for application instead of default ``$0``.

    This value will be used to generate names for log, runlog, pid, status and
    other application files.

    *Type:* ``string``, *default:* ``$0``

``--config-file file-name``
    Name of the configuration file.

    *Type:* ``string``, *default:* autodetected

``--config-file-silent``
    Do not complain in case given configuration file does not exist (*flag*).

    *Type:* ``boolean``, *default:* ``False``

``--config-dir file-name``
    Name of the configuration directory.

    *Type:* ``string``, *default:* autodetected

``--config-file-silent``
    Do not complain in case given configuration directory does not exist (*flag*).

    *Type:* ``boolean``, *default:* ``False``

``--log-file file-name``
    Name of the log file.

    *Type:* ``string``, *default:* autodetected

``--log-level level``
    Logging level [``debug``, ``info``, ``warning``, ``error``, ``critical``].

    *Type:* ``string``, *default:* ``info``

``--runlog-dir dir-name``
    Name of the runlog directory.

    *Type:* ``string``, *default:* autodetected

``--runlog-dump``
    Dump runlog to stdout when done processing (*flag*).

    *Type:* ``boolean``, *default:* ``False``

``--runlog-log``
    Write runlog to logging service when done processing (*flag*)

    *Type:* ``boolean``, *default:* ``False``

``--pstate-file file-name``
    Name of the persistent state file.

    *Type:* ``string``, *default:* autodetected

``--pstate-dump``
    Dump persistent state to stdout when done processing (*flag*).

    *Type:* ``boolean``, *default:* ``False``

``--pstate-log``
    Write persistent state to logging service when done processing (*flag*).

    *Type:* ``boolean``, *default:* ``False``

``--action action``
    Execute given quick action and exit. List of available actions can be displayed with ``--help`` option.

    *Type:* ``string``, *default:* ``None``

``--user name-or-id``
    Name/gid of the system user for process permissions.

    *Type:* ``string``, *default:* ``None``

``--group name-or-id``
    Name/gid of the system group for process permissions.

    *Type:* ``string``, *default:* ``None``
