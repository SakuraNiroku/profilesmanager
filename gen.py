import json
import os

profiles = []

def check_dir_exists(dir_path):
  return os.path.exists(dir_path) and os.path.isdir(dir_path)

if not check_dir_exists('dist'):
    os.makedirs('dist')

with open('profiles.txt','r') as f:
    a = f.read().splitlines()
    for b in a:
        c = b.split('|')
        profiles.append({'name':c[0],'url':c[1]})

with open('dist/profiles.json','w') as f:
    f.write(json.dumps(profiles))