import random
from sys import argv

class Character:
    def __init__(self, name="unnamed", bonus=0, roll=0):
        self.name = name
        self.bonus = bonus
        self.roll = roll
    
    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __lt__(self, other):
        if self.roll == other.roll:
            if self.bonus == other.bonus:
                print("roll-off between: " + str(self) + " and " + str(other))
                return random.randrange(0, 2) < 1
            else:
                return self.bonus < other.bonus
        else:
            return self.roll < other.roll

    def __repr__(self):
        return "[name:" + str(self.name) + ", bonus:" + str(self.bonus) + ", roll:" + str(self.roll) + "]"

def main():
    characters = []
    names, initiatives, num_rolls = handle_args(argv)
    num_names = len(names)
    num_inits = len(initiatives)
    for i in range(max(num_names, num_inits)):
        name = names[i] if i < num_names else "unnamed"
        bonus = initiatives[i] if i < num_inits else 0
        char = Character(name, bonus)
        characters.append(char)
    print("characters after arg parsing: " + str(characters))

    main_options = ["view/edit characters", "adjust/perform runs", "exit"]
    main_options_string = stringify_options(main_options)

    character_options = ["name", "bonus", "roll (does nothing)", "save/exit"]
    character_options_string = stringify_options(character_options)

    run_options = ["edit number of runs", "perform runs", "main menu"]
    run_options_string = stringify_options(run_options)

    is_done = False
    while not is_done:
        choice = get_choice(main_options_string)
        if choice == 0: # view/edit characters
            character_string = make_character_string(characters)
            print(character_string)
            print("[" + str(len(characters)) + "+]: new character")
            response = input("choose a character (number) to edit or -1 to return to main menu.\n")
            num = -1
            try:
                num = int(response.strip())
            except:
                print("view/edit characters: error parsing " + str(response) + " as int.")
            if num >= 0:
                character_done = False
                if num >= len(characters):
                    num = len(characters)
                    newedit = "new"
                    print(str(newedit) + " character")
                    current_char = Character()
                else:
                    newedit = "edit"
                    current_char = characters[num]
                while not character_done:
                    print(current_char)
                    char_choice = get_choice(character_options_string)
                    if char_choice == 0: # name
                        print(str(newedit) + " character: current name: " + str(current_char.name))
                        new_name = input("enter a new name, or nothing to cancel\n").strip()
                        if (len(new_name) > 0):
                            current_char.name = new_name
                            print(str(newedit) + " character name: name has been set to " + str(current_char.name))
                        else:
                            print(str(newedit) + " character name: cancelling. returning to character menu")
                    elif char_choice == 1: # bonus
                        print(str(newedit) + " character: current bonus: " + str(current_char.bonus))
                        new_bonus = input("enter a new bonus, or not a number to cancel\n")
                        try:
                            new_bonus = int(new_bonus.strip())
                            current_char.bonus = new_bonus
                            print(str(newedit) + " character bonus: bonus has been set to " + str(current_char.bonus))
                            if new_bonus < -5 or new_bonus > 15:
                                print(str(newedit) + " character bonus: bonus is set outside of normal expected bounds [-5, 15]")
                        except:
                            print(str(newedit) + " character bonus: non-integer entered. returning to character menu")
                    elif char_choice == 2: # roll
                        print(str(newedit) + " character: current roll: " + str(current_char.roll))
                        print("this field changing should not affect anything.")
                        new_roll = input("enter a new roll, or not a number to cancel\n")
                        try:
                            new_roll = int(new_roll.strip())
                            current_char.roll = new_roll
                            print(str(newedit) + " character roll: roll has been set to " + str(current_char.roll))
                        except:
                            print(str(newedit) + " character roll: non-integer entered. returning to character menu")
                    elif char_choice == 3: # save/exit
                        character_done = True
                        print(str(newedit) + " character: current character: " + str(current_char))
                        yn = input("save changes? Indicate N or n to exit without saving.")
                        if yn not in ("N", "n"):
                            if newedit == "new":
                                characters.append(current_char)
                            else:
                                characters[num] = current_char
                            print("save character: character is now set to: " + str(characters[num]))
                        else:
                            print("exit character: exiting without saving")
        elif choice == 1: # adjust/perform runs
            print("adjust/perform runs: number of runs: " + str(num_rolls))
            run_choice = get_choice(run_options_string)
            if run_choice == 0: # edit number of runs
                print("adjust runs: number of runs: " + str(num_rolls)) 
                response = input("Enter a new number of runs, or a negative number to cancel\n")
                try:
                    new_runs = int(response.strip())
                    if new_runs < 0:
                        print("adjust runs: negative number entered. cancelling...")
                    else:
                        num_rolls = new_runs
                        print("adjust runs: number of runs set to " + str(num_rolls))
                except:
                    print("adjust runs: error parsing " + str(response) + " as an int")
            elif run_choice == 1: # perform runs
                print("perform runs: number of runs: " + str(num_rolls))
                positions = {} # format: character -> (rolling, deck)
                for character in characters:
                    positions[character] = (0, 0)
                for _ in range(num_rolls):
                    # get rolling positions
                    for character in characters:
                        random_roll = random.randrange(1, 20) # simulate roll
                        character.roll = random_roll + character.bonus
                        print(str(character.name) + " got a " + str(character.roll) + "! (" + str(random_roll) + " + " + str(character.bonus) + ")")
                    roll_positions = sorted(characters)
                    print("roll positions: " + str(roll_positions))

                    # get deck positions
                    deck = []
                    for character in characters:
                        for _ in range(character.bonus + 6):
                            deck.append(character)
                    random.shuffle(deck)
                    # print(deck)

                    deck_positions = []
                    for card in deck:
                        if card not in deck_positions:
                            deck_positions.insert(0, card)
                        else:
                            deck.remove(card)
                    print("deck positions: " + str(deck_positions))
                    
                    # get position with each method
                    for character in characters:
                        rolling_position = int(positions[character][0])
                        deck_position = int(positions[character][1])
                        # search rolling positions
                        for i in range(len(roll_positions)):
                            if roll_positions[i] == character:
                                rolling_position = rolling_position + i
                        
                        # search deck positions
                        for i in range(len(deck_positions)):
                            if deck_positions[i] == character:
                                deck_position = deck_position + i
                        
                        positions[character] = (rolling_position, deck_position)
                
                # all rolls are made, take average
                for character in characters:
                    raw_rolling = int(positions[character][0])
                    raw_deck = int(positions[character][1])
                    positions[character] = (raw_rolling/float(num_rolls), raw_deck/float(num_rolls))
                print(positions)
                outfile = open('outfile.txt', 'w')
                for position in positions:
                    outfile.write(str(position))
                    outfile.write(": ")
                    outfile.write(str(positions[position]))
                    outfile.write("\n")
                outfile.close()
        elif choice == 2: # exit
            yn = input("Are you sure? Indicate N or n to not exit.")
            if yn not in ("N", "n"):
                is_done = True

