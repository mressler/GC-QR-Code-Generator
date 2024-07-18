# GameChanger QR Code Generator

Do you obsess over your team schedule, rotation, and lineup like me? Do you also manage your life in spreadsheets? Would you like to embed that rotation in a QR code inside your spreadsheets so that you can flex your nerd cred without forcing other coaches to type in your roster & lineup by hand like neanderthals?

Well look no further! Generate your GameChanger compatible QR Code with this handy open source Python module:

```
from gcQr.models import Player, Position, GameLineup
from gcQr.methods import qr_code_from_lineup

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
```

![lineup](https://github.com/user-attachments/assets/b341dcda-2eef-4a01-ac77-597c111d688c)
