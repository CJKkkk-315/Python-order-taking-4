# -*- coding: utf-8 -*-
import urllib.request, urllib.error, urllib.parse
import json
import os
from pprint import pprint
import pathlib
import re
import pandas as pd
from copy import deepcopy
from pathlib import Path

## %% =========================== GLOB VALs ===================================
# Yes, I also hate global values, move them to MAIN if you like
_API_KEY = "1de0a270-29c5-4dda-b043-7c3580628cd5" # put your key here

# Semantic Group Meaning
dict_semntc_gp = {"ACTI":"Activities & Behaviors",
                    "ANAT":"Anatomy",
                    "CHEM":"Chemicals & Drug",
                    "CONC":"Concepts & Ideas",
                    "DEVI":"Devices",
                    "DISO":"Disorders",
                    "GENE":"Genes & Molecular Sequences",
                    "LIVB":"Living Beings",
                    "OBJC":"Objects",
                    "OCCU":"Occupations",
                    "ORGA":"Organizations",
                    "PHEN":"Phenomena",
                    "PHYS":"Physiology",
                    "PROC":"Procedures"}

dict_link2ont = {'http://purl.lirmm.fr/ontology/MSHFRE/':'MSHFRE',
                'http://purl.lirmm.fr/ontology/MDRFRE':'MDRFRE',
                'http://chu-rouen.fr/cismef/WHO-ART':'WHO-ARTFRE',
                'http://www.romedi.fr/romedi/':'ROMEDI',
                'http://id.who.int/icd/entity/':'CIM-11',
                'http://chu-rouen.fr/cismef/ATC#':'ATCFRE'}


# url_default='''http://services.bioportal.lirmm.fr/annotator/?text=Radiographie%20du%20genou%20droit%20de%20face%20et%20de%20profil%20au%20lit&ontologies=ROMEDI,WHO-ARTFRE,ATCFRE,CIM-11,MSHFRE,MDRFRE&longest_only=true&exclude_numbers=false&whole_word_only=true&exclude_synonyms=false&expand_mappings=false&fast_context=true&certainty=true&temporality=true&experiencer=true&negation=true&score_threshold=0&confidence_threshold=0&display_links=false&display_context=false&apikey=
# '''


params_ann = {'ontologies':'MSHFRE,MDRFRE,ATCFRE,WHO-ARTFRE,ROMEDI,CIM-11',
                'longest_only':'true',
                'exclude_numbers':'false',
                'whole_word_only':'true',
                'exclude_synonyms':'false',
                'expand_mappings':'false',
                'negation':'false',
                'experiencer':'false',
                'temporality':'false',
                'lemmatize':'false',
                'display_links':'false',
                'display_context':'false',
                "fast_context":"false",
                "certainty":"false",
                "score_threshold":0,
                "confidence_threshold":0,
                'apikey':_API_KEY
                }

# ============================== FUNCs ==============================
def get_req_url(text, api_type='annotator', params=None, lang='fr'):
    """This function aims at transform input textual content (and probably a dict with parameters) to the url request known by the API of SIFR web service"""
    # Seems like "%" and "\t" exist in the text will cause the algo not working, replace them with a space will hold the postions for all other words so that the "from" and "to" will be kept undisturbed
    text = re.sub(r'[%\t]',' ',text)  
    # For the annotator, the portal recommended by documentation "http://data.bioportal.lirmm.fr/" seems not meaningful for us, use another instead.
    # The safe here is only to make equal to original web service request 
    if api_type == 'annotator':
        _url = "http://services.bioportal.lirmm.fr/annotator/" if lang.lower()=="fr" else "https://data.bioontology.org/annotator"
        _url += f"?text=" + urllib.parse.quote(text, safe=':,/')
    elif api_type == 'recommender':
        _url = "http://data.bioportal.lirmm.fr/" + f"/{api_type}/?input=" + urllib.parse.quote(text,safe=':,/')

    if isinstance(params, dict) and params:
        _url += r'&' + urllib.parse.urlencode(params, safe=',')
    return _url

