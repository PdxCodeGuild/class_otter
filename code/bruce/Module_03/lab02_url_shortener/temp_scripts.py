import string

chrome_keys_to_process = "'ALLUSERSPROFILE', 'APPDATA', 'CHROME_CRASHPAD_PIPE_NAME', 'COMMONPROGRAMFILES', 'COMMONPROGRAMFILES(X86)', 'COMMONPROGRAMW6432', 'COMPUTERNAME', 'COMSPEC', 'DRIVERDATA', 'FPS_BROWSER_APP_PROFILE_STRING', 'FPS_BROWSER_USER_PROFILE_STRING', 'HOMEDRIVE', 'HOMEPATH', 'LOCALAPPDATA', 'LOGONSERVER', 'NUMBER_OF_PROCESSORS', 'ONEDRIVE', 'ONEDRIVECONSUMER', 'ORIGINAL_XDG_CURRENT_DESKTOP', 'OS', 'PATH', 'PATHEXT', 'POWERSHELL_DISTRIBUTION_CHANNEL', 'PROCESSOR_ARCHITECTURE', 'PROCESSOR_IDENTIFIER', 'PROCESSOR_LEVEL', 'PROCESSOR_REVISION', 'PROGRAMDATA', 'PROGRAMFILES', 'PROGRAMFILES(X86)', 'PROGRAMW6432', 'PSMODULEPATH', 'PUBLIC', 'PYTHONPATH', 'SESSIONNAME', 'SYSTEMDRIVE', 'SYSTEMROOT', 'TEMP', 'TMP', 'USERDOMAIN', 'USERDOMAIN_ROAMINGPROFILE', 'USERNAME', 'USERPROFILE', 'VIRTUAL_ENV', 'WINDIR', 'ZES_ENABLE_SYSMAN', 'TERM_PROGRAM', 'TERM_PROGRAM_VERSION', 'LANG', 'COLORTERM', 'VSCODE_GIT_IPC_HANDLE', 'GIT_ASKPASS', 'VSCODE_GIT_ASKPASS_NODE', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS', 'VSCODE_GIT_ASKPASS_MAIN', 'DJANGO_SETTINGS_MODULE', 'RUN_MAIN', 'SERVER_NAME', 'GATEWAY_INTERFACE', 'SERVER_PORT', 'REMOTE_HOST', 'CONTENT_LENGTH', 'SCRIPT_NAME', 'SERVER_PROTOCOL', 'SERVER_SOFTWARE', 'REQUEST_METHOD', 'PATH_INFO', 'QUERY_STRING', 'REMOTE_ADDR', 'CONTENT_TYPE', 'HTTP_HOST', 'HTTP_CONNECTION', 'HTTP_PRAGMA', 'HTTP_CACHE_CONTROL', 'HTTP_SEC_CH_UA', 'HTTP_SEC_CH_UA_MOBILE', 'HTTP_SEC_CH_UA_PLATFORM', 'HTTP_UPGRADE_INSECURE_REQUESTS', 'HTTP_USER_AGENT', 'HTTP_ACCEPT', 'HTTP_SEC_FETCH_SITE', 'HTTP_SEC_FETCH_MODE', 'HTTP_SEC_FETCH_USER', 'HTTP_SEC_FETCH_DEST', 'HTTP_REFERER', 'HTTP_ACCEPT_ENCODING', 'HTTP_ACCEPT_LANGUAGE', 'HTTP_COOKIE', 'wsgi.input', 'wsgi.errors', 'wsgi.version', 'wsgi.run_once', 'wsgi.url_scheme', 'wsgi.multithread', 'wsgi.multiprocess', 'wsgi.file_wrapper', 'CSRF_COOKIE'"

