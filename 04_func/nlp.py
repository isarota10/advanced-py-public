from rich.console import Console
from typing import Any
from collections import Counter


def normalize(text: str) -> str:
    tr = "çğıöüş"
    en = "cgious"

    xtab = str.maketrans(tr, en)

    return text.strip().lower().translate(xtab)


def tokenize(text: str) -> list[str]:
    return text.split()


def stemmer(tokens: list[str]) -> list[str]:
    return [t[:5] for t in tokens]


def bOw(tokens: list[str]) -> list[str]:
    return Counter(tokens).most_common(100)


def remove_stop_words(tokens: list[str]) -> list[str]:
    turkce_stop_words = [
        "acaba",
        "ama",
        "aslında",
        "az",
        "bazı",
        "belki",
        "ben",
        "bir",
        "biri",
        "birkaç",
        "birşey",
        "biz",
        "bu",
        "çok",
        "çünkü",
        "da",
        "daha",
        "de",
        "defa",
        "degildiye",
        "degil",
        "eğer",
        "en",
        "gibi",
        "hem",
        "hep",
        "hepsi",
        "her",
        "hiç",
        "için",
        "ile",
        "ise",
        "kez",
        "ki",
        "kim",
        "mı",
        "mu",
        "mü",
        "nasıl",
        "ne",
        "neden",
        "nerde",
        "nerede",
        "nereye",
        "niçin",
        "niye",
        "o",
        "sanki",
        "sadece",
        "şey",
        "siz",
        "şu",
        "tüm",
        "ve",
        "veya",
        "ya",
        "yani",
    ]

    return [t for t in tokens if t not in turkce_stop_words]


class Pipeline:
    def __init__(self):
        self.chain = []
        self._console = Console()

    def add_stage(self, fn: callable):
        self.chain.append(fn)

    def run(self, input: str, *, verbose: bool = False) -> Any:
        if len(self.chain) == 0:
            return None

        first_fn, *tail = self.chain

        output = first_fn(input)

        if verbose:
            self._console.print(first_fn.__name__, output)

        for fn in tail:
            output = fn(output)

            if verbose:
                self._console.print(fn.__name__, output)

        return output


