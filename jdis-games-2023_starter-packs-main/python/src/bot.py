import random
from core.action import Action, Direction, Pattern, Teleport
from core.game_state import GameState
from core.game_state import Player

class MyBot:

    rayon = 1
    step = 0
    distanceCercle = 0
    direction = Direction.UP
    tick_absolue =0
    """
    (fr)
    Cette classe représente votre bot. Vous pouvez y définir des attributs et des méthodes qui 
    seront conservés entre chaque appel de la méthode `tick`.

    (en)
    This class represents your bot. You can define attributes and methods in it that will be kept 
    between each call of the `tick` method.
    """
    def __init__(self):
        direction = None
        self.__name = "name_of_my_super_cool_bot"
        self.__first_turn = True
        rayon = 1
        step = 0
        distanceCercle = 4


    def __random_action(self) -> Action:
        return random.choice(list(Direction))


    def tick(self, state: GameState) -> Action:


        #if state.players["VinnieBaby"].alive != self.tick_absolue:
        #    self.rayon = 1


        self.distanceCercle = 2 *self.rayon
        if(self.step == self.distanceCercle):
            self.rayon = self.rayon + 3
            self.step = 0

        self.tick_absolue = self.tick_absolue + 1
        if self.tick_absolue == 255:
            self.rayon = 4


        self.step = self.step + 1

        if self.step < self.distanceCercle/4:
            self.direction = Direction.RIGHT
        elif self.step  > self.distanceCercle/4 and self.step  < self.distanceCercle/2:
            self.direction = Direction.UP
        elif self.step  > self.distanceCercle/2 and self.step  < 3*self.distanceCercle/4:
            self.direction = Direction.LEFT
        elif self.step  > 3*self.distanceCercle/4:
            self.direction = Direction.DOWN


        """
        (fr)
        Cette méthode est appelée à chaque tick de jeu. Vous pouvez y définir le comportement de
        votre bot. Elle doit retourner une instance de `Action` qui sera exécutée par le serveur.

        (en)
        This method is called every game tick. You can define the behavior of your bot. It must 
        return an instance of `Action` which will be executed by the server.

        Args:
            state (GameState):  (fr) L'état du jeu.
                                (en) The state of the game.
        """

        #return Action(Pattern([self.direction]))
        return Action(self.direction)

        #if self.__first_turn:
            #self.__first_turn = False

       

        #return self.__random_action()