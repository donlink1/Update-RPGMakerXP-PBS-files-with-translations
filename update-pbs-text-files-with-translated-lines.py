"""
This program takes some translated lines from the ..-2.txt files and imports them into their original text files. The conversion is as follows:
    1. abilities-2.txt -> abilities.txt
    2. items-2.txt -> items.txt
    3. moves-2.txt -> moves.txt
    4. pokemon-2.txt -> pokemon.txt
    5. trainertypes-2.txt -> trainertypes.txt

NOTE: Make sure all 10 files listed above exist in the same folder as this script before running.
NOTE: Run this program as Administrator in your terminal/ide to avoid authorization issues when accessing the files

Current Workarounds to bugs
    HACK: Double Quotes are removed from descriptions that do not have commas when running this script. 
    To keep the structure as close to the original design as possible to avoid unnecessary bugs, 
    the periods at the end of the descriptions are replaced with commas to keep them quoted.
    This hack can then be manually fixed by going into a text editor and replace evry 2nd occurence of ',"' with '."' 
    or use an editor like Visual Studio code to make a more custom search (like regex) for only getting those 2nd occurences.
    Here's a link explaining why this bug occurs when python's csv module works with quotes in text files:
        https://stackoverflow.com/questions/9353792/python-csv-module-quotes-go-missing 

@Author Lloyd Moore
"""

# Imports
import os
import csv
import logging

currentDirectory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def translateTextFileLineByLine(textFileName, sectionsToTranslate):
    with open(os.path.join(currentDirectory, str(textFileName) + '.txt'), 'r', encoding='mbcs') as originalFile:
        translatedFile = open(os.path.join(currentDirectory, str(textFileName) + '-2.txt'), encoding='mbcs')
        
        # Fetch the contents of the text file and its corresponding '-2' translated text file
        originalFileReader = csv.reader(originalFile)
        translatedFileReader = csv.reader(translatedFile)
        originalFileLines = list(originalFileReader)
        translatedFileLines = list(translatedFileReader)
        
        originalFile.seek(0)
        
        # Check every line in the original file
        for i in range(len(originalFileLines)):
            lastSectionInOriginalFileLine = len(originalFileLines[i]) - 1
            lastSectionInTranslatedFileLine = len(translatedFileLines[i]) - 1
            
            # Replace the original line's section with its correspondind translated file's section
            for section in sectionsToTranslate:
                # HACK: Double Quotes are removed from descriptions that do not have commas. 
                # To keep the structure as close to the original design as possible to avoid unnecessary bugs, 
                # the periods at the end of the descriptions are replaced with commas to keep them quoted.
                if section == 'last' or section == lastSectionInOriginalFileLine:
                    originalFileLines[i][lastSectionInOriginalFileLine] = str(translatedFileLines[i][lastSectionInTranslatedFileLine])[:-1] + ','
                elif textFileName == 'items' and section == sectionsToTranslate[len(sectionsToTranslate)-1]:
                    originalFileLines[i][section] = str(translatedFileLines[i][section])[:-1] + ','
                #elif textFileName == 'items' and 
                else:
                    originalFileLines[i][section] = translatedFileLines[i][section]
                    
        # Write the newly updated text back into the original file
        with open(os.path.join(currentDirectory, str(textFileName) + '.txt'), 'w', newline='', encoding='mbcs') as originalFileOutput:
            originalFileWriter = csv.writer(originalFileOutput)
            originalFileWriter.writerows(originalFileLines)
        
    translatedFile.close()


def translateTextFileByNumberedSelection(textFileName, keysToUpdate):
    with open(os.path.join(currentDirectory, str(textFileName) + '.txt'), 'r+', encoding='mbcs') as originalFile:
        translatedFile = open(os.path.join(currentDirectory, str(textFileName) + '-2.txt'), encoding='mbcs')
        
        # Fetch the contents of the text file and its corresponding '-2' translated text file
        originalFileLines = originalFile.readlines()
        translatedFileLines = translatedFile.readlines()
        
        # Check every line in the original file
        for i in range(len(originalFileLines)):
            originalFileLine = originalFileLines[i]
            translatedFileLine = translatedFileLines[i]
            
            # Replace every line in the original file with the translated file that contains the key we're looking for.
            if originalFileLine:
                for key in keysToUpdate:
                    if key in translatedFileLine:
                        originalFileLines[i] = translatedFileLines[i]
                        break
                
        
        # Write the translated lines back into the original file
        originalFile.seek(0)
        for line in originalFileLines:
            originalFile.write('%s' % line)
        originalFile.truncate()
        
        translatedFile.close()


def main():
    fileName = ''
    
    try:
        print('\n----------Beginning translation on pbs text files----------\n')
        
        fileName = 'abilities'
        print('\nStep 1 of 5: Translating abilities.txt with abilities-2.txt...')
        translateTextFileLineByLine(fileName, [2,3])
        print('\nabilities.txt successfully translated!\n')
        
        fileName = 'items'
        print('\nStep 2 of 5: Translating items.txt with items-2.txt...')
        translateTextFileLineByLine(fileName, [2,3,6])
        print('\nitems.txt successfully translated!\n')
        
        fileName = 'moves'
        print('\nStep 3 of 5: Translating moves.txt with moves-2.txt...')
        translateTextFileLineByLine(fileName, [2, 'last'])
        print('\nmoves.txt successfully translated!\n')
        
        fileName = 'pokemon'
        print('\nStep 4 of 5: Translating pokemon.txt with pokemon-2.txt...')
        translateTextFileByNumberedSelection(fileName, ['Kind', 'Pokedex'])
        print('\npokemon.txt successfully translated!\n')
        
        fileName = 'trainertypes'
        print('\nStep 5 of 5: Translating trainertypes.txt with trainertypes-2.txt...')
        translateTextFileLineByLine(fileName, [2,4,5])
        print('\ntrainertypes.txt successfully translated!\n')
        
        print('\nFinished translating all text files!!!')
    
    except Exception:
        print('\n')
        logging.exception(' Failed to translate ' + str(fileName) + '.txt')
        
    print('\nProgram Closing...')
    print('\n------------------------------------------------------------\n')

if __name__ == "__main__":  
    main()