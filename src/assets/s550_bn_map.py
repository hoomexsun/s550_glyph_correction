#! From speech_dataset/src/utils/bn_map.py
EN_PUNCTUATIONS = {
    "\u0021",  # \u0021 -> ! (Exclamation mark)
    "\u0025",  # \u0025 -> % (Percent sign)
    "\u0028",  # \u0028 -> ( (Left Parenthesis)
    "\u0029",  # \u0029 -> ) (Right Parenthesis)
    "\u002c",  # \u002c -> , (Comma)
    "\u002d",  # \u002d -> - (Hyphen-minus)
    "\u002e",  # \u002e -> . (Full stop)
    "\u003a",  # \u003a -> : (Colon)
    "\u003f",  # \u003f -> ? (Question mark)
    "\u2018",  # \u2018 ->  (Left Single Quotation mark)
    "\u2019",  # \u2019 ->  (Right Single Quotation mark)
}

S550_ADJUST = {
    "\u00e5\u00a1\u00b8": "\u00b8\u00a1\u00e5",  # \u00e5\u00a1\00b8 -> å¡¸ : \u00b8\u00a1\u00e5 -> ¸¡å #! Eg: security, virtual,
}


BN_ALPHABET = {
    "\u0022": "\u0985",  # \u0022 -> " : \u0985 -> অ #! MISSING SP
    "\u0022\u00e0": "\u0986",  # \u0022\u00e0 -> "à : \u0986 -> আ
    "\u00d2\u00fc": "\u0987",  # \u00d2\u00fc -> Òü : \u0987 -> ই
    "\u0023": "\u0988",  # \u0023 -> # : \u0988 -> ঈ
    "\u006c\u00a1\u00fc": "\u0989",  # \u006c\u00a1\u00fc -> l¡ü : \u0989 -> উ
    "\u0024": "\u098a",  # \u0024 -> $ : \u098a -> ঊ
    "\u02dc": "\u098b",  # \u02dc -> ˜ : \u098b -> ঋ #! Unused
    "\u0026": "\u098f",  # \u0026 -> & : \u098f -> এ
    "\u0027": "\u0990",  # \u0027 -> ' : \u0990 -> ঐ
    "\u002a": "\u0993",  # \u002a -> * : \u0993 -> ও
    "\u002b": "\u0994",  # \u002b -> + : \u0994 -> ঔ
    "\u0041": "\u0995",  # \u0041 -> A : \u0995 -> ক
    "\u004a": "\u0996",  # \u004a -> J : \u0996 -> খ
    "\u004b": "\u0997",  # \u004b -> K : \u0997 -> গ
    "\u0051": "\u0998",  # \u0051 -> Q : \u0998 -> ঘ
    "\u0052": "\u0999",  # \u0052 -> R : \u0999 -> ঙ
    "\u0057": "\u099a",  # \u0057 -> W : \u099a -> চ
    "\u00e1": "\u099b",  # \u00e1 -> á : \u099b -> ছ
    "\u005c": "\u099c",  # \u005c -> \ : \u099c -> জ
    "\u0063": "\u099d",  # \u0063 -> c : \u099d -> ঝ
    "\u0064": "\u099e",  # \u0064 -> d : \u099e -> ঞ
    "\u0069": "\u099f",  # \u0069 -> i : \u099f -> ট
    "\u006b": "\u09a0",  # \u006b -> k : \u09a0 -> ঠ
    "\u006c": "\u09a1",  # \u006c -> l : \u09a1 -> ড
    "\u006e": "\u09a2",  # \u006e -> n : \u09a2 -> ঢ
    "\u006f": "\u09a3",  # \u006f -> o : \u09a3 -> ণ
    "\u0074": "\u09a4",  # \u0074 -> t : \u09a4 -> ত
    "\u003d": "\u09a5",  # \u003d -> = : \u09a5 -> থ
    "\u0192": "\u09a6",  # \u0192 -> ƒ : \u09a6 -> দ
    "\u2039": "\u09a7",  # \u2039 -> ‹ : \u09a7 -> ধ
    "\u003e": "\u09a8",  # \u003e -> > : \u09a8 -> ন
    "\u0161": "\u09aa",  # \u0022 -> š : \u09aa -> প
    "\u00f3": "\u09ab",  # \u00f3 -> ó : \u09ab -> ফ
    "\u00a4": "\u09ac",  # \u00a4 -> ¤ : \u09ac -> ব
    "\u00ae": "\u09ad",  # \u00ae -> ® : \u09ad -> ভ
    "\u00b3": "\u09ae",  # \u00b3 -> ³ : \u09ae -> ম
    "\u2122": "\u09af",  # \u2122 -> ™ : \u09af -> য
    "\u00b9": "\u09b0",  # \u00b9 -> ¹ : \u09b0 -> র
    "\u00ba": "\u09b2",  # \u00ba -> º : \u09b2 -> ল
    "\u00c5": "\u09b6",  # \u00c5 -> Å : \u09b6 -> শ
    "\u00c8": "\u09b7",  # \u00c8 -> È : \u09b7 -> ষ
    "\u00ce": "\u09b8",  # \u00ce -> Î : \u09b8 -> স
    "\u00d2": "\u09b9",  # \u00d2 -> Ò : \u09b9 -> হ
    "\u00f5": "\u09c3",  # \u00f5 -> õ : \u09c3 -> ৃ
    "\u00f4": "\u09cd",  # \u00f4 -> ô : \u09cd -> ্
    "\u00ef": "\u09d7",  # \u00ef -> ï : \u09d7 -> ৗ
    "\u00d8": "\u09dc",  # \u00d8 -> Ø : \u09dc -> ড়
    "\u00d9": "\u09dd",  # \u00d9 -> Ù : \u09dd -> ঢ়
    "\u00da": "\u09df",  # \u00da -> Ú : \u09df -> য়
    "\u0030": "\u09e6",  # \u0030 -> 0 : \u09e6 -> ০
    "\u0031": "\u09e7",  # \u0031 -> 1 : \u09e7 -> ১
    "\u0032": "\u09e8",  # \u0032 -> 2 : \u09e8 -> ২
    "\u0033": "\u09e9",  # \u0033 -> 3 : \u09e9 -> ৩
    "\u0034": "\u09ea",  # \u0034 -> 4 : \u09ea -> ৪
    "\u0035": "\u09eb",  # \u0035 -> 5 : \u09eb -> ৫
    "\u0036": "\u09ec",  # \u0036 -> 6 : \u09ec -> ৬
    "\u0037": "\u09ed",  # \u0037 -> 7 : \u09ed -> ৭
    "\u0038": "\u09ee",  # \u0038 -> 8 : \u09ee -> ৮
    "\u0039": "\u09ef",  # \u0039 -> 9 : \u09ef -> ৯
    "\u0081": "\u09F1",  # \u0081 -> (invisible) : \u09F1 -> ৱ #! \x81
}

