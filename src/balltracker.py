from utils.player_builder import PlayerBuilder
from utils.synchronizer import Synchronizer
from utils.cleaner import Cleaner

def collect_clean():
  Synchronizer.sync()
  Cleaner.clean()

if __name__ == '__main__':
  print('lol')

  # build players
  # collect_clean()
  # PlayerBuilder.build()
