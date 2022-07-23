# Update-RPGMakerXP-PBS-files-with-translations
Update PBS files in any RPG Maker XP Pokemon Essentials game made in a different language with this translation tool and instruction guide

How to translate pbs text files

1. Manually translate the "Name" sections of the types.txt file. Leave InternalName unchanged
2. Manually translate the names of the locations  to the right of the # symbol. Should be around 40-50 names total.
        Half of the names are routes, so you can do a find-replace on those in your editor (like Ruta -> Route)  
3. Regular online translators work just fine for the following files:
    * metadata.txt
    * phone.txt
    * townmap.txt  
4. Use online translator for the following scripts below and rename the new files with a "-2" at the end. Next move those new text files and a copy of the original pbs scripts to the same folder as the script. Then run the script to move english translations from the "-2" files to the original files. 
    * The original scripts are updated as follows:
      * abilities.txt (script separates file text line by line and then separates each line's text by the ",")
            name (the one shown to the player)
            description
      * items.txt (script separates file text line by line and then separates each line's text by the ",")
            name for one item
            name for multiple items
            description
      * moves.txt (script separates file text line by line and then separates each line's text by the ",")
            name (the one shown to the player)
            description
      * pokemon.txt (script separates file text by "[")
        * Kind description
        * Pokedex description
      * trainertypes.txt (script separates file text line by line and then separates each line's text by the ",")
            trainer type desciptions (all titles a trainer can have vs the player)
        
        
IF you want to experiment, try testing with the PBS files supplied with Pokemon Essentials. I attached them to this project for easy access.