def get_json_req(url_req, encoding=None):
    opener = urllib.request.build_opener()
    try:
        if encoding is not None:
            print(1)
            return json.loads(opener.open(url_req).read().decode(encoding))
        else:
            print(2)
            return json.loads(opener.open(url_req).read())
    except Exception:
        return opener.open(url_req).read().decode(encoding)

##%%
# opener = urllib.request.build_opener()
# # response = opener.open(url_req)
# response = opener.open(url_default.replace('annotator','recommender'))
# annotations = json.loads(response.read().decode('utf-8'))

def get_info_from_annot_by_term(annotations, filter='all'):
    """This function reads raw response from SIFR web service and extract all annotations whose `annotatedClass` part has cui value"""
    cols = ['from','to','text',"id", 'cui',"semantic_groups", 'semanticType']
    attbt_anntcls = ['cui','semanticType','semantic_groups']
    # iterate terms
    df_flat = pd.DataFrame() # Flat dataframe, each line is just a term with all infos
    for i, annot in enumerate(annotations):
        anncls = annot["annotatedClass"]
        # FLAT DF
        if not annot['annotations']:
            print(f"Line {i} has no annotations")
            continue
        if any([x not in anncls.keys() for x in attbt_anntcls]):
            # print(f"Term {i} has no attributes interested")
            continue
        for ann in annot['annotations']:
            s,e = ann["from"], ann["to"]
            txt_ann = ann["text"]
            id = anncls["@id"]
            cui = anncls['cui'] if 'cui' in anncls.keys() else None # Concept Unique Identifiers (CUI)
            semanticType = anncls['semanticType'] if 'semanticType' in anncls.keys() else None
            semanticGps = anncls["semantic_groups"]if "semantic_groups" in anncls.keys() else None
            df_tmp = pd.DataFrame([[s,e,txt_ann,id,cui,semanticGps,semanticType]],columns=cols)
            df_flat = pd.concat([df_flat, df_tmp])
            # print(i, s,e, txt[s-1:e], annot['annotations'][0]['text'])
        
        if len(annot["mappings"])>0:
            pprint(f"! {i}-th mapping")

    if df_flat.empty:
        return {}
    # some processing
    df_flat['cui'] = df_flat['cui'].map(lambda x:','.join(x) if isinstance(x, list) else x)
    df_flat['semantic_groups'] = df_flat.semantic_groups.map(lambda x:','.join(x) if isinstance(x, list) else x)
    df_flat['semanticType'] = df_flat['semanticType'].map(lambda x:','.join(x) if isinstance(x, list) else x)
    df_flat = df_flat.dropna()
    df_flat.index = range(len(df_flat))

    if filter.lower()=='all':
        df = df_flat
    else:
        # An example, choosing only SEMANTICGROUP: CHEM, DISO
        # Actually we can choose the semantic groups directly by adding them to the input `params` for function `get_req_url`
        lst_conc_chosen = ['CHEM','DISO']
        df = df_flat[df_flat.semantic_groups.isin(lst_conc_chosen)]
    
    if df.empty:
        return {}
    df1 = df.groupby(['from','to','text'])[["id", 'cui',"semantic_groups", 'semanticType']].agg(set).apply(list).reset_index()
    df1[['cui',"semantic_groups", 'semanticType']]  = df1[['cui',"semantic_groups", 'semanticType']].applymap(lambda x:list(set(','.join(x).split(','))))
    json_df = json.loads(df1.to_json(orient='index'))
    return json_df

