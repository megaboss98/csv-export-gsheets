#!/usr/bin/env python

"""
This utility export CSV file to Google Sheets

(c) dlancer, 2019

"""

import sys

from .export import export_csv


def main(args=None):
    """The main routine."""
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default=None, help='path to source CSV file')
    parser.add_argument('--url', default=None, help='destination Google Sheet url')
    parser.add_argument('--cell', default=None, help='destination Google Sheet cell')
    parser.add_argument('--credentials', default=None, help='path to google service credentials file')
    parser.add_argument('--config', default=None, help='path to config file')
    args = parser.parse_args()

    source = args.source
    url = args.url
    cell = args.cell
    credentials = args.credentials
    config = args.config

    try:
        export_csv(source=source, url=url, cell=cell, credentials=credentials, config=config)
    except ValueError as e:
        sys.exit(str(e))


if __name__ == "__main__":
    main()
