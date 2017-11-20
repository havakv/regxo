import re

class Pat(object):
    def __init__(self, expr):
        self.expr = expr
        self.pat = self.compile()

    def _constructor(self, expr):
        return Pat(expr)

    def add(self, obj):
        return self._constructor(self.expr + obj.expr)

    def rep(self, rep, to=None):
        if to:
            rep = '{' + str(rep) + ',' + str(to) + '}'
        elif rep.__class__ is not str:
            rep = '{' + str(rep) + '}'
        return self._constructor(self.expr + rep)

    def compile(self, flags=0):
        return re.compile(self.expr, flags)

    def findall(self, string, pos=None, *args, **kwargs):
        return self.pat.findall(string, pos, *args, **kwargs)

    def find(self, string, pos=None, *args, **kwargs):
        return self.pat.find(string, pos, *args, **kwargs)

    def sub(self, repl, string, count=0, *args, **kwargs):
        return self.pat.sub(repl, string, count, *args, **kwargs)
        
    def group(self):
        '''Return as matching group'''
        expr = '(' + self.expr + ')'
        return self._constructor(expr)
