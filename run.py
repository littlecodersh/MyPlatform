import thread, time
from app import app

if __name__ == "__main__":
    # thread.start_new_thread(client.run, (), {'host': '0.0.0.0', 'port': 80})
    # while 1: time.sleep(1)
    app.run(debug = True, port = 80)
