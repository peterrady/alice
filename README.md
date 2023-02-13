# King of Diamonds Game

#### Video Demo: <https://youtu.be/IQWo0H5bgrs>

#### Description: This is a game called "King of Diamonds" from "Alice in Borderland" TV Series. You should input a number of players in command-line arguments then read the rules and type the name of each player.

The cow will say the number of each round and the winner or loses.

## Based on TV series:

The King of Diamonds is the hardest Diamonds game. It is run by an international lawyer and former no.3 in the Beach Keiichi Kuzuryu. It was a game of Keynesian Beauty Contest between 5 people: Keiichi Kuzuryu (King of Diamonds), Shuntaro Chishiya, Benzo Yashige, Hinako Daimon, and Takashi Asuma. It was completed by Shuntaro Chishiya.

## Game Overview

#### Set-up

Player limit: 5 ~~(including King of Diamonds)~~

#### Time limit: (This property NOT released in this python program )

~~1 minute/round~~ (no round limit)

~~5 minutes/first round & rounds with new rules~~

~~Upon entering, all players shackle themselves to a seat and confirm the operation of the tablet in front of them. Above their heads is a weight/equilibrium stand that fills Aqua Regia.~~

## Rules

#### All players remaining:

* All players select a number between 0 and 100 ~~in the given time~~.
* The average of the values will be multiplied by 4/5ths (0.8).
* The person who chooses the number closest to the calculated number wins. This constitutes one round. All losers will lose a point (All players start with 0 points).
* ~~A new rule is introduced for every player eliminated. On the first round and all following rounds where a new rule is introduced, players are allotted 5 minutes as a way to get used to the rules.~~
New rule will be introduced when 4 players remaining, 3 players remaining and 2 players remaining.

**Game Clear:** Be the last person remaining.

**Game Over:** Reach -10 points.

~~Every player who gets a “Game Over” will cause the weight stand to tip over, dumping Aqua Regia and burning the victim~~
Every player who gets a “Game Over”, The cow will say "[This Player] is died"

#### 4 players remaining:

If there are 2 people or more choose the same number, the number they choose becomes invalid, meaning they will lose a point even if the number is closest to 4/5ths the average.

* ~~Due to two players receiving a Game Over, this rule was introduced in the 3 players remaining announcement instead.~~
If two players died together and transferd from 5 players remaunding to 3 players remainding directly, the 4 players remaining and 3 players remaining new rules will be introduced together.

#### 3 players remaining:

If there is a person who chooses the exact correct number, the loser penalty is doubled.

#### 2 players remaining:

If someone chooses 0, the player who chooses 100 is the winner.

## Strategy

Before the beginning of the game, all players assumed that excess logic and mathematics would be the key to the game. However, it was quickly realized that it would be within the facet of rationality to eliminate abstract ideas such as nash equilibrium, recursive selection, and cognitive limit. Additionally, perfect rationality is also perfectly predictable. In truth, the game tests the players' ability to predict the number the other players will select and simple calculations. it's proved that this theory right when players used a seemingly absurd strategy outside all logic— intentionally picking obscure numbers to round the average into a more favorable value — in order to balance the losses between players so the damage for the King of Diamonds adds up. Below are some strategies employed, all varying greatly in effectiveness.

#### All Players remaining:

- Since the average number will be multiplied by 0.8, the highest possible answer will be 80. Players should not choose a number higher than 80.
	- If all players choose a number below 80, this means that the answer would be 64 or lower.
-   As all players will attempt to pick numbers lower than the average, this means that the answer will naturally get lower and lower. This means that 0 would be the best choice as it is the lowest number.

#### 4 Players remaining:

- After the elimination, players can no longer pick the same number. So, players can no longer rely on selecting 0.
- One very risky strategy is to pick a higher number, hoping that the other players would choose the same number and be eliminated.

#### 3 Players remaining:

