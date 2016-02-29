import collections, hashlib, threading
import modules.file_writer as file_writer
from modules.config import Config

lock = threading.Lock()

def process(file_name):
    with lock:
        print 'Processing file {0}'.format(file_name)
    current_line_number = 0
    dups_found = 0
    d = collections.defaultdict(list)
    with open(file_name, 'r') as datafile:
        for line in datafile:
            line = remove_value_from_string(line)
            current_line_number += 1
            id = hashlib.sha256(line).digest()
            k = id[0:2]
            v = id[2:]
            if v in d[k]:
                dups_found += 1
                line = line.replace('\n', '')
                string_to_write = '"{0}" on Line {1} in {2}{3}'.format(line, current_line_number, file_name, Config.new_line)
                file_writer.write_string(string_to_write, Config.output_file)
            else:
                d[k].append(v)
    with lock:
        print '{0} duplicates found in file {1}'.format(dups_found, file_name)


def remove_value_from_string(line):
    line_split = line.split('|')
    del line_split[4]
    new_line = '|'.join(str(x) for x in line_split)
    return new_line
