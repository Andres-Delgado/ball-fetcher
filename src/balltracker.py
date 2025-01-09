from utils.synchronizer import Synchronizer
from utils.cleaner import Cleaner

def collect_clean():
  Synchronizer.sync()
  Cleaner.clean()

if __name__ == '__main__':
  print('lol')
  # collect_clean()

  # build players
