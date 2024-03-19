from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#pour trouver des emojis : webfx.com/tools/emoji-cheat-sheet
st.set_page_config(page_title="Mon portfolio", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#utiliser le CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#-----LOAD ASSETS------
lottie_girl = load_lottieurl("https://lottie.host/c7931b93-c8d5-4ac4-9212-57dd018d538f/ksZntAqqbB.json")
img_moodle = Image.open("images/moodle.png")
img_filboost = Image.open("images/filboost.png")
img_affiche = Image.open("images/affiche.png")
img_procreate = Image.open("images/procreate.png")
img_livres = Image.open("images/livres.png")
img_criminou = Image.open("images/criminou.png")
img_plats = Image.open("images/plats.png")
img_notionhome = Image.open("images/notionhome.png")
img_notionmaslow = Image.open("images/notionmaslow.png")
img_notioncuisine = Image.open("images/notioncuisine.png")
img_notionrevisions = Image.open("images/notionrevisions.png")
img_moodlefigma = Image.open("images/moodlefigma.png")
img_portraits = Image.open("images/portraits.png")
img_morpion = Image.open("images/morpion.png")
img_site = Image.open("images/site.png")
img_bandedessinee = Image.open("images/bandedessinee.png")
img_page1 = Image.open("images/page1.png")
img_page19 = Image.open("images/page19.png")
img_page21 = Image.open("images/page21.png")
img_page23 = Image.open("images/page23.png")

#Header
with st.container():
    st.subheader("Bonjour, je m'appelle Marina :wave:")
    st.title("Une candidate au master Création Numérique")
    st.write("Je suis en train d'apprendre le Python en créant ce portfolio")
    st.write("Découvrez qui je suis ainsi que mes travaux ici !")

#qui suis-je
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Qui suis-je ?")
        st.write("##")
        st.write(
            """
            Depuis petite je suis passionnée par deux choses.
Ma première passion, c'est de créer. Cuisiner (j'ai écrit deux livres), dessiner sur papier et sur iPad (avec Procreate), peindre, fabriquer des objets, des bijoux, des vêtements, rénover de vieux meubles, faire de la couture, des perles, de la poterie...
Bref : je suis très manuelle et très créative.


Ma deuxième passion ? Les ordinateurs !
J'ai grandi avec vieil ordinateur sous Windows XP, sans même internet ! J'adorais explorer, cliquer partout pour comprendre comment cela fonctionne.

Il y a quelques années je me suis inscrite sur Instagram afin de publier mes recettes de cuisine. J'ai également travaillé comme assistante de communication et étais en charge de créer les visuels de l'entreprise. Et j'ai découvert une nouvelle forme d'art créatif : le design digital ! 
Réaliser un visuel esthétique, efficace, harmonieux, choisir les couleurs, les formes, ça m'a beaucoup plu.
Puis j'ai découvert Notion et ça a été une révélation : j'ai passé des heures et des heures à apprendre son fonctionemment jusqu'à pouvoir créer mon propre "deuxième cerveau". J'ai créé des templates ayant pour but de m'aider sur différents aspects de la vie quotidienne et j'ai même pu les vendre, car ils ont énormément plu.

C'est ainsi que j'ai trouvé ce que je voulais faire professionnellement : créer des produits digitaux (applications, sites internet, e-books, mockups, templates Notion...) utiles au quotidien.
J'adorerais vivre de mes propres produits, toujours me challenger en créant de nouvelles choses, en m'adaptant à de nouveaux besoins, de nouvelles personnes... tout en étant libre de laisser ma créativité s'exprimer !

Aujourd'hui je souhaite donc apprendre à coder avec différents langages, apprendre le design (UX et UI) afin de devenir polyvalente. 
            """
        )
with right_column:
    st_lottie(lottie_girl, height=300, key="coding")

#projets 
with st.container():
    st.write("---") #c'est le divider
    st.header("Mes projets")
    st.write("##") #hashtag pour chaque colonne
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_filboost)
    with text_column :
        st.subheader("Identité visuelle de Filboost")
        st.write(
            """
                 Voici l'avant/après du feed Instagram de l'entreprise. 
                 """
                 )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_affiche)
    with text_column:
        st.subheader("Affiche de recrutement de participants")
        st.write(
            """
            Voici l'avant/après d'une affiche de recrutement de participants pour une expérience sur la psychologie et la musique.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_moodle)
    with text_column:
        st.subheader("Proposition de refonte de Moodle")
        st.write(
            """
            Voici l'avant/après de Moodle tel que je l'imagine. Ici vous voyez Moodle tel qu'il est actuellement
            """
        )
        st.markdown("[Voir en vrai](https://moodle.univ-lille.fr)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_moodlefigma)
    with text_column:
        st.write(
            """
            Et voici ma proposition !
            """
        )
        st.markdown("[Voir sur Figma](https://www.figma.com/file/f02LfNdSTNNk6LIL2KQh8O/MOODLE?type=design&node-id=3101%3A2&mode=design&t=3tFdqvqPXnG2EO0W-1)")




with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notionhome)
    with text_column:
        st.subheader("Mon deuxième cerveau sur Notion")
        st.write(
            """
            Voici le template que j'ai créé. Ici, la page d'accueil avec la navigation.
            """
        )
        st.markdown("[pour voir le template entier](https://silly-trout-24d.notion.site/Bonjour-pr-nom-a6bc4328e8074461a5e6694606ecef00?pvs=4)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notionmaslow)
    with text_column:
        st.write(
            """
            Et la pyramide de Maslow.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notionrevisions)
    with text_column:
        st.write(
            """
            Les révisions
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_notioncuisine)
    with text_column:
        st.write(
            """
            Et la cuisine inventaire.
            """
        )
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_morpion)
    with text_column:
        st.subheader("Un jeu de morpion en python")
        st.write(
            """
            Mon tout premier projet Python fut ce portfolio et ce jeu est le deuxième.
            """
        )
        st.markdown("[pour voir le code sur mon Github](https://github.com/marinanowicki/morpion/blob/9e8df71f9d7dda34512350185de2692dd60afb64/main)")


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_criminou)
    with text_column:
        st.subheader("Le logo de ma boutique de produits digitaux")
        st.write(
            """
            Criminou c'est mon chat...La boutique n'existe pas encore mais c'est en cours de création.
            """
        )

#loisirs 
with st.container():
    st.write("---") #c'est le divider
    st.header("Mes loisirs")
    st.write("##") #hashtag pour chaque colonne
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_procreate)
    with text_column :
        st.subheader("Dessin")
        st.write(
            """
                 Du dessin digital...Voici des dessins réalisés sur Procreate. 
                 """
                 )
        st.markdown("[Voir le timelapse d'un dessin](https://youtu.be/g4fSyc2o_AQ)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_bandedessinee)
    with text_column:
        st.subheader("Bande dessinée")
        st.write(
            """
            J'ai réalisé une bande dessinée de 22 pages pour offrir. Chaque planche représente un souvenir vécu avec la personne. J'ai créé les cases et les bulles avec Canva. J'ai ensuite exporté le document et ai dessiné sur Procreate.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page1)
    with text_column:
        st.write(
            """
            La première de couverture.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page19)
    with text_column:
        st.write(
            """
            La page 19.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page21)
    with text_column:
        st.write(
            """
            La page 21.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_page23)
    with text_column:
        st.write(
            """
            La page 23.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_site)
    with text_column:
        st.subheader("Mon site de cuisine")
        st.write(
            """
            Voici mon site internet "1repas1euro". Il vient tout juste d'être refait donc il n'y a pas encore énormément de contenu dessus car je dois tout remettre à la main !
            """
        )
        st.markdown("[Voir le site](https://1repas1euro.fr)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_livres)
    with text_column:
        st.subheader("Mes deux livres de cuisine")
        st.write(
            """
            Voici les deux livres que j'ai écrits, édités par la maison SOLAR.
            """
        )
 

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_plats)
    with text_column:
        st.subheader("J'essaie d'apprendre la photo")
        st.write(
            """
            J'aimerais pouvoir photographier mes recettes de façon professionnelle, j'essaie donc d'apprendre dans ce domaine.
            """
        )


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_portraits)
    with text_column:
        st.write(
            """
            Et la photo de portraits aussi. Ici ce sont des autoportraits.
            """
        )


#formulaire de contact
with st.container():
    st.write("---")
    st.header("Contactez-moi !")
    st.write("##")

    #formsubmit.com 
    contact_form = """
    <form action="https://formsubmit.co/marinanowicki@outlook.fr" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="nom" placeholder="Votre nom" requiered>
        <input type="email" name="email" placeholder="Votre email" requiered>
        <textarea name="message" placeholder="Votre message" requiered></textarea>
        <button type="submit">Envoyer</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
