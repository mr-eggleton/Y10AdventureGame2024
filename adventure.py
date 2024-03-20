'''
The Crossroads:
    The player encounters a fork in the path. They must choose between the “Glowing Path” (rumoured to lead to the crystal) and the “Misty Trail” (shrouded in mystery).
    Depending on their choice, they face different obstacles (e.g., a riddle-guardian, a bridge over a chasm).
The Talking Trees:
    The player meets ancient trees that share cryptic clues about the crystal’s location.
    The trees respond to specific keywords (e.g., “wisdom,” “light,” “reflection”).
The River of Whispers:
    The player reaches a river with stepping stones.
    They must decipher the whispers carried by the wind to step on the correct stones.
The Enchanted Creatures:
    The player encounters magical beings (e.g., pixies, griffins, talking animals).
    Each creature offers a challenge (e.g., a riddle, a memory game, a dance-off).
The Crystal Chamber:
    The final scene where the crystal awaits.
    Scripts player must solve a complex puzzle (e.g., arranging coloured gems, aligning mirrors) to unlock its power.
'''
class GameElement():
    title = "Default"
    description = "Default description"
    challenges = []
    def __init__(self, title, description):
        self.title = title
        self.description = description

class Scene(GameElement):
    title = "Default Scene"
    description = "Default description"
    challenges = []
    
    def addChallenge(self, challenge):
        self.challenges.append(challenge)
        return self

class Challenge(GameElement):
    title = "Default Challenge"
    success_scene = None
    fail_scene = None
    
    def __init__(self, title, description, success_scene = None, fail_scene = None):
        super().__init__(title, description)
        self.success_scene = success_scene
        self.fail_scene = fail_scene
    
    
scenes = (
    Scene("The Crossroads", "The player encounters a fork in the path. They must choose between the “Glowing Path” (rumoured to lead to the crystal) and the “Misty Trail” (shrouded in mystery).")
    .addChallenge(Challenge("Glowing Path", "a riddle-guardian"))
    .addChallenge(Challenge("Misty Trail", "a bridge over a chasm"))
    )


'''The Talking Trees:
    The player meets ancient trees that share cryptic clues about the crystal’s location.
    The trees respond to specific keywords (e.g., “wisdom,” “light,” “reflection”).
The River of Whispers:
    The player reaches a river with stepping stones.
    They must decipher the whispers carried by the wind to step on the correct stones.
The Enchanted Creatures:
    The player encounters magical beings (e.g., pixies, griffins, talking animals).
    Each creature offers a challenge (e.g., a riddle, a memory game, a dance-off).
The Crystal Chamber:
    The final scene where the crystal awaits.
    Scripts player must solve a complex puzzle (e.g., arranging coloured gems, aligning mirrors) to unlock its power.

'''
    
