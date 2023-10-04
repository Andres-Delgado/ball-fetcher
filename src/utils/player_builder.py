from typing import List

from classes.player import Player
from utils.fileUtils import FileUtils

# TODO: build players first, then save

class PlayerBuilder:
  @classmethod
  def build_player(cls, matchId: str, playerDict: dict):
    name, playerId = playerDict['name'], playerDict['id']['id']
    playerLoad: dict = FileUtils.load_player(playerId)
    player = Player(playerLoad, playerId, name)
    player.append_dict(playerDict, matchId)
    FileUtils.save_player(playerId, player)

  @classmethod
  def build_players(cls, matchId: str, players: List[dict]):
    for player in players:
      cls.build_player(matchId, player)

  @classmethod
  def build_from_replay(cls, replay):
    playersBlue: List[dict] = replay['blue']['players']
    playersOran: List[dict] = replay['orange']['players']
    matchId = replay['id']
    cls.build_players(matchId, playersBlue)
    cls.build_players(matchId, playersOran)

  @classmethod
  def build(cls):
    replays = FileUtils.load_replays()
    [cls.build_from_replay(replay) for replay in replays]
