# -*- coding: utf-8 -*-
import csv
import email
import mimetypes
import email.mime.application
from GmailWrapper import GmailWrapper

toIndex = {'Nom':0, 'Prenom':1, 'ddn':2, 'Rue':3, 'Numero':4, 'Bte':5, 'cpl adresse':6, 'CP':7, 'Localite':8, 'FONCTION':9, 'COTISATION':10 , 'Nom_contact':11, 'Prenom_contact':12, 'mail':13, 'GSM':14, 'Tel_1':15, 'Tel_2':16, 'Branche':17}

def cotisationToString(cotisation_type):
    if 'A -' in cotisation_type:
        return 'Cotisation pleine (46 euros) - pas de frère ou soeur affilié chez \"Les Scouts\" ou aux \"GCB\" '
    if 'B2 -' in cotisation_type:
        return 'Cotisation réduite (37 euros) - 1 frère ou soeur affiliée chez \"Les Scouts\" ou aux \"GCB\" '
    if 'B3 -' in cotisation_type:
        return 'Cotisation réduite (30 euros) - 2 (ou plus) frère(s) ou soeur(s) affilié(es) chez \"Les Scouts\" ou aux \"GCB\" '
    return 'Erreur: pas de cotisation mentionnée'

def generateContactHtml(row, contact_nbr):
    str_contact = ('<b><u>Personne de contact ' + str(contact_nbr) + '</u></b><br>' +
                     '<table><tr><td align="right"><u>Nom:</u></td><td>' + row[toIndex['Nom_contact']] + '</td></tr>' +
                     '<tr><td align="right"><u>Prénom:</u></td><td>' + row[toIndex['Prenom_contact']] + '</td></tr>' +
                     '<tr><td align="right"><u>Adresse:</u></td><td>' + row[toIndex['Rue']] + ', ' + row[toIndex['Numero']] + ' ' + row[toIndex['Bte']] + row[toIndex['cpl adresse']] + '</td></tr>' +
                     '<tr><td align="right"><u> </u></td><td>' + row[toIndex['CP']] + ' ' + row[toIndex['Localite']] + '</td></tr>' +
                     '<tr><td align="right"><u>Mail:</u></td><td>' + row[toIndex['mail']] + '</td></tr>' +
                     '<tr><td align="right"><u>Téléphone 1:</u></td><td>' + row[toIndex['GSM']] + '</td></tr>' +
                     '<tr><td align="right"><u>Téléphone 2:</u></td><td>' + row[toIndex['Tel_1']] + '</td></tr></table><br>')
    return str_contact

def generateAnimeHtml(row):
    str_anime = ('<b><u>Animé(e)</u></b><br>' +
                    '<table><tr><td align="right"><u>Nom:</u></td><td>' + row[toIndex['Nom']] + '</td></tr>' +
                     '<tr><td align="right"><u>Prénom:</u></td><td>' + row[toIndex['Prenom']] + '</td></tr>' +
                     '<tr><td align="right"><u>Date de naissance:</u></td><td>' + row[toIndex['ddn']] + ' (JJ/MM/AAAA)</td></tr>' +
                     '<tr><td align="right"><u>Adresse:</u></td><td>' + row[toIndex['Rue']] + ', ' + row[toIndex['Numero']] + ' ' + row[toIndex['Bte']] + row[toIndex['cpl adresse']] + '</td></tr>' +
                     '<tr><td>     </td><td>' + row[toIndex['CP']] + ' ' + row[toIndex['Localite']] + '</td></tr>' +
                     '<tr><td align="right"><u>Cotisation:</u></td><td>' + str(cotisationToString(row[toIndex['COTISATION']])) + '</td></tr>' +
                     '<tr><td align="right"><u>Mail:</u></td><td>' + row[toIndex['mail']] + '</td></tr>' +
                     '<tr><td align="right"><u>Téléphone 1:</u></td><td>' + row[toIndex['GSM']] + '</td></tr>' +
                     '<tr><td align="right"><u>Téléphone 2:</u></td><td>' + row[toIndex['Tel_1']] + '</td></tr></table><br>')
    return str_anime