BN_PSEUDO_ALPHABET = {
    "\u007d": "\u0982",  # \u007d -> } : \u0982 -> ং
    "\u0040": "\u0983",  # \u0040 -> @ : \u0983 -> ঃ
    "\u003b": "\u09ce",  # \u003b -> ; : \u09ce -> ৎ
}

BN_VOWEL_RIGHT = {
    "\u00e0": "\u09be",  # \u00e0 -> à : \u09be -> া
    "\u00e3": "\u09c0",  # \u00e3 -> ã : \u09c0 -> ী #! sometimes followed by sp
}

BN_VOWEL_LEFT = {
    "\u005b": "\u09bf",  # \u005b -> [ : \u09bf -> ি
    "\u00eb": "\u09c7",  # \u00eb -> ë : \u09c7 -> ে #! SP
    "\u00ec": "\u09c7",  # \u00ec -> ì : \u09c7 -> ে #! NOSP
    "\u00ed": "\u09c8",  # \u00ed -> í : \u09c8 -> ৈ #! SP
    "\u00ee": "\u09c8",  # \u00ee -> î : \u09c8 -> ৈ #! NOSP
}

BN_VOWEL_DOWN = {
    "\u00e5": "\u09c1",  # \u00e5 -> å : \u09c1 -> ু #! Normal - After alphabet
    "\u00e6": "\u09c1",  # \u00e6 -> æ : \u09c1 -> ু #! More Below - After combination
    "\u00e7": "\u09c1",  # \u00e7 -> ç : \u09c1 -> ু #! On right
    "\u00e8": "\u09c2",  # \u00e8 -> è : \u09c2 -> ূ #! Check when followed by y
    "\u00e9": "\u09c2",  # \u00e9 -> é : \u09c2 -> ূ #! NO occurence
}

