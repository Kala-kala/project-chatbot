import sqlite3


conn = sqlite3.connect('ntlk.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS functionality(things TEXT, answer TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS how(name TEXT, area TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS location(monument TEXT, location TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS what(name TEXT, description TEXT)")


def data_entry():
    c.execute("INSERT INTO functionality VALUES('DCmotors', 'connected to source')")
    c.execute("INSERT INTO functionality VALUES('Helicopter', 'change of power')")
    c.execute("INSERT INTO functionality VALUES('Calculator', 'performing calculatins')")
    c.execute("INSERT INTO functionality VALUES('Video Games', 'Through chips')")

def data_entry1():
	c.execute("INSERT INTO location VALUES('Taj Mahal', 'Agra')")
	c.execute("INSERT INTO location VALUES('India Gate', 'Delhi')")
	c.execute("INSERT INTO location VALUES('Qutub Minar', 'Delhi')")
	c.execute("INSERT INTO location VALUES('Eifel Tower', 'Paris')")

def data_entry2(): 
	c.execute("INSERT INTO what VALUES('Cricket', 'Game')")
	c.execute("INSERT INTO what VALUES('Networking', 'Technique')")
	c.execute("INSERT INTO what VALUES('Apple', 'fruit')")
	c.execute("INSERT INTO what VALUES('Ladyfinger', 'veggie')")

def data_entry3(): 
	c.execute("INSERT INTO how VALUES('produced', 'Brazil')")
	c.execute("INSERT INTO how VALUES('exported', 'India')")
	c.execute("INSERT INTO how VALUES('supplied', 'Brazil')")
	c.execute("INSERT INTO how VALUES('bought', 'London')")
    

	conn.commit()
	c.close()
	conn.close()



create_table()
data_entry()
data_entry1()
data_entry2()
data_entry3()
c.close
conn.close()
