import subprocess
import shutil
import os

# See https://github.com/arcsecw/wubi/issues/8
if not os.path.isdir('wubi'):
  subprocess.run(['git', 'clone', 'https://github.com/arcsecw/wubi', 'wubi-repo'])
  shutil.move('wubi-repo/wubi', '.')

import wubi

original = '很高兴见到你'
words = wubi.get(original, 'cw')
print(words)
print(original)

for word, orig in zip(words.split(), original):
  files = [f'{c}.png' for c in word]
  subprocess.run(['montage', '-tile', 'x0'] + files + ['test.png'])
  subprocess.run([
      'convert', 'test.png', '-font', '/Library/Fonts/Arial Unicode.ttf', '-pointsize', '50',
      f"label:{orig}", '-gravity', 'Center', '-append', 'test2.png'
  ])
  subprocess.run(['convert', 'test2.png', '-bordercolor', 'Black', '-border', '1x1', f'{orig}.png'])