- With the addition of the invalidity rule, the strategy for the game completely changes. Consequently, the number of practical numbers and tactics reduce. Prior, 0 was a strong number but now there’s a high risk of choosing the same number. However, if 0 is avoided and 1 is chosen instead, another player could have the same thought process, yielding the person choosing 0 as the winner. On the other hand, if the results are |  **0/ 1/ 2**  | then the player who chooses 1 wins. But there’s not much difference between 2 or 100 either. In the following scenarios: |  **0 /0 /2**  |  **0 /0 /100**  |  **2 /2 /100**  |; 2, 100, and 100 win respectively. This was Daimon’s thought process. In conclusion, this battle is three-way between 0, 1, and 2-100. 2-100 may look nice initially, but if the other 2 choose the same the smallest number wins. This eliminates 3-100. (In this round, all players chose 1 and the only winning move would’ve been to choose any value other than 1).

- As for the rule of 3 players remaining and choosing the exact correct number, it depends on predicting the numbers of the other players, as:
	-   Players are not likely to choose numbers with double digits, such as 66 or 77.
	-   Players are also not likely to choose round numbers ending in 0, such as 60 or 70.
	-   Players are statistically most likely to choose a number with a 3, 5, or 8 in it.
	-   Players are not likely to pick prime numbers.
	-   Players are not likely to choose numbers that are also popular brand names, such as 64 or 76.

#### 2 Players remaining:

When there are only 2 players left, it is the most ideal for the person who is behind in points to choose 100, and for the person in the lead to select 1 or 0. Although 0 is the most powerful number to choose from, it is also balanced by 100 due to new rule.

## Synopsis

The winner of each round is in **bold**.

| **Round** | **Chishiya's number** | **Daimon's number** | **Yashige's number** | **Asuma's number** | **Kuzuryū's number** | **Winning number** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Round 1** | 32<br />(-1) | 40<br />(-1) | 30<br />(-1) | 33<br />(-1) | **29**<br />(0) | 32.8x0.8=**26.24** |
| **Round 2** | 17<br />(-2) | 21<br />(-2) | 16<br />(-2) | 15<br />(-2) | **14**<br />(0) | 16.6x0.8=**13.28** |
| **Round 3** | 7<br />(-3) | 11<br />(-3) | 3<br />(-3) | 7<br />(-3) | **5**<br />(0) | 6.6x0.8=**5.28** |
| **Round 4** | 2<br />(-4) | 4<br />(-4) | 0<br />(-4) | 0<br />(-4) | **1**<br />(0) | 1.14x0.8=**1.12** |
| **Round 5** | 100<br />(-5) | **1**<br />(-4) | 0<br />(-5) | 0<br />(-5) | 0<br />(-1) | 20.2x0.8=**16.16** |
| **Round 6** | **25**<br />(-5) | 100<br />(-5) | 0<br />(-6) | 5<br />(-6) | 17<br />(-2) | 29.2x0.8=**23.52** |
| **Round 7** | 100<br />(-6) | **30**<br />(-5) | 0<br />(-7) | 4<br />(-7) | 10<br />(-3) | 28.8x0.8=**23.04** |
| **Round 8** | **20**<br />(-6) | 10<br />(-6) | 36<br />(-8) | 34<br />(-8) | **20**<br />(-3) | 24x0.8=**19.2** |
| **Round 9** | 6<br />(-7) | **8**<br />(-6) | 2<br />(-9) | 20<br />(-9) | 10<br />(-4) | 9.2x0.8=**7.36** |
| **Round 10** | 1<br />(-8) | 7<br />(-7) | 0<br />(-10)<sup>†</sup> | 0<br />(-10)<sup>†</sup> | **2**<br />(-4) | 2x0.8=**1.6** |
| **Round 11** | 1<br />(-9) | 1<br />(-8) | X | X | 1<br />(-5) | **No winner** |
| **Round 12** | **23** (Exact match)<br />(-9) | 62<br />(-10)<sup>†</sup> | X | X | 1<br />(-7) | 28.66x0.8=**22.93** |
| **Round 13** | **100**<br />(-9) | X | X | X | 0<br />(-8) | **100** overrules 0 |
| **Round 14** | **100**<br />(-9) | X | X | X | 0<br />(-9) | **100** overrules 0 |
| **Round 15** | **100**<br />(-9) | X | X | X | 0<br />(-10)<sup>†</sup> | **100** overrules 0 |

#
