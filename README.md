# TP-SECURITE-ZIP-SLIP

# Sujet

vous êtes aujourd'hui à la foi, l'attaquant et la victime.

### Etape Attaquant

Vous êtes un professeur et vous voulez tester leur franchise de vos élèves.<br>
Pour faire cela vous avez eu une petit idée, après avoir appris qu'il était possible d'executé du code lorsque qu'une personne dezip un dossier, on appel ça le <strong>Zip Slip</strong>.
afin de mettre votre plan à execution vous allez d'abord taper les commandes <strong>Shell</strong> écrite juste en dessous.

```
mkdir -p Correction_DS/../.prank/
cp prank.sh Correction_Ds/../.prank/
chmod +x
Correction_DS/../tmp/prank/prank.sh

zip -r Correction_DS.zip Correction_DS/
```
et ensuite vous avez votre dézipeur que vous devrez transmettre à votre victime <strong>UnZip_program.py</strong><br>
`python3 UnZip_program.py dossier.zip` : commande à executer<br>

