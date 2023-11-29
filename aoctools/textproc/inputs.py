from . import parsing

def readlines(fname):
    with open(fname, 'r', encoding='utf-8') as fp:
        return fp.readlines()

def mapreadlines(fname, f):
    with open(fname, 'r', encoding='utf-8') as fp:
        for line in fp:
            yield f(line)

def readfile(fname):
    with open(fname, 'r', encoding='utf-8') as fp:
        return fp.read()

def readints(fname): return mapreadlines(fname, parsing.getints)

def readlineswith(fname, *re_f): 
    return mapreadlines(fname, lambda line: parsing.match_with(line, *re_f))

__all__ = [
    'readlines',
    'mapreadlines',
    'readfile',
    'readints',
    'readlineswith'
        ]

