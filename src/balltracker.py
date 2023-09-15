from utils.cleaner import Cleaner
from utils.fileUtils import FileUtils
from utils.synchronizer import Synchronizer

if __name__ == '__main__':
  # Synchronizer.sync_week_replays('week1-')
  replays = FileUtils.load_replays(isRaw=True)
  replays = Cleaner.clean(replays)
