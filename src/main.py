import threading
from controller import Controller
from utils.checker import run_checker

def main():
    checker_thread = threading.Thread(target=run_checker)
    checker_thread.daemon = True
    checker_thread.start()

    main = Controller()
    main.run()

    checker_thread.join()



if __name__ == '__main__':
    main()