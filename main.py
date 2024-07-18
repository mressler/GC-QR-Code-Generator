import json
from gcQr.models import Player, Position, GameLineup
from gcQr.methods import qr_code_from_lineup, lineup_from_qr_code_data


if __name__ == '__main__':
    alpha = Player("Alpha", "Pitcher", "4", Position.PITCHER)
    bravo = Player("Bravo", "ExtraHitter", "7", Position.BENCH)
    charlie = Player("Charlie", "Shortstop", "8", Position.SHORTSTOP)
    delta = Player("Delta", "Firstbase", "21", Position.LEFT_FIELD)
    echo = Player("Echo", "Thirdbase", "23", Position.THIRD_BASE)
    foxtrot = Player("Foxtrot", "Secondbase", "24", Position.SECOND_BASE)
    golf = Player("Golf", "Rightfield", "25", Position.RIGHT_FIELD)
    hotel = Player("Hotel", "Firstbase", "37", Position.FIRST_BASE)
    india = Player("India", "Catcher", "96", Position.CATCHER)
    julia = Player("Julia", "Centerfield", "98", Position.CENTER_FIELD)
    kilo = Player("Kilo", "Roamer", "99", Position.ROAMER)

    team = GameLineup([alpha, bravo, charlie, delta, echo, foxtrot, golf, hotel, india, julia, kilo])
    qr_code_from_lineup(team)

    print(json.dumps(team, default=lambda x: x.__json__, indent=4))

    # print(lineup_from_qr_code_data(''))
