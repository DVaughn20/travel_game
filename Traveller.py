import textwrap


class Traveller:
    """
    Some text about what the Traveller object does...
    """

    INSTRUCTIONS = {
        'name': 'root_node',
        'prompt': """

            Reality comes to focus. You're standing in the road, 
            a wrecked car behind you. A white cat limps away.

                0 - Walk toward the cat
                1 - Take out your phone, film the cat   
        """,
        'left_node': {
            'name': 'walk_around_cat',
            'prompt': """
            
                The cat is frantic because of its pain
                      
                      0 - Try to comfort the cat
                      1 - Get back in the car
            """,
            'left_node': {
                'name': 'comfort_cat',
                'prompt': 'The cat attacks you and kills you, Goodbye',
                'left_node': None,
                'right_node': None,
            },
            'right_node': {
                'name': 'back_in_car',
                'prompt': 'You drive home feeling terrible, Goodbye',
                'left_node': None,
                'right_node': None,
            },
        },
        'right_node': {
            'name': 'film_cat',
            'prompt': """   
            
                You film the cat and a neighbor come out yelling at you for being a terrible person
            
                   0 - Ignore the neighbor and leave
                   1 - Fight the neighbor and get beat up
            """,
            'left_node': {
                'name': 'ignore',
                'prompt': 'You leave the scene, Goodbye',
                'left_node': None,
                'right_node': None
            },
            'right_node': {
                'name': 'fight',
                'prompt': 'You fight the neighbor and get beat up, Goodbye',
                'left_node': None,
                'right_node': None,
            },
        },

    }

    def __init__(self):
        """ Init """
        self._player = None

    def run(self):
        """ Main entry-point """
        self._player = input('Who are you? ')
        print(f'Welcome, {self._player}')
        self._evaluate(self.INSTRUCTIONS)

    def _evaluate(self, instructions):
        """
        Ask prompt then evaluate user response
        """
        print(textwrap.dedent(instructions['prompt']))

        left_node = instructions['left_node']
        right_node = instructions['right_node']

        if left_node is None or right_node is None:
            return

        response = input('What do you want to do? ')

        if response == '0':
            new_instructions = instructions['left_node']
        elif response == '1':
            new_instructions = instructions['right_node']
        elif response.lower() in ('q', 'quit'):
            print('\nTerminating program. Goodbye!')
            new_instructions = None
        else:
            print(f'\nInvalid instruction ("{response}"). Prompting again: ')
            new_instructions = instructions

        if new_instructions is not None:
            self._evaluate(new_instructions)


if __name__ == '__main__':
    traveller = Traveller()
    traveller.run()
