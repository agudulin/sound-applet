#!/usr/bin/env python
#-*- coding: utf-8 -*-

import appindicator
import pygtk
import gtk
import pynotify
import os
from amixer_parser import AmixerParser as amixer

__path__ = os.getcwd()

class SoundApplet(object):
    """SoundApplet class"""
    def __init__(self, icon_name):
        self.indicator = appindicator.Indicator("sound-applet", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)
        self.indicator_icon = "audio-volume-" + icon_name + "-panel"
        self.indicator.set_attention_icon(self.indicator_icon)
        self.indicator.set_icon(self.indicator_icon)
        
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
    #print volume, icon_name
    
    indicator = SoundApplet(icon_name)
    gtk.main()

