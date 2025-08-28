import re

from book_reader.reader import BookReader
from utils.author import Author


class Processor:
    def __init__(self):
        self.authors = {}
        self.books = []
        self.edges = []
    def get_books_from_reader(self):
        r = BookReader()
        self.books = r.getBooks()
        return self.books

    def set_word_frequencies(self, book):
        word_frequencies = {}
        lines = book.get_lines()
        print("Reading {} by {}...".format(book.title, book.author))
        for line in lines:
            line = re.sub(r'[^\w\s]','',line)
            words = re.split("\\s+", line)
            for word in words:

                if word not in word_frequencies:
                    word_frequencies[word] = {
                        'count' : 1,
                        'lines': [line]
                    }
                else:
                    word_frequencies[word]['count'] += 1
                    word_frequencies[word]['lines'].append(line)
        book.set_word_freqs(word_frequencies)

    def set_all_word_freqs(self):
        for book in self.books:
            self.set_word_frequencies(book)

    def predicate(self, word, author_name, book):
        author_name = author_name.replace(' ', '')
        author_name = author_name.replace(',', '')
        return ((author_name == word or author_name in word + "s")
                and author_name != book.author
                and not word.startswith("IGNORE"))

    def populate_mentions(self):
        self.set_all_word_freqs()
        author_names = set([book.author for book in self.books])

        for author_name in author_names:
            self.authors[author_name] = Author(author_name)
        for book in self.books:
            freqs = book.get_word_freqs()
            for word in freqs.keys():
                for author_name in self.authors:
                    if self.predicate(word, author_name, book):
                        print("Found {} in {} by {} {} times".format(word, book.title, book.author, freqs[word]['count']))
                        self.authors[author_name].add_mention_by(
                            book.author,
                            freqs[word]['count'],
                            freqs[word]['lines']
                        )
                        continue

    def get_edges(self):
        if len(self.edges) > 0:
            return self.edges
        for author in self.authors:
            for a in self.authors[author].mentioned_by:
                count = self.authors[author].mentioned_by[a]['count']
                self.edges.append((author, a, count))

        return self.edges

    def run(self):
        self.get_books_from_reader()
        self.set_all_word_freqs()
        self.populate_mentions()

'''
for k in authors:
    print("{} is mentioned by.,.".format(k))
    for a in authors[k].mentioned_by:
        count = authors[k].mentioned_by[a]['count']
        print("  {} {} time{}".format(a, count, "s" if count > 1 else ""))
'''