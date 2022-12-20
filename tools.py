import pandas as pd
import re

def addPauseTag(nlp_result):
    '''
        This function aims to add pause tag to a text following some rules (to be defined)
    '''
    # iterate through result
    df = pd.DataFrame(nlp_result)
    pause_tag = []
    for index, rows in df.iterrows():

        # if we have a punct
        if (rows['entity_group'] == "PONCT"):
            # print(rows['entity_group'])
            pause_tag.append('OBL')
        #print("pause obligatoire")
        #df['pause_tag'] = "OBL"
        elif (rows['entity_group'] == "DET" or rows['entity_group'] == "ADJ"):
            # print(rows['entity_group'])
            pause_tag.append('INT')
        elif (rows['entity_group'] == "NC" or rows['entity_group'] == "NPP") or (rows['entity_group'] == "P" or re.match("V",rows['entity_group']) != None):
            # print("others")
            pause_tag.append('FAC')
        else:
            pause_tag.append('INS')
      
    df['pause_tag'] = pause_tag
    
    return df