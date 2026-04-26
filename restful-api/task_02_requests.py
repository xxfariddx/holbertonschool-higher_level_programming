import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


# -----------------------------------------
# Function 1: Fetch and print post titles
# -----------------------------------------
def fetch_and_print_posts():
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


# -----------------------------------------
# Function 2: Fetch and save posts to CSV
# -----------------------------------------
def fetch_and_save_posts():
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        # Convert to list of dictionaries with required fields
        structured_data = []

        for post in posts:
            structured_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        # Write to CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_data)

        print("Data successfully saved to posts.csv")
    else:
        print("Failed to fetch posts.")


# -----------------------------------------
# Example usage
# -----------------------------------------
if __name__ == "__main__":
    print("Fetching and printing posts...\n")
    fetch_and_print_posts()

    print("\nFetching and saving posts to CSV...\n")
    fetch_and_save_posts()
