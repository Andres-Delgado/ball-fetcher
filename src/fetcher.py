import requests
from utils.fileUtils import FileUtils

TOKEN = ''
HEADERS = {
  'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, ' +
    'like Gecko) Chrome/102.0.5005.125 Safari/537.36',
  'Authorization': TOKEN
}
URL = 'https://ballchasing.com/api/'

class Fetcher:
  @staticmethod
  def get_replay(replayId: str) -> dict:
    response = requests.get(URL + f'replays/{replayId}', headers=HEADERS)
    return response.json()

  @classmethod
  def list_replays(cls, groupId: str) -> dict:
    response = requests.get(URL + f'replays?group={groupId}', headers=HEADERS)
    return response.json()

  # might not need this
  @classmethod
  def get_replay_group(cls, groupId: str) -> dict:
    response = requests.get(URL + f'groups/{groupId}', headers=HEADERS)
    return response.json()

  @classmethod
  def list_replay_groups(cls, groupId: str) -> dict:
    response = requests.get(URL + f'groups?group={groupId}', headers=HEADERS)
    return response.json()
