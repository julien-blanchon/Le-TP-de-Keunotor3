---
# pandoc -s cours.md -o cours.pdf --template eisvogel
title: "Cours - Droits"
subtitle: "ModIA - INSA 1A"
author: "[Julien Blanchon](mailto:julien.blanchon@etu.toulouse-inp.fr)"
date: "9 Septembre 2020"
keywords: [droits, insa, modia]
lang: "fr-FR"
titlepage: true,
titlepage-rule-color: "360049"
titlepage-rule-height: 13
#titlepage-background: "~/Documents/backgrounds/background3.pdf"
#logo: "figures/inp-enseeiht.png"
#logo-width: 65mm
#page-background: "~/Documents/backgrounds/background1.pdf"

base: . %Base directory for import file

header-left: "\\hspace{1cm}"
header-center: "\\leftmark"
header-right: "Page \\thepage"
footer-left: "\\thetitle"
footer-center: ""
footer-right: "[Julien Blanchon](mailto:julien.blanchon@etu.toulouse-inp.fr)"

subparagraph: true

output:
pdf_document:
    fontsize: 12pt #30, 11 ou 12pt seulement
    # mainfont: "Roboto"
    # sansfont: "Raleway"
    # monofont: "IBM Plex Mono"
    geometry: [a4paper, bindingoffset=0mm, inner=30mm, outer=30mm, top=30mm, bottom=30mm] # Voir https://ctan.org/pkg/geometry pour les options geometry

toc: true
toc-own-page : true
toc-title: Table des matières
toc_depth: 2
lot: false
lof: false

documentclass: article
...	

# Introduction - L’organisation judiciaire française

## Les différentes juridictions

