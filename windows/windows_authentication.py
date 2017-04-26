import os
import win32security


def get_windows_username():
    """
    Get windows username of currently logged in user
    :return: lowercase string of username
    """
    return os.environ.get('USERNAME').lower()


def windows_login(username, password, domain):
    """
    Returns the authentication token of windows user
    
    :return: PyHandle token for using with other authenticated access
    """
    token = win32security.LogonUser(
        username,
        domain,
        password,
        win32security.LOGON32_LOGON_NETWORK,
        win32security.LOGON32_PROVIDER_DEFAULT
    )
    return token


def windows_authenticate(username, password, domain):
    """
    Silently traps errors with login failure, but may also trap other errors.
    
    :return: Boolean based on authentication 
    """
    try:
        token = windows_login(username, password, domain)
    except Exception as e:
        return False
    else:
        return bool(token)


if __name__ == '__main__':
    #
    # Note, when testing failure for your app, make username wrong, not password
    # This might keep you from getting locked out of your account, depending
    # on security procedures with your domain.

    domain = 'windows_domain_here'
    username = get_windows_username()
    print('Your windows username is {}'.format(username))
    password = input('Input Password:')
    if windows_authenticate(username, password, domain):
        print('Authentication Successful.')
        token = windows_login(username, password, domain)
        print('Token received {}'.format(str(token)))
    else:
        print('Authentication Failed.')
