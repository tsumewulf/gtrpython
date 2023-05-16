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
    for name, notes in tunings.items():
        normalized_name = name.lower().replace(' ', '')
        if normalized_tuning_name == normalized_name:
            return name, notes
    return None, None

while True:
    tuning_name = input("Enter the name of the tuning (or 'exit' to quit): ")
    if tuning_name.lower() == "exit":
        print("Thank you for using my Python tuner!")
        break

    found_tuning_name, tuning_notes = get_string_tuning(tuning_name)

    if found_tuning_name and tuning_notes:
        print(f"The string tuning for {found_tuning_name} is:")
        print(", ".join([note.upper() for note in tuning_notes]))
    elif found_tuning_name:
        print(f"Did you mean {found_tuning_name}?")
    else:
        print("Tuning not found.")
