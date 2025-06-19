def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    ''' (str) -> bool
    Return True if the DNA sequence is valid (is a combination of "A", "T", "C" and "G")
    A string is not a valid DNA sequence if it contains lowercase letters.

    >>> is_valid_sequence("ATCGGC")
    True
    >>> is_valid_sequence("ATKVC")
    False

    '''
    valid_n = ["A", "T", "C", "G"]
    for char in dna:
        if char not in valid_n:
            return False
    else:
        return True

def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at
    the given index.

    >>> insert_sequence("ATGCA", "GGT", 1)
    'AGGTTGCA'
    >>> insert_sequence("ATCGGC", "AAC", 0)
    'AACATCGGC'
    >>> insert_sequence("ATCGGC", "AAC", -1)
    'ATCGGAACC'

    '''
    dna_combo = dna1[:index] + dna2 + dna1[index:]
    return dna_combo

def get_complement(nucleotide):
    '''(str) -> str
    Return the nucleotide's complement.

    >>> get_complement("A")
    'T'
    >>> get_complement("T")
    'A'
    >>> get_complement("G")
    'C'
    >>> get_complement("C")
    'G'
    '''
    complement = ""
    if nucleotide == "A":
        complement = complement + "T"
    elif nucleotide == "T":
        complement = complement + "A"
    elif nucleotide == "G":
        complement = complement + "C"
    elif nucleotide == "C":
        complement = complement + "G"
    return complement

def get_complementary_sequence(dna):
    '''(str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence("ATCGGC")
    'TAGCCG'
    >>> get_complementary_sequence("TAGCCG")
    'ATCGGC'
    >>> get_complementary_sequence("AGGTTGCA")
    'TCCAACGT'
    >>> get_complementary_sequence("TCCAACGT")
    'AGGTTGCA'
    '''
    complementary = ""
    for letter in dna:
        if letter == "A":
            complementary = complementary + "T"
        elif letter == "T":
            complementary = complementary + "A"
        elif letter == "G":
            complementary = complementary + "C"
        elif letter == "C":
            complementary = complementary + "G"
    return complementary