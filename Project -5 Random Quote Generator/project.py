import random
def randomQuotes():
    quotes = [
    "Joy isn’t loud, it’s just real — like laughter when no one’s watching.",
    "Happiness is a moment that doesn’t ask for more.",
    "Sunshine lives in the smallest smiles.",
    "A happy heart dances even on the dullest days.",
    "Sometimes peace is just not needing to explain yourself.",
    "Hope whispers even when the world shouts.",
    "Every sunrise holds more promise than the last.",
    "Kindness is the quietest form of strength.",
    "The best moments are the ones you didn’t plan.",
    "Your value doesn’t shrink just because someone else can't see it.",
    "Let your soul breathe where your heart feels free.",
    "Small steps still move you forward.",
    "You don’t have to be loud to be strong.",
    "Storms make the roots grow deeper.",
    "Rest is also a form of progress.",
    "Not all progress is visible.",
    "The sky doesn’t apologize for being blue.",
    "It’s okay to bloom slowly.",
    "Silence is sometimes the best answer.",
    "You are allowed to be both a masterpiece and a work in progress.",
    "Courage is often just showing up anyway.",
    "Peace begins the moment you decide not to let fear control you.",
    "Gratitude turns what we have into enough.",
    "You’ve survived 100% of your worst days.",
    "Growth feels a lot like breaking at first.",
    "Be proud of how quietly you kept going.",
    "Rain makes things grow. Let it fall.",
    "It’s not selfish to protect your energy.",
    "Not everyone deserves a front-row seat in your life.",
    "Some people are chapters, not the whole story.",
    "Healing isn’t linear, but it’s always forward.",
    "Dreams don’t expire unless you quit.",
    "Even slow progress is progress.",
    "It’s okay to rest. That’s how you recharge your light.",
    "The mountain you’re climbing may just be you becoming yourself.",
    "Your pace doesn’t have to match theirs.",
    "You are the author of your next chapter.",
    "Believe in the things you haven't seen yet.",
    "Gentleness is not weakness. It's wisdom.",
    "You’re allowed to start again.",
    "Quiet moments often reveal the most truth.",
    "You are not behind; you’re on your own path.",
    "Messy beginnings often lead to beautiful endings.",
    "It's okay if the only thing you did today was breathe.",
    "Your soft heart is your superpower.",
    "You don’t need to have it all figured out to move forward.",
    "What if everything works out better than expected?",
    "Trust the timing of your life.",
    "The most beautiful growth is often invisible at first.",
    "Even on cloudy days, the sun is still there."
    ]
    return random.choice(quotes)

def main():
    print("Welcome to Random Quote Generator")
    i=1
    while i!=0:
        print(randomQuotes())
        i=int(input("enter zero to exit :- "))

main()