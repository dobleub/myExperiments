:from pyramid_socketio.io import SocketIOContext, socketio_manage
import gevent

class ConnectIOContext(SocketIOContext):
    def msg_connect(self, msg):
        self.msg("connected")
        import subprocess

        def sendtop():
            prev = None
            while self.io.connected():
                cmd = 'top -b -n 1'
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                txt = p.communicate()[0]
                self.msg("showdata", txt = txt)
                gevent.sleep(1.0)

        self.spawn(sendtop)

@view_config(route_name="socket.io")
def socket_io(request):
    print "Socket.IO request running"
    retval = socketio_manage(ConnectIOContext(request))
    return Response(retval)

@view_config(route_name="top", 
             renderer='ejemplo:templates/htop.html')
def htop(request):
    return {}