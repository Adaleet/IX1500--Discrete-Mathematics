import genanki

# Create Anki deck for graph theory concepts
deck_name = "Graph Theory Concepts"
deck_id = 2147000001
graph_deck = genanki.Deck(deck_id, deck_name)

# Define the model for the flashcards
model_id = 2147000002
graph_model = genanki.Model(
    model_id,
    "Graph Model",
    fields=[
        {"name": "Concept"},
        {"name": "Definition"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Concept}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Definition}}",
        },
    ],
)

# List of concepts and their definitions
concepts = [
    ("Kromatiskt tal", 
     "Det kromatiska talet c(G) för en graf G är det minsta antalet färger som behövs för att färga hörnen så att inga angränsande hörn har samma färg. "
     "Till exempel har en komplett graf Kn det kromatiska talet c(Kn) = n. För en planär graf gäller att c(G) ≤ 4, enligt Appel och Hakens bevis från 1976."),
    ("Kromatiskt polynom", 
     "Det kromatiska polynomet P(G, λ) anger antalet sätt att färga grafen G med högst λ färger. "
     "Det beräknas med hjälp av relationer som involverar grafens struktur och antalet färgalternativ."),
    ("Kontraktion", 
     "En kontraktion av en graf innebär att två hörn som är förbundna med en kant slås samman, vilket ger en ny graf där denna kant inte längre finns. "
     "Notation G - e används för grafen efter att en kant e tagits bort, medan Ge används för grafen där hörnen incidenta med e har fusionerats. "
     "Sambandet för det kromatiska polynomet ges av: P(G, λ) = P(G - e, λ) - P(Ge, λ)."),
    ("Planära grafer", 
     "En planär graf är en graf som kan ritas i ett plan utan att några kanter korsar varandra. "
     "Exempelvis är K4 en planär graf, medan K5 inte är det."),
    ("Bipartita grafer", 
     "En bipartit graf är en graf där mängden hörn kan delas upp i två disjunkta delmängder, V1 och V2, så att varje kant i grafen förbinder ett hörn i V1 med ett hörn i V2. "
     "Den kompletta bipartita grafen med |V1| = m och |V2| = n betecknas Km,n."),
    ("Homeomorfa grafer", 
     "Två grafer är homeomorfa om de kan härledas från samma ursprungsgraf genom en sekvens av expansioner. "
     "En graf är planär om och endast om den inte innehåller en delgraf som är homeomorf med K5 eller K3,3 (enligt Kuratowskis sats)."),
    ("Eulers polyederformel", 
     "För en sammanhängande planär graf gäller formeln v + r - e = 2, där v är antalet hörn, e är antalet kanter, och r är antalet delytor som grafen delar planet i."),
    ("Eulergrafer", 
     "En Eulercykel är en cykel som passerar varje kant i en graf precis en gång och återvänder till utgångspunkten. "
     "En Eulergraf är en graf som innehåller en Eulercykel. För att en graf ska vara en Eulergraf måste alla hörn ha jämn grad och grafen vara sammanhängande. "
     "En Eulerväg är en väg som passerar varje kant precis en gång, men den behöver inte återvända till startpunkten. "
     "En graf har en Eulerväg om högst två hörn har udda grad och grafen är sammanhängande."),
    ("Hamiltongrafer", 
     "En Hamiltoncykel är en cykel som passerar varje hörn i grafen precis en gång och återvänder till utgångspunkten. "
     "En Hamiltongraf är en graf som innehåller en Hamiltoncykel. En Hamiltonväg är en väg som passerar varje hörn i grafen precis en gång, men behöver inte vara en cykel. "
     "En graf med n ≥ 3 hörn som är öglefri och där summan av graderna för alla par av hörn som inte är grannar är minst n, är en Hamiltongraf.")
]

# Add cards to the deck
for concept, definition in concepts:
    note = genanki.Note(
        model=graph_model,
        fields=[concept, definition]
    )
    graph_deck.add_note(note)

# Save the deck to a file
deck_file = 'Graph_Theory_Concepts.apkg'
genanki.Package(graph_deck).write_to_file(deck_file)

print(f"Anki deck saved as {deck_file}")
