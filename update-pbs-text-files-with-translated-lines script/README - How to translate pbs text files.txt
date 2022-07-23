How to translate pbs text files

    Manually translate the "Name" sections of the types.txt file. Leave InternalName unchanged
    Manually translate the names of the locations  to the right of the # symbol. Should be around 40-50 names total.
        Half of the names are routes, so you can do a find-replace on those in your editor (like Ruta -> Route)

    Regular online translators work just fine for the following files:
        metadata.txt
        phone.txt
        townmap.txt

    Use online translator for the following scripts below and rename the new files with a "-2" at the end. 
    Next move those new text files and a copy of the original pbs scripts to the "update-pbs-text-files-with-translated-lines script" folder. 
    Then run the script in that folder to move english translations from the "-2" files to the original files. 
    The original scripts are updated as follows:
        abilities.txt (script separates file text line by line and then separates each line's text by the ",")
            name (the one shown to the player)
            description
        items.txt (script separates file text line by line and then separates each line's text by the ",")
            name for one item
            name for multiple items
            description
        moves.txt (script separates file text line by line and then separates each line's text by the ",")
            name (the one shown to the player)
            description
        pokemon.txt (script separates file text by "[")
            Kind description
            Pokedex description
        trainertypes.txt (script separates file text line by line and then separates each line's text by the ",")
            trainer type desciptions (all titles a trainer can have vs the player)
        
        
