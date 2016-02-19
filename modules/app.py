import Queue, time, multiprocessing
import modules.file_to_process_retriever as file_to_process_retriever
from modules.file_processor_worker import FileProcessorWorker

class App:

    WORKERS = multiprocessing.cpu_count()

    def start(self, arguments):
        print 'App started {0}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
        self.__arguments = arguments
        self.__queue = Queue.Queue(0)
        self.start_workers()
        self.add_files_to_queue()
        self.__queue.join()
        self.add_queue_terminators()
        print 'App ended {0}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))

    def start_workers(self):
        for i in range(self.WORKERS):
            FileProcessorWorker(self.__queue).start()

    def add_files_to_queue(self):
        files = file_to_process_retriever.retrieve(self.__arguments[1])
        for filePath in files:
            self.__queue.put(filePath)

    def add_queue_terminators():
        for i in range(self.WORKERS):
            self.__queue.put(None)
