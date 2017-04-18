#! /usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import sys
import traceback
from contextlib import contextmanager

from frozenidea import FrozenIdea


MODULES = 'modules'
MODULES_DIR = './' + MODULES + '/'


@contextmanager
def safe():
    try:
        yield
    except:
        traceback.print_exc(file=sys.stdout)

def _get_func(func):
    def new_func(self, *args, **kwargs):
        getattr(super(self.__class__, self), func)(*args, **kwargs)
        for module in self.modules.values():
            with safe():
                try:
                    module_func = getattr(getattr(module, func), '__func__')
                except AttributeError:
                    continue
                module_func(self, *args, **kwargs)

    return new_func


class Modularize(type):

    def __new__(mcs, name, bases, attrs, **kwargs):
        for method in filter(lambda x: x.startswith('on_'), bases[0].__dict__):
            attrs[method] = _get_func(method)

        return type.__new__(mcs, name, bases, attrs)


class Bruno2(FrozenIdea):
    __metaclass__ = Modularize

    def _load_modules(self):
        for module in os.listdir(MODULES_DIR):
            if os.path.isfile(MODULES_DIR + module) and module.endswith('.py'):
                module = module.rstrip('.py')
                module_name = '%s.%s' % (MODULES, module)
                with safe():
                    imported = __import__(module_name, fromlist=[module])
                    imported = getattr(imported, module)
                    self.modules[module] = imported

    def __init__(self, nickname, server, port=6667):
        super(Bruno2, self).__init__(nickname, server, port)

        self.modules = {}
        self._load_modules()


if __name__ == '__main__':
    Bruno2(*sys.argv[1:]).run()
