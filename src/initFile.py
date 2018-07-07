#!/usr/bin/python
#  /etc/init.d/http-system-control
### BEGIN INIT INFO
# Provides:             led
# Required-Start        $remote_fs $syslog
# Required-Stop         $remote_fs $syslog
# Default-Start:        2 3 4 5
# Default-Stop          0 1 6
# Short-Description     System control through HTTP
# Description           Provides control and informtion about this system through a REST API interface
### END INIT INFO

import sys
from httpSystemControl import Service

service = Service("/var/run/http-system-control.pid")

if len(sys.argv) < 2:
	print("Please either use start, stop or restart")
elif sys.argv[1] == "start":
	service.start()
elif sys.argv[1] == "stop":
	service.stop()
elif sys.argv[1] == "restart":
	service.restart()
else:
	print("Please either use start, stop or restart")

