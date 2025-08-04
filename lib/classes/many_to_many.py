

class Game:

    all = []

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string")
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not hasattr(self, "_title"):
            if isinstance(value, str) and value.strip():
                self._title = value

    def results(self):
        return [m for m in Result.all if m.game == self]

    def players(self):
        player_list = [p.player for p in Result.all if p.game == self]
        return list(set(player_list))

    def average_score(self, player):
        results = [m for m in Result.all if m.game == self]
        player_results = [r for r in results if r.player == player]
        scores = [r.score for r in player_results]
        total = sum(scores)
        return total / len(scores) if scores else 0
        

class Player:

    all = []

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value

    def results(self):
        player_results = [p for p in Result.all if p.player == self]
        return player_results

    def games_played(self):
        games_played = [g.game for g in Result.all if g.player == self]
        return list(set(games_played))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([r for r in self.results() if r.game == game])


class Result:

    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value
    
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value

    @property
    def score(self):
        return self._score

    
    @score.setter
    def score(self, value):
        if hasattr(self, '_score'):
            return  
        if isinstance(value, int) and 1 <= value <= 5000:
            self._score = value
    