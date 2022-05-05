# Copyleft 2022 Forrest Sheng Bao
# This is a simple Python function to beautifully print parsing trees from Stanza NLP toolbox. 
# Many NLP toolboxes will output parsing results in S-expressing like below: 
#
#       (ROOT (S (NP (DT This)) (VP (VBZ is) (NP (DT a) (NN test)))))
#
# It is not readable. SpaCy has a visualizer but Stanza does not. So I cranked this myself. 
# This script will convert it into something much more readable like this: 
# 0_(ROOT 
# 1 |_(S 
# 2 | |_(NP 
# 3 | | |_(DT This)) 
# 2 | |_(VP 
# 3 | | |_(VBZ is) 
# 3 | | |_(NP 
# 4 | | | |_(DT a) 
# 4 | | | |_(NN test))) 
# 2 | |_(. .)))


def stanza_parsing_tree_viz(bracket_string:str):
    indent_level = 0
    prompt = ""
    for c in bracket_string:
        if c == "(":
            print (f'\n{indent_level}{prompt}_{c}', end="")
            prompt += " |"
            indent_level += 1
        elif c == ")":
            print (c, end="")
            indent_level -= 1
            prompt = prompt[:-2]
        else: 
            print (c, end="")
            
    
