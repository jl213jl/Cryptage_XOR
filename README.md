#  Cryptage XOR (via SHA-256)

Salut ! Je suis **JL213JL**.  
J'ai conçu ce script Python pour permettre de crypter et décrypter n'importe quel fichier de manière simple et efficace.

---

##  Présentation
Ce script utilise l'opération logique **XOR** combinée à un hachage **SHA-256** de votre clé pour transformer vos données. La robustesse vient du fait que même une clé courte génère une empreinte de 32 octets (256 bits) pour le processus de chiffrement.

##  Comment ça marche ?

1. **Input :** Indiquez le nom du fichier source (ex: `photo.jpg`).
2. **Output :** Indiquez le nom du fichier de destination (ex: `photo_cryptee.dat`).
3. **Clé :** Entrez votre mot de passe secret.

> [!IMPORTANT]
> **POUR DÉCRYPTER :** Vous devez impérativement utiliser la **MÊME CLÉ** que celle utilisée lors du cryptage. Le processus est symétrique.

