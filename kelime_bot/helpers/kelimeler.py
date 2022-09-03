import random
kelimeler = ["gözəl ","beyin","sual","sağlam ","buraxmaq","zaman","su","eləmək","döymək","olmaq","ölmək",
             "durmaq", "yaşamaq", "yemək", "azərbaycan", "yüksəlmək", "salam", "şəhər", "eləmək", "şüphə", "xoşbəxt", "qəmli",
             "kədər", "rahat", "tələsmək", "nicat", "sürüşmək", "yazmaq", "katibə", "kitab", "paylaşmaq", "hesab", "bədən",
             "torpag", "yaşamaq", "külək", "xoş", "çəkmək", "texnik", "yaxınlaşmaq", "il", "tarix", "dəqiq", "bacı",
             "inci", "əyər", "uçmaq", "qarşılıq","savaşmaq", "sahib", "qayıdmaq", "kişi", "ehtiyac", "duymaq", "görüşmək", "dalaşmaq",
             "oxumaq", "vacib", "tapmaq", "siz", "dövlət", "arxa", "en", "baxmaq", "oturmaq", "belə", "bəzı", "qəmli",
             "tutmaq", "kəsir", "uçmaq", "etmək", "su", "bal", "hal", "doğru", "orta", "başqa", "böyük", "etmək",
             "yeni", "hədd", "soruşmaq", "onlar", "açmaq", "darıxmaq", "daraq", "səs", "anlamaq", "insan", "saat", "necə",
             'çoxalmaq', 'və', 'ev', 'qırmaq', 'tökmək', 'o', 'mən', 'demək', 'sevmək', 'ölmək', 'yıxılmaq', 'öyrənmək', 'daha', 'almaq',
             'var', 'fəxri', 'gəlmək', 'getmək', 'vermək', 'amma', 'salam', 'çiçək', 'yer', 'çay', 'insan', 'giriş', 'çıxış',
             'istəmək', 'il', 'çıxmaq', 'görmək', 'gün', 'biz', 'getmək', 'iş', 'bilməmək', 'ara', 'vermək', 'bilmək', 'əl', 'vaxt',
             'yastıq', 'qapı', 'qardaş', 'baxmaq', 'işləmək', 'içində', 'böyük', 'ok', 'başlamaq', 'yol', 'qalmaq', 'niyə', 'siz',
             'xəritə', 'siqaret', 'gözəl', 'çirkin', 'ev', 'bilməmək', 'tapmaq', 'söymək', 'göz', 'razılaşmaq', 'dünya',
             'baş', 'vəziyyət', 'otur', 'ümüd', 'sən', 'onlar', 'yəni', 'qabaq', 'görüş'  'ölkə', 'ailə', 'döyüş','görüş', 'tutmaq','çəkmək', 'unutmaq',
             'bağlamaq', 'cırmaq','yatmaq', 'oyun', 'söz', 'əsmək', 'bağlı', 'burda', 'oğurlamaq', 'mahir', 'qiymət', 'doğru', 'pomidor', 'əşya', 'evli','divan', 'girmək', 'imtahan', 'qələm', 'dəftər', 'kitab', 'qaçmaq', 'pubg', 'inanmaq', 'uduzmaq', 'udmaq', 'sevmək', 'əymək', 'qucaqlamaq','yemək', 'şirin', 'qoyun', 'eynək', 'video','etmək', 'dağıdmaq', 'qarabağ', 'qaçmaq', 'siyahı', 'qəpik', 'təəccüb', 'ehtiyac', 'ehtiyat', 'mahnı', 'ibtidai'
             ]


def kelime_sec():
    return random.choice(kelimeler)
