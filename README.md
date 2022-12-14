# Taichi Bodytracking project
## From IMT ATLANTIQUE students 

In this readme, I will explain how the database is arranged.
I'll present what is in it and how to access it efficiently.

### Raw data
Firstly, the raw data in csv and fbx format are stocked in the raw_csv and raw_fbx files.
These are files directly exported from the software Motive using the Optitrack tracking system.

### Usable data
All the cleaned data is stocked in the "data" file.
There is also a file gravity center that contains all of the data concerning the gravity center for some other specific use.
It's a csv with lines corresponding to the time series and the cols corresponding to each degree of freedom for each body part of the avatar.

The col_info csv give us all the information about what column is what kind of data.

[col_info.csv](https://github.com/perroquent/Taichi/files/10158137/col_info.csv)

### Classification 

Each data file is named this way : 
Id_data.csv

And the caracteristics about each data file are in the file info.csv
It contains : 
- the id 
- the praticant 
- the praticant level
- the date of tracking 


#### Praticant level 
They are ranked in 5 differents categories 
- Beginner
- Amateur
- Intermediate
- Competent
- Master