# Try to resovle pb: HTTP Error 414: Request-URI Too Long
def text_part(text_to_annotate, _MAX_TXT_LEN = 5000):
    """# Function `text_part` divides text_to_annotate to partitions 
        # whose length is lower than _MAX_TXT_LEN = 5000
        # The annoataions of each partition will be merged by function `split_txt_merge_annots`"""
    lst_wds_span = [(match.start(), match.end()) for match in re.finditer(r'\w+',text_to_annotate)]
    len_div = len(text_to_annotate)//2 
    ind = [x<=len_div for _,x in lst_wds_span].index(False)
    ind_txt = lst_wds_span[ind][1]
    sub_txt1, sub_txt2 = [text_to_annotate[:ind_txt], text_to_annotate[ind_txt:]]
    if len_div<_MAX_TXT_LEN:
        return [sub_txt1, sub_txt2]
    else:
        return text_part(sub_txt1) + text_part(sub_txt2)
    
def split_txt_merge_annots(text_to_annotate, params=None, encoding='utf-8', info_type='filter',lang='fr'):
    api_type ='annotator'
    lst_subtxt = text_part(text_to_annotate) # partitions of original text
    len_subtxt = list(map(len, lst_subtxt))

    for i,subtxt in enumerate(lst_subtxt):
        # txt_re = re.sub(r'[%\t]',' ',subtxt)
        annotations = get_json_req(get_req_url(subtxt, api_type=api_type, params=params_ann, lang=lang), encoding)
        annotations = get_info_from_annot_by_term(annotations)
        if i==0:
            res = deepcopy(annotations)
            continue
        len_res = len(res)
        len_cumsum = sum(len_subtxt[:i])
        # print(i, len_cumsum)
 
        for j, d in annotations.items():
            d["from"]= d["from"] + len_cumsum
            d["to"]= d["to"] + len_cumsum
            new_ind = j if isinstance(j, int) else int(j)
            new_ind += len_res
            res[str(new_ind)] = d
    return res
