from enum import Enum, unique
from dataclasses import dataclass, field
import uuid
from uuid import UUID
from typing import TypeVar

GameLineup_T = TypeVar('GameLineup_T', bound='GameLineup')
Player_T = TypeVar('Player_T', bound='Player')

@unique
class Position(Enum):
    PITCHER = 4
    CATCHER = 5
    FIRST_BASE = 1
    SECOND_BASE = 2
    THIRD_BASE = 3
    SHORTSTOP = 10
    LEFT_FIELD = 7
    CENTER_FIELD = 6
    RIGHT_FIELD = 8
    ROAMER = 9
    BENCH = 11

    @property
    def __json__(self):
        return self.value


@dataclass
class Player:
    first_name: str
    last_name: str
    number: str
    position: Position
    uuid: UUID = field(default_factory=uuid.uuid4)

    @staticmethod
    def from_dict(some_dict: dict) -> Player_T:
        return Player(
            first_name=some_dict['f'],
            last_name=some_dict['l'],
            uuid=UUID(some_dict['i']),
            number=some_dict['n'],
            position=Position(some_dict['p'])
        )

    @property
    def __json__(self):
        return {
            "f": self.first_name,
            "l": self.last_name,
            "i": str(self.uuid),
            "n": self.number,
            "p": self.position
        }


@dataclass
class GameLineup:
    lineup: list[Player]
    non_playing: list[Player] = field(default_factory=list)
    game_uuid: UUID = field(default_factory=uuid.uuid4)
    team_uuid: UUID = field(default_factory=uuid.uuid4)

    @staticmethod
    def from_dict(some_dict: dict) -> GameLineup_T:
        return GameLineup(
            lineup=[Player.from_dict(p) for p in some_dict['h']],
            non_playing=[Player.from_dict(p) for p in some_dict['n']],
            game_uuid=UUID(some_dict['e']),
            team_uuid=UUID(some_dict['t'])
        )

    @property
    def __json__(self):
        return {
            "e": str(self.game_uuid),
            "h": self.lineup,
            "n": self.non_playing,
            "t": str(self.team_uuid)
        }
