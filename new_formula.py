# All the functions needed to print out the orderbook
import bisect
import sys
import numpy as np

# The key for bid_dict is the Price Level
# The value is a tuple
# The first element of the tuple is the number of elements traded under that 
# price
# The second element of the tuple is a dictionary, with the key being the order_id,
# and the value being the quantity of a certain order_id

# example
# bid_dict = {"100": (5, {"1" : 2, "2" : 3})}
# this data structure means at a price of 100, there are 5 unfilled order
# 2 of them come from order_id "1", and 3 of them come from order_id "3"
# bid_price_list saves all the bid price in the order book


# A sample order book looks like this (will be defined under a class later)
# class OrderBook:
#  def __init__(self):
#  self.bid_dict = {}
#  self.ask_dict = {}
#  self.bid_price_list = []
#  self.ask_price_list = []



class NonPositiveQuantity(Exception):
    pass

class InvalidSide(Exception):
    pass

class NonPositivePrice(Exception):
    pass

class IDAlreadyAppeared(Exception):
    pass

class OrderAlreadyChanged(Exception):
    pass


class Open_Order:
    def __init__(self, id, quantity, side, price):
        self.id = id
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price must be positive")
        if quantity > 0:
            self.quantity = quantity
        else:
            raise NonPositiveQuantity("Quantity Must Be Positive!")
        if side == "buy":
            self.side = side
        elif side == "sell":
            self.side = side
        else:
            raise InvalidSide("Side Must Be Either Buy or Sell!")

class Done_Order:
    def __init__(self, id, quantity, side, price):
        self.id = id
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price must be positive")
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise NonPositiveQuantity("Quantity Must Be Nonegative!")
        if side == "buy":
            self.side = side
        elif side == "sell":
            self.side = side
        else:
            raise InvalidSide("Side Must Be Either Buy or Sell!")

class Match_Order:
    def __init__(self, maker_id, taker_id, quantity, side, price):
        self.maker_id = maker_id
        self.taker_id = taker_id
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price must be positive")
        if quantity > 0:
            self.quantity = quantity
        else: 
            raise NonPositiveQuantity("Quantity Must Be Positive!")
        if side == "buy":
            self.side = side
        elif side == "sell":
            self.side = side
        else:
            raise InvalidSide("Maker Side Must Be Either Buy or Sell!")

class STP_Order:
    # a type of change order, which only changes the size
    def __init__(self, id, side, new_size, old_size, price):
        self.id = id
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price must be positive")
        if old_size <= 0:
            raise NonPositiveQuantity("Quantity Must Be Positive!")
        elif new_size < 0:
            raise NonPositiveQuantity("Quantity Must Be Non-negative!")
        else:
            self.old_size = old_size
            self.new_size = new_size
        if side == "buy":
            self.side = side
        elif side == "sell":
            self.side = side
        else:
            raise InvalidSide("Maker Side Must Be Either Buy or Sell!")

class Modify_Order:
    # a type of change order, which can change size and price simultaneously
    def __init__(self, id, side, new_size, old_size, new_price, old_price):
        self.id = id
        if (new_price <= 0) or (old_price <=0):
            raise NonPositivePrice("Price must be positive")
        else:
            self.old_price = old_price
            self.new_price = new_price
        if old_size <= 0:
            raise NonPositiveQuantity("Quantity Must Be Positive!")
        elif new_size < 0:
            raise NonPositiveQuantity("Quantity Must Be Non-negative!")
        else:
            self.old_size = old_size
            self.new_size = new_size
        if side == "buy":
            self.side = side
        elif side == "sell":
            self.side = side
        else:
            raise InvalidSide("Maker Side Must Be Either Buy or Sell!")

# remove a price from our data structure if the price falls to zero, check negative quantity
def check_remove_price(dict, price_list, price):
    if dict[price][0] <= 0:
        # if the quantity drops to nonpositive, delete thr price info
        del dict[price]
        price_list.remove(price)

# insert a open order into our data structure
def o_insert(dict, price_list, order:Open_Order):
    if order.price in dict:
        # The price level has already appeared in the order book before
        if order.id in dict[order.price][1]:
            raise IDAlreadyAppeared("Open Error: Order ID has already appeared before\n")
        else:
            dict[order.price][1][order.id] = order.quantity
            dict[order.price][0] += order.quantity  
    else:
        # The price level has never appeared in the order book before
        dict[order.price] = [order.quantity, {order.id: order.quantity}] 
        bisect.insort(price_list, order.price)

# insert an done order into our data structure
def d_insert(dict, price_list, order: Done_Order):
    if order.price not in dict:
        return # the price may appear before we start to document the order book, ignore this order
    else:
        # The price level has not appeared in the order book before
        if order.id not in dict[order.price][1]:
            return
        else:
            # delete done order from total quantity
            dict[order.price][0] -= dict[order.price][1][order.id]
            # delete order from order book
            del dict[order.price][1][order.id]

            # remove price info if quantity drops to nonpositive
            check_remove_price(dict, price_list, order.price)

# insert a match order into our data structure
def m_insert(dict, price_list, order: Match_Order):
    if order.price not in dict:
        # The price level has not appeared in the order book before
        return
    else:
        if order.maker_id not in dict[order.price][1]:
            # Maker_id should be in the orderbook
            return
        else:
            remaining_size = dict[order.price][1][order.maker_id]
            if (remaining_size > order.quantity):
                # taker does not fully fill maker order
                dict[order.price][1][order.maker_id] -= order.quantity
                dict[order.price][0] -= order.quantity
            elif (remaining_size <= order.quantity):
                dict[order.price][0] -= remaining_size
                del dict[order.price][1][order.maker_id]

                # remove price info if quantity drops to nonpositive
                check_remove_price(dict, price_list, order.price)

