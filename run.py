import thread, time
import client

if __name__ == "__main__":
    # thread.start_new_thread(client.run, (), {'host': '0.0.0.0', 'port': 80})
    # while 1: time.sleep(1)
    client.run(debug = True, port = 80)
