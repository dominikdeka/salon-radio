#!/usr/bin/env python

import asyncio
import websockets

import RPi.GPIO as GPIO
import time
import json
import os
import signal
import subprocess
import re
from multiprocessing import Pool
import audio_manager


# from pigpio_encoder import pigpio_encoder

async def playpause(uri):
    async with websockets.connect(uri) as websocket:

        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.get_state"}, indent='\t'))
        message = await websocket.recv()
        data = json.loads(message)

        if data['result'] == 'playing':
            await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.pause"}, indent='\t'))
        else:
            await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}, indent='\t'))

async def playnext(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.next"}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_single", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": True}}, indent='\t'))

async def playprevious(uri):
    async with websockets.connect(uri) as websocket:
        #        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_single", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.previous"}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_single", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": True}}, indent='\t'))

async def play357(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"method":"core.mixer.set_volume","params":{"volume":35},"jsonrpc":"2.0","id":47}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.clear","jsonrpc":"2.0","id":73}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.add","params":{"uris":["https://stream.rcs.revma.com/ye5kghkgcm0uv"]},"jsonrpc":"2.0","id":87}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}, indent='\t'))

async def playNS(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"method":"core.mixer.set_volume","params":{"volume":35},"jsonrpc":"2.0","id":47}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.clear","jsonrpc":"2.0","id":73}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.add","params":{"uris":["https://stream.rcs.revma.com/ypqt40u0x1zuv"]},"jsonrpc":"2.0","id":87}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}, indent='\t'))

async def play1(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"method":"core.mixer.set_volume","params":{"volume":35},"jsonrpc":"2.0","id":47}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.clear","jsonrpc":"2.0","id":73}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.add","params":{"uris":["tunein:station:s9542"]},"jsonrpc":"2.0","id":87}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}, indent='\t'))

async def play2(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"method":"core.mixer.set_volume","params":{"volume":35},"jsonrpc":"2.0","id":47}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.clear","jsonrpc":"2.0","id":73}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.add","params":{"uris":["tunein:station:s20311"]},"jsonrpc":"2.0","id":87}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}, indent='\t'))

async def play3(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"method":"core.mixer.set_volume","params":{"volume":35},"jsonrpc":"2.0","id":47}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.clear","jsonrpc":"2.0","id":73}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"method":"core.tracklist.add","params":{"uris":["tunein:station:s103812"]},"jsonrpc":"2.0","id":87}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}, indent='\t'))


# def rotary_callback(counter):
#     print("Counter value: ", counter)
#
# def sw_short():
#     print("Switch pressed")

# my_rotary = pigpio_encoder.Rotary(clk=23, dt=24, sw=27)
# my_rotary.setup_rotary(rotary_callback=rotary_callback)
# my_rotary.setup_switch(sw_short_callback=sw_short)

# Pin In Number
CHANGE_STATE_PINS = {
    23: {'lastStatus': 0},
    22: {'lastStatus': 0},
    24: {'lastStatus': 0},
    25: {'lastStatus': 0},
    5: {'lastStatus': 0},
    6: {'lastStatus': 0},
    12: {'lastStatus': 0},
    # 17: {'lastStatus': 0},
    13: {'lastStatus': 0},
    16: {'lastStatus': 0},
    26: {'lastStatus': 0},
    14: {'lastStatus': 0}
}
Enc_A = 27
Enc_B = 15
# 17,25,
GPIO.setmode(GPIO.BCM)
for k, v in CHANGE_STATE_PINS.items():
    GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(Enc_A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Enc_B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

currentPlaylist = {}
tp = Pool(10)

async def jumpplaylists(uri, prefix):
    async with websockets.connect(uri) as websocket:

        global currentPlaylist
        previousPlaylistUri = ''

        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playlists.as_list"}, indent='\t'))
        message = await websocket.recv()
        data = json.loads(message)
        result = [k for k in data['result'] if k['name'].startswith(prefix)]
        if currentPlaylist == {} or prefix not in currentPlaylist['name']:
            currentPlaylist = result[0]
        else:
            for v in result:
                if previousPlaylistUri == currentPlaylist['uri']:
                    currentPlaylist = v
                    break
                else:
                    previousPlaylistUri = v['uri']

            if currentPlaylist['uri'] == previousPlaylistUri:
                currentPlaylist = result[0]
        print(currentPlaylist)
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playlists.get_items", "params": {"uri": currentPlaylist['uri']}}, indent='\t'))
        message = await websocket.recv()
        data = json.loads(message)
        uris = []
        for v in data['result']:
            uris.append(v['uri'])
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.clear"}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.add", "params": {"uris": uris}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_random", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_single", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.set_repeat", "params": {"value": True}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}, indent='\t'))

async def changestate(uri, pin):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({'pin': pin}, indent='\t'))

