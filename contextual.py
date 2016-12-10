

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from os import listdir
from os.path import isfile, join

NOTES_PATH = 'notes'

store = Gtk.ListStore(str)

# get file names
file_names = [f for f in listdir(NOTES_PATH) if isfile(join(NOTES_PATH, f))]
for name in file_names:
	store.append([name])

#file name list view
tree =  Gtk.TreeView(store)
renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Title", renderer, text=0)
tree.append_column(column)
scrollTree = Gtk.ScrolledWindow()
scrollTree.add(tree)

# Text Editor
te = Gtk.TextView()

# File Names, Text Editor Split View
vp = Gtk.VPaned()
vp.add1(scrollTree)
vp.add2(te)

# Search Create Text Bar
sc = Gtk.Entry()
sc.set_placeholder_text('Search or Create')

# Put view into container
vb = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
vb.pack_start(sc, False, False, 0)
vb.pack_start(vp, True, True, 0)

# Set up window, add views
win = Gtk.Window()
win.set_title('Contextual')
win.connect("delete-event", Gtk.main_quit)

win.add(vb)
win.show_all()

Gtk.main()

