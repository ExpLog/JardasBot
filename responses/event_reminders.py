import random

PHRASES = [
    "Este sábado há convívios, apareçam seus caralhos",
    "Seus bêbados de merda, sábado é pra ir ao tasco",
    "Saiam do covil e venham ao convívio deste sábado seus retardados",
]

def choose_phrase() -> str:
    return random.choice(PHRASES)