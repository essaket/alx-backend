#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters"""
    startPage = (page - 1) * page_size
    endPage = page * page_size
    return (startPage, endPage)
