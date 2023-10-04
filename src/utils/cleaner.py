from pathlib import Path
from typing import List

from utils.fileUtils import FileUtils

class Cleaner:
  @classmethod
  def remove_extra_player(cls, team: dict) -> dict:
    team['players'] = [player for player in team['players'] if player['stats']['core']['score'] != 0]
    return team

  @classmethod
  def remove_extra_players(cls, replay: dict) -> dict:
    replay['blue'] = cls.remove_extra_player(replay['blue'])
    replay['orange'] = cls.remove_extra_player(replay['orange'])
    return replay

  @classmethod
  def has_extra_players(cls, replay):
    playersBlue = len(replay['blue']['players'])
    playersOrange = len(replay['orange']['players'])
    return playersBlue > 3 or playersOrange > 3

  @classmethod
  def clean_directories(cls, dirPath: Path):
    child: Path
    for child in dirPath.iterdir():
      if child.is_dir():
        cls.clean_directories(child)
        continue

      replay = FileUtils.load_replay(child)
      if (cls.has_extra_players(replay)):
        replayClean = cls.remove_extra_players(replay)
        FileUtils.save_replay(dirPath, child.name, replayClean)

  @classmethod
  def clean(cls) -> List[dict]:
    cleanPath = FileUtils.get_data_clean_path()
    cls.clean_directories(cleanPath)
