import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

## IMPORT DATA

bigFive = ['extraversion', 'agreeableness', 'conscientiousness', 'neuroticism', 'openness']

# Create an empty dataframe to store the correlation coefficients

#Function taking the judge number 01-11 to return their table of scores
def printJudge(judgeNo):
   # [640rows x 6 columns]
    # Columns: Clip_ID (0), Extraversion (1), Agreeableness (2), Conscientiousness (3), Neuroticism (4), Openness (5)
   return pd.read_csv(f'src/data/Personality_Scores/Score_0{judgeNo}.csv', delimiter=',')

# [640rows x 4 columns]
#  Columns: Clip_ID (0), Speaker_ID (1), Gender (2), Status (3)
metadata = pd.read_csv('src/data/metadata.csv')

# Data per Judge
judge1= np.array(printJudge('01'))
judge2= np.array(printJudge('02'))
judge3= np.array(printJudge('03'))
judge4= np.array(printJudge('04'))
judge5= np.array(printJudge('05'))
judge6= np.array(printJudge('06'))
judge7= np.array(printJudge('07'))
judge8= np.array(printJudge('08'))
judge9= np.array(printJudge('09'))
judge10= np.array(printJudge('10'))
judge11= np.array(printJudge('11'))

# print(np.array(metadata)[5,2])

# Connect Data  parameters --> F or M , judge1 etc.
def splitPerGender(gender, judgeNo):
    judgeData = judgeNo
    listOfGender = np.where(np.array(metadata)[:,2] == gender)[0]
    judgeGenderData = judgeData[listOfGender]
    return (judgeGenderData)

print(splitPerGender('F',judge1))

#CORRELATION
#Pearson Correlation coefficients
# np.corrcoef() - Returns the correlation matrix 
'''
array x vs array y
    x   y 
x   1   Pearson correlation coefficient(PCC)
y   PCC    1
'''


# correlation of two judges rating for a specific attibute
numpyPearson = np.corrcoef(judge1[:,2].tolist(), judge2[:,2].tolist())
# print(type(x))

#Show the correlation coefficient between each trait between two judges
def corrPerTrait(judgeA, judgeB):
    listOfCoefficients = []
    i=1
    while i <6:
        listOfCoefficients.append(np.corrcoef(judgeA[:,i].tolist(), judgeB[:,i].tolist())[0:1][0][1])
        i = i + 1
    return (listOfCoefficients)

   
# For a specific trait (parameter -> 1-6) creates a list of all correlations between all 55 unique combinations of judges to 2 decimal places
def corrAllJudgesOneTrait(trait):
    listOfCoefficients = []
    listOfPairs = []
    for i in range(11):
        if (i<9):
            x = '0' + str(i+1)
        else:
            x = str(i+1)
        judgeA = np.array(printJudge(x))
        for j in range(i+1,11):
            if (j<9):
                y = '0' + str(j+1)
            else:
                y = str(j+1)
            judgeB = np.array(printJudge(y))
            # listOfPairs.append((i+1,j+1))
            listOfCoefficients.append(np.corrcoef(judgeA[:,trait].tolist(), judgeB[:,trait].tolist())[0:1][0][1])
    # print(listOfPairs)
    return (np.round(listOfCoefficients,2))

# print(corrAllJudgesOneTrait(1))


'''
##SciPy Correlation Coefficients
# return two values --> correlation coefficient & p-value

print(scipy.stats.pearsonr(judge1[:,2].tolist(), judge1[:,3].tolist())) #Pearson's r
print(scipy.stats.spearmanr(judge1[:,2].tolist(), judge1[:,3].tolist())) #Spearman's rho
print(scipy.stats.kendalltau(judge1[:,2].tolist(), judge1[:,3].tolist())) # Kendall's tau
'''

# GRAPH
'''
# plt.imshow(numpyPearson, cmap='viridis', interpolation='nearest')
# plt.scatter(judge1[:,2].tolist(), judge1[:,3].tolist())
# plt.xlabel('X-axis label')
# plt.ylabel('Y-axis label')
# plt.xticks(range(numpyPearson.shape[0]))
# plt.yticks(range(numpyPearson.shape[0]))
# plt.show()

# plt.figure()
# plt.scatter(judge1[:,1].tolist(), judge1[:,3].tolist(), label='1')

# frequency of scores for Extraversion of judge 1
# plt.hist(judge1[:,1].tolist(), bins=30, color='blue', label='1')


# plt.figure()
# plt.scatter(x[:,2].tolist(), x[:,3].tolist(), label='2')
# plt.hist(judge1[:,2].tolist(), bins=30, color='red', label='2')
# plt.scatter(x[:,3].tolist(), bins=30, color='blue')
# plt.show()
'''

#HISTOGRAMS OF Frequency against Correlation Coefficient between judges for a specific trait
'''
fig, axs = plt.subplots(3, 2, figsize=(8, 8))
axs = axs.flatten()
for i in range(1,6):
    axs[i-1].hist(corrAllJudgesOneTrait(i), bins=90, range=(-0.25,0.5), color='blue', edgecolor='black', rwidth=0.8, label=f'All correlations between judges {bigFive[i-1]}')
    axs[i-1].set_title(f'Frequency against Correlation Coefficient between judges for {bigFive[i-1]}', fontsize=6)
    axs[i-1].set_xlabel('Correlation Coefficient between judges', fontsize=6)
    axs[i-1].set_ylabel('Frequency of a specific correlation', fontsize=6)
axs[5].axis('off')
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()
'''

def medianOfCorrelationsBetweenJudges(trait):
    return (np.median(corrAllJudgesOneTrait(trait)))

def meanOfCorrelationsBetweenJudges(trait):
    return (np.round(np.mean(corrAllJudgesOneTrait(trait)),2))


# plt.scatter([0,1,2,3,4,5,6,7,8,9,10,11], c=corrAllJudgesOneTrait(2), cmap='coolwarm', vmin=-1, vmax=1)
# plt.colorbar(label='Correlation Coefficient')

'''WRITE A FUNCTION THAT DOES THE PEARSON CORRELATION FOR EVERY 
COMBINATION OF JUDGES - 55 combinations
Write some kind of function comparing them and showing any 
significant correlations????'''
