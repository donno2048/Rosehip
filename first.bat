curl.exe -o p.exe https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe --ssl-no-revoke
START /WAIT p.exe /quiet PrependPath=1
second.bat
