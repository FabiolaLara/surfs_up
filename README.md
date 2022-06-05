# surfs_up
Using SQLite, SQLAlquemy, Flask and Visual COde

# Overview of the analysis:
This analysis is related to filter data bases that are located in the SQLite format, then using our jupyter notebook we will be importing the sqlalchemy library which provided the resources to import values from de SQLite data base.

Our filters will be: Filtering values contained in the columns: `measurement`, `station` and 'tobs' contained in the hawaii.sqlite Data Base.
This info will be display as a list and then as a Data Frame.

Finally using the `describe()` fuction will show stats values for the information filtered before.

# Results: 
Mentioning three of the major important point in these analysis deliverables:
1. It is very important to impot all the dependencies in order to retrieve data from this SQLite Data Base, those are the mention below:
  + import sqlalchemy
  + from sqlalchemy.ext.automap import automap_base
  + from sqlalchemy.orm import Session
  + from sqlalchemy import create_engine, func
  + from sqlalchemy import extract

2. The second point to make this Date Base attend to our code is to create some variables and stablished connection links to retrieve data.

- To set up the ability to query a SQLite database
  + engine = create_engine("sqlite:///hawaii.sqlite")
  
- reflect an existing database into a new model
  + Base = automap_base()
  
- reflect the tables
  + Base.prepare(engine, reflect=True)

- Save references to each table
  + Measurement = Base.classes.measurement
  + Station = Base.classes.station

- To convert into a Data Frame
  + import pandas as pd

# Summary:

We can say that this way to engine Data Bases is very useful and the commands for this are no so difficult at all, but also this way to be into python environment and running the code in each line and not to be selecting a piece of a snippet code and running like in PgAdmin for example makes to retrieve data easier and faster. 

These SQLite Data Bases are very managable as they are treated as objects. We can query them in many different ways, lets show two additional queries to show data.



Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
