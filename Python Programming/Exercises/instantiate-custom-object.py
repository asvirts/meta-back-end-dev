class MyFirstClass:
    def __init__(self, philosopher, book):
        self.philosopher = philosopher
        self.book = book
        print("Who wrote this?")

    def hand_list(self):
        print("%s wrote the book: %s." % (self.philosopher, self.book))


whodunnit = MyFirstClass("Sun Tzu", "The Art of War")
whodunnit.hand_list()