def make_character_string(characters):
    out_string = "Characters:\n"
    for i in range(len(characters)):
        character = characters[i]
        if isinstance(character, Character):
            out_string = str(out_string) + "[" + str(i) + "]: " + str(character) + "\n"
        else:
            print("make_character_string: non-Character in characters: " + character)
    out_string = out_string[:-1]
    return out_string

def get_choice(options):
    print(options)
    try:
        response = input("choose an option from above:\n")
        num = int(response.strip())
    except:
        print("input: error parsing " + str(response) + " as an int. try again")
        num = get_choice(options)
    return num
    
def stringify_options(options):
    options_string = ""
    for i in range(len(options)):
        options_string = options_string + "[" + str(i) + "]: " + str(options[i]) + "\n"
    options_string = options_string[:-1]
    return options_string
     
def handle_args(argv):
    c_index = argv.index("-c") if "-c" in argv else -1
    i_index = argv.index("-i") if "-i" in argv else -1
    r_index = argv.index("-r") if "-r" in argv else -1
    f_index = argv.index("-f") if "-f" in argv else -1

    names = []
    initiatives = []
    num_rolls = 1
    if c_index > 0:
        arg_names = argv[c_index + 1].split(",")
        for name in arg_names:
            names.append(name.strip())
    if i_index > 0:
        arg_inits = argv[i_index + 1].split(",")
        for init in arg_inits:
            try:
                initiatives.append(int(init.strip()))
            except:
                print("initiatives: error parsing " + init + " as int.")
    if r_index > 0:
        arg_runs = argv[r_index + 1]
        try:
            num_rolls = int(arg_runs)
        except:
            print("num_runs: error parsing " + arg_runs + " as int.")
    if f_index > 0:
        readfilelines = []
        filename = argv[f_index + 1]
        try:
            readfilelines = open(filename, 'r').readlines()
        except:
            print("file: unable to open file and parse lines: " + filename)
        try:
            num_rolls = int(readfilelines[0].strip())
            readfilelines = readfilelines[1:]
        except:
            message = "error parsing " + readfilelines[0] + " as int." if len(readfilelines) > 1 else "readfilelines is empty or has no characters."
            print("file: " + message)
        for line in readfilelines:
            splitline = line.split(",")
            if len(splitline) == 2:
                names.append(splitline[0].strip())
                try:
                    initiatives.append(int(splitline[1].strip()))
                except:
                    print("file: error parsing " + splitline[1] + " as int.")
            else:
                print("file: tuple is not two parts for line:" + line)
    return names, initiatives, num_rolls

main()