if __name__ == "__main__":
    text = (
        "Cem Karaca, Türkiye'nin müzik tarihinde önemli bir dönüm noktası olarak kabul "
        "edilen Anadolu rock müziğinin öncülerinden biridir. 1945 yılında İstanbul'da "
        "doğan Karaca, sanat yaşamına tiyatro ile başlamış, sonrasında müziğe yönelerek "
        "özgün tarzıyla Türk rock müziğinin yapıtaşlarını oluşturmuştur. Cem Karaca'nın "
        "müziği, Batı enstrümanlarıyla Anadolu'nun yerel ezgilerini birleştirerek, hem "
        "toplumsal içerikli hem de bireysel duyguları derinlikli şekilde işleyen eserlerle "
        "dikkat çekmiştir. Moğollar, Apaşlar, Kardaşlar ve Dervişan gibi önemli gruplarla "
        "çalışarak, bu grupların müzikal kimliklerine de büyük katkıda bulunmuştur. "
        "Şarkılarında siyasi ve toplumsal mesajlar vermekten çekinmeyen Karaca, dönemin "
        "politik atmosferinde sesini yükselten ender sanatçılardan biri olmuştur. Özellikle "
        "'Tamirci Çırağı', 'Bu Son Olsun', 'Deniz Üstü Köpürür', 'Resimdeki Gözyaşları' gibi "
        "parçalarıyla geniş kitlelere ulaşmış, müzikseverlerin kalbinde yer edinmiştir. "
        "Cem Karaca'nın Anadolu rock anlayışı, sadece bir müzik tarzı değil, aynı zamanda "
        "bir duruş, bir yaşam biçimi olarak da değerlendirilmiştir. Dönemin baskıcı "
        "politikaları nedeniyle yurtdışına çıkmak zorunda kalan Karaca, Almanya'da sürgün "
        "hayatı yaşamış, ama müzik üretimine ara vermemiştir. Sürgün yıllarında da "
        "toplumcu sanat anlayışını sürdürmüş, halkın sesi olmaya devam etmiştir. 1987 yılında "
        "Türkiye'ye dönüşü, hem sanat dünyasında hem de dinleyiciler arasında büyük sevinçle "
        "karşılanmıştır. Dönüşüyle birlikte 'Merhaba Gençler ve Her Zaman Genç Kalanlar' adlı "
        "albümünü yayımlamış, yeniden geniş kitlelere ulaşmıştır. Anadolu rock müziği, Cem "
        "Karaca ile birlikte sadece müzikal bir ifade değil, aynı zamanda sosyolojik ve "
        "politik bir anlatım biçimi kazanmıştır. Onun müziğinde emek, adalet, eşitlik ve "
        "özgürlük temaları güçlü bir şekilde hissedilir. Cem Karaca'nın vokal tarzı, "
        "duygusal yoğunluğu ve sahne performansı, Türk müziğinde benzersiz bir yere sahiptir. "
        "Kendine has yorum gücüyle, dinleyiciyi sadece eğlendiren değil, düşündüren ve "
        "etkileyen bir sanatçı olmuştur. Anadolu rock’ın gelişiminde büyük rol oynayan "
        "Karaca, genç müzisyenler için de ilham kaynağı olmaya devam etmektedir. Sanatçının "
        "mirası, sadece plaklarında değil, aynı zamanda fikirlerinde ve duruşunda da yaşar. "
        "Onun bıraktığı eserler, halen yeni kuşaklar tarafından keşfedilmekte ve yeniden "
        "yorumlanmaktadır. Cem Karaca, modern müzik ile halk müziği arasında köprü kurarak, "
        "kültürel devamlılığı sağlayan en önemli figürlerden biri olmuştur. Anadolu rock "
        "sayesinde hem doğunun mistik tınıları hem batının dinamik ritimleri aynı potada "
        "erimiş, ortaya özgün ve derinlikli bir müzik tarzı çıkmıştır. Bugün hâlâ pek çok "
        "müzik grubunun repertuvarında onun eserlerine rastlamak mümkündür. Karaca'nın "
        "şarkıları, yalnızca dönemsel tepkiler değil, evrensel temaları işlediği için "
        "zamansızdır. 'Ay Karanlık', 'Ceviz Ağacı', 'Beni Siz Delirttiniz' gibi eserleri, "
        "insan psikolojisinin ve toplumsal çatışmaların derinliklerini yansıtan önemli "
        "örneklerdir. Anadolu rock, onun sayesinde bir alt kültür olmaktan çıkıp ana akım "
        "müzik içerisinde saygın bir yer edinmiştir. Bugün Türkiye'nin dört bir yanında "
        "düzenlenen müzik festivallerinde onun adı anılmakta, eserleri binlerce kişiyle "
        "birlikte söylenmektedir. Cem Karaca’nın katkılarıyla Anadolu rock sadece müzikte "
        "değil, tiyatro, edebiyat ve sinema gibi farklı sanat dallarında da etkisini "
        "göstermiştir. Onun bütünsel sanat anlayışı, genç sanatçılar için hâlâ yol gösterici "
        "bir pusuladır. Yaşamı boyunca halkın yanında olmuş, sanatıyla sesini duyuramayanların "
        "sözcüsü olmuştur. Cem Karaca, Anadolu’nun sesi, toplumun vicdanı ve Türk müziğinin "
        "öncüsü olarak hafızalarda yaşamaya devam etmektedir."
    )

    console = Console()

    ppl = Pipeline()

    ppl.add_stage(normalize)
    ppl.add_stage(tokenize)
    ppl.add_stage(remove_stop_words)
    ppl.add_stage(stemmer)
    ppl.add_stage(remove_stop_words)
    ppl.add_stage(bOw)

    console.print(ppl.run(text, verbose=False)[:10])
