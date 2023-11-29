"""Priority queue implementation based on heapq"""
import heapq

_PQCOUNTER = 0 # monotonic creation counter, NOT thread safe.

class _pqentry:
    def __init__(self, item, key=None):
        global _PQCOUNTER
        _PQCOUNTER += 1

        self._key = item if key is None else key
        self._ic = _PQCOUNTER
        self._item = item
        self._has_key = key is not None
        self._is_removed = False
    def remove(self):
        self._is_removed = True
    def is_removed(self):
        return self._is_removed
    def new_with_key(self, key):
        new = _pqentry(self._item, key)
        new._ic = self._ic
        return new
    def get(self):
        return self._item, (self._key if self._has_key else None)
    def get_item(self): return self._item
    def __lt__(self, other):
        return self._ic < other._ic if self._key == other._key else self._key < other._key
    def __repr__(self):
        if self._is_removed:
            return "<removed>"
        return f"_pqentry({repr(self._item)}" + (f", {self._key})" if self._has_key else ")")

class pqueue:
    """A simple priority queue implementation using the heapq algorithm.
    If each item inserted is unique (hash-wise) then the priority of the item
    can be changed in-place."""
    def __init__(self, *xs):
        self._queue = []
        self._entry = {}
        self.append(xs)
    def insert(self, item, key=None):
        """Insert a single item into the list, optionally with a key used for comparison.
        It is up to the user to guarantee that the keys/items are comparable order-wise."""
        entry = _pqentry(item, key)
        heapq.heappush(self._queue, entry)
        self._entry[item] = entry
    def append(self, xs):
        """Insert every item in the list into the pqueue. Supply a tuple of (item, key) if
        you want to order by key"""
        for x in xs:
            if isinstance(x, tuple):
                self.insert(*x)
            else:
                self.insert(x)
    def flush(self):
        """Flush removed items, assuring the first item is valid or the queue is empty"""
        while len(self._queue) > 0:
            if self._queue[0].is_removed():
                heapq.heappop(self._queue)
                continue
            break
    def peek(self):
        """Peek the first item in the queue after flushing, without removing the item"""
        self.flush()
        entry = self._queue[0]
        return entry.get()
    def next(self):
        """Return the first item in the queue after flusing and remove it form the queue"""
        self.flush()
        entry = heapq.heappop(self._queue)
        del self._entry[entry.get_item()]
        return entry.get()
    def change(self, item, new_priority):
        """Change the priority of the item in-place. Undefined behaviour if
        item is not unique. Inserts the item if it does not exist"""
        entry = self._entry.get(item)
        # insert item if it does not already exist
        if entry is None:
            self.insert(item, new_priority)
            return

        new_entry = entry.new_with_key(new_priority)
        entry.remove() # mark item as invalid
        self._entry[item] = new_entry
        heapq.heappush(self._queue, new_entry)
    def remove(self, item):
        """Remove the item from the queue"""
        self._entry[item].remove()
        del self._entry[item]
    def is_empty(self):
        """Flush the queue and check if there are no more available items"""
        self.flush()
        return len(self._queue) == 0

    def __iter__(self): return pqueue_iterator(self)
    def __contains(self, item): return item in self._entry

class pqueue_iterator:
    """A consuming iterator over the pqueue"""
    def __init__(self, pq):
        self._pq = pq
    def __next__(self):
        if self._pq.is_empty(): raise StopIteration()
        return self._pq.next()
    def __iter__(self):
        return pqueue_iterator(self._pq)
