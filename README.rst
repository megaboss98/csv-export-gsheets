Export CSV files to Google Sheets
=================================

Simple CSV export wrapper for gspread package https://gspread.readthedocs.io.

.. image:: https://travis-ci.org/dlancer/csv-export-gsheets.svg?branch=master
    :target: https://travis-ci.org/dlancer/csv-export-gsheets/
    :alt: Build status

.. image:: https://img.shields.io/pypi/v/csv-export-gsheets.svg
    :target: https://pypi.python.org/pypi/csv-export-gsheets/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/format/csv-export-gsheets.svg
    :target: https://pypi.python.org/pypi/csv-export-gsheets/
    :alt: Download format

.. image:: https://img.shields.io/pypi/l/csv-export-gsheets.svg
    :target: https://pypi.python.org/pypi/csv-export-gsheets/
    :alt: License

Installation
============


PIP
---

You can install the latest stable package running this command::

    $ pip install csv_export_gsheets


Also you can install the development version running this command::

    $ pip install git+http://github.com/dlancer/csv_export_gsheets.git@dev


Usage
=====

Before you start you should:

1. Create Google Account Service key (use JSON format):

   https://gspread.readthedocs.io/en/latest/oauth2.html

2. Create new Google Spreadsheet

3. Share this spreadsheet with email from created service account file.

From command line::

    $ csv2gsheets --help


From python code:

.. code-block:: python

    from csv_export_gsheets.export import export_csv

    # src - path to csv file
    # url - google sheet url
    # credentials - path to service account credentials or dict object
    export_csv(source=src, url=url, credentials=credentials)

