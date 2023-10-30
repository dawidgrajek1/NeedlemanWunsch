from Bio import SeqIO

MATCH = 1
MISMATCH = -1
GAP = -1

fasta_sequences = SeqIO.parse(open("seq.fasta"), "fasta")
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)
    print(name)
    print(sequence)
    print("")