La justice française est organisée en deux ordre: l'**ordre judiciaire** et l'**ordre administratif**. Subdivisée encore en différentes cours de justice (exemple: cours de cassation, cours d'appel ...).

# Introduction : L’organisation judiciaire française

Rendre la justice est l’une des fonctions de l’Etat prévue par la Constitution. Pour parvenir à cette fin, l’organisation judiciaire doit respecter un certain nombre de principes généraux (I). La justice est rendue par des organes compétents en la matière, appelés juridictions (II), celles-ci devant respecter des règles particulières de procédures (III).

## I- Les principes généraux du système judiciaire français

La justice est le monopole de l’Etat : c’est un service public dont l’organisation répond à un certain nombre de principes.

### A- La justice est un monopole d’Etat

**Principe :**
Seuls les tribunaux légalement institués par l’Etat peuvent rendre des décisions ayant autorité de la chose jugée (qui donnent une solution au litige) et force exécutoire (qui s’imposent immédiatement aux parties, elles doivent donc les respecter et les appliquer). Rendre la justice est donc un attribut de la souveraineté de l’Etat.

**Exception :**
La loi autorise les particuliers, dans certaines conditions à recourir à une justice privée : l’arbitrage. C’est une procédure en générale moins coûteuse et surtout discrète (procédure confidentielle qui échappe au principe de la publicité), en effet, elle évite d’ébruiter certains litiges dont la connaissance serait préjudiciable aux parties.
Le litige sera alors tranché par des personnes privées, arbitres, choisis par les parties.

Il est interdit de recourir à l’arbitrage dans certains domaines :
- l’état et la capacité des personnes (ex : filiation)
- divorce ou séparation de corps
- contestation intéressant les collectivités publiques et les établissements publics -les choses hors du commerce ou contraire aux bonnes meurs
- les conflits pour lesquels la loi attribue une compétence impérative à une juridiction (RJ et LJ).

En matière de conflits nés à l’occasion du travail, l’arbitrage n’est pas possible lorsqu’il s’agit d’un litige relatif à l’exécution d’un contrat de travail ou d’un licenciement. Par contre, il est possible de recourir à cette procédure s’il s’agit de régler un conflit collectif, notamment en cas de grève (ART L 525-1 du code du travail).
Le choix des arbitres par les parties est libre, sous réserve de respecter le principe d’imparité. Les arbitres devant statuer dans les délais fixés par le contrat. Ils sont tenus de respecter les principes directeurs du procès (procédure contradictoire, droit de la défense, communication des pièces....).

Les arbitres rendent une solution, nommée, sentence arbitrale. Elle a autorité de la chose jugée relativement à la question qu’elle tranche et entre les parties. Elle est considérée comme un acte juridictionnel, mais elle n’a pas par elle-même une force exécutoire. Si l’une des parties ne se soumet pas à la sentence, pour être susceptible d’exécution forcée, elle doit être assortie d’une ordonnance d’exéquatur délivrée à la demande de l’une des parties par le Président du TGI ou du juge de l’exécution.

### B- La justice est un service public

Les principes généraux qui régissent l’organisation judiciaire tendent à garantir aux justiciables un service public qui se veut **gratuit**, **continu**, **égalitaire**, **indépendant** et **fiable**, ces principes souffrant d’un certain nombre d’exceptions.


```raw
- **Égalité de la justice** : Nous somme tous jugés au même règles.
- **Indépendance de la justice vis à vis du justiciable** : Les membres du gouvernements n'ont pas à s'imiser dans une décision de droits. Indépendance des magistrats du siège. Cependant les magistrats du parquets sont directement soumis au ministre de la justice. *L'indépendance vis à vis du justiciable* signifie qu'il n'y a aucune relation entre le magistrat et le partie     
```

#### 1- La gratuité

Le recours à la justice est gratuit : les parties ne rémunèrent pas les juges, qui sont des fonctionnaires. Cependant, les frais engagés pour un procès sont souvent très élevés : il faut rémunérer l’avocat, l’huissier, les experts.

Ces frais sont appelés les dépends et sont en principe à la charge de celui qui perd le procès. L’engagement de ces frais peut constituer une entrave au libre accès à la justice, la loi du 10 juillet 1991 a institué l’aide juridique aux personnes ayant des revenus modestes. L’aide juridictionnelle revêt deux aspects :
- L’aide juridictionnelle qui permet la prise en charge totale ou partielle des frais de procès selon le montant des revenus (droit à l’avocat et commission d’office).
- L’aide à l’accès au droit qui comprend l’aide à la consultation et à l’assistance au cours des procédures juridictionnelles.

#### 2- La continuité
La possibilité d’avoir recours à la justice est permanente. Ainsi, les tribunaux ne sont jamais en vacances et les juges n’ont pas le droit de grève. Par ailleurs, il est possible d’obtenir une décision de justice à n’importe quel moment, en cas d’urgence grâce à la procédure de référé. Afin de prévenir un dommage imminent ou de faire cesser un trouble manifestement contraire à la loi, un magistrat unique (le président du tribunal judiciaire, du tribunal de commerce ou du Conseil des prud’hommes) peut prendre une décision rapide.

#### 3- L’égalité
Tout le monde a accès à la justice. Aucune discrimination n’est admise dans les procédures et les mêmes règles de droit s’appliquent à tous les justiciables.


#### 4- L’indépendance

La justice ne peut être impartiale qu’à condition que les magistrats ne puissent ni recevoir d’ordre de l’Etat, ni subir la pression des justiciables.

*L’indépendance vis à vis de l’Etat*

Elle est assurée par le principe de séparation des fonctions, qui implique que le pouvoir exécutif, ne peut intervenir dans le domaine judiciaire. L’indépendance est absolue en ce qui concerne les magistrats du siège (ceux qui exercent la fonction de juger), ici l’Etat ne peut intervenir dans leur mission, d’une quelconque façon que se soit. Par contre, l’indépendance n’est pas absolue, en ce qui concerne les magistrats du parquet, c’est à dire les représentants de la société, en charge de la conduite de l’action publique (Ministère public). 

Ici, le principe est celui de la subordination hiérarchique et l’article 30 du code de procédure pénale, place le Garde des Sceaux au sommet de la hiérarchie du parquet. De plus, cet article fait de la politique d’action publique, une politique définit par le gouvernement et mise en œuvre par le Ministère public sous l’autorité du Garde des sceaux.


*L’indépendance vis à vis du justiciable*

L’administration de la justice doit garantir à tout justiciable sont droit d’être jugé par un tribunal indépendant et impartial (notion définit par la CEDH). L’impartialité se définit à deux niveaux :

- L’impartialité objective : C’est un principe qui veut que des hommes neufs doivent intervenir à tous les stades du procès. Ceci afin que le juge ne se soit déjà forgé une opinion sur le justiciable et les faits dont il a à juger.
- L’impartialité subjective : C’est le principe selon lequel, le juge ne laisse transparaître dans les décisions qu’il rend, ses opinions personnelles. Cette impartialité subjective est présumée.
La procédure de récusation récusation permet au justiciable de faire respecter le principe et permet au justiciable de demander la récusation d’un magistrat, en vue d’obtenir le respect de l’impartialité objective.

#### 5- La fiabilité

Deux principes tendent à assurer la fiabilité de la justice : la professionnalité des magistrats et la collégialité des juridictions.

En principe, les magistrats sont des juges professionnels. Recrutés par l’Etat, ce sont des fonctionnaires. Par exception toutefois, pour faire juger le litige parles pairs de celui qui est en cause, des non professionnel élus, peuvent rendre la justice (Tribunal de commerce, Conseil de prud’hommes).

En principe, les jugements doivent être rendus par au moins trois juges : le président et deux assesseurs. Par exception, dans un nombre toujours plus grand de juridictions (juge aux affaires familiales, président des tribunaux statuant en référé, juge du contentieux de la protection, tribunal de police ou correctionnel dans certains cas) les jugements sont rendus par un juge unique. Le recours au juge unique s’est développé dans un souci d’économie et de rapidité.

# II- La compétence des juridictions françaises

![Schéma des différentes juridictions](schéma.png "Schéma des différentes juridictions")



Les juridictions françaises obéissent à des règles de compétence précises et sont organisées selon un système pyramidal.

## A- Les règles de compétence
La compétence est l’aptitude d’une juridiction à connaître d’un litige. Il faut distinguer deux ordres de juridictions.


### 1- Les deux ordres de juridictions
La distinction entre l’ordre administratif et l’ordre judiciaire est la conséquence du principe de la séparation des pouvoirs : l’exécutif (l’administration) ne peut donner des ordres au pouvoir judiciaire, et inversement, le pouvoir judiciaire ne saurait sanctionner ni critiquer les actes du pouvoir exécutif.

Ainsi, seule une catégorie particulière de tribunaux, ceux de l’ordre administratif peuvent statuer sur les litiges où la puissance publique est en cause. Les autres litiges relèvent des tribunaux de l’ordre judiciaire.

La délimitation de la compétence entre les deux ordres étant parfois incertaine, c’est le tribunal des conflits qui tranche. Il s’agit d’une juridiction, présidée par le ministre de la justice et composée de trois conseillers de la Cour de cassation et de trois conseillers du Conseil d’Etat.

#### 2- La compétence des tribunaux

Il n’est pas possible qu’un tribunal puisse juger tous les litiges quel qu’en soit l’objet ou le lieu. Les règles de compétence permettent ainsi une bonne administration de la justice en prévoyant :
- la compétence d’attribution : qui détermine la répartition des affaires en fonction de la nature et du montant du litige
- la compétence territoriale : qui fixe parmi les tribunaux de France compétent, le lieu de celui qui doit juger le procès.
Les juridictions judiciaires
Compétence d’attribution

Ces juridictions sont deux types : **civiles** ou **pénales**.

- **Les juridictions civiles connaissent essentiellement des litiges entre particulier.** Le litige est alors résolu par une réparation pécuniaire (dommage et intérêts) destinée à compenser le préjudice causé.
Les juridictions civiles comprennent des tribunaux de droit commun ou tribunaux ordinaires (tribunal judiciaire) et des tribunaux d’exception (tribunal de commerce, conseil des prud’hommes, tribunal paritaire de baux ruraux).
    Tribunal judiciaire : en fonction depuis le 1er janvier 2020, il reprend les anciennes compétences des tribunaux d’instance et de grande instance
    Il est compétent pour toutes les affaires mobilières ou immobilières de droit privé qui ne sont pas réservées à une autre juridiction quel que soit le montant du litige. Cependant, les affaires dont le montant est inférieur ou égal à 5000 € l’appel n’est pas possible devant la cour d’appel (jugement rendu en premier et dernier ressort). Il a une compétence exclusive concernant l’état des personnes (divorce, adoption, protection des personnes majeures etc...).
    Il regroupe en son sein :
    - le juge aux affaires familiales ;
    - le juge du contentieux de la protection : compétent en matière d
    - le pôle social : compétent pour tous les litiges des particuliers concernant, aides sociales (Caf et MSA) ainsi que les litiges financiers avec la CPAM et pôle emploi ;
    - tribunal pour enfant

    Conseil de prud’hommes :
    Il est compétent pour juger des conflits individuels du travail. C’est à dire de tous les conflits entre employeur et salarié relatif à l’exécution d’un contrat de travail. Il statut en premier et dernier ressort pour tout litige inférieur ou égal à 5000€.
    Tribunal de commerce

    Il est compétent pour trancher des litiges nés entre commerçants à l’occasion de leur commerce, ainsi que des litiges relatifs aux actes de commerce passés entre toutes personnes (litiges relatifs à une lettre de change ect...) et des contestations relatives aux sociétés commerciales (leur fonctionnement, leur existence et leur liquidation). Il statut en premier et dernier ressort pour tout litige inférieur ou égal à 5000€.

- Les juridictions pénales ou répressives connaissent des affaires dans lesquelles ont considère que toute la société a subi un dommage (dommage social). La condamnation du délinquant est destinée à réparer le dommage subi par la société et non pas le préjudice subi par la victime (qui elle recevra des dommages et intérêts). La condamnation punit les individus coupables d’infractions et s’effectue par le versement d’une somme d’argent au Trésor public (amende) et / ou par des peines privatives de droit (prison, privation des droits civils tel l’autorité parentale, privation des droits civiques tel l’inéligibilité...).

    Le tribunal de police : Il est compétent pour juger des infractions qualifiées de contravention (punies de peine d’amende seulement montant maxi = 1 000 euros et 1 500 en cas de récidives)
    Le tribunal correctionnel : Il est compétent pour juger des infractions qualifiées de délit (punies d’une peine d’emprisonnement jusqu’à 10 ans)
    La cour d’assises : Elle juge les infractions qualifiées de crime (punies d’une peine pouvant aller jusqu’à perpétuité)
    e surendettement, de protection
    des personnes vulnérables, de baux d’habitation et de crédit à la consommation.
    Compétence territoriale
    Il s’agit de répondre ici à la question de savoir quelle juridiction en France doit-on saisir ou peut-on saisir n’importe quelle juridiction sur le territoire français ?
    Dans une action en justice on distingue :
    - le demandeur à l’action : celui qui est à l’origine de l’action en justice, qui demande la reconnaissance d’un droit, l’exécution d’une prestation ou la réparation d’un dommage ;
    - le défendeur à l’action : celui contre qui l’action est initiée, le débiteur d’une obligation ou la personne qui a causé un préjudice.
    PP : En principe, le tribunal territorialement compétent est celui du domicile du défendeur.
    En matière familiale : tribunal du dernier domicile des époux ou du lieu de résidence des enfants mineurs. En droit des sociétés, lieu du siège social (domicile) de la société.
    Exceptions : Il existe cependant un certain nombre d’exceptions
    - en matière contractuelle (lieu d’exécution de la prestation ou de livraison de la chose),
    - en matière de responsabilité délictuelle (lieu du fait dommageable),
    - en matière de droit du travail (lieu de l’établissement où le contrat de travail est exécuté, sinon, celui du domicile du salarié s’il travail à domicile ou de la résidence de l’employeur), - en matière immobilière (lieu de l’immeuble),
    - en matière de société, lieu d’un établissement de cette dernière dès lors, qu’il est doté d’une personne physique capable d’engager juridiquement celle-ci.
    Les juridictions administratives
    Compétence d’attribution
    On peut distinguer deux types de juridictions :
    Les tribunaux administratifs :
    Ils jugent les affaires qui n’ont pas été retirées à leur compétence par un texte exprès. C’est la juridiction de droit commun.
    Le Conseil d’Etat :
    Il intervient exceptionnellement au premier degré et juge en premier et dernier ressort les recours pour excès de pouvoir contre les décrets, la légalité des mesures individuelles concernant les fonctionnaires...
    Compétence territoriale
    C’est en principe le tribunal du siège de l’autorité administrative en cause qui est compétente, sauf exception. Lorsque le Conseil d’Etat intervient, celui-ci est unique et siège à Paris.

## B - Le système pyramidal
 Afin de garantir aux justiciables une justice équitable, chaque ordre de juridiction est organisé suivant une hiérarchie qui permet l’exercice de voies de recours contre les décisions rendues par une première juridiction, devant des juges nouveaux (c’est-à-dire qui n’ont pas jamais connu de l’affaire).
1- La hiérarchie des juridictions judiciaires
Chaque plaideur bénéficie de la possibilité de faire contrôler le jugement des tribunaux de première instance dont il fait l’objet (en matière civile comme en matière pénale) par une juridiction supérieure. On dit alors que la juridiction du premier degré statue en premier ressort, c’est-à-dire que l’appel est possible devant une juridiction du second degré : la cour d’appel.
Le rôle de la cour d’appel est donc de réexaminer les jugements sur le plan de l’appréciation des faits et de l’application correcte des règles de droit. Pour les affaires civiles de petite importance l’appel n’est pas possible et on dit que la juridiction du premier degré statue en premier et dernier ressort.
Il s’agit :
-des décisions rendues par le tribunal judiciaire dont le montant est inférieur à 5000 € -des décisions du Conseil des prud’hommes lorsque le litige est inférieur à 5000 € -des décisions du tribunal de commerce lorsque le litige est inférieur à 5000 €
La cour d’appel a deux possibilités, elle peut confirmer ou infirmer la décision rendue en première instance.
Outre l’appel, chaque partie dispose d’une autre voie de recours : elle peut se pourvoir en cassation. La cour de cassation, dont le siège est à Paris, est la Cour suprême de l’ordre judiciaire. Elle peut aussi être saisie soit par une partie qui conteste l’arrêt rendu par la cour d’appel, soit par une partie qui conteste une décision d’une juridiction du premier degré rendue en première et dernier ressort.
La cour de cassation ne constitue pas un troisième degré de juridiction. En effet, son rôle n’est pas de rejuger l’affaire mais de veiller à la bonne application du droit : elle ne juge donc que le droit et non les faits.
La cour de cassation a deux possibilités :
-elle peut soit rejeter le pourvoi, si elle estime que la juridiction d’appel a bien appliqué le droit
-soit casser la décision, si elle estime que la juridiction d’appel a mal jugé, deux options s’offrent à la cour de cassation, elle peut alors, soit renvoyer l’affaire devant une juridiction de même niveau que celle dont la décision a été cassée, soit trancher définitivement le litige.
2- La hiérarchie des juridictions administratives
Dans l’ordre administratif, le premier degré de juridiction est constitué par les tribunaux administratifs et exceptionnellement par le Conseil d’Etat.
  7

Puis, le second degré est constitué par les cours administratives d’appel et le Conseil d’Etat, suite à l’appel des jugements rendus par les tribunaux administratifs.
C’est enfin le Conseil d’Etat qui connaît de tous les recours en cassation contre toutes les décisions rendues en dernier ressort par les différentes juridictions administratives.
III- L’organisation des procédures
L’action en justice consiste à saisir la justice pour faire reconnaître un droit qui est contesté.
Elle donne naissance à un procès entre :
- le demandeur qui exerce l’action en vue de la reconnaissance d’un droit
- le défendeur qui conteste la prétention du demandeur (il est celui contre qui l’action est exercée). Le procès ou l’instance doit se dérouler dans le respect des principes généraux de procédure.
A- L’action en justice
1- Les conditions de l’action en justice
L’exercice de l’action en justice nécessite la réunion de trois conditions, l’intérêt à agir, la qualité et la capacité.
L’intérêt à agir :
La personne qui exerce l’action en justice doit justifier d’un intérêt, d’une raison qu’il estime légitime pour pouvoir être à l’initiative du procès. L’intérêt peut être moral ou pécuniaire mais il doit être né et actuel (pas hypothétique ou éventuel). Il doit exister au moment de la demande.
La qualité à agir :
En principe seul peut agir le titulaire du droit, c’est-à-dire la personne qui justifie d’un intérêt direct et personnel.
Ex : en matière de responsabilité civile, seule la victime peut exercer l’action en réparation, c’est-à- dire la personne qui se prévaut d’un dommage direct et personnel.
Sont aussi concernés, les héritiers, les créanciers (seulement au civil et pas au pénal) ou le mandataire de la victime.
Dans certains cas, certaines associations peuvent intenter un procès au nom et pour le compte de ses membres.
La capacité à agir :
C’est l’aptitude à être sujet de droits et d’obligation et à les exercer. Sont privé de la capacité d’exercer leurs droits les mineurs non émancipé et les incapables majeurs.
      8

2- Les différents types d’actions
 Le plus souvent, le droit que l’on vise à faire reconnaître par le juge est contesté : on parle de procédure contentieuse. Il peut cependant arriver que le demandeur n’ai pas d’adversaire : on parle alors de procédure gracieuse, par exemple en matière d’adoption.
B- Le déroulement du procès
La procédure doit se dérouler dans le respect d’un certain nombre de formalités.
1- Les premières phases de la procédure
La demande introductive d’instance : Elle est formée par le demandeur par une assignation du défendeur. L’assignation à comparaître devant le tribunal compétent doit indiquer l’objet de la demande et l’avocat du demandeur.
La mise au rôle : L’affaire est inscrite au « rôle » du tribunal. Un juge est alors désigné pour la suivre la procédure.
La communication des pièces : La procédure est en principe contradictoire : aucun acte ne peut être fait, aucun document ne peut être produit, aucun argument ne peut être développé devant le juge sans que l’autre partie en ait connaissance. Les avocats se communiquent leurs plaidoiries ainsi que les documents et preuves à l’appui de leurs prétentions.
2- L’audience
En principe, les débats et les jugements ont lieu en audience publique (la publicité des débats est un gage d’impartialité de la justice). Ainsi, le public est en quelque sorte le témoins de la régularité du procès.
L’audience est orale (plaidoiries à l’audience) et écrite (les conclusions, c’est-à-dire les arguments des avocats, sont transmises à l’adversaire et au tribunal).
Le rôle du juge dépend du système dans lequel on se trouve : accusatoire ou inquisitoire.
Dans le système accusatoire, se sont les parties qui dirigent le procès et la justice est saisie dès lors qu’une demande est intentée. Dans un système inquisitoire, c’est le juge qui dirige le procès. En France, le système st hybride et diffère en fonction du domaine dans lequel on se trouve.
Procédure civile :
Elle s’applique en matière civile, commerciale et sociale devant les juridictions l’ordre judiciaire. La procédure est accusatoire, le juge doit arbitrer entre les preuves qui lui sont fournies par les parties. Elle est publique et contradictoire, demandeur et défendeur se font mutuellement connaître leurs prétentions.
       9

Procédure pénale :
 Il faut distinguer :
-Dans un premier temps, la procédure est dite inquisitoire, elle est écrite et secrète. L’initiative de la poursuite est en principe réservée aux représentants de la société qui, par le biais de la police judiciaire, du parquet et des magistrats instructeurs, recherchent et rassemblent des preuves (le charge de la preuve pèse sur le ministère public = le parquet).
-Au moment du jugement, la procédure devient orale et publique. Le juge forge son intime conviction en fonction des éléments de preuve présentés par les parties, il peut aussi demander de nouvelles preuves. La procédure est contradictoire, l’accusé se défendant librement contre le représentant de la société (ministère public, procureur) qui l’accuse et le cas échéant, la victime qui lui demande des dommages et intérêts.
Les différentes actions devant les juridictions pénales :
-L’action publique : c’est l’action qui est menée par le ministère public et qui tend à la condamnation du délinquant, par le prononcé d’une peine (amende ou emprisonnement).
-L’action civile : c’est l’action qui appartient à la victime et tend à la réparation du préjudice causé par l’infraction, par le versement de dommages et intérêts. En France, la victime dispose d’une option procédurale, elle peut en effet, porter son action soit devant les juridictions civiles ou alors devant les juridictions pénales, elle devient alors, l’accessoire de l’action publique.
Le procès pénal débute par le déclenchement de l’action publique par le ministère public, dont il a le monopole d’exercice. Mais la victime peut forcer au déclenchement de l’action publique et lutter contre l’inertie du ministère public, en portant plainte avec constitution de partie civile.
La procédure administrative :
Il est possible de demander au juge administratif, soit d’annuler une décision administrative, soit d’indemniser un préjudice. La procédure est alors écrite, contradictoire et inquisitoire, le juge administratif joue un rôle essentiel.
3- Le jugement
L’issue du procès est le prononcé d’une décision, qui présente deux caractères :
- La force exécutoire : les décisions judiciaires sont obligatoires et leur bénéficiaire peut en obtenir l’exécution grâce au recours de la force publique.
L’autorité de la chose jugée : ce qui a été jugé ne peut l’être à nouveau devant la même juridiction pour la même cause et les mêmes parties. Toutefois, les parties disposent de voies de recours.