class WordsFinder:
    def __init__(self,*files):
        self.file_names=files
    
    def get_all_words(self):
        for file in self.file_names:
