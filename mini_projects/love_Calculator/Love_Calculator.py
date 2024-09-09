def true_love_calculator(name1, name2):
    # Combine names and convert to lowercase
    combined_names = name1.lower() + name2.lower()

    # Calculate the love score based on the occurrence of letters in "true love"
    true_score = sum(combined_names.count(char) for char in "true")
    love_score = sum(combined_names.count(char) for char in "love")

    # Combine the scores to get the final love percentage
    love_percent = (true_score + love_score) * 5  # Arbitrary scaling factor for fun

    # Ensure the percentage is capped at 100
    love_percent = min(love_percent, 100)

    return love_percent

# Get names from the user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate and print the love percentage
love_percentage = true_love_calculator(name1, name2)
print(f"The true love percentage between {name1} and {name2} is: {love_percentage}%")
