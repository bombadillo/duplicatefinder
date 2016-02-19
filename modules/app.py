import Queue
import modules.file_to_process_retriever as file_to_process_retriever
from modules.file_processor_worker import FileProcessorWorker

class App:

    dups_found = 0
    WORKERS = 2

    def start(self, arguments):
        queue = Queue.Queue(0)
        for i in range(self.WORKERS):
            FileProcessorWorker(queue).start()

        files = file_to_process_retriever.retrieve(arguments[1])
        for filePath in files:
            queue.put(filePath)

        for i in range(self.WORKERS):
            queue.put(None)
