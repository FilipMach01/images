major_chords = {
    "C maj": ["C", "E", "G"],
    "G maj": ["G", "B", "D"],
    "D maj": ["D", "F#", "A"],
    "A maj": ["A", "C#", "E"],
    "E maj": ["E", "G#", "B"],
    "B maj": ["B", "D#", "F#"],
    "F maj": ["F", "A", "C"],
    "Bb maj": ["Bb", "D", "F"],
    "Eb maj": ["Eb", "G", "Bb"],
    "Ab maj": ["Ab", "C", "Eb"]
}

minor_chords = {
    "C min": ["C", "Eb", "G"],
    "G min": ["G", "Bb", "D"],
    "D min": ["D", "F", "A"],
    "A min": ["A", "C", "E"],
    "E min": ["E", "G", "B"],
    "B min": ["B", "D", "F#"],
    "F min": ["F", "Ab", "C"],
    "Bb min": ["Bb", "Db", "F"],
    "Eb min": ["Eb", "Gb", "Bb"],
    "Ab min": ["Ab", "B", "Eb"]
}

seventh_chords = {
    "C 7": ["C", "E", "G", "Bb"],
    "G 7": ["G", "B", "D", "F"],
    "D 7": ["D", "F#", "A", "C"],
    "A 7": ["A", "C#", "E", "G"],
    "E 7": ["E", "G#", "B", "D"],
    "B 7": ["B", "D#", "F#", "A"],
    "F 7": ["F", "A", "C", "Eb"],
    "Bb 7": ["Bb", "D", "F", "Ab"],
    "Eb 7": ["Eb", "G", "Bb", "Db"],
    "Ab 7": ["Ab", "C", "Eb", "Gb"]
}

diminished_chords = {
    "C dim": ["C", "Eb", "Gb"],
    "G dim": ["G", "Bb", "Db"],
    "D dim": ["D", "F", "Ab"],
    "A dim": ["A", "C", "Eb"],
    "E dim": ["E", "G", "Bb"],
    "B dim": ["B", "D", "F"],
    "F dim": ["F", "Ab", "B"],
    "Bb dim": ["Bb", "Db", "E"],
    "Eb dim": ["Eb", "Gb", "A"],
    "Ab dim": ["Ab", "B", "D"]
}

chord_types = {
    "major": major_chords,
    "minor": minor_chords,
    "seventh": seventh_chords,
    "diminished": diminished_chords
}
