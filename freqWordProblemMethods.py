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


#Read the data from file based on the user choise:
def readData(f):
    #Choose a dataset:
    if f == 1 or f == "1":
        filename = "dataset_1.txt"
    elif f == 2 or f == "2":
        filename = "dataset_2.txt"
    else:
        print("This dataset does not exist! ")

    #Read the file of the choosen dataset:
    try:
        dataSet = open(filename, 'r')
        #Save file content into a list[]:
        data = dataSet.read().splitlines()
    except:
        print("Something went worng! Please try again..\n")
    finally:
        dataSet.close()
    return data


def frequentWords(txt, k):
    freqPtterns = []
    #Create map of k-mer, count & find the maximum repeaed value:
    freqMap = frequencyMap(txt, k)
    maxCount = maxValue(freqMap)
    #Create list of most frequent k-mers:
    for pattern, occurCount in freqMap.items():
        if occurCount == maxCount:
            freqPtterns.append(pattern)
    return freqPtterns


def frequencyMap(txt, k):
    freqMap = {}
    n = len(txt)
    #Craete a map from the k-mer substrings:
    for i in range (n-k+1):
        pattern = txt[i:i+k]
        #Count occurance of each k-mer:
        if freqMap.get(pattern, 0) == 0:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] +=1
    return freqMap


def maxValue(map):
    #Find the maximum repetition value among all k-mers:
    PatternKey = max(map, key=map.get)
    return map[PatternKey]