chrome_request_to_process = ''''ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Bruce\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_23348_ZQMZBBLDBOHQZFPU', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DELL-GAMING-DES', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Bruce', 'LOCALAPPDATA': 'C:\\Users\\Bruce\\AppData\\Local', 'LOGONSERVER': '\\\\DELL-GAMING-DES', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\Bruce\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\Bruce\\OneDrive', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\Bruce\\.virtualenvs\\lab02_url_shortener-zO0gRMS_/Scripts;C:\\Program Files\\PowerShell\\7;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\PowerShell\\7\\;C:\\Shortcuts;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\Bruce\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\Bruce\\AppData\\Local\\GitHubDesktop\\bin;c:\\users\\bruce\\.local\\bin;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.LNK;.CPL', 'POWERSHELL_DISTRIBUTION_CHANNEL': 'MSI:Windows 10 Home', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 13, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0d', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\Bruce\\OneDrive\\Documents\\PowerShell\\Modules;C:\\Program Files\\PowerShell\\Modules;c:\\program files\\powershell\\7\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYTHONPATH': 'C:\\Users\\Bruce\\Programming\\', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\Bruce\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\Bruce\\AppData\\Local\\Temp', 'USERDOMAIN': 'DELL-GAMING-DES', 'USERDOMAIN_ROAMINGPROFILE': 'DELL-GAMING-DES', 'USERNAME': 'Bruce', 'USERPROFILE': 'C:\\Users\\Bruce', 'VIRTUAL_ENV': 'C:\\Users\\Bruce\\.virtualenvs\\lab02_url_shortener-zO0gRMS_', 'WINDIR': 'C:\\WINDOWS', 'ZES_ENABLE_SYSMAN': '1', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.64.2', 'LANG': 'en_US.UTF-8', 'COLORTERM': 'truecolor', 'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-87a105558d-sock', 'GIT_ASKPASS': 'c:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 'DJANGO_SETTINGS_MODULE': 'short_project.settings', 'RUN_MAIN': 'true', 'SERVER_NAME': 'DELL-GAMING-DESKTOP', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_PRAGMA': 'no-cache', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_SEC_CH_UA': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"', 'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_SEC_CH_UA_PLATFORM': '"Windows"', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'HTTP_SEC_FETCH_SITE': 'same-origin', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_SEC_FETCH_DEST': 'document', 'HTTP_REFERER': 'http://127.0.0.1:8000/', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9', 'HTTP_COOKIE': 'csrftoken=nxAzGW5RTsleqtXUdqxQH1MS8rN8U1fgVYe76CcOyLXgp37ponsxb8Oz00Qs04eh; sessionid=0baq3ndmgo9t2io8vpuhyyg7v9uybge0', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x000002032960FDF0>, 'wsgi.errors': <colorama.ansitowin32.StreamWrapper object at 0x0000020327E95BA0>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 'nxAzGW5RTsleqtXUdqxQH1MS8rN8U1fgVYe76CcOyLXgp37ponsxb8Oz00Qs04eh'''

edge_keys_to_process = """
'ALLUSERSPROFILE', 'APPDATA', 'CHROME_CRASHPAD_PIPE_NAME', 'COMMONPROGRAMFILES', 'COMMONPROGRAMFILES(X86)', 'COMMONPROGRAMW6432', 'COMPUTERNAME', 'COMSPEC', 'DRIVERDATA', 'FPS_BROWSER_APP_PROFILE_STRING', 'FPS_BROWSER_USER_PROFILE_STRING', 'HOMEDRIVE', 'HOMEPATH', 'LOCALAPPDATA', 'LOGONSERVER', 'NUMBER_OF_PROCESSORS', 'ONEDRIVE', 'ONEDRIVECONSUMER', 'ORIGINAL_XDG_CURRENT_DESKTOP', 'OS', 'PATH', 'PATHEXT', 'POWERSHELL_DISTRIBUTION_CHANNEL', 'PROCESSOR_ARCHITECTURE', 'PROCESSOR_IDENTIFIER', 'PROCESSOR_LEVEL', 'PROCESSOR_REVISION', 'PROGRAMDATA', 'PROGRAMFILES', 'PROGRAMFILES(X86)', 'PROGRAMW6432', 'PSMODULEPATH', 'PUBLIC', 'PYTHONPATH', 'SESSIONNAME', 'SYSTEMDRIVE', 'SYSTEMROOT', 'TEMP', 'TMP', 'USERDOMAIN', 'USERDOMAIN_ROAMINGPROFILE', 'USERNAME', 'USERPROFILE', 'VIRTUAL_ENV', 'WINDIR', 'ZES_ENABLE_SYSMAN', 'TERM_PROGRAM', 'TERM_PROGRAM_VERSION', 'LANG', 'COLORTERM', 'VSCODE_GIT_IPC_HANDLE', 'GIT_ASKPASS', 'VSCODE_GIT_ASKPASS_NODE', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS', 'VSCODE_GIT_ASKPASS_MAIN', 'DJANGO_SETTINGS_MODULE', 'RUN_MAIN', 'SERVER_NAME', 'GATEWAY_INTERFACE', 'SERVER_PORT', 'REMOTE_HOST', 'CONTENT_LENGTH', 'SCRIPT_NAME', 'SERVER_PROTOCOL', 'SERVER_SOFTWARE', 'REQUEST_METHOD', 'PATH_INFO', 'QUERY_STRING', 'REMOTE_ADDR', 'CONTENT_TYPE', 'HTTP_HOST', 'HTTP_CONNECTION', 'HTTP_PRAGMA', 'HTTP_CACHE_CONTROL', 'HTTP_SEC_CH_UA', 'HTTP_SEC_CH_UA_MOBILE', 'HTTP_SEC_CH_UA_PLATFORM', 'HTTP_UPGRADE_INSECURE_REQUESTS', 'HTTP_USER_AGENT', 'HTTP_ACCEPT', 'HTTP_SEC_FETCH_SITE', 'HTTP_SEC_FETCH_MODE', 'HTTP_SEC_FETCH_USER', 'HTTP_SEC_FETCH_DEST', 'HTTP_REFERER', 'HTTP_ACCEPT_ENCODING', 'HTTP_ACCEPT_LANGUAGE', 'HTTP_COOKIE', 'wsgi.input', 'wsgi.errors', 'wsgi.version', 'wsgi.run_once', 'wsgi.url_scheme', 'wsgi.multithread', 'wsgi.multiprocess', 'wsgi.file_wrapper', 'CSRF_COOKIE'
"""

