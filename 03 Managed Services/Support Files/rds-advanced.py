#*********************************************************************************************************************
# Author - Nirmallya Mukherjee
# This script will connect to a MySQL DB using multiple driver options & use Redis cache for optimization
# Need to install redis module as follows
#       sudo pip install redis
# To check the keys in redis use ->
#       redis-cli keys '*'
#*********************************************************************************************************************

import mysql.connector
import pickle
import redis

#Example elasticache end point can be redis.scsdmx.ng.0001.usw2.cache.amazonaws.com
redis_host = 'localhost'
hostname = 'localhost'

username = 'root'
password = 'password'
database = 'employees'


class Order:
    def __init__(self, orderid, userid, shipping, email):
        self.orderid = orderid
        self.userid = userid
        self.shipping = shipping
        self.email =email
        self.tostring()
    def tostring(self):
        print " Order is {0} {1} {2} {3}".format(self.orderid, self.userid, self.shipping, self.email)



def getAllOrders() :
    print "\n\nUsing mysql.connector"
    print "---------------------"
    conn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT OrderID, OrderUserID, OrderShipName, OrderEmail FROM orders")
    for orderid, userid, shipping, email in cur.fetchall() :
        order_obj = Order(orderid, userid, shipping, email)
    cur.close()
    conn.close()



def getOrder(order_id):
    print "\nGetting the order", order_id
    red = redis.StrictRedis(host=redis_host, port=6379, db=0)
    red_obj = red.get(order_id)
    if red_obj != None:
        print "Object found in cache, not looking in DB"
        #Deserialize the object coming from Redis
        order_obj = pickle.loads(red_obj)
        order_obj.tostring()
    else:
        print "No key found in redis, going to database to take a look"
        conn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
        cur = conn.cursor()
        cur.execute("SELECT OrderID, OrderUserID, OrderShipName, OrderEmail FROM orders where OrderID='%s'" % (order_id))
        for orderid, userid, shipping, email in cur :
            order_obj = Order(orderid, userid, shipping, email)
            #Serialize the object
            ser_obj = pickle.dumps(order_obj)
            red.set(order_id, ser_obj)
            print " Order fetched from DB and pushed to redis"
        cur.close()
        conn.close()



def main() :
    getAllOrders()
    getOrder('ord00001')


main()
