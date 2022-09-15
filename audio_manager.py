import subprocess
import re
import asyncio
import websockets
import json

async def stopPlayback(uri):
    print(uri)
    async with websockets.connect(uri) as websocket:
        print(uri)
        await websocket.send(json.dumps({"jsonrpc":"2.0","id":0,"method":"core.playback.stop"}, indent='\t'))

def releaseAudioResource(recipient):
    result = subprocess.run(['/home/pi/salon-radio/list_audio_consumers.sh'], stdout=subprocess.PIPE)
    matchObj = re.search(r'channels', result.stdout.decode('utf-8'), re.M)
    if(matchObj):
        a = matchObj.group(0)
        if a == 'channels':
            result = subprocess.run(['sudo', 'lsof', '/dev/snd/pcmC0D0p'], stdout=subprocess.PIPE)
            matchObj = re.search(r'^([^ ]*)([ ]*)([0-9]*)(.*)pcmC0D0p', result.stdout.decode('utf-8'), re.M)

            a = matchObj.group(1)
            if a != recipient:
                if a == 'mopidy':
                    print('mopidy')
                    asyncio.get_event_loop().run_until_complete(
                        stopPlayback('ws://192.168.1.36:6680/mopidy/ws'))
                if a == 'pulseaudio':
                    print('chrome')
                    print(matchObj.group(3))
                    subprocess.run(['sudo', 'kill', '-9', matchObj.group(3)], stdout=subprocess.PIPE)
                if a == 'kodi.bin_':
                    print('kodi')
                    print(matchObj.group(3))
                    subprocess.run(['sudo', 'kill', '-9', matchObj.group(3)], stdout=subprocess.PIPE)

def volumeUp():
    result = subprocess.run(['amixer', 'sget', 'Digital'], stdout=subprocess.PIPE)
    matchObj = re.search(r'Front Left: Playback(.*)\[(.*)\%\]', result.stdout.decode('utf-8'), re.M)
    a = int(matchObj.group(2));
    if a <= 75:
        subprocess.run(['amixer', 'sset', 'Digital', '2%+'], stdout=subprocess.PIPE)
    print("direction --> ")


def volumeDown():
    subprocess.run(['amixer', 'sset', 'Digital', '2%-'], stdout=subprocess.PIPE)
    print("direction <-- ")
