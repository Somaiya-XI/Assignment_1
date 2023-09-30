#############################################################################################
## Description:   {This program is used to find the most frequent pattern occrance given a
##                 text sequenece and the k value, this solution's complexity is O(|text|*k)}
#############################################################################################
## Key Portions:  {First the data is read from the give files by using readData() method
##                 then frequentWords() method is used to create a list of the most frequent 
##                 k-mer inside frequentWords() there are 2 other methods one creates a map
##                 of substrings of length k frequencyMap(), and the other finds the maximum
##                 repetition value among all k-mers }
#############################################################################################
## Student Name:  {Somiyah Saad}
## Student ID:    {4111674}
## Student Email: {4111674@upm.edu.sa}
#############################################################################################
## NOTE: Refer to the README.md file for detailed execution instructions
#############################################################################################

from  freqWordProblemMethods import frequentWords, readData

def Main():
    #Read Dataset 1 & Save inputs as Text, K:
    Data = readData(1)
    Text = Data[0]
    Kmer = int(Data[1])
    #Run the frequent words problem with the choosen set:
    RepeatedPatterns = frequentWords(Text, Kmer)
    #Print the most frequent patterns:
    print("The maost frequent k-mers in dataset 1 are: ", RepeatedPatterns, "\n")

    #Read Dataset 2 & Save inputs as Text, K:
    Data = readData(2)
    Text = Data[0]
    Kmer = int(Data[1])
    #Run the frequent words problem with the choosen set:
    RepeatedPatterns = frequentWords(Text, Kmer)
    #Print the most frequent patterns:
    print("The maost frequent k-mers in dataset 2 are: ", RepeatedPatterns)

if __name__ == "__main__":
    Main()
