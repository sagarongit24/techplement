import argparse
import json
import os

# Function to load favorite cities from a JSON file
def load_favorite_cities(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save favorite cities to a JSON file
def save_favorite_cities(favorite_cities, file_path):
    with open(file_path, 'w') as file:
        json.dump(favorite_cities, file)

# Function to add a city to favorites
def add_to_favorites(city, file_path):
    favorite_cities = load_favorite_cities(file_path)
    if city not in favorite_cities:
        favorite_cities.append(city)
        save_favorite_cities(favorite_cities, file_path)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in favorites.")

# Function to remove a city from favorites
def remove_from_favorites(city, file_path):
    favorite_cities = load_favorite_cities(file_path)
    if city in favorite_cities:
        favorite_cities.remove(city)
        save_favorite_cities(favorite_cities, file_path)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} is not in favorites.")

# Function to list all favorite cities
def list_favorite_cities(file_path):
    favorite_cities = load_favorite_cities(file_path)
    if favorite_cities:
        print("Favorite Cities:")
        for city in favorite_cities:
            print(city)
    else:
        print("No favorite cities.")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Favorites Management Application")
    parser.add_argument("-a", "--add", help="Add city to favorites")
    parser.add_argument("-r", "--remove", help="Remove city from favorites")
    parser.add_argument("-l", "--list", action="store_true", help="List all favorite cities")
    parser.add_argument("-f", "--file", default="favorite_cities.json", help="Path to favorite cities file")
    args = parser.parse_args()

    if args.add:
        add_to_favorites(args.add, args.file)
    elif args.remove:
        remove_from_favorites(args.remove, args.file)
    elif args.list:
        list_favorite_cities(args.file)
    else:
        print("Please provide a valid command.")

if __name__ == "__main__":
    main()
