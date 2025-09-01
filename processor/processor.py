import re
import time
from book_reader.reader import BookReader
from utils.author import Author


def populate_word_frequencies(book):
    word_frequencies = {}
    word_count = 0
    lines = book.get_lines()
    print("Reading {} by {}...".format(book.title, book.author))
    for line in lines:
        line = re.sub(r'[^\w\s]','',line)
        words = re.split("\\s+", line)
        for word in words:
            word_count += 1
            if word not in word_frequencies:
                word_frequencies[word] = {
                    'count' : 1,
                    'lines': [line]
                }
            else:
                word_frequencies[word]['count'] += 1
                word_frequencies[word]['lines'].append(line)
    book.set_word_freqs(word_frequencies)
    return word_count


def predicate(word, author_name, book):
    author_name = author_name.replace(' ', '')
    author_name = author_name.replace(',', '')
    return ((author_name in word)
            and author_name != book.author
            and not word.startswith("IGNORE"))


class Processor:
    def __init__(self):
        self.authors = {}
        self.books = []
        self.edges = []

    def print_done(self):
        print("\033[1;32m" + "Done!" + "\033[0m")
        print("------------------------------------------------")

    def get_books_from_reader(self):
        r = BookReader()
        self.books = r.getBooks()
        return self.books

    def populate_all_word_freqs(self):
        print("Reading books:")
        count = 0
        for book in self.books:
            count += populate_word_frequencies(book)
        self.print_done()
        print("Total words:", count)

    def populate_mentions(self):
        print("Finding mentions:")

        author_names = set([book.author for book in self.books])

        for author_name in author_names:
            self.authors[author_name] = Author(author_name)
        for book in self.books:
            freqs = book.get_word_freqs()
            for word in freqs.keys():
                for author_name in self.authors:
                    if predicate(word, author_name, book):
                        print("Found {} in {} by {} {} times".format(word, book.title, book.author, freqs[word]['count']))
                        self.authors[author_name].add_mention_by(
                            book.author,
                            freqs[word]['count'],
                            freqs[word]['lines']
                        )
        self.print_done()

    def get_edges(self):
        for author in self.authors:
            for a in self.authors[author].mentioned_by:
                count = self.authors[author].mentioned_by[a]['count']
                self.edges.append((author, a, count))

        return self.edges

    def get_lines(self, mentionee, mentioner):
        return self.authors[mentionee].mentioned_by[mentioner]['lines']

    def run(self):
        self.get_books_from_reader()
        self.populate_all_word_freqs()
        self.populate_mentions()



'''
for k in authors:
    print("{} is mentioned by.,.".format(k))
    for a in authors[k].mentioned_by:
        count = authors[k].mentioned_by[a]['count']
        print("  {} {} time{}".format(a, count, "s" if count > 1 else ""))
'''
