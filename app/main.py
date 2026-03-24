from app.knight import Knight


def battle(knights_config: dict) -> dict:
    # Створюємо об'єкти лицарів
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot_power = lancelot.power
    mordred_power = mordred.power

    lancelot.take_damage(mordred_power)
    mordred.take_damage(lancelot_power)

    arthur_power = arthur.power
    red_knight_power = red_knight.power

    arthur.take_damage(red_knight_power)
    red_knight.take_damage(arthur_power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
