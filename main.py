from videogame import Videogame
import fresh_tomatoes


zeldaBOW = Videogame(
                "Zelda Breath of The Wild", "RPG", "E",
                "img/zelda.jpg",
                "https://www.youtube.com/watch?v=zw47_q9wbBE")

ds3 = Videogame(
                "Dark Souls", "RPG", "M",
                "img/ds3.png",
                "https://www.youtube.com/watch?v=oX0cvtjKt9E")

mgs5 = Videogame(
                "Metal Gear Solid 5", "Stealth", "M",
                "img/mgsv.png",
                "https://www.youtube.com/watch?v=NL4ZxDWLwpM")

marioOddysey = Videogame(
                "Zelda Breath of The Wild", "RPG", "E",
                "img/mario.jpg",
                "https://www.youtube.com/watch?v=wGQHQc_3ycE")

hollowKnight = Videogame(
                "Hollow Knight", "RPG", "E",
                "img/hollow.jpg",
                "https://www.youtube.com/watch?v=UAO2urG23S4")

theWitcher3 = Videogame(
                "The Witcher 3", "RPG", "M",
                "img/witcher.jpg",
                "https://www.youtube.com/watch?v=53MyR_Z3i1w")

games = [zeldaBOW, ds3, mgs5, marioOddysey, hollowKnight, theWitcher3]

fresh_tomatoes.open_movies_page(games)

