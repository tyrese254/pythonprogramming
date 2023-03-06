class book:
    def text(self):
        print("The Jolly rodger")

    def sub_heading(self):
        print("The Foustin lake")


class Description(book):
    def author(self):
        print("AUTHOR : John Whistler")

class story_line(Description):
    def line(self):
        print("Story Line : Is about a young man called Tompson who found love in terrible war and stuggle to have the love of his life")

class setting(story_line):
    def place(self):
        print("Story Setting : The story is set in Califonia in the 80's")

s = setting()
s.author()
s.sub_heading()
s.line()
s.place()
s.text()

