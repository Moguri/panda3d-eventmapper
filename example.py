import sys

from direct.showbase.ShowBase import ShowBase
import panda3d.core as p3d

import eventmapper


p3d.load_prc_file_data(
    '',
    'event-map-item-quit escape q\n'
    'event-map-item-move-forward raw-w\n'
    'event-map-item-move-backward raw-s\n'
    'event-map-item-move-left raw-a\n'
    'event-map-item-move-right raw-d\n'
)


class GameApp(ShowBase):
    def __init__(self):
        super().__init__()

        self.eventmapper = eventmapper.EventMapper()
        self.accept('quit', sys.exit)
        self.accept('move-forward', print, ['move forward'])
        self.accept('move-backward', print, ['move backward'])
        self.accept('move-left', print, ['move left'])
        self.accept('move-right', print, ['move right'])

GameApp().run()
