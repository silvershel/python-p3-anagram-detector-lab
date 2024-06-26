class Anagram:

    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        match_list = []
        for str in list:
            if sorted(str) == sorted(self.word):
                match_list.append(str)
        return match_list