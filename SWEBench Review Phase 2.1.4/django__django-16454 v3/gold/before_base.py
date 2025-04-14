import os
import sys
from argparse import ArgumentParser, HelpFormatter
from io import TextIOBase

import django
        else:
            raise CommandError("Error: %s" % message)


def handle_default_options(options):
    """