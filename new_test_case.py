import new_formula

coinbase_orderbook = new_formula.OrderBook()
def print_orderbook(coinbase_orderbook):
    print(coinbase_orderbook.bid_dict)
    print(coinbase_orderbook.bid_price_list)
    print(coinbase_orderbook.ask_dict)
    print(coinbase_orderbook.ask_price_list)


# order_1 to order_14 are used to check the correctness of Open
order_1 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 1,
  "order_id": "0x1",
  "price": "200.2",
  "remaining_size": "1.00",
  "side": "sell"
}

new_formula.read_order(order_1, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_2 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x2",
  "price": "50.2",
  "remaining_size": "3.00",
  "side": "buy"
}

new_formula.read_order(order_2, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_3 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x3",
  "price": "10.2",
  "remaining_size": "1.02",
  "side": "buy"
}

new_formula.read_order(order_3, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_4 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x4",
  "price": "10.2",
  "remaining_size": "12",
  "side": "buy"
}

new_formula.read_order(order_4, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_5 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x5",
  "price": "200.2",
  "remaining_size": "3.5",
  "side": "sell"
}
new_formula.read_order(order_5, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)


order_6 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x6",
  "price": "2000.2",
  "remaining_size": "0.05",
  "side": "sell"
}
new_formula.read_order(order_6, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_7 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x7",
  "price": "315.2",
  "remaining_size": "1",
  "side": "sell"
}
new_formula.read_order(order_7, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_8 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x8",
  "price": "415.2",
  "remaining_size": "1",
  "side": "sell"
}
new_formula.read_order(order_8, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_9 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x9",
  "price": "700.2",
  "remaining_size": "2",
  "side": "sell"
}
new_formula.read_order(order_9, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_10 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x10",
  "price": "200",
  "remaining_size": "2",
  "side": "sell"
}
new_formula.read_order(order_10, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_11 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x11",
  "price": "100",
  "remaining_size": "2",
  "side": "buy"
}
new_formula.read_order(order_11, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_12 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x12",
  "price": "100.2",
  "remaining_size": "1",
  "side": "buy"
}
new_formula.read_order(order_12, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_13 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x13",
  "price": "85",
  "remaining_size": "1.76",
  "side": "buy"
}
new_formula.read_order(order_13, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_14 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x14",
  "price": "89",
  "remaining_size": "2",
  "side": "buy"
}
new_formula.read_order(order_14, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

# # Order 15 to Order 17 are used to check the correctness of Done

order_15 = {
  "type": "done",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "price": "700.2",
  "order_id": "0x9",
  "reason": "filled", 
  "side": "sell",
  "remaining_size": "0"
}
new_formula.read_order(order_15, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_16 = {
  "type": "done",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "price": "200.2",
  "order_id": "0x1",
  "reason": "filled", 
  "side": "sell",
  "remaining_size": "0"
}
new_formula.read_order(order_16, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_17 = {
  "type": "done",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "price": "10.2",
  "order_id": "0x4",
  "reason": "filled", 
  "side": "buy",
  "remaining_size": "0"
}
new_formula.read_order(order_17, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)


# Order 18 to Order 20 are used  to check the correctness of match
order_18 = {
  "type": "match",
  "trade_id": 10,
  "sequence": 50,
  "maker_order_id": "0x2",
  "taker_order_id": "0x18",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "size": "1",
  "price": "50.2",
  "side": "buy"
}
new_formula.read_order(order_18, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_19 = {
    "type": "open",
    "time": "2014-11-07T08:19:27.028459Z",
    "product_id": "BTC-USD",
    "sequence": 10,
    "order_id": "0x19",
    "price": "315.2",
    "remaining_size": "8.5",
    "side": "sell"
}
new_formula.read_order(order_19, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

# Order 20 to Order 23 are used  to check the correctness of match

order_20 = {
  "type": "match",
  "trade_id": 10,
  "sequence": 50,
  "maker_order_id": "0x19",
  "taker_order_id": "0x20",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "size": "5",
  "price": "315.2",
  "side": "sell"
}
new_formula.read_order(order_20, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_21 = {
  "type": "match",
  "trade_id": 10,
  "sequence": 50,
  "maker_order_id": "0x5",
  "taker_order_id": "0x21",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "size": "3.5",
  "price": "200.2",
  "side": "sell"
}
new_formula.read_order(order_21, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_22 = {
  "type": "match",
  "trade_id": 10,
  "sequence": 50,
  "maker_order_id": "0x3",
  "taker_order_id": "0x22",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "size": "5",
  "price": "10.2",
  "side": "buy"
}
new_formula.read_order(order_22, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)


order_23 = {
  "type": "match",
  "trade_id": 10,
  "sequence": 50,
  "maker_order_id": "0x6",
  "taker_order_id": "0x22",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "size": "1",
  "price": "2000.2",
  "side": "sell"
}
new_formula.read_order(order_23, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

# # Order 24 to Order 30 are used to check the correctness of STP_insert

order_24 = {
  "type": "change",
  "reason":"STP",
  "time": "2014-11-07T08:19:27.028459Z",
  "sequence": 80,
  "order_id": "0x7",
  "side": "sell",
  "product_id": "BTC-USD",
  "old_size": "1.0",
  "new_size": "9.0",
  "price": "315.2"
}
new_formula.read_order(order_24, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)


order_25 = {
  "type": "change",
  "reason":"STP",
  "time": "2014-11-07T08:19:27.028459Z",
  "sequence": 80,
  "order_id": "0x11",
  "side": "buy",
  "product_id": "BTC-USD",
  "old_size": "2.0",
  "new_size": "18.0",
  "price": "100.0"
}
new_formula.read_order(order_25, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_26 = {
  "type": "change",
  "reason":"STP",
  "time": "2014-11-07T08:19:27.028459Z",
  "sequence": 80,
  "order_id": "0x2",
  "side": "buy",
  "product_id": "BTC-USD",
  "old_size": "2.0",
  "new_size": "1.0",
  "price": "50.2"
}
new_formula.read_order(order_26, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)


order_27 = {
  "type": "change",
  "reason":"STP",
  "time": "2014-11-07T08:19:27.028459Z",
  "sequence": 80,
  "order_id": "0x2",
  "side": "buy",
  "product_id": "BTC-USD",
  "old_size": "1.0",
  "new_size": "0.0",
  "price": "50.2"
}
new_formula.read_order(order_27, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)


# # test negative quantity

order_28 = {
  "type": "change",
  "reason":"STP",
  "time": "2014-11-07T08:19:27.028459Z",
  "sequence": 80,
  "order_id": "0x13",
  "side": "buy",
  "product_id": "BTC-USD",
  "old_size": "1.76",
  "new_size": "-2",
  "price": "50.2"
}
# new_formula.read_order(order_28, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_29 = {
  "type": "change",
  "reason":"STP",
  "time": "2014-11-07T08:19:27.028459Z",
  "sequence": 80,
  "order_id": "0x7",
  "side": "sell",
  "product_id": "BTC-USD",
  "old_size": "9.0",
  "new_size": "6.0",
  "price": "315.2"
}
new_formula.read_order(order_29, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_30 = {
  "type": "change",
  "reason":"STP",
  "time": "2014-11-07T08:19:27.028459Z",
  "sequence": 80,
  "order_id": "0x11",
  "side": "buy",
  "product_id": "BTC-USD",
  "old_size": "18.0",
  "new_size": "3.0",
  "price": "100.0"
}
new_formula.read_order(order_30, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

# #Order 31 to Order  are used to check Modify Insert

order_31 = {
  "type": "change",
  "reason":"modify_order",
  "time": "2022-06-06T22:55:43.433114Z",
  "sequence": 24753,
  "order_id": "0x10",
  "side": "sell",
  "product_id": "BTC-USD",
  "old_size": "2.0",
  "new_size": "5.0",
  "old_price": "200.0",
  "new_price": "378.0"
}
new_formula.read_order(order_31, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_32 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 10,
  "order_id": "0x32",
  "price": "378.0",
  "remaining_size": "34.0",
  "side": "sell"
}
new_formula.read_order(order_32, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_33 = {
  "type": "change",
  "reason":"modify_order",
  "time": "2022-06-06T22:55:43.433114Z",
  "sequence": 24753,
  "order_id": "0x32",
  "side": "sell",
  "product_id": "BTC-USD",
  "old_size": "34.0",
  "new_size": "0.05",
  "old_price": "378.0",
  "new_price": "415.2"
}
new_formula.read_order(order_33, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_34 = {
  "type": "change",
  "reason":"modify_order",
  "time": "2022-06-06T22:55:43.433114Z",
  "sequence": 24753,
  "order_id": "0x13",
  "side": "buy",
  "product_id": "BTC-USD",
  "old_size": "1.76",
  "new_size": "2.0",
  "old_price": "85.0",
  "new_price": "74.2"
}
new_formula.read_order(order_34, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)


order_35 = {
  "type": "open",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "sequence": 1,
  "order_id": "0x35",
  "price": "300",
  "remaining_size": "2.00",
  "side": "buy"
}
new_formula.read_order(order_35, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

# order_36 = {
#   "type": "open",
#   "time": "2014-11-07T08:19:27.028459Z",
#   "product_id": "BTC-USD",
#   "sequence": 1,
#   "order_id": "0x35",
#   "price": "-2",
#   "remaining_size": "2.00",
#   "side": "buy"
# }
# new_formula.read_order(order_36, coinbase_orderbook)
# new_formula.show_orderbook(coinbase_orderbook)
# print_orderbook(coinbase_orderbook)

order_37 = {
  "type": "match",
  "trade_id": 10,
  "sequence": 50,
  "maker_order_id": "0x11",
  "taker_order_id": "0x37",
  "time": "2014-11-07T08:19:27.028459Z",
  "product_id": "BTC-USD",
  "size": "3",
  "price": "100.0",
  "side": "buy"
}
new_formula.read_order(order_37, coinbase_orderbook)
new_formula.show_orderbook(coinbase_orderbook)
print_orderbook(coinbase_orderbook)