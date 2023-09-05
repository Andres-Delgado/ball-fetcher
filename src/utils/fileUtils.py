import pathlib
import json

class FileUtils:
  @classmethod
  def get_data_path(cls) -> pathlib.Path:
    path = pathlib.Path.joinpath(pathlib.Path.cwd(), 'data')
    if not path.is_dir():
      path.mkdir(parents=True, exist_ok=True)
    return path

  @classmethod
  def get_replays_path(cls) -> pathlib.Path:
    path = pathlib.Path.joinpath(cls.get_data_path(), 'replays')
    if not path.is_dir():
      path.mkdir(parents=True, exist_ok=True)
    return path

  @classmethod
  def save_replay_json(cls, replay: json, filename: str):
    with open(cls.get_replays_path().joinpath(filename + '.json'), 'w') as outfile:
      json.dump(replay, outfile, indent=2)
      # outfile.write(replay)

  @classmethod
  def load_replay(cls, fileName: str) -> dict:
    with open(cls.get_replays_path().joinpath(fileName)) as file:
      replay = json.load(file)
      return replay

  @classmethod
  def load_replays(cls) -> list[dict]:
    replayNames = [replay.name for replay in cls.get_replays_path().glob('*.json')]
    return [cls.load_replay(name) for name in replayNames]
