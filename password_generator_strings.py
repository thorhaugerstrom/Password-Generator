import random
import requests

def get_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    word = response.json()[0]
    return word

def generate_password():
    words = [get_random_word() for _ in range(5)]
    password = '-'.join(words)
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)