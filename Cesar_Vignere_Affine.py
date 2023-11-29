
            # CHIFFREMENT CESAR

import string

def chiffrement_cesare(texte, motcle):
    texte = texte.upper()
    alphabet = string.ascii_uppercase
    motcle = int(motcle)
    tableau_chiffrement = str.maketrans(alphabet, alphabet[motcle:] + alphabet[:motcle])
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_cesare(texte_chiffre, motcle):
    texte_chiffre = texte_chiffre.upper()
    alphabet = string.ascii_uppercase
    motcle = int(motcle)
    tableau_dechiffrement = str.maketrans(alphabet[motcle:] + alphabet[:motcle], alphabet)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte

def cryptage():
    print('1 - Chiffrement Césare')
    print('2 - Déchiffrement Césare')
    choice = int(input('Faites votre choix : '))
    
    if choice == 1:
        text = input("Veuillez saisir le texte à crypter : ")
        key = input("Veuillez saisir la clé de cryptage : ")
        texte_chiffrer = chiffrement_cesare(text, key)
        print("Texte chiffré :",texte_chiffrer)
    elif choice == 2:
        texte = input("Veuillez saisir le texte crypté : ")
        cle = input("Veuillez saisir la clé de décryptage : ")
        texte_dechiffrer = dechiffrement_cesare(texte, cle)
        print("Texte déchiffré :",texte_dechiffrer)
    else:
        print('Veuillez faire un choix entre 1 et 2')

cryptage()


            # CHIFFREMENT AFFINE


import string

def chiffrement_affine(texte, a, b):
    texte = texte.upper()
    alpha = string.ascii_uppercase
    tableau_chiffrement = str.maketrans(alpha, ''.join([alpha[(a*i + b) % 26] for i in range(26)]))
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_affine(texte_chiffre, a, b):
    texte_chiffre = texte_chiffre.upper()
    alpha = string.ascii_uppercase
    tableau_dechiffrement = str.maketrans(''.join([alpha[(a*i + b) % 26] for i in range(26)]), alpha)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte

def cryptage_affine():
    choix = input("Voulez-vous chiffrer (A) ou déchiffrer (B) ? ").upper()
    
    if choix == 'A':
        texte = input("Entrez le texte à chiffrer : ")
        a = int(input("Entrez la valeur de a pour la clé : "))
        b = int(input("Entrez la valeur de b pour la clé : "))
        texte_chiffre = chiffrement_affine(texte, a, b)
        print("Texte chiffré :", texte_chiffre)
        
    elif choix == 'B':
        texte_chiffre = input("Entrez le texte à déchiffrer : ")
        a = int(input("Entrez la valeur de a pour la clé : "))
        b = int(input("Entrez la valeur de b pour la clé : "))
        texte_dechiffre = dechiffrement_affine(texte_chiffre, a, b)
        print("Texte déchiffré :", texte_dechiffre)
        
    else:
        print("Choix invalide. Veuillez choisir 'C' pour chiffrer ou 'D' pour déchiffrer.")

# Appel de la fonction d'interaction avec l'utilisateur
cryptage_affine()


            # CHIFFREMENT VIGENERE
            
import string

def chiffrement_vigenere(text, motcle):
    text = text.upper()
    motcle = motcle.upper()
    alphabet = string.ascii_uppercase
    tableau_chiffrement = str.maketrans(alphabet, alphabet[len(motcle):] + alphabet[:len(motcle)])
    texte_chiffre = text.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_vigenere(texte_chiffre, motcle):
    texte_chiffre = texte_chiffre.upper()
    motcle = motcle.upper()
    alphabet = string.ascii_uppercase
    tableau_dechiffrement = str.maketrans(alphabet[len(motcle):] + alphabet[:len(motcle)], alphabet)
    text = texte_chiffre.translate(tableau_dechiffrement)
    return text


def cryptage():
    print('1 - Chiffrement Vigénère')
    print('2 - Déchiffrement Vigénère')
    choice = int(input('Faites votre choix : '))
    
    if choice == 1:
        texte = input("Veuillez saisir le texte à crypter : ")
        key = input("Veuillez saisir la clé de cryptage : ")
        texte_chiffrer = chiffrement_vigenere(texte, key)
        print("Texte chiffré :",texte_chiffrer)
    elif choice == 2:
        texte = input("Veuillez saisir le texte crypté : ")
        cle = input("Veuillez saisir la clé de décryptage : ")
        texte_dechiffrer = dechiffrement_vigenere(texte, cle)
        print("Texte déchiffré :" ,texte_dechiffrer)
    else:
        print('Veuillez faire un choix entre 1 et 2')

cryptage()