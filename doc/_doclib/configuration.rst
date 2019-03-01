.. _section-pyzenkit-configuration:

Configuration
================================================================================

Every application supports multiple means for adjusting the internal configurations.
When appropriate the default values for each configuration is hardcoded in module
source code. However there are several options to change the value:

* Override the internal default value when instantinating the application object
  by passing different value to object constructor.
* Pass the different value by configuration file.
* Pass the different value by command line option.

The configuration values are assigned from the sources mentioned above in that
particular order, so the value given by command line option overwrites the value
written in configuration file.


Command line parameters
--------------------------------------------------------------------------------

Configuration can be passed down to application by command line options. These options
have the highest priority and will overwrite any other configuration values. Depending
on the base object of the application different set of options is available.


Common application options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Following configuration options are available for all applications based on
:py:mod:`pyzenkit.baseapp`:

.. include:: _inc_bin.cfg_cli_app.rst


Common script options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Following configuration options are available on top of common applicationsoptions
for all applications based on :py:mod:`pyzenkit.zenscript`:

.. include:: _inc_bin.cfg_cli_script.rst


Common daemon options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Following configuration options are available on top of common application options
for all applications based on :py:mod:`pyzenkit.zendaemon`:

.. include:: _inc_bin.cfg_cli_daemon.rst


Configuration files and directories
--------------------------------------------------------------------------------

Configurations can be passed down to application using a combination of configuration
file or configuration directory. Values from configuration files override the values
from configuration directories. Configuration directories can therefore be used to
define common or default configuration values and those can be overriden when
necessary for given application component.

The available configuration keys are very similar to command line options and the
names differ only in the use of ``_`` character instead of ``-``. However there is
a certain set of configuration keys that is available only through command line
options and not through configuration file and vice versa.

