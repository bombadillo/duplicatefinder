import modules.file_to_process_retriever as file_to_process_retriever
import modules.file_processor as file_processor

class App:

    dups_found = 0

    def start(self, arguments):
        files = file_to_process_retriever.retrieve(arguments[1])
        for filePath in files:
            self.dups_found += file_processor.process(filePath)
        print '{0} duplicates found'.format(self.dups_found)
