import urwid
import webbrowser
from api_interface import get_recent

def menu(title, track_listing):
	body = [
			urwid.Text(title),
			urwid.Divider()
			]
	for c in track_listing:
		button = urwid.Button(c) # create a new button from c

		# call item_chosen(c) on click event,
		urwid.connect_signal(button, 'click', item_chosen, c) 
		#append to the list of menuitems (focus_map: apply different styling when focused.)
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
	response = urwid.Text([u"You chose: ", choice, u"\n"])
	done = urwid.Button(u"Ok")
	urwid.connect_signal(done, 'click', exit_program)
#	urwid.connect_signal(done, 'click', open_browser)
	main.original_widget = urwid.Filler(
			urwid.Pile(
				[
					response,
					urwid.AttrMap(done, None, focus_map='reversed')
					]
				)
			)

def exit_program(button):
	raise urwid.ExitMainLoop()

def open_browser(button):
	webbrowser.open_new('http://www.python.org')

def get_track_listing():
	tracks = get_recent(5)
	track_listing = []
	for track in tracks:
		track_listing.append(f"{track.artist} - {track.name}")
	return track_listing

track_listing = get_track_listing()
main = urwid.Padding(menu(u"Recent tracks", track_listing), left=3, right=3)
#top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
#	align='center', width=('relative', 60),
#	valign='middle', height=('relative', 60),
#	min_width=20, min_height=9)
#urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
loop = urwid.MainLoop(main, palette=[('reversed', 'standout', 'default')])
loop.run()
