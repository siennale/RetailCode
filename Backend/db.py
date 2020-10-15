import psycopg2

def connect_db():
    try:
        # TODO: Move it to env variable 
        connection = psycopg2.connect(user = "postgres",
                                    password = "test",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "postgres")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
        return cursor

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)





# TODO -----------------------------------------------------
def get_product_price_by_barcode(barcode, cursor):
    # return the price 


def initialize_db(cursor):
    # Creates all tables with the required headers. 

# Function for putting a entry in db. Payload is json form data e.g. { product_barcode : [ 12344, 123231, 123213]}
def set_tranasction(cursor, payload):
    # add it to the Transaction table. 
    # Also reduce the quantity from the Products table. 

# this is the whole puchase. Payload is e.g. { total_sale_price: 89, product_barcode :[12321, 12312, 12321]}
def set_sale(cursor, payload):
    # add it to the sales table and then call set_transaction to add a product sale. 

# Orders is e.g. Json { Product_barcode: 34, order_place: "costco", order_quantity: 34, product_purchase_price: 2}
def set_orders(cursor, orders):
















# finally:
#     #closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")W