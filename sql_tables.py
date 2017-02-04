from pony.orm import *

db = Database()
db.bind('sqlite', 'database.sqlite', create_db=True)
#db.bind('mysql', host='127.0.0.1', user='root', passwd='', db='pony_test')

class Utilisateur(db.Entity):
	mail = PrimaryKey(str)
	pseudo = Required(str)
	password = Required(str)
	admin = Required(bool)
	def obtenir_nom_entier(self):
		return "%s" % (self.pseudo)

class Post(db.Entity):
	id = PrimaryKey(int, auto=True)
	titre = Required(str)
	contenu = Required(str)
	categorie = Required(Categorie)
	tags = Set(Tag)

class Categorie(db.Entity):
	id = PrimaryKey(int, auto=True)
	intitule = Required(str)
	descriptif = Required(str)
	posts = Set(Post)

class Tag(db.Entity):
	intitule = PrimaryKey(str)
	posts = Set(Post)

db.generate_mapping(create_tables=True) 

@db_session
def ajouter_utilisateur(mail, nom, prenom, password, autorise,hote):
    Utilisateur(mail=mail, pseudo=pseudo, password=password, admin=admin)

@db_session
def ajouter_post(titre, contenu, categorie, tags):
    Post(titre=titre, contenu=contenu, categorie=categorie, tags=tags)

@db_session
def ajouter_categorie(intitule, descriptif, posts):
    Categorie(intitule=intitule, descriptif=descriptif, posts=posts)

@db_session
def ajouter_tag(intitule, posts):
    Tag(intitule=intitule, posts=posts)