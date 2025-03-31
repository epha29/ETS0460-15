bible_verses={
    "faith": "hebrews 11:1 - faith is confidence in what we hope for.",  
    "provision": "matthew 6:26 - God feeds the birds , and He will provides for you "
}
 
# The get method is used to retrieve a value for a given key. If the key is not found, it returns the default value provided.
missing_verse=bible_verses.get( "forgiveness", "colossians 3:13- forgive as the lord forgave you") 
verse= bible_verses.get("faith") # Retrieves the verse associated with the key "faith"
print(missing_verse)
print (verse)