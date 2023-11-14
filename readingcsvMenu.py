import csv

FILENAME = "gameTitles.csv"
game_list = [""]


def get_value():
    """
    This function reads the file.
    """
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader: 
                game_list.append(row)
        return game_list[0]
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")

def set_value(value):
    
    with open(FILENAME, "r") as inf, open(FILENAME, "w") as outf:
        reader = csv.writer(inf)
        writer = csv.writer(outf)
        for line in reader:
            writer.writerow(line[0], value)


    




    