def rotation_decode(Enc_A):
    time.sleep(0.002)
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)

    if (Switch_A == 1) and (Switch_B == 0):
        tp.apply_async(audio_manager.volumeUp)
        print("direction -> ")
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        return

    elif (Switch_A == 1) and (Switch_B == 1):
        tp.apply_async(audio_manager.volumeDown)
        print("direction <- ")
        while Switch_A == 1:
            Switch_A = GPIO.input(Enc_A)
        return
    else:
        return

try:
    print("start")
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=10)

    while True:
        for k, v in CHANGE_STATE_PINS.items():
            pin_status = GPIO.input(k)

            if v['lastStatus'] == 1 and pin_status == 0:
                if k == 16:
                    asyncio.get_event_loop().run_until_complete(
                        playnext('ws://192.168.1.36:6680/mopidy/ws'))
                elif k == 13:
                    asyncio.get_event_loop().run_until_complete(
                        playpause('ws://192.168.1.36:6680/mopidy/ws'))
                elif k == 12:
                    asyncio.get_event_loop().run_until_complete(
                        playprevious('ws://192.168.1.36:6680/mopidy/ws'))
                elif k == 24:
                    audio_manager.releaseAudioResource('mopidy')
                    asyncio.get_event_loop().run_until_complete(
                        # play1('ws://192.168.1.36:6680/mopidy/ws'))
                        playNS('ws://192.168.1.36:6680/mopidy/ws'))
                elif k == 22:
                    audio_manager.releaseAudioResource('mopidy')
                    asyncio.get_event_loop().run_until_complete(
                        # play2('ws://192.168.1.36:6680/mopidy/ws'))
                        play357('ws://192.168.1.36:6680/mopidy/ws'))
                elif k == 14:
                    subprocess.run(['amixer', 'sset', 'Digital', 'toggle'], stdout=subprocess.PIPE)
                elif k == 25:
                    audio_manager.releaseAudioResource('mopidy')
                    asyncio.get_event_loop().run_until_complete(
                        jumpplaylists('ws://192.168.1.36:6680/mopidy/ws', '1_'))
                elif k == 5:
                    audio_manager.releaseAudioResource('mopidy')
                    asyncio.get_event_loop().run_until_complete(
                        jumpplaylists('ws://192.168.1.36:6680/mopidy/ws', '2_'))
                elif k == 6:
                    audio_manager.releaseAudioResource('mopidy')
                    asyncio.get_event_loop().run_until_complete(
                        jumpplaylists('ws://192.168.1.36:6680/mopidy/ws', '3_'))
                elif k == 26:
                    asyncio.get_event_loop().run_until_complete(
                        changestate('ws://192.168.1.12:8899', 3))
                elif k == 23:
                    print("kodi")
                    audio_manager.releaseAudioResource('kodi')
                    result = subprocess.Popen(['runuser', '-u', 'pi', '--', 'kodi', '&'], stdout=subprocess.PIPE)
                    # asyncio.get_event_loop().run_until_complete(
                    #     play3('ws://192.168.1.36:6680/mopidy/ws'))

            CHANGE_STATE_PINS[k]['lastStatus'] = pin_status
        time.sleep(0.1)
finally:
    GPIO.cleanup()

