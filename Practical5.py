# pip install biopython
# Import pairwise2 module
from Bio import pairwise2

# Import format_alignment method
from Bio.pairwise2 import format_alignment


# Define two sequences to be aligned
X = "ACGGGT"
Y = "ACGT"

print("sequence 1: ", X)
print("sequence 2: ", Y)

alignments = pairwise2.align.globalxx(X, Y)

# Use format_alignment method to format the alignments in the list
for a in alignments:
    print(format_alignment(*a))