``--regular``
    Operational mode: regular script execution (*flag*). Conflicts with ``--shell`` option.

    *Type:* ``boolean``, *default:* ``False``

``--shell``
    Operational mode: manual script execution from shell (*flag*). Conflicts with ``--regular`` option.

    *Type:* ``boolean``, *default:* ``False``

``--command name``
    Name of the script command to be executed.

    *Type:* ``string``, *default:* autodetected

``--interval interval``
    Execution interval. This value should correspond with related cron script.

    *Type:* ``string``, *default:* ``daily``

``--adjust_thresholds``
    Round-up time interval threshols to interval size (*flag*).

    *Type:* ``boolean``, *default:* ``False``

``--time_high time``
    Upper time interval threshold.

    *Type:* ``float``, *default:* time.time
