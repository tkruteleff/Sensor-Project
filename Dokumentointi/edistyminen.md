## Raspberry projekti 3: tilan/ruokalajonon status 

#### Raspberry Pi
Raspian Lite asennettu
Yhteys työasemasta Puttylla
Staattinen IP
SSH yhteys Tietokantaan

#### Python koodi
Hakee raspi dataa ja lisää sen kantaan

#### Linux Xubuntu VM (Tietokanta)
Asennettu Cloud Platformiin Xubuntu
Putty SSH yhteys toimii
Tietokanta luotu


#### Tarvikkeet
Tilattu Verkkokaupasta:
Raspberry Pi 8.0 Mpix v2 kameramoduuli Raspberry Pi:lle
HC-SR04 ultraäänisensori Raspberry Pi sekä Arduino ‐alustoille

Tarvitaan transistoreita (Kaapo hankkii?)



## Update 5.4.2017

#### Tarvikkeet
Kaikki osat saatu:

#### Distance:
Nykyisellä koodilla kahden mittarin järjestelmällä vain lyhyempi matka printataan.

## Update 12.4.2017

#### RasPi
Ratkaistu: Oikea Sensori mittaa aina saman arvon
 
Sensorit toimivat yksittäin, mutta ei yhdessä -> Toimiiiiiii!!!!!

#### PHP
Prototyyppi: Pystyy hakemaan dataa kannasta ja näyttää ne .php sivulla
 
Tekeillä: Datan lajittelu graaphiseen muotoon .php:llä

## Update 19.4.2017

#### RasPi .py
Koodi ei pysty tulostamaan haluttuja arvoja "1" ja "2" oikeissa parametreissä -> tarvitaan ratkaisu

#### PHP
Näyttää datan järkevässä aikajanassa.
Testidatan puutteessa näyttö on erittäin tarkkaa, aikarajoituksia ym. tulee lisätä


## Update 24.4.2017

#### RasPi .py
Koodi ei saa raakoja arvoja importista, vain metodit toimivat
-> Ratkaisu: Kutsutaan metodia arvon sijaan

Kantaan saadaan molempia 'state' arvoja, 1 ja 2.
-> Ongelma: Vasen sensori saa vääriä arvoja (~180cm) FIXED

Ranget oikein

#### PHP
Rajoitus kymmeneen uusimpaan tapahtumaan. 
-> Ongelma: Data on "väärinpäin" eli vasemmalta oikealle luettaessa uusin on ensin. Tarkoitus saada rajoitus n. 15 tapahtumaan(tai useampaan) ja saada vanhin ensimmäiseksi aikajanalle. 


## Update 25.4.2017
#### Revelation
Muutos kantaan: Statesta muutetaan count, jonka idea on kertoa suoraan senhetkinen paikalla olijoiden määrä. Raspin python koodi tarkastaa kumpi sensoreista aktivoituu ensin ja lisää/vähentää kokonaismäärästä, joka pusketaan kantaan.

#### Tilanne: 
Python koodi saadaan tukemaan ideaa, mutta php graphin SQL lausetta ei saada oikeaan muotoon. (Jos "count(*) as state" muutetaan, graph menee rikki.

#### Progress
SQL lause toimii, näyttää sarakkeen sisällön. ( Tällähetkellä vielä state) Kantamuutosta ei tehty.
