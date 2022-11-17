import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='r',
                    help="file open mode.")

args = parser.parse_args()
mode = str(input('Enter file open mode.\n'))


if mode == 'w':
    args.mode = mode
    text = str(input('Write your text:\n'))
    file = open('cli_file', args.mode, encoding='utf-8')
    file.write(text)
    file.close()

args.mode = 'r'
file_read = open('cli_file', args.mode, encoding='utf-8')
var = str(file_read.read())
sys.stdout.write(str(var))
print(file_read.tell(), end='\n')
print(file_read.read())
file_read.close()
