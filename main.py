tunings = {
        # Standard Tunings
        "E Standard": ["E", "A", "D", "G", "B", "E"],
        "Eb Standard": ["Eb", "Ab", "Db", "Gb", "Bb", "Eb"],
        "D Standard": ["D", "G", "C", "F", "A", "D"],
        "Db Standard": ["Db", "Gb", "C", "F#", "Ab", "Db"],
        "C Standard": ["C", "F", "A#", "D#", "G", "C"],
        "B Standard": ["B", "E", "A", "D", "F#", "B"],
        "Bb Standard": ["Bb", "Eb", "Ab", "Db", "Gb", "Bb"],
        "A Standard": ["A", "D", "G", "C", "E", "A"],
        "Ab Standard": ["Ab", "Db", "Gb", "C", "Eb", "Ab"],
        "G Standard": ["D", "G", "C", "F", "A", "D"],
        "F Standard": ["C", "F", "A#", "D#", "G", "C"],
        "Eb Standard": ["Eb", "Ab", "Db", "Gb", "Bb", "Eb"],
        "Db Standard": ["Db", "Gb", "C", "F#", "Ab", "Db"],
        "C# Standard": ["C#", "F#", "B", "E", "G#", "C#"],

        # Open Tunings
        "Open D": ["D", "A", "D", "F#", "A", "D"],
        "Open E": ["E", "B", "E", "G#", "B", "E"],
        "Open G": ["D", "G", "D", "G", "B", "D"],
        "Open A": ["E", "A", "E", "A", "C#", "E"],
        "Open C": ["C", "G", "C", "G", "C", "E"],
        "Open Db": ["Db", "Ab", "Db", "F", "Ab", "Db"],
        "Open C#": ["C#", "G#", "C#", "F#", "A#", "C#"],

        # Drop Tunings
        "Drop D": ["D", "A", "D", "G", "B", "E"],
        "Drop C": ["C", "G", "C", "F", "A", "D"],
        "Drop B": ["B", "F#", "B", "E", "G#", "C#"],
        "Drop A": ["A", "E", "A", "D", "F#", "B"],
        "Eb Drop Db": ["Eb", "Ab", "Db", "Gb", "Bb", "Eb"],
        "Db Drop Cb": ["Db", "Gb", "Cb", "Fb", "Ab", "Db"],
        "C Drop B": ["C", "F", "Bb", "Eb", "G", "C"],
        "B Drop Bb": ["B", "E", "A#", "D#", "F#", "B"],
        "C# Drop B": ["C#", "F#", "B", "E", "G#", "C#"],
    }

def get_string_tuning(tuning_name):
    normalized_tuning_name = tuning_name.lower().replace(' ', '')
    matching_tunings = []

    for name in tunings.keys():
        normalized_name = name.lower().replace(' ', '')
        if normalized_tuning_name in normalized_name:
            matching_tunings.append(name)

    return matching_tunings

while True:
    tuning_name = input("Enter the name of the tuning (or 'exit' to quit): ")
    if tuning_name.lower() == "exit":
        print("Thank you for using my Python tuner!")
        break

    matching_tunings = get_string_tuning(tuning_name)

    if matching_tunings:
        if len(matching_tunings) == 1:
            found_tuning_name = matching_tunings[0]
            tuning_notes = tunings[found_tuning_name]
            print(f"The string tuning for {found_tuning_name} is:")
            print(", ".join([note.upper() for note in tuning_notes]))
        else:
            print("Multiple matching tunings found. Please select one from the list:")
            for i, tuning in enumerate(matching_tunings, start=1):
                print(f"{i}. {tuning}")
            choice = input("Enter the number corresponding to your choice: ")
            try:
                choice = int(choice)
                if choice >= 1 and choice <= len(matching_tunings):
                    found_tuning_name = matching_tunings[choice - 1]
                    tuning_notes = tunings[found_tuning_name]
                    print(f"The string tuning for {found_tuning_name} is:")
                    print(", ".join([note.upper() for note in tuning_notes]))
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please enter a number.")
    else:
        print("Tuning not found.")