edge_request_to_process = """
'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Bruce\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_23348_ZQMZBBLDBOHQZFPU', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DELL-GAMING-DES', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Bruce', 'LOCALAPPDATA': 'C:\\Users\\Bruce\\AppData\\Local', 'LOGONSERVER': '\\\\DELL-GAMING-DES', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\Bruce\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\Bruce\\OneDrive', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\Bruce\\.virtualenvs\\lab02_url_shortener-zO0gRMS_/Scripts;C:\\Program Files\\PowerShell\\7;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\PowerShell\\7\\;C:\\Shortcuts;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\Bruce\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\Bruce\\AppData\\Local\\GitHubDesktop\\bin;c:\\users\\bruce\\.local\\bin;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.LNK;.CPL', 'POWERSHELL_DISTRIBUTION_CHANNEL': 'MSI:Windows 10 Home', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 13, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0d', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\Bruce\\OneDrive\\Documents\\PowerShell\\Modules;C:\\Program Files\\PowerShell\\Modules;c:\\program files\\powershell\\7\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYTHONPATH': 'C:\\Users\\Bruce\\Programming\\', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\Bruce\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\Bruce\\AppData\\Local\\Temp', 'USERDOMAIN': 'DELL-GAMING-DES', 'USERDOMAIN_ROAMINGPROFILE': 'DELL-GAMING-DES', 'USERNAME': 'Bruce', 'USERPROFILE': 'C:\\Users\\Bruce', 'VIRTUAL_ENV': 'C:\\Users\\Bruce\\.virtualenvs\\lab02_url_shortener-zO0gRMS_', 'WINDIR': 'C:\\WINDOWS', 'ZES_ENABLE_SYSMAN': '1', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.64.2', 'LANG': 'en_US.UTF-8', 'COLORTERM': 'truecolor', 'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-87a105558d-sock', 'GIT_ASKPASS': 'c:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\Bruce\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 'DJANGO_SETTINGS_MODULE': 'short_project.settings', 'RUN_MAIN': 'true', 'SERVER_NAME': 'DELL-GAMING-DESKTOP', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'localhost:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_SEC_CH_UA': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"', 'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_SEC_CH_UA_PLATFORM': '"Windows"', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_SEC_FETCH_DEST': 'document', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9', 'HTTP_COOKIE': 'csrftoken=kK3pBo9UDKyvn9T6Gr0fL2V4nULG8ixPbvtZ2V4B1ke4liEiWGFosSRqImRKPoqb', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x0000012CD8823FA0>, 'wsgi.errors': <colorama.ansitowin32.StreamWrapper object at 0x0000012CD7145BA0>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 'kK3pBo9UDKyvn9T6Gr0fL2V4nULG8ixPbvtZ2V4B1ke4liEiWGFosSRqImRKPoqb'
"""


def remove_comma_space_return_rest(string):
    string = string.replace(', ', '\n')
    return string


# print(string_to_process)
# print(remove_comma_space_return_rest(string_to_process))


print(remove_comma_space_return_rest(edge_request_to_process))