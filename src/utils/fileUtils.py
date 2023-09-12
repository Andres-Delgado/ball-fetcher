import json
from pathlib import Path
from typing import List

class FileUtils:
  ################
  # Path Methods #
  ################

  @classmethod
  def verify_dir(cls, path: Path):
    if not path.is_dir():
      path.mkdir(parents=True, exist_ok=True)

  @classmethod
  def get_data_path(cls) -> Path:
    path = Path.joinpath(Path.cwd(), 'data')
    cls.verify_dir(path)
    return path

  @classmethod
  def get_csrl_path(cls) -> Path:
    path = Path.joinpath(cls.get_data_path(), 'csrl')
    cls.verify_dir(path)
    return path

  @classmethod
  def get_csrl_week_path(cls, weekStr: str) -> Path:
    path = Path.joinpath(cls.get_csrl_path(), weekStr)
    cls.verify_dir(path)
    return path

  ##################
  # Create Methods #
  ##################

  @classmethod
  def create_csrl_week_path(cls, weekStr: str):
    path = Path.joinpath(cls.get_csrl_path(), weekStr)
    cls.verify_dir(path)

  @classmethod
  def create_csrl_week_match_path(cls, week: str, match: str):
    path = Path.joinpath(cls.get_csrl_week_path(week), match)
    cls.verify_dir(path)

  ################
  # Save Methods #
  ################

  @classmethod
  def save_week_replay(cls, replay: json, week: str, match, filename: str):
    with open(cls.get_csrl_week_path(week).joinpath(match).joinpath(filename + '.json'), 'w') as outfile:
      json.dump(replay, outfile, indent=2)

  ################
  # Load Methods #
  ################

  @classmethod
  def load_replay(cls, fileName: str) -> dict:
    with open(cls.get_replays_path().joinpath(fileName)) as file:
      replay = json.load(file)
      return replay

  @classmethod
  def load_replays(cls) -> List[dict]:
    replayNames = [replay.name for replay in cls.get_replays_path().glob('*.json')]
    return [cls.load_replay(name) for name in replayNames]
