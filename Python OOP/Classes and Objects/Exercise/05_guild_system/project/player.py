class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost) -> str:
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for skill_name, mana_cost in self.skills.items():
            result += f"==={skill_name} - {mana_cost}\n"
        return result