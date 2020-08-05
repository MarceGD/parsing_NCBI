##Este pequeño codigo extrae El titulo y el abstract de un articulo en particular
from Bio import Entrez


Entrez.email = "mdgamarraok@gmail.com" #siempre para entrar a NCBI hay que decir quien sos
handle=Entrez.efetch(db="pubmed",id='30407518',rettype="null",retmode="xml") #aca digo la base de datos db, el id del paper (rettype y retmode nose que es)
record = Entrez.read(handle) ##dedino record que es el diccionario con la informacion y empiezo a parsear las llaves
dic1 = record['PubmedArticle'][0]
dic2 = dic1['MedlineCitation']
dic3 = dic2['Article']
#dic3.keys() para ver que posee ese diccionario
dic4 = dic3['Abstract'] #Extrae el abstract del articulo 

print(dic3['ArticleTitle'] + '\n') #titulo del articulo

print(dic4['AbstractText'][0]) #Abstrac

#rettype = This parameter specifies the record view returned, such as Abstract or MEDLINE from PubMed, or GenPept or FASTA from protein
#retmode = This parameter specifies the data format of the records returned, such as plain text, HMTL or XML (R)