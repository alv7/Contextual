
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from os import listdir
from os.path import isfile, join
import c_search as csearch

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
#set word wrap
te.set_wrap_mode(2)

def show_file(file_name):
	text_buffer = Gtk.TextBuffer()
	text_buffer.set_text('')
	with open(join(NOTES_PATH, file_name), 'r') as fl:
		text_buffer.set_text(fl.read())
	te.set_buffer(text_buffer)

def tree_selection_changed(selection):
	model, treeiter = selection.get_selected()
	if treeiter != None:
		show_file(model[treeiter][0])

tree.get_selection().connect("changed", tree_selection_changed)

# File Names, Text Editor Split View
vp = Gtk.VPaned()
vp.add1(scrollTree)

text_view_scroll_view = Gtk.ScrolledWindow()
text_view_scroll_view.add(te)
vp.add2(text_view_scroll_view)

# Search Create Text Bar
sc = Gtk.Entry()
sc.set_placeholder_text('Search or Create')

def on_text_change(entry):
	file_names = csearch.search_folder(entry.get_text())
	print(file_names, entry.get_text())
	store.clear()
	for name in file_names:
		store.append([name])

sc.connect('changed', on_text_change)

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
