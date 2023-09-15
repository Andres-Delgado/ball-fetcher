from typing import List

class Cleaner:
  @classmethod
  def remove_extra_player(cls, team: dict) -> dict:
    team['players'] = [player for player in team['players'] if player['stats']['core']['score'] != 0]
    return team

  @classmethod
  def remove_extra_players(cls, replays: List[dict]) -> dict:
    for replay in replays:
      replay['blue'] = cls.remove_extra_player(replay['blue'])
      replay['orange'] = cls.remove_extra_player(replay['orange'])
    return replays

  @classmethod
  def check_lengths(cls, replays):
    for replay in replays:
      playersBlue = len(replay['blue']['players'])
      playersOrange = len(replay['orange']['players'])

      if (playersBlue > 3 or playersOrange > 3):
        print('found')

  @classmethod
  def clean(cls, replays: List[dict]) -> List[dict]:
    replays = cls.remove_extra_players(replays)
    return replays

