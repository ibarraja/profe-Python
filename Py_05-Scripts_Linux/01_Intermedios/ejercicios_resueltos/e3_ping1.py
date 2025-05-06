#!/usr/bin/python3

import sys
import subprocess


def main() -> None:
   ip = get_ip()
   test_comunication(ip)


def get_ip() -> str:
   if len(sys.argv[1:]) != 1:
       print('ERROR: Hay que suministar la dirección IP')
       sys.exit(1)

   ip = sys.argv[1]
   return ip


def test_comunication(ip: str) -> None:
   result = subprocess.run(
       ['ping', '-c', '1', ip],
       text = True,
       capture_output = True
   )

   if result.returncode == 0:
       print('Hay comunicación con el destino')
   else:
       print('No hay comunicación con el destino')


if __name__ == '__main__':
   main()
 