BN_VOWEL_OUTSIDE = {
    "\u09c7\u09be": "\u09cb",  # \u09c7\u09be -> ে +  া : \u09cb ->  ো
    "\u09c7\u09d7": "\u09cc",  # \u09c7\u09d7 -> ে +  ৗ : \u09cc ->  ৌ
}

BN_EXTRA = {
    "\u007b": "\u09bf\u0981",  # \u007b -> { : \u09bf\u0981 -> িঁ  (this need to be moved left together)
    "\u2026": "\u09c0\u0981",  # \u2026 -> … : \u09c0\u0981 -> ীঁ
    "\u005d": "\u09d7\u0981",  # \u005d -> ] : \u09d7\u0981 -> ৗঁ
}

BN_COMPLETE = {
    "\u0042": "\u0995\u09cd\u0995",  # \u0042 -> B : \u0995\u09cd\u0995 -> ক্ + ক -> ক্ক
    "\u0043": "\u0995\u09cd\u099f",  # \u0043 -> C : \u0995\u09cd\u099f -> ক্ + ট -> ক্ট
    "\u0044": "\u0995\u09cd\u09a4\u09cd\u09ac",  # \u0044 -> D : \u0995\u09cd\u09a4\u09cd\u09ac -> ক্ত্ব
    "\u0045": "\u0995\u09cd\u09ac",  # \u0045 -> E : \u0995\u09cd\u09ac -> ক্ + ব -> ক্ব
    "\u0046": "\u0995\u09cd\u09ae",  # \u0046 -> F : \u0995\u09cd\u09ae -> ক্ + ম -> ক্ম
    "\u0047": "\u0995\u09cd\u09b8",  # \u0047 -> G : \u0995\u09cd\u09b8 -> ক্ + স -> ক্স
    "\u004c": "\u0997\u09cd\u0997",  # \u004c -> L : \u0997\u09cd\u0997 -> গ্ + গ -> গ্গ
    "\u004d": "\u0997\u09cd\u09ac",  # \u004d -> M : \u0997\u09cd\u09ac -> গ্ + ব -> গ্ব
    "\u0050": "\u0997\u09c1",  # \u0050 -> P : \u0997\u09c1 -> গ +  ু -> গু
    "\u0053": "\u0999\u09cd\u0995",  # \u0053 -> S : \u0999\u09cd\u0995 -> ঙ্ + ক -> ঙ্ক
    "\u0054": "\u0999\u09cd\u0996",  # \u0054 -> T : \u0999\u09cd\u0996 -> ঙ্ + খ -> ঙ্খ
    "\u0055": "\u0999\u09cd\u0997",  # \u0055 -> U : \u0999\u09cd\u0997 -> ঙ্ + গ -> ঙ্গ
    "\u0058": "\u099a\u09cd\u099e",  # \u0058 -> X : \u099a\u09cd\u099e -> চ্ + ঞ -> চ্ঞ
    "\u0059": "\u099a\u09cd\u099b\u09cd\u09ac",  # \u0059 -> Y : \u099a\u09cd\u099b\u09cd\u09ac -> চ্ছ্ব
    "\u005e": "\u099c\u09cd\u099c\u09cd\u09ac",  # \u005e -> ^ : \u099c\u09cd\u099c\u09cd\u09ac -> জ্জ্ব
    "\u005f": "\u099c\u09cd\u099d",  # \u005f -> _ : \u099c\u09cd\u099d -> জ্ + ঝ -> জ্ঝ
    "\u0060": "\u099c\u09cd\u099e",  # \u0060 -> ` : \u099c\u09cd\u099e -> জ্ + ঞ -> জ্ঞ
    "\u0061": "\u099c\u09cd\u09ac",  # \u0061 -> a : \u099c\u09cd\u09ac -> জ্ + ব -> জ্ব
    "\u0062": "\u099c\u09cd\u09b0",  # \u0062 -> b : \u099c\u09cd\u09b0 -> জ্ + র -> জ্র
    "\u0065": "\u099e\u09cd\u099a",  # \u0065 -> e : \u099e\u09cd\u099a -> ঞ্ + চ -> ঞ্চ
    "\u0066": "\u099e\u09cd\u099b",  # \u0066 -> f : \u099e\u09cd\u099b -> ঞ্ + ছ -> ঞ্ছ
    "\u0067": "\u099e\u09cd\u099c",  # \u0067 -> g : \u099e\u09cd\u099c -> ঞ্ + জ -> ঞ্জ
    "\u0068": "\u099e\u09cd\u099d",  # \u0068 -> h : \u099e\u09cd\u099d -> ঞ্ + ঝ -> ঞ্ঝ
    "\u006a": "\u099f\u09cd\u099f",  # \u006a -> j : \u099f\u09cd\u099f -> ট্ + ট -> ট্ট
    "\u006d": "\u09a1\u09cd\u09a1",  # \u006d -> m : \u09a1\u09cd\u09a1 -> ড্ + ড -> ড্ড
    "\u0070": "\u09a3\u09cd\u09a3",  # \u0070 -> p : \u09a3\u09cd\u09a3 -> ণ্ + ণ -> ণ্ণ
    "\u0071": "\u09a3\u09cd\u09a0",  # \u0071 -> q : \u09a3\u09cd\u09a0 -> ণ্ + ঠ ->  ণ্ঠ
    "\u0072": "\u09a3\u09cd\u09a1",  # \u0072 -> r : \u09a3\u09cd\u09a1 -> ণ্ + ড -> ণ্ড
    "\u0075": "\u09a4\u09cd\u09ae",  # \u0075 -> u : \u09a4\u09cd\u09ae -> ত্ + ম -> ত্ম
    "\u0076": "\u09a4\u09cd\u09a4",  # \u0076 -> v : \u09a4\u09cd\u09a4 -> ত্ + ত -> ত্ত
    "\u0076\u00a1\u00fb": "\u0995\u09cd\u09a4",  # \u0076\u00a1\u00fb -> v¡û : \u0995\u09cd\u09a4 -> ক্ + ত -> ক্ত
    "\u0077": "\u09a4\u09cd\u09a4\u09cd\u09ac",  # \u0077 -> w : \u09a4\u09cd\u09a4\u09cd\u09ac -> ত্ত্ব
    "\u0078": "\u09a4\u09cd\u09a5",  # \u0078 -> x : \u09a4\u09cd\u09a5 -> ত্ + থ -> ত্থ
    "\u0079": "\u09a4\u09cd\u09b0",  # \u0076 -> y : \u09a4\u09cd\u09a4 -> ত্ + র -> ত্র
    "\u0079\u00fb": "\u0995\u09cd\u09b0",  # \u0076\u00fb -> yû : \u0995\u09cd\u09a4 -> ক্ + র -> ক্র
    "\u008f": "\u09a8\u09cd\u09a8",  # \u008f ->  : \u09a8\u09cd\u09a8 -> ন্ + ন -> ন্ন #! INVISIBLE
    "\u0090": "\u09a8\u09cd\u09b8",  # \u0090 ->  : \u09a8\u09cd\u09b8 -> ন্ + স -> ন্স #! INVISIBLE
    "\u009d": "\u09aa\u09cd\u09aa",  # \u009d ->  : \u09aa\u09cd\u09aa -> প্ + প -> প্প #! INVISIBLE
    "\u00a5": "\u09ac\u09cd\u099f",  # \u00a5 -> ¥ : \u09ac\u09cd\u099f -> ব্ + ট -> ব্ট
    "\u00a6": "\u09ac\u09cd\u09a6",  # \u00a6 -> ¦ : \u09ac\u09cd\u09a6 -> ব্ + দ -> ব্দ
    "\u00a7": "\u09ac\u09cd\u09a7",  # \u00a7 -> § : \u09ac\u09cd\u09a7 -> ব্ + ধ -> ব্ধ
    "\u00a8": "\u09ac\u09cd\u099d",  # \u00a8 -> ¨ : \u09ac\u09cd\u099d -> ব্ + ঝ -> ব্ঝ
    "\u00a9": "\u09ac\u09cd\u09a1",  # \u00a9 -> © : \u09ac\u09cd\u09a1 -> হ্  | ব্ + ড -> ব্ড
    "\u00aa": "\u09ac\u09cd\u099c",  # \u00aa -> ª : \u09ac\u09cd\u099c -> ব্ + জ -> ব্জ
    "\u00af": "\u09ad\u09cd\u09b2",  # \u00af -> ¯ : \u09ad\u09cd\u09b2 -> ভ্ + ল -> ভ্ল
    "\u00b0": "\u09ad\u09cd\u09b0",  # \u00b0 -> ° : \u09ad\u09cd\u09b0 -> ভ্ + র -> ভ্র
    "\u00bb": "\u09b2\u09cd\u0995",  # \u00bb -> » : \u09b2\u09cd\u0995 -> ল্ + ক -> ল্ক
    "\u00bc": "\u09b2\u09cd\u0997",  # \u00bc -> ¼ : \u09b2\u09cd\u0997 -> ল্ + গ -> ল্গ
    "\u00bd": "\u09b2\u09cd\u0997\u09c1",  # \u00bd -> ½ : \u09b2\u09cd\u0997\u09c1 -> ল্গু
    "\u00be": "\u09b2\u09cd\u09ac",  # \u00be -> ¾ : \u09b2\u09cd\u09ac -> ল্ + ব -> ল্ব
    "\u00bf": "\u09b2\u09cd\u09aa",  # \u00bf -> ¿ : \u09b2\u09cd\u09aa -> ল্ + প -> ল্প
    "\u00c0": "\u09b2\u09cd\u09b2",  # \u00c0 -> À : \u09b2\u09cd\u09b2 -> ল্ + ল -> ল্ল
    "\u00c1": "\u09b2\u09cd\u09a1",  # \u00c1 -> Á : \u09b2\u09cd\u09a1 -> ল্ + ড -> ল্ড
    "\u00c7": "\u09b6\u09c1",  # \u00c7 -> Ç : \u09b6\u09c1 -> শ +   ু -> শু
    "\u00c9": "\u09b7\u09cd\u09ac",  # \u00c9 -> É : \u09b7\u09cd\u09ac -> ষ্ + ব -> ষ্ব
    "\u00ca": "\u09b7\u09cd\u099f",  # \u00ca -> Ê : \u09b7\u09cd\u099f -> ষ্ + ট ->  ষ্ট
    "\u00cb": "\u09b7\u09cd\u09a0",  # \u00cb -> Ë : \u09b7\u09cd\u09a0 -> ষ্ + ঠ ->  ষ্ঠ
    "\u00cc": "\u09b7\u09cd\u09a3",  # \u00cc -> Ì : \u09b7\u09cd\u09a3 -> ষ্ + ণ -> ষ্ণ
    "\u00cf": "\u09b8\u09cd\u0996",  # \u00cf -> Ï : \u09b8\u09cd\u0996 -> স্ + খ -> স্খ
    "\u00d0": "\u09b8\u09cd\u099f",  # \u00d0 -> Ð : \u09b8\u09cd\u099f -> স্ + ট -> স্ট
    "\u00d3": "\u09b9\u09cd\u09b2",  # \u00d3 -> Ó : \u09b9\u09cd\u09b2 -> হ্ + ল -> হ্ল
    "\u00d4": "\u09b9\u09cd\u09ac",  # \u00d4 -> Ô : \u09b9\u09cd\u09ac -> হ্ + ব -> হ্ব
    "\u00d5": "\u09b9\u09cd\u09ae",  # \u00d5 -> Õ : \u09b9\u09cd\u09ae -> হ্ + ম -> হ্ম
    "\u00d6": "\u09b9\u09cd\u09a3",  # \u00d6 -> Ö : \u09b9\u09cd\u09a3 -> হ্ + ণ -> হ্ণ
    "\u00d7": "\u09b9\u09c1",  # \u00d7 -> × : \u09b9\u09c1 -> হ +  ু ->  হু
    "\u00db": "\u0995\u09cd\u09b7",  # \u00db -> Û : \u0995\u09cd\u09b7 -> ক্ + ষ -> ক্ষ
    "\u00dc": "\u0995\u09cd\u09b7\u09cd\u09ae",  # \u00dc -> Ü : \u0995\u09cd\u09b7\u09cd\u09ae -> ক্ + ষ্ + ম -> ক্ষ্ম
    "\u00dd": "\u0995\u09cd\u09b7\u09cd\u09a8",  # \u00dd -> Ý : \u0995\u09cd\u09b7\u09cd\u09a8 -> ক্ + ষ্ + ন -> ক্ষ্ন
    "\u00de\u00ea": "\u09a8\u09cd\u09a7",  # \u00de\u00ea -> Þê : \u09a8\u09cd\u09a7 -> ন্ + ধ -> ন্ধ
    "\u00de\u00f8\u00fd": "\u09a8\u09cd\u09a7\u09cd\u09b0",  # \u00de\u00f8\u00fd -> Þøý : \u09a8\u09cd\u09a7\u09cd\u09b0 -> ন্ + ধ্ + র -> ন্ধ্র
    "\u00df": "\u09aa\u09cd\u09b0",  # \u00df -> ß : \u09aa\u09cd\u09b0 -> প্ + র -> প্র
    "\u00e4": "\u09a6\u09cd\u09a6\u09cd\u09ac",  # \u00e4 -> ä : \u09a6\u09cd\u09a6\u09cd\u09ac -> দ্দ্ব
    "\u00f0": "\u099c\u09cd\u099c",  # \u00f0 -> ð : \u099c\u09cd\u099c -> জ্ + জ -> জ্জ
    "\u0152": "\u09a7\u09cd\u09ae",  # \u0152 -> Œ : \u09a7\u09cd\u09ae -> ধ্ + ম -> ধ্ম
    "\u0153": "\u09aa\u09cd\u09a4",  # \u0153 -> œ : \u09aa\u09cd\u09a4 -> প্ + ত -> প্ত
    "\u02c6": "\u09a6\u09cd\u09ae",  # \u02c6 -> ˆ : \u09a6\u09cd\u09ae -> দ্ + ম -> দ্ম
    "\u201c": "\u09a8\u09cd\u09a1",  # \u201c -> “ : \u09a8\u09cd\u09a1 -> ন্ + ড -> ন্ড
    "\u201e": "\u09a6\u09cd\u09a6",  # \u201e -> „ : \u09a6\u09cd\u09a6 -> দ্ + দ -> দ্দ
    "\u2020": "\u09a6\u09cd\u09a7\u09cd\u09ac",  # \u2020 -> † : \u09a6\u09cd\u09a7\u09cd\u09ac -> দ্ + ধ্ + ব -> দ্ধ্ব
    "\u2021": "\u09a6\u09cd\u09ac",  # \u2021 -> ‡ : \u09a6\u09cd\u09ac -> দ্ + ব -> দ্ব
    "\u2021\u00fd": "\u09a6\u09cd\u09a7",  # \u2021\u00fd -> ‡ý : \u09a6\u09cd\u09a7 -> দ্ + ধ -> দ্ধ
    "\u2030": "\u09a6\u09cd\u09b0",  # \u2030 -> ‰ : \u09a6\u09cd\u09b0 -> দ্ + র -> দ্র
    "\u203a": "\u09aa\u09cd\u09b8",  # \u203a -> › : \u09aa\u09cd\u09b8 -> প্ + স -> প্স
}

