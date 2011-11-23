import dbus.service
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import sys
 
class VolumeChanged(dbus.service.Object):

    def __init__(self, object_path):
        dbus_loop = DBusGMainLoop()
        bus = dbus.SystemBus(mainloop=dbus_loop)
        dbus.service.Object.__init__(self, bus, object_path)

    @dbus.service.signal(dbus_interface='com.sagod.SoundApplet', signature='u')
    def current_volume(self, volume):
        pass

volume = 15
if sys.argv[1]:
    volume = int(sys.argv[1])
sgnl = VolumeChanged('/current_volume')
sgnl.current_volume(volume)
