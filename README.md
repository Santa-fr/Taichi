# Taichi Bodytracking project
### From IMT ATLANTIQUE students 

In this readme, I will explain how the database is arranged.
I'll present what is in it and how to access it efficiently.

## Raw data
Firstly, the raw data in csv and fbx format are stocked in the raw_csv and raw_fbx files.
These are files directly exported from the software Motive using the Optitrack tracking system.

## Usable data
All the cleaned data is stocked in the "data" file.
There is also a file gravity center that contains all of the data concerning the gravity center for some other specific use.
It's a csv with lines corresponding to the time series and the cols corresponding to each degree of freedom for each body part of the avatar.

The col_info csv give us all the information about what column is what kind of data.

[col_info.csv](https://github.com/perroquent/Taichi/files/10158137/col_info.csv)

## Classification 

Each data file is named this way : 
Id_data.csv

And the caracteristics about each data file are in the file info.csv
It contains : 
- the id 
- the praticant 
- the praticant level
- the movement sequence id
- the date of tracking 


### Praticant level 
They are ranked in 5 differents categories 
- Beginner
- Amateur
- Intermediate
- Competent
- Master

### Movements
Each movements sequences are several Tai-Chi movements from Chen 31

First sequence : Id = 1
1. Jin Gang Dao Dui (La foudre pulvérise)
2. Lan Za Yi (Soutenir le pan du vêtement)
3. Liu Feng Si Bi (Fermeture apparente)
4. Dan Bian (Simple fouet)

Second sequence : Id = 2
1. Bai Lan Tui (Un coup de pied en lotus)
2. Qiu Di Long (Dragon au sol)
3. Jin Ji Du Li (Le coq se tient sur une patte)

Third sequence : Id = 3
1. Pai Jiao (Taper le pied)
2. Yu Nu Chuan Shuo (La fille de jade tisse et lance la navette)
3. Ma Bu Shuang Ya Zhou (un coup de coude)

# Some more movements will be added SOON ! 
# The database will be finished on January.
