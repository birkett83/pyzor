"""Database backends for pyzord.

The database class must expose a dictionary-like interface, allowing access
via __getitem__, __setitem__, and __delitem__.  The key will be a forty
character string, and the value should be an instance of the Record class.

If the database backend cannot store the Record objects natively, then it
must transparently take care of translating to/from Record objects in
__setitem__ and __getitem__.

The database class should take care of expiring old values at the
appropriate interval.
"""

from pyzor.engines import gdbm_
from pyzor.engines import mysql


__all__ = ["database_classes"]

database_classes = {"gdbm": gdbm_.handle,
                    "mysql": mysql.handle
                    }

