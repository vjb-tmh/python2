#!/usr/bin/python

import sqlite3
import json
import csv
import xml.etree.ElementTree as ET
from multiprocessing import Process,Queue,Pipe

'''
Browse the database using the browser from http://sqlitebrowser.org/
'''

def get_table_names():
    '''
    Get table column names.
    @param con: the db connection
    '''
    curs = con.cursor()
    curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(curs.fetchall())
    print

def get_column_names(table_name):
    '''
    Get table column names.
    @param table_name: the name of the table
    '''
    curs = con.cursor()
    query = 'SELECT * FROM ' + table_name + ';'
    columns = curs.execute(query)
    columns = [description[0] for description in columns.description]
    print(columns)
    print

def select_all_agents():
    '''
    Query all rows in the agents table
    @param con: the Connection object
    '''
    curs = con.cursor()
    curs.execute("SELECT * FROM agents;")

    rows = curs.fetchall()

    for row in rows:
        print(row)

def select_all_listings():
    '''
    Query all rows in the listings table
    @param con: the Connection object
    '''
    curs = con.cursor()
    curs.execute("SELECT * FROM listings;")

    rows = curs.fetchall()

    for row in rows:
        print(row)

def select_all_offices():
    '''
    Query all rows in the offices table
    @param con: the Connection object
    '''
    curs = con.cursor()
    curs.execute("SELECT * FROM offices;")

    rows = curs.fetchall()

    for row in rows:
        print(row)

def print_list_of_dicts(d):
    '''
    Print a list of dicts
    '''
    for a in d:
        for k,v in a.iteritems():
            print k + ' >> ' + v

def parse_json_data():
    """
    Parse json data
    listings = list of dicts
    listings[i] = dict for single listing
    @return: list of listings
    """
    listings = json.load(open('data/mls002/feed.json'))

    # extract listings
    data = []
    single_listing = []
    for listing in listings:
        single_listing = []
        single_listing.append(None)
        single_listing.append(listing['street_address'])
        single_listing.append(listing['city'])
        single_listing.append(listing['state'])
        single_listing.append(listing['zip'])
        single_listing.append(listing['mls_number'])
        single_listing.append(listing['price'])
        single_listing.append(listing['status'])
        single_listing.append(listing['type'])
        single_listing.append(listing['description'])
        single_listing.append(listing['agent_code'])
        single_listing.append(listing['office_code'])
        data.append(list(single_listing))

    insert_listings(data)

def parse_xml_data():
    '''
    Parse xml data
    '''
    # parse xml tree
    tree = ET.parse('data/mls001/data.xml')

    # get the root of the tree, e.g. listings
    root = tree.getroot()

    # find each listing in the tree
    # create list of lists holding all listings
    data = []
    single_listing = []
    for listing in root.findall('listing'):
        single_listing = []
        single_listing.append(None)
        single_listing.append(listing.find('address').find('street').text)
        single_listing.append(listing.find('address').find('city').text)
        single_listing.append(listing.find('address').find('state').text)
        single_listing.append(listing.find('address').find('zip').text)
        single_listing.append(listing.find('mls_number').text)
        single_listing.append(listing.find('price').text)
        single_listing.append(listing.find('status').text)
        single_listing.append(listing.find('type').text)
        single_listing.append(listing.find('description').text)
        single_listing.append(listing.find('agent').find('code').text)
        single_listing.append(listing.find('broker').find('code').text)
        data.append(list(single_listing))

    insert_listings(data)

def parse_csv_data():
    '''
    Parse csv data
    '''
    # get offices csv data
    data = []
    with open('data/mls003/offices.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        cnt = 0
        for row in reader:
            if(cnt == 0):
                cnt += 1
                continue
            row.insert(0,None)
            data.append(list(row))

    insert_offices(data)

    # get agents csv data
    data = []
    with open('data/mls003/agents.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        cnt = 0
        for row in reader:
            if(cnt == 0):
                cnt += 1
                continue
            row.pop(2) # remove data for second column
            row.insert(0,None)
            data.append(list(row))

    insert_agents(data)

    # get listings csv data
    data = []
    with open('data/mls003/listings.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        cnt = 0
        for row in reader:
            if(cnt == 0):
                cnt += 1
                continue
            tmp = row.pop(0)
            row.insert(4,tmp)
            tmp = row.pop(-1)
            row.insert(8,tmp)
            row.insert(0,None)
            data.append(list(row))

    insert_listings(data)

def insert_agents(data):
    '''
    insert agents into db
    '''
    curs = con.cursor()
    query = "insert into agents values (?,?,?,?,?,?,?)"
    for agent in data:
        curs.execute(query,tuple(agent))
    #con.commit()

def insert_offices(data):
    '''
    insert offices into db
    '''
    curs = con.cursor()
    query = "insert into offices values (?,?,?,?,?,?,?)"
    for office in data:
        curs.execute(query,tuple(office))
    #con.commit()

def insert_listings(data):
    '''
    insert listings into db
    '''
    curs = con.cursor()
    query = "insert into listings values (?,?,?,?,?,?,?,?,?,?,?,?)"
    for listing in data:
        curs.execute(query,tuple(listing))
    #con.commit()

if __name__ == "__main__":

    # get db connection
    con = sqlite3.connect('data/db/homes.db')

    # get table names
    get_table_names()

    # parse listings data
    parse_json_data()

    # parse listings data
    parse_xml_data()

    # parse offices, agents, and listings data
    parse_csv_data()

    # check db contents
    select_all_agents()
    select_all_offices()
    select_all_listings()

    con.close()