#%%
if __name__ == "__main__":
    SAVE_OUTPUT = False
    # logging system
    import logging
    from logging.handlers import RotatingFileHandler
    logging.basicConfig(level=logging.INFO,
                        handlers=[RotatingFileHandler('./annotators.log', maxBytes=100000, backupCount=10)],
                    format='%(asctime)s  %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S +0000')
    # Inputs
    SAVE_OUTPUT = True
    path_txt = pathlib.Path().cwd()
    # path_txt = pathlib.Path().home() + "train1.txt"

    # Init
    # files = [x for x in pathlib.Path(path_txt).iterdir() if x.suffix in ['.txt']]
    files = Path("train1.txt")
    pathOut = pathlib.Path(path_txt)
    pathOut = pathOut.with_name(pathOut.stem+'_ann')
    pathOut_rawresp = pathOut.with_name(pathOut.stem+"_raw_annots")

    if not pathOut.exists():
        pathOut.mkdir(parents=True, exist_ok=True)
    if not pathOut_rawresp.exists():
        pathOut_rawresp.mkdir(parents=True, exist_ok=True)

    files_error = set()
    train=open("train1.txt","rb")
    print("file opened")

    line = train.readline().decode("utf-8")
    while line:
        try:
            print("begin annotation")
            annotations = get_json_req(get_req_url(line, 'annotator', params_ann), 'utf-8')
            info1_annot = get_info_from_annot_by_term(annotations)
            print("line annotated")
        except urllib.error.HTTPError:
            try:
                info1_annot = split_txt_merge_annots(line, params=params_ann, encoding='utf-8')
            except Exception:
                logging.error(f'Error, annotator with file {train}',exc_info=True)
                files_error.update(train)
                annotations = []
                info1_annot = {}
                break

        if SAVE_OUTPUT:
            # empty annotaions will result in empty files, not no file at all
            # raw annots means response from server sans modification
            print("begin saving")
            with open((pathOut_rawresp/f'train1_raw_ann.json').as_posix(),'w', encoding='utf-8') as filehlr:
                print(f'->Saving: {filehlr.name}')
                json.dump(annotations, filehlr, indent=4, ensure_ascii=False)
            # Here is the processed one
            with open((pathOut/f'train1_ann.json').as_posix(),'w', encoding='utf-8') as filehlr:
                print(f'->Saving: {filehlr.name}')
                json.dump(info1_annot, filehlr, indent=4, ensure_ascii=False)
        train.readline()
    # for afile in files:
    #     print(f'\n+ Current file {afile.as_posix()}')
    #     with open(afile.as_posix(),'r',encoding='utf-8') as filehdlr:
    #         text_to_annotate = filehdlr.read()
    #     # already added in func `get_req_url`
    #     # txt_re = re.sub(r'[%\t]',' ',text_to_annotate) # Seems like % and \t exists in the text will cause the algo not working
    #

        # if len(text_to_annotate)==0:
        #     logging.info(f'Empty file {files.stem}, skipped')
        #     info1_annot, info2_recmd = [], {}
        # else:
        #     try:
        #         # output 1
        #         annotations = get_json_req(get_req_url(text_to_annotate, 'annotator', params_ann), 'utf-8')
        #         info1_annot = get_info_from_annot_by_term(annotations)
        #     except urllib.error.HTTPError:
        #         try:
        #             info1_annot = split_txt_merge_annots(text_to_annotate, params=params_ann, encoding='utf-8')
        #         except Exception:
        #             logging.error(f'Error, annotator with file {afile.stem}',exc_info=True)
        #             files_error.update(afile.name)
        #             annotations = []
        #             info1_annot = {}
        #
        # if SAVE_OUTPUT:
        #     # empty annotaions will result in empty files, not no file at all
        #     # raw annots means response from server sans modification
        #     with open((pathOut_rawresp/f'{afile.stem}_rawann.json').as_posix(),'w', encoding='utf-8') as filehlr:
        #         print(f'->Saving: {filehlr.name}')
        #         json.dump(annotations, filehlr, indent=4, ensure_ascii=False)
        #     # Here is the processed one
        #     with open((pathOut/f'{afile.stem}_ann.json').as_posix(),'w', encoding='utf-8') as filehlr:
        #         print(f'->Saving: {filehlr.name}')
        #         json.dump(info1_annot, filehlr, indent=4, ensure_ascii=False)

    ### =========================== A DF for all =================================

    files = [x for x in pathOut.iterdir() if not x.stem.startswith('.') and x.suffix=='.json']

    # def find_onto_type(link):
    #     for k,v in dict_link2ont.items():
    #         if link.startswith(k):
    #             return v
    #     return 'None'
    #
    # ##%% Iterate all annotations
    # cols = ['filename','from','to','text','ids']
    # df = pd.DataFrame()
    # for i,afile in enumerate(files):
    #     with open(afile.as_posix(), 'r', encoding='utf-8') as filehdlr:
    #         annots = json.load(filehdlr)
    #     if annots:
    #         df_tmp = pd.DataFrame().from_dict(annots, orient='index')
    #         df_tmp['filename'] = [afile.stem.replace('_ann','')]*len(df_tmp)
    #         df = pd.concat([df,df_tmp])
    #
    # df['ontologies'] = df.id.apply(lambda x:[find_onto_type(y) for y in x ] if x is not None else None)
    # df['ontologies'] = df['ontologies'].map(lambda x:list(set(x)))
    # df.index=range(len(df))
    #
    # df = df[['filename','from', 'to', 'text', 'id', 'cui', 'semantic_groups', 'semanticType',
    #         'ontologies']]
    # if SAVE_OUTPUT:
    #     df.to_csv((pathOut/'table_terms_onto.csv').as_posix(),encoding='utf-8')

    print('-> All Done')

# %%
# https://services.bioportal.lirmm.fr/annotator?text=""&longest_only=false&exclude_numbers=false&whole_word_only=true&exclude_synonyms=false&expand_mappings=false&fast_context=false&certainty=false&temporality=false&experiencer=false&negation=false&lemmatize=false&score_threshold=0&confidence_threshold=0&display_links=false&display_context=false&apikey=1de0a270-29c5-4dda-b043-7c3580628cd5