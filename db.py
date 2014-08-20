#!/usr/bin/python --

import apsw

connection = apsw.Connection("cookbook1.db3")
cursor = connection.cursor()

#sql = "CREATE TABLE recipes (pkiD INTEGER PRIMARY KEY, name TEXT, servings TEXT, source TEXT)"
#cursor.execute(sql)

#sql = "CREATE TABLE Instructions (pkID INTEGER PRIMARY KEY, instructions TEXT, recipeID NUMERIC)"
#cursor.execute(sql)

#sql = "CREATE TABLE Ingredients (pkID INTEGER PRIMARY KEY, ingredients TEXT, recipeID NUMERIC)"
#cursor.execute(sql)

sql = 'INSERT INTO Recipes (name, serves, source) VALUES ("Spanish Rice", 4, "Greg Walters")'

