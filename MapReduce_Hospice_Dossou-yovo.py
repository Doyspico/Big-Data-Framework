import numpy as np
# La fonction decompose permettra de supprimer les ponctuations des phrases et 
# identifier les mots du texte
def decompose(texte):
    # Supprimer les ponctuations en les remplaçant par des espaces
    texte1= texte.replace(', ',' ')
    texte2= texte1.replace('?',' ')
    texte3= texte2.replace('!',' ')
    texte4= texte3.replace("'",' ')
    texte5= texte4.replace(";",' ')
    texte6= texte5.replace('. ',' ')
    texte7= texte6.replace('.',' ')
    texte8= texte7.replace(',',' ')
    # Identifier les mots par les espaces
    mots = texte8.split(' ')
    # Transformer en matrice
    mots=np.array(mots)
    # Transformer la matrice précédente en matrice colonne
    m_mots= np.reshape(mots, (len(mots),1))
    return m_mots
    
def mapp(texte):
    m_mots = decompose(texte)
    # Création d'une matrice colonne constituée de 1 de taille 
    #le nombre de mots contenus dans le texte
    m_init=np.reshape(np.ones(len(m_mots)),(len(m_mots),1))
    # fusion des matrices m_mots et init
    mapp= np.concatenate((m_mots,m_init),axis=1)
    return mapp
    
def reduce(texte):
    m_mots= decompose(texte)
    # Comptage des occurences de chaque mot de la matrice constituée des mots
    count = np.unique(m_mots, return_counts=True)
    m_count = np.array(count)
    # Conversion en matrice colonne
    reduction = m_count.transpose()
    return reduction

# La fonction map_reduce affiche le map et le reduce du texte introduit en arguments
def map_reduce(texte):
    a = print("Voici le Map de votre texte:")
    b = print(mapp(texte))
    c = print("Voici le Reduce de votre texte")
    d = print(reduce(texte))
    return a, b, c, d
# Exemple
a= mapp("maman est malade, maman est guerie")
print(a)
b=reduce("maman est malade, maman est guerie")
print(b)
c=map_reduce("maman est malade, maman est guerie")


