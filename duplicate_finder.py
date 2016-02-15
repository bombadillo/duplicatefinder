import sys, time
import modules.file_processor as file_processor

print time.strftime("%Y-%m-%d %H:%M:%S")
file_processor.process(sys.argv[1])
print time.strftime("%Y-%m-%d %H:%M:%S")
