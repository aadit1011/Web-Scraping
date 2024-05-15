from bs4 import BeautifulSoup

# Open and read the HTML file
with open('D:\\Python\\Beautiful_Soup\\index3.html', 'r', encoding='utf-8') as file:
    content = file.read()  # Read the file's content into a variable

# Parse the HTML content using BeautifulSoup with the lxml parser
soup = BeautifulSoup(content, 'lxml')

# Find all the div elements with the class 'player'
player_details = soup.find_all('div', class_='player')

# Loop through each player detail div element
for player in player_details:
    # Extract the player's name
    # The player's name is within the h2 tag and further within the span tag
    player_name = player.find('h2').span.text.strip()  # .strip() removes leading/trailing whitespace

    # Extract the player's salary
    # The player's salary is within the last p tag in the div
    salary_paragraphs = player.find_all('p')  # Find all p tags within the current player div
    player_salary = salary_paragraphs[-1].span.text.strip()  # Access the last p tag's span text

    # Print the extracted information
    print('Player Name =', player_name)
    print('Player Salary =', player_salary)

    # For additional details, you could also extract club and country in a similar way
    # Extract the player's club
    player_club = salary_paragraphs[0].span.text.strip()  # Assuming club is in the first p tag

    # Extract the player's country
    player_country = salary_paragraphs[1].span.text.strip()  # Assuming country is in the second p tag

    # Print the additional information
    print('Player Club =', player_club)
    print('Player Country =', player_country)
    print('-' * 40)  # Separator for readability
