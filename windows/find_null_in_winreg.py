import winreg as _winreg

# This script will print all classes that have NULL in string.
# Use SysInternals RegDelNull to delete these.

hkcr = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, "")

i = 0
while True:
    try:
        ctype = _winreg.EnumKey(hkcr, i)
    except EnvironmentError:
        break
    else:
        if '\x00' in ctype:
            print("{} -> {}\n".format(type(ctype), ctype))

    i += 1

print('Complete')
