import subprocess
import pykka

from mopidy.core import CoreListener


class NotifierFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(NotifierFrontend, self).__init__()
        self.config = config
        self.core = core

    def on_start(self):
        print('start')

    def on_stop(self):
        print('stop')

    def track_playback_started(self, tl_track):
        print('started')
