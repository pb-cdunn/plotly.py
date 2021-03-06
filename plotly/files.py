import os

# file structure
PLOTLY_DIR = os.environ.get("PLOTLY_DIR",
                            os.path.join(os.path.expanduser("~"), ".plotly"))

CREDENTIALS_FILE = os.path.join(PLOTLY_DIR, ".credentials")
CONFIG_FILE = os.path.join(PLOTLY_DIR, ".config")
TEST_FILE = os.path.join(PLOTLY_DIR, ".permission_test")

# this sets both the DEFAULTS and the TYPES for these files
FILE_CONTENT = {CREDENTIALS_FILE: {'username': '',
                                   'api_key': '',
                                   'proxy_username': '',
                                   'proxy_password': '',
                                   'stream_ids': []},
                CONFIG_FILE: {'plotly_domain': 'https://plot.ly',
                              'plotly_streaming_domain': 'stream.plot.ly',
                              'plotly_api_domain': 'https://api.plot.ly',
                              'plotly_ssl_verification': True,
                              'plotly_proxy_authorization': False,
                              'world_readable': True,
                              'sharing': 'public',
                              'auto_open': True}}


def _permissions():
    try:
        if not os.path.exists(PLOTLY_DIR):
            try:
                os.mkdir(PLOTLY_DIR)
            except Exception:
                # in case of race
                if not os.path.isdir(PLOTLY_DIR):
                    raise
        with open(TEST_FILE, 'w') as f:
            f.write('testing\n')
        try:
            os.remove(TEST_FILE)
        except Exception:
            pass
        return True
    except Exception: # Do not trap KeyboardInterrupt.
        return False


_file_permissions = None


def ensure_writable_plotly_dir():
    # Cache permissions status
    global _file_permissions
    if _file_permissions is None:
        _file_permissions = _permissions()
    return _file_permissions
