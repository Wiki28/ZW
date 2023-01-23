import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "8529843")) #optional
API_HASH = getenv("API_HASH", "6e06fb8f7b42fb33821f272597321bc1") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1980553307").split()))
OWNER_ID = int(getenv("OWNER_ID", "2133434438"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://kontol:kontol@cluster0.cuiswrb.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5043589686:AAG-072NPFsbu0gioKF3TdElC8RT34N_eTk")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "-1001667983274")
LOG_GROUP = getenv("LOG_GROUP", "-1001667983274")
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/Wiki28/ZW")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAazsDPKvH33dQPcCb-ZeIqUmkbmMYTA022dAjNI62r9bldO_y-X5H4AJl295hqBicFWTvQlsnLkfiiqj5XRSMkPKYgf88ptTzkXPipPoflNVPsnBIyjrMrjLUvtOsnojvI0W9uftDqZn9z73nrlfvh9Ux0VZnBmHm2JF_Kw5qi78ZdYaNjme3613DNvYnzV-RwJgOXQyauCL6ggPS7Pw1QtRMg1_67R4aGMRNbXjrHCPLmYLBWI5-Vdf3yBJeGzWVlMDiYFFbGOWdpHKpGEICsoACmBhXH51GPv-qrXbD4gSANfCgGa7kqUjV1JBGz-Ur5X4VaYJgr6tEJrZgq1iIyAAAAAB_KaBGAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQC2OfZ6_EAbLatSRTXPlA0iz6MoYd-WKn6-2aZpQl3yBV4wuXO3DgSSW8suT7C99aJTvcuMR8En2UDqwblFEMmT5Lkgs4n-yzrfT3OJJ1Wwj-wq7QjhQNUtKIGq3a4CcSReWT0Ikqqh6pSZM_6sm-sESMRnEBnNqH0LTEDkSvEllikqRCYuih5dcn7uiqPvJaR8JqrL4JXRHTzqk_oCQlCwDh0iePG-kdi8XzEt7DQ6euu2AKQ8aqaMiUTnnuVjTB1s1JfRlvcLVD059JcLmWd_XD1qLbXypCqnmSCEH27G0P52wGuzE-19VbCN4J5J8RERHNs961uAac0A2ao3xeuRdgzYWwA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
