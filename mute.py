import subprocess

subprocess.run(['amixer', 'sset', 'Digital', 'toggle'], stdout=subprocess.PIPE)
