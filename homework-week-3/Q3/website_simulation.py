# Sample dictionary to represent the links on the website
# The keys are link names and the values are the corresponding URLs
website_links = {
    'Home': 'https://www.example.com',
    'About': 'https://www.example.com/about',
    'Services': 'https://www.example.com/services',
    'Contact': 'https://www.example.com/contact'
}

# Initialize history and current_url
history = []
current_url = website_links['Home']

while True:
    print("Options:")
    for link_name in website_links:
        print(f"{link_name}: {website_links[link_name]}")
    if history:
        print("Back: Go back to previous page")

    choice = input("Choose a link: ")

    if choice in website_links:
        history.append(current_url)
        current_url = website_links[choice]
        print(f"Current URL: {current_url}")
    elif choice == 'Back' and history:
        current_url = history.pop()
        print(f"Current URL: {current_url}")
    else:
        print("Invalid choice. Please choose a valid link or 'Back'.")