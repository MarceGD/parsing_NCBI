##Este pequeño codigo extrae El titulo y el abstract de un articulo en particular


from Bio import Entrez
import pandas as pd 

Entrez.email = "mdgamarraok@gmail.com"
lista_pmids = ['32714499', '32708835', '32698099', '32686918', '32683879', '32683791']
df = pd.DataFrame(columns=['PMID', 'Title', 'Abstract'])

for pmid in lista_pmids:
    handle=Entrez.efetch(db="pubmed",id= pmid,rettype="null",retmode="xml")
    record = Entrez.read(handle)
#parsea los elementos del articulo (diccionario de diccionarios)    
#dic3.keys() para ver los elementos de ese diccionario   
    dic1 = record['PubmedArticle'][0]
    dic2 = dic1['MedlineCitation']
    dic3 = dic2['Article']
    Authors = (dic3['AuthorList'][0])['LastName'] + ' ' + ((dic3['AuthorList'][0])['ForeName'])
    Journal = dic3['Journal']['Title']
    dic4 = dic3['Abstract']
    Title = dic3['ArticleTitle']
    Abstract = dic4['AbstractText'][0]
#Definir los elementos del Dataframe   
    df = df.append({'PMID': pmid, 'Title': Title, 'Abstract': Abstract, 'Author': Authors, 'Journal': Journal}, ignore_index=True)
print(df)
