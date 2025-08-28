class Author:

    def __init__(self, author):
        self.name = author
        self.books = []
        self.mentioned_by = {}
        self.mentions = {}

    def add_book(self, book):
        self.books.append(book)


    def add_mention_by(self, author, count, lines):
        if author not in self.mentioned_by:
            self.mentioned_by[author] = {'count': count, 'lines': lines}
        else:
            self.mentioned_by[author]['count'] += count
            self.mentioned_by[author]['lines'].extend(lines)

    def __str__(self):
        return self.name