def generateMsgHtml(contactsHtml):
    html = """\
    <html>
        <head></head>
        <body>
            <p>Chers parents,<br><br>
            Voici le temps de la rentrée guide. Si votre enfant désire continuer son aventure au sein de notre unité, nous vous demandons de remplir les formalités d'inscription décrites ci-dessous.<br><br>
    <ol>
    <li><b><u> Rencontrer les animateurs de la branche </u></b><br>
        Nous vous encourageons, particulièrement si votre enfant change de branche cette année, à vous présenter auprès des chefs de votre enfant.
    </li><li><b><u> Vérifier vos coordonnées </u></b><br>
        Vous trouverez ci-dessous les coordonnées dont nous disposons. Merci de les vérifier avec attention.<br>
        Il est important que nous disposions d'au moins 1 adresse et 1 (idéalement 2) numéro(s) de téléphone.<br><br>
        
        Compléter ensuite <a href="https://goo.gl/PSrd4i">ce formulaire</a> pour confirmer ou modifier vos coordonnées (pour chaque enfant, même si les coordonnées sont correctes).
        <br>
    </li><li><b><u> Payer la cotisation sur le compte de l'unité avant le 15 octobre </u></b><br>
        Cette cotisation comprend l’affiliation au mouvement, l’assurance en cas d’accident, l’abonnement aux revues et les frais administratifs pour l’unité.<br>

        Le montant de la cotisation s’élève à :
        <ul>
            <li> 46 euros/enfant si vous avez un enfant inscrit chez les guides (GCB) ou les scouts.
            </li><li> 37 euros/enfant si vous avez deux enfants inscrits chez les guides (GCB) ou les scouts.
            </li><li> 30 euros/enfant si vous avez trois enfants ou plus inscrits chez les guides (GCB) ou les scouts.
        </li></ul>
        Ces prix sont d'application pour chaque enfant inscrit dans notre unité. La réduction tient compte du nombre d'enfants inscrits dans notre unité mais aussi dans d'autres unités "GCB" ou "Les Scouts".<br><br>

        La cotisation doit être versée sur le compte de l'unité guide d'Ecaussinnes : <b>BE64  1043  5830  8852</b>, avec la communication : <b>Prénom de l'enfant  NOM de l'enfant - branche</b> <br>
        Attention, seules les cotisations des enfants inscrits dans notre unité doivent être versées sur ce compte.
        <br>
    </li><li><b><u> Payer la participation aux frais de la branche </u></b><br>
        Les modalités de paiement vous sont communiquées par les staffs de chaque branche.
        <br>
    </li></ol><br>
    Nous ne voudrions pas que des difficultés financières empêchent un enfant de participer aux activités. C'est pourquoi, vous pouvez prendre contact avec un membre du staff d'unité pour obtenir un étalement ou une réduction. Vous pouvez compter sur notre discrétion.<br><br>

    Toutes les informations utiles, la composition des staffs, les coordonnées des chefs et bien plus sont repris sur notre site internet: <a href="www.guidesecaussinnes.be">www.guidesecaussinnes.be</a> Pour les pages protégées, le mot de passe est "guide4HC". <br><br>

    Cordialement, <br>
    Le Staff d'unité <br><br>

    Merci de vérifier les contacts suivants: <br><font color="blue">""" + contactsHtml + """ 
    </font></p>
        </body>
    </html>
    """
    return html


def createMimeMessage(contactsHtml, mailTo):
    body_html = email.mime.Text.MIMEText(generateMsgHtml(contactsHtml), 'html', 'UTF-8')

    msgMain = email.mime.Multipart.MIMEMultipart()
    msgMain['Subject'] = """Reinscription 2018-2019 unite guide Ecaussinnes"""
    msgMain['From'] = 'guides4hc@gmail.com'
    msgMain['To'] = str(mailTo)

    # PDF attachment
    filename2 = 'invit_passage.pdf'
    fp2 = open(filename2, 'rb')
    att2 = email.mime.application.MIMEApplication(fp2.read(), _subtype="pdf")
    fp2.close()
    att2.add_header('Content-Disposition', 'attachment', filename=filename2)

    filename = 'Inscriptions_courrier.pdf'
    fp = open(filename, 'rb')
    att = email.mime.application.MIMEApplication(fp.read(), _subtype="pdf")
    fp.close()
    att.add_header('Content-Disposition', 'attachment', filename=filename)

    msgMain.attach(att2)
    msgMain.attach(att)
    msgMain.attach(body_html)

    return msgMain


# TODO: doit venir du fichier json
mailWrapper = GmailWrapper('userName', 'Pswrd')

f_errors = open('NotValid_august.txt', 'a')

f_contacts = open('2_try.csv', 'r')
list_contacts = csv.reader(f_contacts)

all_contacts_html = ''
current_nom = ''
current_prenom = ''
hasPhoneNumber = False
isAnime = True
contact_nbr = 0
mailTo = ''
for row in list_contacts:
    if row[toIndex['Nom']] in current_nom and row[toIndex['Prenom']] in current_prenom:
        contact_nbr += 1
        all_contacts_html += generateContactHtml(row, contact_nbr)
    else:
        mimeContent = createMimeMessage(all_contacts_html, mailTo)
        try:
            mailWrapper.sendEmail(mailTo, mimeContent)
        except:
            f_errors.write(current_nom + ' ' + current_prenom + '\n')
        print('---------NewContact--------')
        all_contacts_html = ''
        contact_nbr = 0
        current_nom = row[toIndex['Nom']]
        current_prenom = row[toIndex['Prenom']]
        mailTo = row[toIndex['mail']]
        isAnime = ('1' in str(row[toIndex['FONCTION']]))
        if (row[toIndex['GSM']] or row[toIndex['Tel_1']]):
            hasPhoneNumber = True
        all_contacts_html += generateAnimeHtml(row)
mimeContent = createMimeMessage(all_contacts_html, mailTo)
try:
    mailWrapper.sendEmail(mailTo, mimeContent)
except:
    f_errors.write(current_nom + ' ' + current_prenom + '\n')
print('---------Ending script ...--------')

f_errors.close()
f_contacts.close()
