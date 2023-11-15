from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib

# Calcul du hash
def calculer_hash_fichier(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            hash_value = hashlib.sha256(file_data).hexdigest()
            return hash_value
    except FileNotFoundError:
        print(f"Fichier hash.txt introuvable.")
    except Exception as e:
        print(f"Erreur lors du calcul du hachage : {e}")
    return None

# �criture du hash dans hashVerif.txt
if calculer_hash_fichier('message_chiffre.bin'):
    with open('hashVerif.txt', 'w') as hashD_file:
        hashD_file.write(calculer_hash_fichier('message_chiffre.bin'))

# Comparaison des hash
try:
    with open('hash.txt', 'r') as hash_file, open('hashVerif.txt', 'r') as hashD_file:
        if hash_file.read().strip() == hashD_file.read().strip():
            print("L'int�grit� du message a �t� v�rifi�e.")
        else:
            print("Attention, le message a �t� modifi�.")
except FileNotFoundError:
    print("Au moins l'un des fichiers est introuvable.")
except Exception as e:
    print(f"Une erreur est survenue lors de la comparaison des fichiers : {e}")
            
input("Appuyez sur Entr�e pour continuer...")

def dechiffre(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
    return plaintext.decode()

with open("cle_privee.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend())

with open("message_chiffre.bin", "rb") as f:
    message_chiffre = f.read()

print("Message d�chiffr�:", dechiffre(message_chiffre, private_key))

input("Appuyez sur Entr�e pour quitter...")
