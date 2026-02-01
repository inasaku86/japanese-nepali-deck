import csv

# Read the original CSV
with open('n5-vocab.csv', 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Create new CSV with merged columns
with open('n5-vocab-anki.csv', 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)

    for row in rows:
        if len(row) >= 4:
            # Combine columns 1 & 2 for front (Japanese + English)
            front = f"{row[0]}<br>{row[1]}"

            # Combine columns 3 & 4 for back (Nepali + pronunciation)
            back = f"{row[2]}<br>{row[3]}"

            writer.writerow([front, back])

print("Conversion complete! Created n5-vocab-anki.csv")
