SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be nonre-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

def is_it_true(anything):
    if anything:
        print("yes, it is true")
    else:
        print("no, it is false")

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))

    print("\nNUMBERS")
    print(True + True)
    print(type(1))
    print(type(1.0))
    print(isinstance(1, int))
    print(int(2.9))

    print("\nNUMERICAL OPERATIONS")
    print(11 / 2)
    print(11 // 2)
    print(11 // 2)
    print(11.0 // 2)
    print(11 ** 2)
    print(11 % 2)

    print("\nFRACTIONS")
    import fractions
    fraction = fractions.Fraction(1, 3)
    print(fraction);
    print(2*fraction);

    reducedFraction = fractions.Fraction(4, 6)
    print(reducedFraction);

    import math
    print(math.tan(math.pi / 4))

    print(is_it_true(1))
    print(is_it_true(-1))
    print(is_it_true(0))

    print("\nLISTS")
    a_list = ['a', 'b', 'c', 'example']
    print(a_list)
    print(a_list[0])
    print(a_list[1])
    print(a_list[2])
    print(a_list[-1])
    print(a_list[-2])

    print("\nslicing list")
    print(a_list[1:3])
    print(a_list[1:-2])
    print(a_list[2:])
    print(a_list[:])

    print("\nadding item to a list")
    a_list = ['a']
    a_list = a_list + [2.0, 3]
    print(a_list)
    a_list.append(True)
    print(a_list)
    a_list.extend(['four', 'fifth'])
    print(a_list)
    a_list.insert(0, "AAA")
    print(a_list)

    print("\nextend vs. append")
    a_list = ['a', 'b', 'c']
    a_list.extend(['d', 'e', 'f'])
    print(a_list)
    print(len(a_list))

    a_list.append(['g', 'h', 'i'])
    print(a_list)
    print(len(a_list))

    print("\nremoving item from a list")
    del a_list[0]
    print(a_list)

    a_list.remove("b")
    print(a_list)
    
    a_list.remove(['g', 'h', 'i'])
    print(a_list)

    a_list.pop()
    print(a_list)

    a_list.pop(1)
    print(a_list)

    print("\nTUPLES - they are immutable")
    a_tuple = ("a", "b", "c", "d", "example")
    print(a_tuple)

    print("\nassign multiple values at once")
    v = ('a', 2, True)
    (xx, yy, zz) = v
    print(xx)
    print(yy)
    print(zz)

    (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
    print(MONDAY)
    print(TUESDAY)

    print("\nSETS")
    a_set = {1}
    print(a_set)
    a_list = ['a', 'b', 'mpilgrim', True, False, 42]
    a_set = set(a_list)
    print(a_set)

    a_set.add(9)
    print(a_set)

    a_set.add(9)
    print(a_set)

    a_set.update({9,50,51,52})
    print(a_set)

    a_set.discard(9)
    print(a_set)
    a_set.discard(9)

    a_set.remove(50)
    print(a_set)
    #a_set.remove(50) - Raises a KeyError exception
    
    a_set.pop();
    a_set.pop();
    print(a_set)

    a_set.clear()
    a_set = set()
    #a_set.pop(); - Raises a KeyError exception

    print(a_set)

    print("\nDICTIONARIES")
    a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
    print(a_dict)
    a_dict['database'] = 'mongo'
    print(a_dict)
    a_dict['user'] = 'tono'
    print(a_dict)

    print("\nNONE")
    print(None == false)
    print(None == 0)
    print(None == '')
    print(None == None)