# insert an stp change order into our data structure
def stp_insert(dict, price_list, order:STP_Order):
    if order.price not in dict:
        # The price level has not appeared in the order book before
        return
    else:
        if (order.id not in dict[order.price][1]):
            return
        else: 
            if (order.new_size == 0):
                dict[order.price][0] -= order.old_size
                del dict[order.price][1][order.id]
                        
                # remove price info if quantity drops to zero, check negativity
                check_remove_price(dict, price_list, order.price)

            else:
                # update the total quantity and the new quantity of the order
                dict[order.price][0] = dict[order.price][0] - order.old_size + order.new_size
                dict[order.price][1][order.id] = order.new_size

# insert an modify change order into our data structure
def modify_insert(dict, price_list, order: Modify_Order):
    if order.old_price not in dict:
        # The price level has not appeared in the order book before
        return
    if order.id not in dict[order.old_price][1]:
        return
    if order.old_price == order.new_price:
        # only change size if price doesn't change
        dict[order.old_price][0] = dict[order.old_price][0] - order.old_size + order.new_size
        dict[order.old_price][1][order.id] = order.new_size
    else:
        if (order.new_price in dict):
            if (order.id in dict[order.new_price][1]):
                raise OrderAlreadyChanged("Modify_Order Warning: Order has already been changed\n")
            else:
                # update 
                dict[order.new_price][1][order.id] = order.new_size
                dict[order.new_price][0] += order.new_size
                dict[order.old_price][0] -= order.old_size
                del dict[order.old_price][1][order.id]

                # remove price info if quantity drops to nonpositive
                check_remove_price(dict, price_list, order.old_price)
        else:
            # new price not appeared before
            dict[order.new_price] = [order.new_size, {order.id: order.new_size}]
            bisect.insort(price_list, order.new_price)

            dict[order.old_price][0] -= order.old_size
            del dict[order.old_price][1][order.id]

            # remove price info if quantity drops to nonpositive
            check_remove_price(dict, price_list, order.old_price)

class OrderBook:
    def __init__(self):
        self.bid_dict = {}
        self.ask_dict = {}
        self.bid_price_list = []
        self.ask_price_list = []

    # insert an open order into the order book
    def open_insert(self, order: Open_Order):
        if order.side == "buy":
            o_insert(self.bid_dict, self.bid_price_list, order)
        else:
            o_insert(self.ask_dict, self.ask_price_list, order)
    
    # insert a done order into the order book
    def done_insert(self, order: Done_Order):
        if order.side == "buy":
            d_insert(self.bid_dict, self.bid_price_list, order)
        else:
            d_insert(self.ask_dict, self.ask_price_list, order)
    
    # insert a match order into the order book
    def match_insert(self, order: Match_Order):
        if order.side == "buy":
            m_insert(self.bid_dict, self.bid_price_list, order)
        else:
            m_insert(self.ask_dict, self.ask_price_list, order)

    # insert a STP Change order into the order book
    def STP_insert(self, order: STP_Order):
        if order.side == "buy":
            stp_insert(self.bid_dict, self.bid_price_list, order)
        else:
            stp_insert(self.ask_dict, self.ask_price_list, order)

    # insert a Modify Change order into the order book
    def Modify_insert(self, order: Modify_Order):
        if order.side == "buy":
            modify_insert(self.bid_dict, self.bid_price_list, order)
        else:
            modify_insert(self.ask_dict, self.ask_price_list, order)

    #check Locked Error
    def LockedError(self):
        if (len(self.ask_price_list) > 0) and (len(self.bid_price_list) > 0):
            if self.bid_price_list[-1] >= self.ask_price_list[0]:
                sys.exit("This is a Locked Error\n")

# read order into order book
def read_order (order: dict, Coinbase_Orderbook: OrderBook):
    if order["type"] == "open":
        data = Open_Order(order["order_id"], float(order["remaining_size"]), order["side"],float(order["price"]))
        Coinbase_Orderbook.open_insert(data)
    elif order["type"] == "done":
        data = Done_Order(order["order_id"], float(order["remaining_size"]), order["side"], float(order["price"]))
        Coinbase_Orderbook.done_insert(data)
    elif order["type"] == "match":
        data = Match_Order(order["maker_order_id"], order["taker_order_id"], float(order["size"]), order["side"], float(order["price"]))
        Coinbase_Orderbook.match_insert(data)
    elif order["type"] == "change":
        if order["reason"] == "STP":
            data = STP_Order(order["order_id"], order["side"], float(order["new_size"]), float(order["old_size"]), float(order['price']))
            Coinbase_Orderbook.STP_insert(data)
        else:
            data = Modify_Order(order["order_id"], order["side"], float(order["new_size"]), float(order["old_size"]), float(order["new_price"]), float(order["old_price"]))
            Coinbase_Orderbook.Modify_insert(data)
    Coinbase_Orderbook.LockedError()

# print out the orderbook
def show_orderbook (book: OrderBook):
    len_ask = len(book.ask_price_list)
    ask_show_len = min(5, len_ask)
    for i in range(ask_show_len-1, -1, -1):
        # find the lowest ask price
        price = book.ask_price_list[i]
        print(str("{:.5f}".format(book.ask_dict[price][0])) + " @ " + str("{:.2f}".format(price)))
    print("-------------------")
    len_bid = len(book.bid_price_list)
    bid_show_len = min(5, len_bid)
    for i in range(bid_show_len):
        # find the highest bid price
        price = book.bid_price_list[len_bid -1 - i]
        print(str("{:.5f}".format(book.bid_dict[price][0])) + " @ " + str("{:.2f}".format(price)))
    print("\n")
