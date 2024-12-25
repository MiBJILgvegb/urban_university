import os.path,string

class WordsFinder:
    def __init__(self,*files):
        self.file_names=files
        self.work_dir=os.path.dirname(os.path.realpath(__file__))

    def _file_exists(self,file_name):
        return os.path.exists(file_name)
    def _read_and_convert(self,file_path):
        with open(file_path, "r") as f:
            s = f.read()
            for char in s:
                if char in string.punctuation:
                    s = s.replace(char, "").lower()
            return s.split()
    def get_all_words(self):
        result={key: [] for key in self.file_names}
        for file_name in self.file_names:
            file_path = self.work_dir + "\\" + file_name
            if(not self._file_exists(file_path)):
                print(f"Файл {file_name} не найден.")
                continue
            result[file_name]=self._read_and_convert(file_path)
        return  result
    def find(self,word):
        all_words=self.get_all_words()
        result={key: [] for key in self.file_names}
        for file in all_words.keys():
            #result[file] =-1
            #if(word in all_words[file]):
                result[file]=all_words[file].index(word.lower())+1
        return  result
    def count(self,word):
        all_words=self.get_all_words()
        result={key: [] for key in self.file_names}
        for file in all_words.keys():
            result[file]=all_words[file].count(word.lower())
        return  result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего