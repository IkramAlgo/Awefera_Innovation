# Function to reverse a string
def reverse_string(text):
    return text[::-1]  # Reverse using slicing

# Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0  
    for char in text:  
        if char in vowels:  
            count += 1  
    return count  

# Main function
def main():
    user_input = input("Enter a string: ").strip()  # Get input and remove spaces (Strip)

    if not user_input:  # Check if input is empty
        print("Error: Please enter a valid string.")
        return  

    reversed_text = reverse_string(user_input)  
    vowel_count = count_vowels(user_input)  

    print(f"Reversed string: {reversed_text}")  
    print(f"Number of vowels: {vowel_count}")  

# Run the program
if __name__ == "__main__":
    main()
