import sys, time
import modules.file_to_process_retriever as file_to_process_retriever
import modules.file_processor as file_processor

print time.strftime("%Y-%m-%d %H:%M:%S")

files = file_to_process_retriever.retrieve(sys.argv[1])

dups_found = 0
for filePath in files:
    dups_found += file_processor.process(filePath)

print '{0} duplicates found'.format(dups_found)

print time.strftime("%Y-%m-%d %H:%M:%S")
