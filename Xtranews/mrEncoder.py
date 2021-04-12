from bs4 import BeautifulSoup, NavigableString

def decodeIt(encodedtext):
    print("Original : " + encodedtext)
    space_in = encodedtext.replace("-" , " ")
    hyphen_in = space_in.replace("$hyphen$" , "-")
    double_quote_in = hyphen_in.replace("$22$" , "\"")
    single_quote_in = double_quote_in.replace("$27$" , "\'")
    question_mark_in = single_quote_in.replace("$3F$" , "?")
    hash_tag_in = question_mark_in.replace("$23$" , "#")

    decodedText = hash_tag_in
    print("Decoded : " + decodedText)
    return decodedText

def encodeTitle(title):
    single_quote_out = title.replace("\'" , '')
    double_quote_out = single_quote_out.replace("\"" , '')
    hash_tag_out = double_quote_out.replace("#" , '')
    question_mark_out = hash_tag_out.replace("?" , '')
    hyphen_in = question_mark_out.replace(" " , "-")
    comm_out = hyphen_in.replace("," , '')
    colon_out = comm_out.replace(":" , '')
    dot_out = colon_out.replace("." , '')
    fSlash_out = dot_out.replace("/" , '')
    rSlash_out = fSlash_out.replace("\\" , '')
    return rSlash_out

def replaceLinksFromFullDescription(soup , invalid_tags):
    for tag in invalid_tags: 
        for match in soup.findAll(tag):
            match.replaceWithChildren()
    return soup
