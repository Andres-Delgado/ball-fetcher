import shutil
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
  def get_data_raw_path(cls) -> Path:
    path = Path.joinpath(cls.get_data_path(), 'raw')
    cls.verify_dir(path)
    return path

  @classmethod
  def get_data_clean_path(cls) -> Path:
    path = Path.joinpath(cls.get_data_path(), 'clean')
    cls.verify_dir(path)
    return path

  @classmethod
  def get_csrl_path(cls, isRaw = False) -> Path:
    dataPath = cls.get_data_raw_path() if isRaw else cls.get_data_clean_path()
    path = Path.joinpath(dataPath, 'csrl')
    cls.verify_dir(path)
    return path

  @classmethod
  def get_csrl_week_path(cls, weekStr: str, isRaw = False) -> Path:
    path = Path.joinpath(cls.get_csrl_path(isRaw), weekStr)
    cls.verify_dir(path)
    return path

  ##################
  # Create Methods #
  ##################

  @classmethod
  def create_csrl_week_path(cls, weekStr: str, isRaw = False):
    path = Path.joinpath(cls.get_csrl_path(isRaw), weekStr)
    cls.verify_dir(path)

  @classmethod
  def create_csrl_week_match_path(cls, week: str, match: str, isRaw = False):
    path = Path.joinpath(cls.get_csrl_week_path(week, isRaw), match)
    cls.verify_dir(path)

  ################
  # Save Methods #
  ################

  @classmethod
  def save_replay(cls, path: Path, filename: str, replay: json):
    with open(path.joinpath(filename), 'w') as outfile:
      json.dump(replay, outfile, indent=2)

  @classmethod
  def save_week_replay(cls, replay: json, week: str, match, filename: str, isRaw = False):
    with open(cls.get_csrl_week_path(week, isRaw).joinpath(match).joinpath(filename + '.json'), 'w') as outfile:
      json.dump(replay, outfile, indent=2)

  @classmethod
  def copy_raw_to_clean_replays(cls):
    rawPath = cls.get_data_raw_path()
    cleanPath = cls.get_data_clean_path()
    shutil.copytree(rawPath, cleanPath, dirs_exist_ok=True)

  ################
  # Load Methods #
  ################

  @classmethod
  def load_replay(cls, path: Path) -> dict:
    with open(path) as file:
      replay = json.load(file)
      return replay

  @classmethod
  def load_replays(cls, isRaw = False) -> List[dict]:
    dataPath = cls.get_data_raw_path() if isRaw else cls.get_data_clean_path()
    replayPaths = dataPath.rglob('*.json')
    return [cls.load_replay(path) for path in replayPaths]
