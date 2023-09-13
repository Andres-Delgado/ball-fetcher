from fetcher import Fetcher
from utils.fileUtils import FileUtils

class Synchronizer:

  # @classmethod
  # def sync_replay(cls, week, match, replay):


  # for each match
  #   get_replays in group
  #   for each replay
  #       get_replay
  #       save replay

  @classmethod
  def sync_match_replays(cls, week, match, replays):
    replayIds = [replay['id'] for replay in replays]


    # replays = {{'id': replay['id'], 'name': replay['replay_title']} for replay in replays}

    # sort by replays.list.date
    # rename

    # print(*replays, sep='\n')

    # for replayId in replayIds:
    #   replay = Fetcher.get_replay(replayId)
    #   FileUtils.save_week_replay(replay, week, match, )
    #   pass

  @classmethod
  def sync_matches(cls, week, matchIds):
    for matchId in [matchIds[0]]:
      # Fetcher.get_replay(matchId)
      replays = Fetcher.list_replays(matchId)
      cls.sync_match_replays(week, matchId, replays['list'])


      # cls.sync_replay(week, match, name)

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

    # print(*matchIds, sep='\n')

    cls.sync_matches(week, matchIds)

