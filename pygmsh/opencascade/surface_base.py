# -*- coding: utf-8 -*-
#


class SurfaceBase(object):
    _ID = 0

    def __init__(self, id0=None):
        isinstance(id0, str)
        if id0:
            self.id = id0
        else:
            self.id = 's{}'.format(SurfaceBase._ID)
            SurfaceBase._ID += 1
        return
