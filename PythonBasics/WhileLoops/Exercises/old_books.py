book = input()
count_books = 0

while True:
    curren_book = input()

    if curren_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count_books} books.")
        break
    if curren_book == book:
        print(f"You checked {count_books} books and found it.")
        break

    count_books += 1