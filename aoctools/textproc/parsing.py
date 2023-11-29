import re

def getints(text):
    buffer = []
    for c in text:
        if c.isdigit() or (not buffer and c == '-'):
            buffer.append(c)
        elif buffer:
            yield int("".join(buffer))
            buffer = []
    if buffer:
        yield int("".join(buffer))

__match_with_re_cache = {}
def match_with(text, *re_f):
    """Try applying the regexp in the order given until one succedds, 
    optionally mapping the output to the given function, if supplied"""
    global __match_with_re_cache
    regexps= []
    for m in re_f:
        if isinstance(m, tuple):
            r, f = m
        else:
            r, f = m, lambda x: x

        if not isinstance(r, re.Pattern):
            rp = __match_with_re_cache.get(r)
            if rp is None:
                rp = re.compile(r)
                __match_with_re_cache[r] = rp
                
            r = rp
        regexps.append((r, f))

    for r, f in regexps:
        m = re.search(r, text)
        if m is None: continue
        gd = m.groupdict()
        if len(gd) == 0:
            groups = m.groups()
            return f(m[0] if len(groups) == 0 else list(m.groups()))
        else:
            d = {i: s for i, s in enumerate(m.groups())}
            d[0] = m[0]
            d.update(gd)
            return f(d)
    return None


__all__ = [
    'getints',
    'match_with'
        ]
