class Player(object):
  def __init__(self, playerLoad: dict, playerId: str, name: str):
    self.id = playerId
    self.name = name

    if len(playerLoad):
      self.core = playerLoad['core']
      self.boost = playerLoad['boost']
      self.movement = playerLoad['movement']
      self.positioning = playerLoad['positioning']
      self.demo = playerLoad['demo']
      self.matches = playerLoad['matches']
    else:
      self.init_matches()
      self.init_core()
      self.init_boost()
      self.init_movement()
      self.init_positioning()
      self.init_demo()

  def init_matches(self, matchId: str = None):
    self.matches = self.matches if hasattr(self, 'matches') else []
    if (matchId): self.matches.append(matchId)

  def init_core(self, core: dict = {}):
    self.core = self.core if hasattr(self, 'core') else {}
    self.core['shots'] = Player.get_value('shots', self.core, core)
    self.core['shots_against'] = Player.get_value('shots_against', self.core, core)
    self.core['goals'] = Player.get_value('goals', self.core, core)
    self.core['goals_against'] = Player.get_value('goals_against', self.core, core)
    self.core['saves'] = Player.get_value('saves', self.core, core)
    self.core['assists'] = Player.get_value('assists', self.core, core)
    self.core['score'] = Player.get_value('score', self.core, core)
    self.core['mvp'] = Player.get_value('mvp', self.core, core)
    self.core['shooting_percentage'] = Player.get_value('shooting_percentage', self.core, core)

  def init_boost(self, boost: dict = {}):
    self.boost = self.boost if hasattr(self, 'boost') else {}
    self.boost['bpm'] = Player.get_value('bpm', self.boost, boost)
    self.boost['bcpm'] = Player.get_value('bcpm', self.boost, boost)
    self.boost['avg_amount'] = Player.get_value('avg_amount', self.boost, boost)
    self.boost['amount_collected'] = Player.get_value('amount_collected', self.boost, boost)
    self.boost['amount_stolen'] = Player.get_value('amount_stolen', self.boost, boost)
    self.boost['amount_collected_big'] = Player.get_value('amount_collected_big', self.boost, boost)
    self.boost['amount_stolen_big'] = Player.get_value('amount_stolen_big', self.boost, boost)
    self.boost['amount_collected_small'] = Player.get_value('amount_collected_small', self.boost, boost)
    self.boost['amount_stolen_small'] = Player.get_value('amount_stolen_small', self.boost, boost)
    self.boost['count_collected_big'] = Player.get_value('count_collected_big', self.boost, boost)
    self.boost['count_stolen_big'] = Player.get_value('count_stolen_big', self.boost, boost)
    self.boost['count_collected_small'] = Player.get_value('count_collected_small', self.boost, boost)
    self.boost['count_stolen_small'] = Player.get_value('count_stolen_small', self.boost, boost)
    self.boost['amount_overfill'] = Player.get_value('amount_overfill', self.boost, boost)
    self.boost['amount_overfill_stolen'] = Player.get_value('amount_overfill_stolen', self.boost, boost)
    self.boost['amount_used_while_supersonic'] = Player.get_value('amount_used_while_supersonic', self.boost, boost)
    self.boost['time_zero_boost'] = Player.get_value('time_zero_boost', self.boost, boost)
    self.boost['percent_zero_boost'] = Player.get_value('percent_zero_boost', self.boost, boost)
    self.boost['time_full_boost'] = Player.get_value('time_full_boost', self.boost, boost)
    self.boost['percent_full_boost'] = Player.get_value('percent_full_boost', self.boost, boost)
    self.boost['time_boost_0_25'] = Player.get_value('time_boost_0_25', self.boost, boost)
    self.boost['time_boost_25_50'] = Player.get_value('time_boost_25_50', self.boost, boost)
    self.boost['time_boost_50_75'] = Player.get_value('time_boost_50_75', self.boost, boost)
    self.boost['time_boost_75_100'] = Player.get_value('time_boost_75_100', self.boost, boost)
    self.boost['percent_boost_0_25'] = Player.get_value('percent_boost_0_25', self.boost, boost)
    self.boost['percent_boost_25_50'] = Player.get_value('percent_boost_25_50', self.boost, boost)
    self.boost['percent_boost_50_75'] = Player.get_value('percent_boost_50_75', self.boost, boost)
    self.boost['percent_boost_75_100'] = Player.get_value('percent_boost_75_100', self.boost, boost)

  def init_movement(self, movement: dict = {}):
    self.movement = self.movement if hasattr(self, 'movement') else {}
    self.movement['avg_speed'] = Player.get_value('avg_speed', self.movement, movement)
    self.movement['total_distance'] = Player.get_value('total_distance', self.movement, movement)
    self.movement['time_supersonic_speed'] = Player.get_value('time_supersonic_speed', self.movement, movement)
    self.movement['time_boost_speed'] = Player.get_value('time_boost_speed', self.movement, movement)
    self.movement['time_slow_speed'] = Player.get_value('time_slow_speed', self.movement, movement)
    self.movement['time_ground'] = Player.get_value('time_ground', self.movement, movement)
    self.movement['time_low_air'] = Player.get_value('time_low_air', self.movement, movement)
    self.movement['time_high_air'] = Player.get_value('time_high_air', self.movement, movement)
    self.movement['time_powerslide'] = Player.get_value('time_powerslide', self.movement, movement)
    self.movement['count_powerslide'] = Player.get_value('count_powerslide', self.movement, movement)
    self.movement['avg_powerslide_duration'] = Player.get_value('avg_powerslide_duration', self.movement, movement)
    self.movement['avg_speed_percentage'] = Player.get_value('avg_speed_percentage', self.movement, movement)
    self.movement['percent_slow_speed'] = Player.get_value('percent_slow_speed', self.movement, movement)
    self.movement['percent_boost_speed'] = Player.get_value('percent_boost_speed', self.movement, movement)
    self.movement['percent_supersonic_speed'] = Player.get_value('percent_supersonic_speed', self.movement, movement)
    self.movement['percent_ground'] = Player.get_value('percent_ground', self.movement, movement)
    self.movement['percent_low_air'] = Player.get_value('percent_low_air', self.movement, movement)
    self.movement['percent_high_air'] = Player.get_value('percent_high_air', self.movement, movement)

  def init_positioning(self, positioning: dict = {}):
    self.positioning = self.positioning if hasattr(self, 'positioning') else {}
    self.positioning['avg_distance_to_ball'] = Player.get_value('avg_distance_to_ball', self.positioning, positioning)
    self.positioning['avg_distance_to_ball_possession'] = Player.get_value('avg_distance_to_ball_possession', self.positioning, positioning)
    self.positioning['avg_distance_to_ball_no_possession'] = Player.get_value('avg_distance_to_ball_no_possession', self.positioning, positioning)
    self.positioning['avg_distance_to_mates'] = Player.get_value('avg_distance_to_mates', self.positioning, positioning)
    self.positioning['time_defensive_third'] = Player.get_value('time_defensive_third', self.positioning, positioning)
    self.positioning['time_neutral_third'] = Player.get_value('time_neutral_third', self.positioning, positioning)
    self.positioning['time_offensive_third'] = Player.get_value('time_offensive_third', self.positioning, positioning)
    self.positioning['time_defensive_half'] = Player.get_value('time_defensive_half', self.positioning, positioning)
    self.positioning['time_offensive_half'] = Player.get_value('time_offensive_half', self.positioning, positioning)
    self.positioning['time_behind_ball'] = Player.get_value('time_behind_ball', self.positioning, positioning)
    self.positioning['time_infront_ball'] = Player.get_value('time_infront_ball', self.positioning, positioning)
    self.positioning['time_most_back'] = Player.get_value('time_most_back', self.positioning, positioning)
    self.positioning['time_most_forward'] = Player.get_value('time_most_forward', self.positioning, positioning)
    self.positioning['time_closest_to_ball'] = Player.get_value('time_closest_to_ball', self.positioning, positioning)
    self.positioning['time_farthest_from_ball'] = Player.get_value('time_farthest_from_ball', self.positioning, positioning)
    self.positioning['percent_defensive_third'] = Player.get_value('percent_defensive_third', self.positioning, positioning)
    self.positioning['percent_offensive_third'] = Player.get_value('percent_offensive_third', self.positioning, positioning)
    self.positioning['percent_neutral_third'] = Player.get_value('percent_neutral_third', self.positioning, positioning)
    self.positioning['percent_defensive_half'] = Player.get_value('percent_defensive_half', self.positioning, positioning)
    self.positioning['percent_offensive_half'] = Player.get_value('percent_offensive_half', self.positioning, positioning)
    self.positioning['percent_behind_ball'] = Player.get_value('percent_behind_ball', self.positioning, positioning)
    self.positioning['percent_infront_ball'] = Player.get_value('percent_infront_ball', self.positioning, positioning)
    self.positioning['percent_most_back'] = Player.get_value('percent_most_back', self.positioning, positioning)
    self.positioning['percent_most_forward'] = Player.get_value('percent_most_forward', self.positioning, positioning)
    self.positioning['percent_closest_to_ball'] = Player.get_value('percent_closest_to_ball', self.positioning, positioning)
    self.positioning['percent_farthest_from_ball'] = Player.get_value('percent_farthest_from_ball', self.positioning, positioning)

  def init_demo(self, demo: dict = {}):
    self.demo = self.demo if hasattr(self, 'demo') else {}
    self.demo['inflicted'] = Player.get_value('inflicted', self.demo, demo)
    self.demo['taken'] = Player.get_value('taken', self.demo, demo)

  def append_dict(self, playerDict: dict, matchId: str):
    self.init_matches(matchId)
    self.init_core(playerDict['stats']['core'])
    self.init_boost(playerDict['stats']['boost'])
    self.init_movement(playerDict['stats']['movement'])
    self.init_positioning(playerDict['stats']['positioning'])
    self.init_demo(playerDict['stats']['demo'])

  @staticmethod
  def get_value(stat: str, selfDict: dict, statDict: dict) -> list:
    statsOg: list = selfDict.get(stat, [])
    if len(statDict): statsOg.append(statDict[stat])
    return statsOg
