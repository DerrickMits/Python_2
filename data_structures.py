# Task 1: List of integers and their sum
# Accepting user input to create a list of integers and calculating the sum

# Prompt user to enter integers separated by spaces
int_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
# Calculate the sum of the integers
total_sum = sum(int_list)
# Display the result
print(f"The sum of the integers in the list is: {total_sum}")

# Task 2: Tuple of favorite books
# Creating a tuple of favorite books and printing each book on a new line

# Tuple with 5 favorite book names
favorite_books = ("1984", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice", "Moby Dick")
print("\nMy favorite books are:")
for book in favorite_books:
    print(book)

# Task 3: Dictionary to store person information
# Using a dictionary to store user-provided information and displaying it

# Dictionary to store information
person_info = {}
# Asking user for input
person_info['name'] = input("\nEnter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")
# Displaying the dictionary
print("\nPerson Information:")
print(person_info)

# Task 4: Sets of integers and common elements
# Accepting user input to create two sets and finding common elements

# Prompt user to enter integers for the first set
set1 = set(map(int, input("\nEnter integers for the first set, separated by spaces: ").split()))
# Prompt user to enter integers for the second set
set2 = set(map(int, input("Enter integers for the second set, separated by spaces: ").split()))
# Finding the intersection (common elements)
common_elements = set1 & set2
# Displaying the result
print(f"The common elements in both sets are: {common_elements}")

# Task 5: List comprehension for words with an odd number of characters
# Creating a list of words and using list comprehension to filter based on character count

# List of words
words_list = ["hello", "world", "python", "is", "awesome", "code"]
# List comprehension to find words with an odd number of characters
odd_char_words = [word for word in words_list if len(word) % 2 != 0]
# Displaying the result
print(f"\nWords with an odd number of characters: {odd_char_words}")
