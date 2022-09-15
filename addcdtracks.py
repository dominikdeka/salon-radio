#!/usr/bin/env python

import asyncio
import websockets
import json
import audio_manager

async def addCdTracks(uri):
    audio_manager.releaseAudioResource('mopidy')
    async with websockets.connect(uri) as websocket:
        data = []
        await websocket.send(json.dumps({"jsonrpc":"2.0","id":0,"method":"core.playback.stop"}, indent='\t'))

        await websocket.send(json.dumps({"jsonrpc":"2.0","id":1,"method":"core.tracklist.clear"}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc":"2.0","id":2,"method":"core.library.browse","params":{"uri":"cd:/"}}, indent='\t'))

        while 'id' not in data or data['id'] != 2:
            message = await websocket.recv()
            data = json.loads(message)

        uris = []
        if data:
            for v in data['result']:
                uris.append(v['uri'])
        await websocket.send(json.dumps({"jsonrpc":"2.0","id":3,"method":"core.tracklist.add", "params": {"uris": uris}}, indent='\t'))

        await websocket.send(json.dumps({"jsonrpc":"2.0","id":4,"method":"core.tracklist.set_random", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc":"2.0","id":5,"method":"core.tracklist.set_single", "params": {"value": False}}, indent='\t'))
        await websocket.send(json.dumps({"jsonrpc":"2.0","id":6,"method":"core.tracklist.set_repeat", "params": {"value": True}}, indent='\t'))


        while 'id' not in data or data['id'] != 6:
            message = await websocket.recv()
            data = json.loads(message)

        await websocket.send(json.dumps({"jsonrpc":"2.0","id":6,"method":"core.playback.play"}, indent='\t'))

asyncio.get_event_loop().run_until_complete(
    addCdTracks('ws://192.168.1.36:6680/mopidy/ws'))
