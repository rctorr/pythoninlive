#-------------------------------------------------------------------------------
# Name:        Show text files
# Purpose:
# Read one text filwe and show it in one window
#
# Author:      rctorr
#
# Created:     12/03/2013
# Copyright:   (c) user 2013
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import gtk

class TextExample:
    def close_ap(self, widget):
        gtk.mainquit()

    def __init__(self):
        win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        win.set_usize(600, 500)
        win.connect("destroy", self.close_ap)
        win.set_title("Leyendo archivos de texto")
        win.set_border_width(0)

        box1 = gtk.VBox(gtk.FALSE, 0)
        win.add(box1)
        box1.show()

        box2 = gtk.VBox(gtk.FALSE, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, gtk.TRUE, gtk.TRUE, 0)
        box2.show()

        textview = gtk.TextView()
        textbuffer = textview.get_buffer()
        box2.pack_start(textview, gtk.TRUE, gtk.TRUE, 0)
        textview.show()

        # Carga del archivo
        infile = open("show-text-files.py", "r")

        if infile:
            lines = infile.read()
            infile.close()
            textbuffer.set_text(lines)

        button = gtk.Button("Close")
        button.connect("clicked", self.close_ap)
        box2.pack_start(button, gtk.TRUE, gtk.TRUE, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()

        win.show()


def main():
    gtk.mainloop()
    return 0

if __name__ == '__main__':
    TextExample()
    main()
