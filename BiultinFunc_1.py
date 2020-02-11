# filter函数
"""class filter(object)
 |  filter(function or None, iterable) --> filter object
 |
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |
 |  Methods defined here:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(...)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
"""
a1 = filter(None, [1, 0, False, True])
print(list(a1))


def odd(x):
    return x % 2


a2 = list(filter(odd, [12, 45, 35, 26, 33, 78]))
print(a2)
a3 = list(filter(lambda x: x % 2, [12, 45, 35, 26, 33, 78]))
print(a3)

# map函数
a4 = list(map(lambda x: x * 2, range(10)))
print(a4)
