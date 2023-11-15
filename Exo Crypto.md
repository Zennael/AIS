**Introduction à la cryptographie**

1. Générer et partager une clé de chiffrement AES256 ainsi que les IV avec le destinataire 


2. Comment générer une clé de chiffrement de manière sure ? Quel est le risque si les IV sont toujours les mêmes ? 

Pour générer une clé de chiffrement sécurisée, il faut utilisez un générateur de nombres aléatoires cryptographiquement sûr, choisir une longueur de clé appropriée et la stockez de manière sécurisée. Les IV (Initialization Vectors) doivent être aléatoires et uniques pour chaque opération de chiffrement afin d'éviter les risques liés à la répétition des IV, ce qui pourrait compromettre la sécurité du chiffrement. 

3. Chiffrer un message et l’envoyer 


4. Recevoir et déchiffrer le message 



5. Comment pourrait-on s'assurer de l'intégrité du message et de l'authenticité du destinataire ? Ajouter cette fonctionnalité à l'aide d'un script ou d'un outil en CLI. 

J’utilise des clés de chiffrement asymétrique et un calcul de hash  



6. Reprendre la question 4 avec un algorithme post quantique En cours

   
8. le message suivant a été intercepté : 

"prggr grpuavdhr f'nccryyr yr puvsserzrag qr prnfre, vy a'rfg cyhf hgvyvft nhwbheq'uhv, pne crh ftphevft" 

"cette technique s'appelle le chiffrement de caesar, il n'est plus utilisé aujourd'hui, car peu sécurisé" 

