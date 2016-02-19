import threading
import modules.file_processor as file_processor

class FileProcessorWorker(threading.Thread):

    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            filePath = self.__queue.get()
            if filePath is None:
                break            
            file_processor.process(filePath)
