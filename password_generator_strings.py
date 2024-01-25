import requests
import hashlib

def get_random_word(length):
    url = f"https://random-word-api.herokuapp.com/word?length={length}"
    response = requests.get(url)
    word = response.json()[0]
    return word

def generate_password(min_length):
    words = [get_random_word(min_length) for _ in range(5)]
    password = '-'.join(words)

    # Calculate the hash of the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    return password, hashed_password

if __name__ == "__main__":
    min_length = int(input("Enter the minimum length for random words: "))
    password, hashed_password = generate_password(min_length)
    
    print("Generated Password:", password)
    print("Hashed Password:", hashed_password)
