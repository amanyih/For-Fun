def dna(sequence):
    sequence = sequence.replace("A","t")
    sequence = sequence.replace("T","a")
    sequence = sequence.replace("G","c")
    sequence = sequence.replace("C","g")
    sequence = sequence.upper()
    return sequence

print(dna("ATTAGCCGG"))

