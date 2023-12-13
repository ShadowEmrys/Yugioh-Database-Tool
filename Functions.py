import csv
def csv_to_list(file_path):
    card_list = []  # Adds csv file to 2d list

    with open(file_path, newline='') as csvfile:
        # Reads each row in the csv file and appends it to the created list
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            card_set, card_name, card_type, card_attribute, monster_type, card_level, card_rank, card_link = row[1], row[4],row[6],row[7],row[8], row[9], row[18], row[19]
            card_list.append((card_set, card_name, card_type, card_attribute, monster_type, card_level,card_rank, card_link))  # Append a tuple (card_set, card_name)

    return card_list  # Returns a list of tuples


def cardtype_tolist(card_list,user_card_type):
    search_result = []
    for card in card_list:
        if card[2] == user_card_type:
            search_result.append(card)
    return search_result
            
def write_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            for row in data:
                file.write(','.join(map(str, row)) + '\n')
        return f"Data successfully written to {filename}"
    except Exception as e:
        return f"Error writing to file: {e}"