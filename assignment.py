# def make_order(order):
import pandas as pd

pd.read_csv('INPUT FILE')

database={}  #store list of books and each book has 2 dictionarues with key values buy and sell

def order_ADDING(order):
    order_book=order.book
    order_op=order.operation
    order_price=order.price
    order_vol=order.volume
    order_id=order.orderID
    if order_op=='BUY':
        try:
            K=database[order_book]['SELL']
            if K[0].price>order_price:
                database[order_book]['BUY'].insert[order]

            else:
                if K[0].volume>order_vol:
                    K[0].volume=K[0].volume-order_vol
                else:
                    order_dlt(K[0])
                    order.volume= order_vol-K[0].volume
                    order_ADDING(order)
        except:
            database[order_book]={'BUY':{order}, 'SELL':{}}


    if order_op=='SELL':
        try:
            K=database[order_book]['BUY']
            if K[0].price>order_price:
                database[order_book]['SELL'].insert[order]

            else:
                if K[0].volume>order_vol:
                    K[0].volume=K[0].volume-order_vol
                else:
                    order.dlt(K[0])
                    order.volume= order_vol-K[0].volume
                    order_ADDING(order)
        except:
            database[order_book]={'SELL':{order}, 'BUY':{}}
    


def order_dlt(order):