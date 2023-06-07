code = {
    "a": "2", "b": "22", "c": "222", "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444", "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666", "p": "7", "q": "77", "r": "777",
    "s": "7777", "t": "8", "u": "88", "v": "888", "w": "9", "x": "99",
    "y": "999", "z": "9999", "1": "a", "2": "b", "3": "c", "4": "d",
    "5": "e", "6": "f", "7": "g", "8": "h", "9": "i", "0": "j", " ": "~", 
    "é": "3333", "á":"2222", "í": "4444", "ü": "88888", "ű":"888888", 
    "ö":"66666", "ő":"666666", "ó":"6666","ú":"8888"
}

def encode(text):
    encoded = ''
    for char in text.lower():
        if char in code:
            encoded += code[char] + ' '
    return encoded.strip()

def decode(encoded_text):
    decoded = ''
    for encoded_char in encoded_text.split(' '):
        for key, value in code.items():
            if encoded_char == value:
                decoded += key
                break
    return decoded

text = 'Egy távoli galaxisban, egy fiatal és feltörekvő csillagrendszerben található Trigala, ahol az élet már régóta virágzik. A bolygó tele van élettel, és a legkülönbözőbb fajok élnek egymás mellett. A legmagasabb hegycsúcsoktól a legmélyebb tengeri árkokig, mindenhol megfigyelhető az élet és a gazdagság. Azonban a békés életnek vége szakad, amikor a Trigala legfőbb bányáját megtámadják. Az idegen fajokból álló inváziós erőknek csak egyetlen célja van: megszerezni az értékes nyersanyagot. A bolygó őrei kétségbeesetten küzdenek az ellenséges támadókkal, de számukra az esélytelennek tűnő küzdelem csak rövid időre tolja el az elkerülhetetlent. Egy fiatal nő, Thalia, aki a bányákban dolgozik, különleges képességeket birtokol. Az ősi varázserők birtokosa, aki még sosem használta erejét. Most azonban, amikor az élete veszélyben van, kénytelen megtenni az első lépést és megtanulni, hogyan használja erejét, hogy megvédje Trigalát és az értékes nyersanyagot. A varázserők és a bölcsességek útjának követése nem könnyű, de Thalia kitartó és gyorsan fejlődik. Az idő múlásával új barátokat szerez, akikkel együtt az ellenséges támadókkal szemben egyre hatékonyabbak lesznek. Thalia és a csapata nehéz harcokat vívnak, azonban az ellenséges erők túlságosan erősek és a csata megnyerése egyre kétségesebb. Azonban Thalia nem adja fel, és végül egy új tervvel áll elő, amelynek célja, hogy elűzze az ellenséget. A terv alapján Thalia és a csapata az éjszaka leple alatt támadást indítanak az ellenséges bázisok ellen, és a meglepetés támadásnak köszönhetően sikerül legyőzni az inváziós erőket. Thalia és a csapata visszanyerik Trigala békéjét és gazdagságát, és az értékes nyersanyag továbbra is biztosítja a bolygó jólétét. Thalia azonban tudja, hogy mindig készen kell állnia arra, hogy megvédje a bolygóját és a népét, és továbbra is fejleszni fogja képességeit és a kapcsolatát a varázserőkkel, hogy felkészüljön a következő kihívásokra. Az invázió után Thalia és csapata elkezdték újraépíteni a bolygót és segítették az embereket visszatalálni a mindennapi életbe. Azonban Thalia mégsem érezte magát elégedettnek azzal, hogy csak megvédte a bolygót. Tudta, hogy más világokban is vannak olyanok, akiket meg kell védeni az ellenséges támadásoktól és hogy az ő varázserői lehetnek a kulcs a győzelemhez. Thalia felkészülésbe kezdett és újabb kalandokra indult. Új csapatot hozott létre, akikkel az űrbe utaztak, hogy más bolygókon segítsenek a bajba jutott civilizációknak. Az utazás során új fajokkal és kihívásokkal találkoztak, de Thalia bölcsessége és ereje vezette őket mindig a helyes irányba. Az egyik bolygón azonban egy különleges helyet fedeztek fel, amelyben titokzatos erők lappangtak. Thalia érezte, hogy ez lehet az a hely, amelynek a kulcsa a varázserők mélyebb megértéséhez vezethet. Az érdeklődésének köszönhetően elkezdték kutatni a területet, és hamarosan rájöttek, hogy itt az ősi varázserők legjobb titkai vannak elrejtve. Thalia és csapata a tudás felé nyúltak, és hatalmas erővel tértek vissza a bolygóra, ahol mindenki számára megosztották, amit megtanultak. A tudás, amit az űrutazásuk során megszereztek, nemcsak Trigala, hanem az egész csillagrendszer számára új lehetőségeket kínált. A történet végére Thalia a varázserők tudása és az űrutazás során szerzett tapasztalatok segítségével sikerült nem csak saját bolygóját megmenteni, de más civilizációk számára is segítséget nyújtani. Így a csillagrendszerben az összes faj békében és harmóniában élhetett egymással. Thalia végül egy nagy tanítómesterként élt tovább, akinek a neve legendává vált a csillagrendszerben.'
encoded_text = encode(text)
print(f"Encoded: {encoded_text}")

decoded_text = decode(encoded_text)
print(f"Decoded: {decoded_text}")
def encode(text):
    encoded = ''
    for char in text.lower():
        if char in code:
            encoded += code[char] + ' '
    return encoded.strip()

def decode(encoded_text):
    decoded = ''
    for encoded_char in encoded_text.split(' '):
        for key, value in code.items():
            if encoded_char == value:
                decoded += key
                break
    return decoded

text = "Hello world"
encoded_text = encode(text)
print(f"Encoded: {encoded_text}")

decoded_text = decode(encoded_text)
print(f"Decoded: {decoded_text}")