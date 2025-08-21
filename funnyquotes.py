import random

# List of 40 funny quotes
quotes = [
    "I used to think I was indecisive, but now I'm not so sure. – Tommy Cooper",
    "I'm not arguing, I'm just explaining why I'm right. – Bill Hicks",
    "Behind every great man is a woman rolling her eyes. – Jim Carrey",
    "My fake plants died because I did not pretend to water them. – Mitch Hedberg",
    "I haven't spoken to my wife in years. I didn't want to interrupt her. – Rodney Dangerfield",
    "I used to do drugs. I still do, but I used to, too. – Mitch Hedberg",
    "Why do they call it rush hour when nothing moves? – Robin Williams",
    "I can resist everything except temptation. – Oscar Wilde",
    "My therapist says I have a preoccupation with vengeance. We'll see about that. – Stewart Francis",
    "I told my wife the truth. I told her I was seeing a psychiatrist. Then she told me the truth: she was seeing a psychiatrist, two plumbers, and a bartender. – Rodney Dangerfield",
    "I went to a bookstore and asked the saleswoman, 'Where's the self-help section?' She said if she told me, it would defeat the purpose. – George Carlin",
    "I haven't slept for ten days, because that would be too long. – Mitch Hedberg",
    "My wife and I were happy for twenty years. Then we met. – Rodney Dangerfield",
    "I'm writing a book. I've got the page numbers done. – Steven Wright",
    "I intend to live forever. So far, so good. – Steven Wright",
    "My favorite machine at the gym is the vending machine. – Caroline Rhea",
    "If at first you don't succeed, then skydiving definitely isn't for you. – Steven Wright",
    "I used to sell furniture for a living. The trouble was, it was my own. – Les Dawson",
    "I like escalators, because they can never break. They can only become stairs. – Mitch Hedberg",
    "I don’t have a girlfriend. But I do know a woman who would be mad at me for saying that. – Mitch Hedberg",
    "Some people see the glass half full, others see it half empty. I see a glass that's twice as big as it needs to be. – George Carlin",
    "I love deadlines. I love the whooshing noise they make as they go by. – Douglas Adams",
    "Comedy is acting out optimism. – Robin Williams",
    "I believe in the institution of marriage, and I intend to keep trying until I get it right. – Richard Pryor",
    "The first time I smoked pot, I thought, ‘Hey, I like this!’ The second time I smoked pot, I thought, ‘Hey, I like this a lot!’ – Eddie Murphy",
    "I don't have pet peeves, I have major psychotic hatreds. – George Carlin",
    "You're only given a little spark of madness. You mustn't lose it. – Robin Williams",
    "I went to a fight the other night, and a hockey game broke out. – Rodney Dangerfield",
    "Life is nothing if you're not laughing. – Richard Pryor",
    "I tell ya, I was so poor growing up, if I wasn't a boy, I'd have nothing to play with. – Eddie Murphy",
    "I put a dollar in one of those change machines. Nothing changed. – George Carlin",
    "Some cause happiness wherever they go; others whenever they go. – Oscar Wilde",
    "No one realizes that some people expend tremendous energy merely to be normal. – Albert Camus",
    "I used to be a smoker, but I quit when I realized my lungs could actually hear me yelling. – Richard Pryor",
    "You’ll never find anybody who can give you better advice than a comic. – George Carlin",
    "You will have bad times, but they will always wake you up to the stuff you weren’t paying attention to. – Robin Williams",
    "I think I am, therefore, I am. But I am not responsible for it. – Eddie Murphy",
    "I don’t believe in astrology; I’m a Sagittarius and we’re skeptical. – Richard Pryor",
    "I think the saddest people always try their hardest to make people happy. – Robin Williams",
    "When I was a kid, my parents moved a lot, but I always found them. – Mitch Hedberg"
]

print("Press ENTER to get a new quote. Type 'q' and press ENTER to quit.\n")

# Shuffle quotes initially
shuffled_quotes = quotes.copy()
random.shuffle(shuffled_quotes)
index = 0

while True:
    user_input = input()
    if user_input.lower() == "q":
        print("Goodbye!")
        break

    # Get the next quote
    print("\n" + shuffled_quotes[index])
    index += 1

    # If we reached the end, reshuffle
    if index >= len(shuffled_quotes):
        random.shuffle(shuffled_quotes)
        index = 0
