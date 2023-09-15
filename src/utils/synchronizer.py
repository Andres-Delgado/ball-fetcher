from typing import List

from fetcher import Fetcher
from utils.fileUtils import FileUtils

class Synchronizer:
  @classmethod
  def sync_match(cls, week: str, matchName: str, replays: List[dict]):
    replayIds = [replay['id'] for replay in replays]
    replayTitles = [replay['replay_title'].replace(' ', '_') for replay in replays]
    replaysDict = dict(zip(replayIds, replayTitles))

    # get and save each replay in a match
    for replayId, replayTitle in replaysDict.items():
      replay = Fetcher.get_replay(replayId)
      FileUtils.save_week_replay(replay, week, matchName, replayTitle)

  @classmethod
  def sync_matches(cls, week: str, matches: dict):
    # get list of replays for each match in week
    for matchId, matchName in matches.items():
      replays = Fetcher.list_replays(matchId)
      cls.sync_match(week, matchName, replays['list'])

  @classmethod
  def sync_week_replays(cls, weekId: str):
    # create week dir
    week = weekId.split('-')[0]
    FileUtils.create_csrl_week_path(week)

    # get match replay groups from weekId
    groups = Fetcher.list_replay_groups(weekId)

    # create week/match dirs
    matchNames = [group['name'] for group in groups['list']]
    [FileUtils.create_csrl_week_match_path(week, match) for match in matchNames]

    # get matchIds in week
    matchIds = [group['id'] for group in groups['list']]

    matches = dict(zip(matchIds, matchNames))
    cls.sync_matches(week, matches)
