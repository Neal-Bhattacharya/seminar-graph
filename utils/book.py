from utils.author import Author


class Book:

    def __init__(self, author, title, lines):
        self.author = author
        self.title = title
        self.lines = lines
        self.word_freqs = {}
        self.mentions = {}

    def add_mention(self, mention):
        for k,v  in mention:
            if k not in self.mentions:
                self.mentions[k] = v
            else: self.mentions[k] += v

    def set_word_freqs(self, word_freqs):
        self.word_freqs = word_freqs

    def get_word_freqs(self):
        return self.word_freqs

    def get_lines(self):
        return self.lines

    def __str__(self):
        return "Author: {}; Title: {}".format(self.author, self.title)

