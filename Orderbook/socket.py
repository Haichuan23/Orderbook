import json, time
from threading import Thread
from websocket import create_connection
from websocket import WebSocketConnectionClosedException
import new_formula

# The websokcet part is modified based on this source: https://medium.com/coinmonks/coinbase-pro-websockets-dea21da31d7b
# Note: For quantity, I have only kept 5 digits after the decimal point. If the 
# quantity shown is 0.00000, it means the quantity is very small, but not zero


# connect to coinbase exchange
def main():
    coinbase_orderbook = new_formula.OrderBook()

    ws = None
    thread = None
    thread_running = False
    thread_running = False
    thread_keepalive = None

    def websocket_thread():
        global ws
        global cnt
        cnt = 0     # a debug variable used to limit the amount of output

        ws = create_connection("wss://ws-feed.exchange.coinbase.com")
        ws.send(
            json.dumps(
                {
                    "type": "subscribe",
                    "product_ids": ['BTC-USD'],
                    "channels": ["full"],
                }
            )
        )

        thread_keepalive.start()
        while not thread_running:
            try:
                data = ws.recv()
                if data != "":
                    msg = json.loads(data)
                    # cnt += 1
                    new_formula.read_order(msg, coinbase_orderbook)
                    new_formula.show_orderbook(coinbase_orderbook)
    
                    # if (cnt == 200): #debugging code, stop after processing some amount of market events
                    #     break
                else:
                    msg = {}
            except ValueError as e:
                print(e)
                print("{} - data: {}".format(e, data))
            except Exception as e:
                print(e)
                print("{} - data: {}".format(e, data))

        try:
            if ws:
                ws.close()
        except WebSocketConnectionClosedException:
            pass
        finally:
            thread_keepalive.join()

    def websocket_keepalive(interval=30):
        global ws
        while ws.connected:
            ws.ping("keepalive")
            time.sleep(interval)

    thread = Thread(target=websocket_thread)
    thread_keepalive = Thread(target=websocket_keepalive)
    thread.start()


if __name__ == "__main__":
    main()
