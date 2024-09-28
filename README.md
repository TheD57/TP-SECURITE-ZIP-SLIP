# TP-SECURITE-ZIP-SLIP

# Sujet

vous êtes aujourd'hui à la foi, l'attaquant et la victime.

### Etape Attaquant

Vous êtes un professeur et vous voulez tester leur franchise de vos élèves.<br>
Pour faire cela vous avez eu une petit idée, après avoir appris qu'il était possible d'executé du code lorsque qu'une personne dezip un dossier, on va donc implémenté un programme malveillant dans notre zip afin qu'il s'éxecuter lors d'un dézippage non sécurisé on appel ça le <strong>Zip Slip</strong>.
afin de mettre votre plan à execution vous allez d'abord récupérer le programme python :

```
Create_EvilZip.py
```

Celui-ci ce base sur le GitHub de ceasarsotovalero :
https://github.com/cesarsotovalero/zip-slip-exploit-example/blob/master/evilarc.py

vous aurez besoin de python pour executer le programme et voici comment l'utilisé :
```
python Create_EvilZip.py -d 10 -o unix .prank.sh
```

maintenant vous avez un zip totalement infecté, celui-ci executera donc le programme <strong>.prank.sh</strong>.

Vous enverrez à votre victime, le zip et le UnZip_Program.py qui est vunérable à ce type d'attaque car il manque une vérification.
### Etape Victime

notre victime va donc recevoir un fichier zip contenant tous ces "précieuse correction"

`python3 UnZip_program.py dossier.zip` : maintenant executer ce programme sur votre dossier zipper<br>

Comme vous pouviez vous en doutez le piège c'est donc activé
