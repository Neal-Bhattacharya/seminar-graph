import os
import sys

from utils.book import Book
from pathlib import Path

class BookReader:
    files = os.listdir('../books')

    def getBooks(self):
        books = []
        for book in self.files:
            f = open('../books/' + book, 'r')
            if "DS_Store" in f.name:
                continue
            name = Path(f.name).stem.split('-')
            lines = [line.strip() for line in f.readlines() if line.strip() != '']
            books.append(Book(name[0], name[1], lines))
        return books