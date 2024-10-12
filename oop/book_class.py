class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructure
    def __del__(self):
        print(f"Deleting {self.title}")

    #string Representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    #official Representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
