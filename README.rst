grafana-backup
==============

Create dashboards backups using the Grafana API.


Installation
------------

The latest stable version can be installed from PyPi:

::

    $ pip install kea-exporter


and upgraded with:

::

    $ pip install --upgrade kea-exporter


Usage
----

::

    Usage: grafana-backup [OPTIONS]

    Options:
      --api-key TEXT      API key of the target grafana  [required]
      --grafana-url TEXT  base url of the target grafana  [required]
      --help              Show this message and exit.
