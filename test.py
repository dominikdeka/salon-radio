from mopidy import core
import time

def PlaybackStopped():
    print('stopped')

def PlaybackPlaying():
    print('playing')

def playbackStateChanged(self, OldState, NewState):
  print(OldState)
  print(NewState)
  print('lala')

listener = core.CoreListener()
listener.playback_state_changed = playbackStateChanged
# listener.track_playback_paused(PlaybackStopped)

while True:
    time.sleep(0.1)
