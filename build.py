# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from tools.core import Configuration
from ca.core import CertificateAuthority
from server.core import Server
import print_pems as ppems  #a été ajouté pour l'impression

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
CA_PASSWORD = 'mot_de_passe_CA'
SERVER_PASSWORD = 'mot_de_passe_serveur'

CA_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Sevenans", "UTBM_CA", "localhost") 
SERVER_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Sevenans", "UTBM_SER", "localhost") 

# Création de l'autorité de certification
certificate_authority = CertificateAuthority(CA_CONFIGURATION,CA_PASSWORD,CA_PRIVATE_KEY_FILENAME,CA_PUBLIC_KEY_FILENAME)
    # regardez en haut et ca/core.py

# Création du server
server = Server(SERVER_CONFIGURATION,SERVER_PASSWORD,SERVER_PRIVATE_KEY_FILENAME,SERVER_CSR_FILENAME)
    # regardez en haut et server/core.py

# Signature du certificat par l'autorité de certification
signed_certificate = certificate_authority.sign(server._csr,SERVER_PUBLIC_KEY_FILENAME)# A compléter regardez ca/core.py et server/core.py

#impression des certificats à compléter regardez #print_pems

print("______________________")
print("CA public key filename")
ppems.print_perms(CA_PUBLIC_KEY_FILENAME)
ppems.print_perms(SERVER_PRIVATE_KEY_FILENAME)
print("______________________")

print("finished ...")
