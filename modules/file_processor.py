import collections, hashlib
import modules.file_writer as file_writer
from modules.config import Config

current_line_number = 0

def process(file_name):
    global current_line_number
    d = collections.defaultdict(list)
    with open(file_name, 'r') as datafile:
        for line in datafile:
            current_line_number += 1
            id = hashlib.sha256(line).digest()
            k = id[0:2]
            v = id[2:]
            if v in d[k]:
                line = line.replace('\n', '')
                string_to_write = 'Line No: {0} - {1}'.format(current_line_number, line)
                file_writer.write_string(string_to_write, Config.output_file)
            else:
                d[k].append(v)
