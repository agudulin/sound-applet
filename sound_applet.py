#!/usr/bin/env python
#-*- coding: utf-8 -*-

import appindicator
import pygtk
import gtk
import pynotify
import os
from amixer_parser import AmixerParser as amixer

import dbus, gobject
from dbus.mainloop.glib import DBusGMainLoop

class SoundApplet(object):
    """SoundApplet class"""
    def __init__(self, control, icon_name):
        self.control = control
        self.indicator = appindicator.Indicator("sound-applet", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)
        self.indicator_icon = "audio-volume-" + icon_name + "-panel"
        self.indicator.set_attention_icon(self.indicator_icon)
        self.indicator.set_icon(self.indicator_icon)
        
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
        bus.add_signal_receiver(self.change_icon, dbus_interface="com.sagod.SoundApplet", signal_name="current_volume")
        
        self.menu = gtk.Menu()
        
        quit_item = gtk.MenuItem("Quit")
        quit_item.connect("activate", self.quit)
        quit_item.show()
        self.menu.append(quit_item)
     
        self.menu.show()
        self.indicator.set_menu(self.menu)
        
    def quit(self, *arg):
        """Closes applet"""
        gtk.main_quit()
        
    def change_icon(self, current_volume):
        self.indicator_icon = "audio-volume-" + self.control[current_volume] + "-panel"
        self.indicator.set_attention_icon(self.indicator_icon)
        self.indicator.set_icon(self.indicator_icon)
        
        
if __name__ == '__main__':
    control = []
    control.append("muted")
    for i in range(1,  8): control.append("low-zero")
    for i in range(8,  15): control.append("low-panel")
    for i in range(15, 22): control.append("medium")
    for i in range(22, 32): control.append("high")
    
    amixer = amixer()
    volume = amixer.get_volume()
    icon_name = control[volume]
    
    indicator = SoundApplet(control, icon_name)
    gtk.main()

