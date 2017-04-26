from win32event import CreateMutex
from win32api import CloseHandle, GetLastError
from winerror import ERROR_ALREADY_EXISTS

class SingleInstance:
    """ Limits application to single instance """

    def __init__(self):
        self.mutexname = "app_name_{073360E2-38EB-41BF-A4FD-149CA9B28D6C}"
        self.mutex = CreateMutex(None, False, self.mutexname)
        self.lasterror = GetLastError()

    def alreadyrunning(self):
        return self.lasterror == ERROR_ALREADY_EXISTS

    def __del__(self):
        if self.mutex:
            CloseHandle(self.mutex)
           
if __name__ == '__main__':
    si = SingleInstance()
    if si.alreadyrunning():
        print('Process already running.')
    else:
        print('First process started.')
