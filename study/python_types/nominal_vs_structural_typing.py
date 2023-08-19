class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title  = title
        self.pages  = pages
        
    def __len__(self) -> int:
        return self.pages
    
my_str = "Hello"
print(len(my_str))
my_list = [1,2,3,4,5]
print(len(my_list))

my_dict = {"a": 1, "b": 2}
len(my_dict)