from sql_tables import *
from pony.orm import *
import hashlib
import getpass

# on obtient le mail
mail = raw_input("Mail : ")
# et le pass
m = hashlib.md5()
m.update(getpass.getpass("Password : "))
# le pseudo
pseudo = raw_input("Mail : ")
ajouter_utilisateur(mail, pseudo, m.hexdigest(), True)