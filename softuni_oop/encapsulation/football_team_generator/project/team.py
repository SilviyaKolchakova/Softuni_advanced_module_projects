from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, target_player):
        for player in self.__players:
            if player.name == target_player.name:
                return f"Player {target_player.name} has already joined"
        self.__players.append(target_player)
        return f"Player {target_player.name} joined team {self.__name}"

    def remove_player(self, target_player_name):
        for player in self.__players:
            if player._Player__name == target_player_name:
                return self.__players.pop()

        return f"Player {target_player_name} not found"

