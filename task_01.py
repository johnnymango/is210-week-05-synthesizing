#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the module which assigns the current date. """


import datetime


CURDATE = None


def get_current_date():
    """This functions gets the current date..

    Args:
        None

    Returns:
        Date Object: Returns the current date.

    Examples:

        >>> get_current_date()
        datetime.date(2015, 9, 27)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
