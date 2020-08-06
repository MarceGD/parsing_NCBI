##Este pequeño codigo extrae El titulo y el abstract de un articulo en particular


from Bio import Entrez
import pandas as pd 
#Entres (NCBI) necesita un mail para saber quien es el que ingres
Entrez.email = "mdgamarraok@gmail.com"
#Listas de ids de articulos (esto puede ser sacado con un for loop)
lista_pmids = ['32714499', '32708835', '32698099', '32686918', '32683879', '32683791']
#Defino las columnas de mi data frame
df = pd.DataFrame(columns=['PMID', 'Title', 'Abstract', 'Journal'])
   
class NCBI:
    
    def Pubmed(name):
        handle=Entrez.efetch(db="pubmed",id= name ,rettype="null",retmode="xml")
        #rettype = This parameter specifies the record view returned, such as Abstract or MEDLINE from PubMed, or GenPept or FASTA from protein
        #retmode = This parameter specifies the data format of the records returned, such as plain text, HMTL or XML (R)
        record = Entrez.read(handle)
        #parsea los elementos del articulo (diccionario de diccionarios)
        Title = (((record['PubmedArticle'][0])['MedlineCitation'])['Article'])['ArticleTitle']
        Abstract = ((((record['PubmedArticle'][0])['MedlineCitation'])['Article'])['Abstract'])['AbstractText'][0]
        Journal = (((record['PubmedArticle'][0])['MedlineCitation'])['Article'])['Journal']
        Authors = ((((record['PubmedArticle'][0])['MedlineCitation'])['Article'])['AuthorList'][0])['LastName'] + ' ' + (((((record['PubmedArticle'][0])['MedlineCitation'])['Article'])['AuthorList'][0])['ForeName'])
        global df #avisa a la funcion que df ya esta definido afuera
        df = df.append({'PMID': i, 'Title': Title, 'Abstract': Abstract, 'Author': Authors, 'Journal': Journal}, ignore_index=True)
       

for i in lista_pmids:
    NCBI.Pubmed(i)

print(df)
