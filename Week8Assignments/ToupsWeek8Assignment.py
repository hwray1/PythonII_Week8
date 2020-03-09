#############################
#    Author: Ben Toups
#      3/9/2020
#############################

# Accepts an input DNA template sequence from the user
## using raw_input because....python 2.6
dna = raw_input("Enter in a DNA template sequence: ")

# Function to generate the compliment sequence of a DNA sequence
def Compl(seq):
	# First, reverses the input sequence
	revSeq = ''
	for i in range (1,len(seq)+1):
		revSeq += seq[-i]

	# Next, goes through each base in the sequence and creates a new sequence containing 
	## their compliments
	compliment = ''
	for i in range(0,len(revSeq)):
		if revSeq[i] == 'A':
			compliment += 'T'
		elif revSeq[i] == 'C':
			compliment += 'G'
		elif revSeq[i] == 'G':
			compliment += 'C'
		elif revSeq[i] == 'T':
			compliment += 'A'
		else:
			print('Invalid base entry')
			break
	
	# Finally, returns the final compliment sequence
	return compliment

# Print call on the function using the user's input sequence
print(Compl(dna))
