def card_magician(output, cards, trick):
    for card in cards:
        output = trick(output, card)
    return output

def card_magus(a,b,c,d,e):
    if a is tuple():
        a = c # Replace your answer here.
        b = c
        def c(a,x):
            if len(a) < 1:
                return None
        #see if the card (x) is a duplicated cards
            count = 0
            for z in a:
                if z == x:
                    count += 1
            if count > 1:
                b = tuple()
                for z in a:
                    if z != x:
                        b += (z,)
                return b
            return a
        lol = card_magician(a, b, c)
        new = tuple()
        for y in a:
            if y not in lol and y not in new:
                new += (y,)
        return new
    if type(a) is type(str()):
        count = 0
        for x in c:
            if a == x:
                count += 1
        return count
    if a == 0:
        return 4
        

duplicate_cards = card_magus((),
                             (),
                             ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD'),
                             lambda abra, kadabra, alakazam: (abra + (alakazam,), kadabra) if alakazam in kadabra and not alakazam in abra else (abra, kadabra + (alakazam,)),
                             lambda please, thank_you: thank_you)

card_to_count = '3D'
number_of_cards = card_magus(card_to_count,
                             (),
                             ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD'),
                             lambda oo, ee, aa: (oo, ee + ((aa,) if aa == oo else ())),
                             lambda ting, tang: len(ting))

also_number_of_cards = card_magus(0,
                                  0,
                                  ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD', '3D', '3D'),
                                  lambda avada_kedavra, crucio, imperio: (0, crucio + 1 if imperio == card_to_count else crucio),
                                  lambda rictusempra, everte_statum: rictusempra)
