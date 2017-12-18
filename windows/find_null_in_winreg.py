import winreg as _winreg

# This script will print all classes that have NULL in string.
# Use SysInternals RegDelNull to delete these.

hkcr = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, "")

i = 0
try:
    while True:
        ctype = _winreg.EnumKey(hkcr, i)
        if '\x00' in ctype:
            print(ctype)
        if not isinstance(ctype, str):
            print("{} -> {}".format(type(ctype), ctype))
        i += 1
except WindowsError:
    # Will always go off the end of EnumKey to escape the while
    pass

