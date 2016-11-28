#test_binding

from Qt import __binding__

if __binding__ in ('PySide2', 'PyQt5'):
    print('Qt5 binding available')
elif __binding__ in ('PySide', 'PyQt4'):
    print('Qt4 binding available.')
else:
    print('No Qt binding available.')