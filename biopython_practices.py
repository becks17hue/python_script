from Bio import SeqIO
for record in SeqIO.parse("sequences.fasta", "fasta"):
    print(record.id, record.seq)
for record in SeqIO.parse("reads.fastq", "fastq"):
    print(record.id, record.seq, record.letter_annotations["phred_quality"])