BN_INCOMPLETE = {
    "\u0048": "\u09cd\u0995",  # \u0048 -> H : \u09cd\u0995 -> ্ + ক ->  ্ক #! Down as [sk]
    "\u004e": "\u0997\u09cd",  # \u004e -> N : \u09cd\u0997 -> গ্ #! Up as [gn, gr, gl]
    "\u004f": "\u0997\u09cd",  # \u004f -> O : \u0997\u09cd -> গ্ #! Left as []
    "\u0056": "\u0999\u09cd",  # \u0056 -> V : \u0999\u09cd -> ঙ্ #! Left as [ng-gh]
    "\u005a": "\u099a\u09cd",  # \u005a -> Z : \u099a\u09cd -> চ্ #! Left as []
    "\u0073": "\u09a3\u09cd",  # \u0073 -> s : \u09a3\u09cd -> ণ্ #! Left as []
    "\u007a": "\u09cd\u09a4",  # \u007a -> z : \u09cd\u09a4 -> ্ত #! Down as [nt, st, str]
    "\u007c": "\u09cd\u09a4\u09cd\u09b0",  # \u007c -> | : \u09cd\u09a4\u09cd\u09b0 -> ্ + ত্ + র -> ত্র #! Down as [ntr, mtr, str]
    "\u00e2": "\u09a4\u09cd",  # \u00e2 -> â : \u09a4 -> ত্ #! UP as [tn, tv]
    "\u00a3": "\u09cd\u09ab",  # \u00a3 -> £ : \u09cd\u09ab -> ্ফ #! Ryt as [mf, lf]
    "\u00ab": "\u09cd\u09ac",  # \u00ab -> « : \u09cd\u09ac -> ্ব #! Down as [tv, tw, sv, khv, thv]
    "\u00ac": "\u09cd\u09ac",  # \u00ac -> ¬ : \u09cd\u09ac -> ্ব #! Down as [mb, sv]
    "\u002f": "\u09ac\u09cd",  # \u002f -> / : \u09ac\u09cd -> ব্ #! Up as []
    "\u00b1": "\u09cd\u09ad",  # \u00b1 -> ± : \u09cd\u09ad -> ্ভ #! Down as [mv]
    "\u00b2": "\u09cd\u09ad\u09cd\u09b0",  # \u00b2 -> ² : \u09cd\u09ad\u09cd\u09b0 -> ্ + ভ্ + র ->   ্ভ্র #! Down as []
    "\u00b4": "\u09ae\u09cd",  # \u00b4 -> ´ : \u09ae\u09cd -> ম্ #! Up as [mv]
    "\u00f1": "\u09cd\u09a4\u09cd\u09a4",  # \u00f1 -> ñ : \u0993 -> \u09cd\u09a4\u09cd\u09a4 -> ্ + ত্ + ত -> ত্ত #! Down as [st-t]
    "\u0049": "\u09cd\u0995\u09cd\u09b0",  # \u0049 -> I : \u09cd\u0995\u09cd\u09b0 -> ্ + ক্ + র ->  ্ক্র #! Down as [skr]
    "\u00b5": "\u09cd\u09ae",  # \u00b5 -> µ : \u09cd\u09ae -> ্ম #! Right as [nm, lm, sm]
    "\u00b6": "\u09cd\u09ae",  # \u00b6 -> ¶ : \u09cd\u09ae -> ্ম #! Right as [mm, sm]
    "\u00b8": "\u09cd\u09af",  # \u00b8 -> ¸ : \u09cd\u09af -> ্য #! Right as [*many]
    "\u00c2": "\u09b2\u09cd",  # \u00c2 -> Â : \u09b2\u09cd -> ল্ #! Left as [lt, lm]
    "\u00c3": "\u09cd\u09b2",  # \u00c3 -> Ã : \u09cd\u09b2 -> ্ল #! Down as [kl, gl, ml, pl, bl]
    "\u00c4": "\u09b2\u09cd",  # \u00c2 -> Â : \u09b2\u09cd -> ল্ #! Left as [lf]
    "\u00c6": "\u09b6\u09cd",  # \u00c6 -> Æ : \u09b6\u09cd -> শ্ #! Left as [sm]
    "\u00cd": "\u09b7\u09cd",  # \u00cd -> Í : \u09b7\u09cd -> ষ্ #! Up as []
    "\u00d1": "\u09b8\u09cd",  # \u00d1 -> Ñ : \u09b8\u09cd -> স্ #! Left/Up as [sp, sk, sv, skr, st, sr]
    "\u00f2": "\u00a2\u09cd",  # \u00f2 -> ò : \u00a2\u09cd -> ্র #! MISUSED (\u0981 -> ঁ )
    "\u00f6": "\u09cd\u09b0",  # \u00f6 -> ö : \u09cd\u09b0 -> ্র #! Down as [str, pr, dr, ptr]
    "\u00f7": "\u09cd\u09b0",  # \u00f7 -> ÷ : \u09cd\u09b0 -> ্র #! Down as [mr, sr]
    "\u00f8": "\u09cd\u09b0",  # \u00f8 -> ø : \u09cd\u09b0 -> ্র #! Down as [pr, khr, gr, dr, shr, br, fr]
    "\u00f9": "\u09cd\u09b0",  # \u00f9 -> ù : \u09cd\u09b0 -> ্র #! Down as []
    "\u0160": "\u09a6\u09cd",  # \u0160 -> Š : \u09a6\u09cd -> দ্ #! Up as []
    "\u0178": "\u09aa\u09cd",  # \u0178 -> Ÿ : \u09aa\u09cd -> প্ #! Left as []
    "\u2013": "\u09a8\u09cd",  # \u2013 -> – : \u09a8\u09cd -> ন্ #! Left as [nd, nm, nt]
    "\u2014": "\u09cd\u09a8",  # \u2014 -> — : \u09cd\u09a8 -> ্ন #! Left-Down as [kn, pn, mn, gn, tn]
    "\u201a": "\u09cd\u09a5",  # \u201a -> ‚ : \u09a5 -> ্থ #! Down as [nth, sth]
    "\u201d": "\u09a8\u09cd",  # \u201d -> ” : \u09a8\u09cd -> ন্ #! Up as [nt, nth, ntr, ndr]
    "\u2022": "\u09cd\u09a8",  # \u2022 -> • : \u09cd\u09a8 -> ্ন #! Down as [sn]
}


BN_PUNCTUATION = {
    "\u00fa": " ",  # \u00fa -> ú : \u200c -> #! Actually cheikhei
}

BN_R_RIGHT = {
    "\u00a2": "\u09b0\u09cd",  # \u00a2 -> ¢ : \u09b0\u09cd -> র্
}

S550_INSIGNIFICANT_CHARS = {
    "\u00a1",  #! \u00a1 -> ¡ : as joiner or space
    "\u00fc",  #! \u00fc -> ü : as top part of e or u
    "\u00ff",  #! \u00ff -> ÿ
    "\uf000",  #! \uf000 -> 
}
