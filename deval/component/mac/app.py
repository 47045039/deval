# -*- coding: utf-8 -*-

import os
from deval.component.std.appcomponent import AppComponent


class MacAppComponent(AppComponent):
    def __init__(self, uri, dev, name=None):
        super(MacAppComponent, self).__init__(uri, dev, name)

    def start_app(self, path, **kwargs):
        """
        Use the console command to start a program

        Parameters:
            path - the command
        """
        os.system("open %s" % path)