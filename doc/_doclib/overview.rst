.. _section-pyzenkit-overview:

Framework overview
================================================================================

The whole framework is broken down into following submodules:

:py:mod:`pyzenkit.jsonconf`
    Module for handling JSON based configuration files and directories.

:py:mod:`pyzenkit.daemonizer`
    Module for taking care of all process daemonization tasks.

:py:mod:`pyzenkit.baseapp`
    Module for writing generic console applications.

:py:mod:`pyzenkit.zenscript`
    Module for writing generic console scripts with built-in support for repeated
    executions (for example by cron-like service).

:py:mod:`pyzenkit.zendaemon`
    Module for writing generic system services (daemons).


Application types
--------------------------------------------------------------------------------

Base application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The base application implemented in :py:class:`pyzenkit.baseapp.BaseApp` provides
features usefull for every application including (but not limited to) the following:

* Application configuration service
* Logging service
* Persistent state service
* Application runlog service
* Plugin system
* Application actions

Please see the documentation for :py:mod:`pyzenkit.baseapp` in API section for more
in-depth details.

Please see the source code for an example implementation of demo application in
:py:class:`pyzenkit.baseapp.DemoBaseApp` class.


Script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The script application implemented in :py:class:`pyzenkit.zenscript.ZenScript`
provides the base implementation of generic one-time execution script.
It may be used to implement large variety of applications like backup scripts,
control scripts, etc. These applications are intended to be executed either by user
from terminal, or periodically via cron-like service.

The implementation is based on :py:class:`pyzenkit.baseapp.BaseApp` class, so it
includes all of its features. On top of that there are following additional features:

* Support for executing multiple different **commands** within one executable.
* Support for multiple execution modes (**regular**, **shell**).
* Support for regular executions with defined time intervals.

Please see the documentation for :py:mod:`pyzenkit.zenscript` in API section for more
in-depth details.

Please see the source code for an example implementation of demo application in
:py:class:`pyzenkit.zenscript.DemoZenScript` class.


Daemon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The daemon application implemented in :py:class:`pyzenkit.zendaemon.ZenDaemon`
provides the base implementation of generic daemon.

The implementation is based on :py:class:`pyzenkit.baseapp.BaseApp` class, so it
includes all of its features. On top of that there are following additional features:

* Fully automated daemonization process (detaching, PID files, ...)
* Event driven design.
* Support for arbitrary signal handling.
* Support for modularity and reusability with daemon components.

Please see the documentation for :py:mod:`pyzenkit.zendaemon` in API section for more
in-depth details.

Please see the source code for an example implementation of demo application in
:py:class:`pyzenkit.zendaemon.DemoZenDaemon` class.
