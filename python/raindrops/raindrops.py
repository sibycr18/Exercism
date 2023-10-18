def convert(number):
    final_sound = ""
    sounds = {3 : "Pling", 5 : "Plang", 7 : "Plong"}
    for factor, sound in sounds.items():
        if number % factor == 0:
            final_sound += sound
    return str(number) if final_sound == "" else final_sound