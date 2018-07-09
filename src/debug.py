from httpSystemControl import Service

s = Service("/var/run/httpSystemControlDebug.pid")
s.run()
