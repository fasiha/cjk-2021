---
title: 'Chinese 中 Japanese 日 Korean 韓 (CJK) text processing and languages'
description: 'Annotated slides'
---

# Chinese 中 Japanese 日 Korean 韓 (CJK) text processing and languages

Notes:

## What I’d like to talk about
Some factoids about the Chinese, Japanese, and Korean languages and their digital textual representations

Hopefully interesting but also useful to the practicing programmer

> (I’m not a fluent speaker or reader in any of these languages. `TODO` get reviewers.)

---

## “CJK”? 😒

Why lump these three extremely different languages into one abbreviation? Seems problematic?

---

👋 **Handwavium** 👋 This [900-page door stopper](https://www.oreilly.com/library/view/cjkv-information-processing/9780596156114/) by Ken Lunde

![Lunde, CJKV Information Procesing cover](https://fasiha.github.io/cjk-2021/cjkv-cover.png)

Notes:

Chinese, Japanese, and Korean (and here Vietnamese) get lumped together because, to varying degrees, they all make use of *Chinese characters*, which have traditionally been very interesting from a digital representation perspective

This is compounded by the fact that all these also use *other* scripts with their own quirks, so there are many considerations for correct and readable textual representation

> Another interesting commonality: their scripts (Chinese characters *and* others) are readily monospaced.

---

## Linguistics note

![Dr @lynnguist](https://fasiha.github.io/cjk-2021/lynnguist.jpg)

Notes:

To linguists, languages are *spoken*

Their written representations are a very ancillary concern

---

## Chinese writing 漢語

<img src="https://fasiha.github.io/cjk-2021/The_Calligraphy_Model_Sunny_after_Snow_by_Wang_Xizhi-clip.jpg">

Notes:

> ([Image](https://commons.wikimedia.org/wiki/File:The_Calligraphy_Model_Sunny_after_Snow_by_Wang_Xizhi.jpg) is an excerpt from [Wang Xizhi](https://en.wikipedia.org/wiki/Wang_Xizhi) (303–361 CE), “Sunny after Snow” calligraphy model on paper, most likley a Tang (618~907 CE) copy)

It’s well-known that “Chinese”, as any kind of unified spoken language, is a politically-backed mirage: Mandarin, Shanghaiese, Cantonese, Fujianese, etc., are mutually unintelligible and vary considerably “in grammar, syntax, phonology, vocabulary, etc.” ([Language Log](https://languagelog.ldc.upenn.edu/nll/?p=4628))

> (This mirage may harden into reality as the winner-take-all dynamics of lingua francas, helped along by the People’s Republic of China’s active efforts, slowly kills some of these non-Mandarin languages)

However! Speakers of these languages will use Chinese characters to *write*, so please let me keep the title of this section “Chinese writing”

---

### Pictographs

<img src="https://fasiha.github.io/cjk-2021/bone__FS-7864_17.jpg">


Notes:

Image: bone fragment, 1300-1050 BCE. [Sackler Gallery, Smithsonian](https://asia.si.edu/object/S2012.9.461/)

Like every writing system invented (until the Phonecians invented an abjad, which led to alphabets and syllabaries), the ancient Chinese carved pictograms on bone or turtle shells to represent things.

The earliest of these representations come from oracle bones found dating from the Shang dynasty. They were inscribed on ox bones or turtle plastrons (undershell), which were then heated till they cracked, or stabbed with a hot poker—the cracks were inspected for divination. Thousands of characters have been found on these bones and shells, indicating a long incubation period that is alas as of now invisible in the archaeological record.


---

<img src="https://fasiha.github.io/cjk-2021/carapace__FS-7668_24.jpg">

Notes:

Image: turtle carapace, 1300-1050 BCE. [Sackler Gallery, Smithsonian](https://asia.si.edu/object/S2012.9.445/)

---


Imagine the sun 🌞

| | |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| 1500 BCE (bone) | <img src="https://fasiha.github.io/cjk-2021/日-oracle.svg" width="50em"> |
| 800 BCE (bronze) | <img src="https://fasiha.github.io/cjk-2021/日-bronze.svg" width="50em"> |
| 300 BCE (bamboo) | <img src="https://fasiha.github.io/cjk-2021/日-silk.svg" width="50em"> |
| 200 BCE | <img src="https://fasiha.github.io/cjk-2021/日-seal.svg" width="50em"> |
| Today | 日 |


---

#### Or an eye

<img src="https://fasiha.github.io/cjk-2021/目-oracle.svg" width="50em">

<img src="https://fasiha.github.io/cjk-2021/目-bronze.svg" width="50em">

<img src="https://fasiha.github.io/cjk-2021/目-slip.svg" width="50em">

<img src="https://fasiha.github.io/cjk-2021/目-seal.svg" width="50em"> 

Today:

目

(A box with *two* lines, or 👁 👀)


---

New characters for words whose representation hadn’t been decided could be invented in any number of ways.

👩‍🎨🖌

---

#### Reuse

昌: two suns: sunlight, prosperous, beautiful, …

林: two trees (木): woods

森: *three* trees: (guess!)

姦: three women (女): today solely negative dictionary definitions (really, ancient misogynistic men writers, really? 🤦)

---

#### Combine

Combine meanings
- 日 (sun) +
- 月 (moon) =
- 明 (bright)

・・・・

Combine sound:
- 早 (zǎo, early) +
- 艹 (vegetation) =
- 草 (cǎo, grass)

Notes:

Writing with a brush (which even the Shang people did, on bamboo, etc.) can lend itself to creativity in constructing new pictographs.

Although today spoken Mandarin only has around 450 syllables (many of which exist in multiple tones), Old Chinese had considerably less homophony. But this was another source for innovation in characters.

---

### Encoding thousands of characters

<img src="https://fasiha.github.io/cjk-2021/joyo-poster.jpg" width="500em" alt="2136 characters tested in Japanese schools">

Notes:

This leads to the classic data representation problem: literally thousands of characters for daily use—
- ~2500 taught in elementary school and ~1000 taught in middle school in PRC ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Commonly_Used_Characters_in_Modern_Chinese))
- 2663 tested by HSK level 6 ([Wikipedia](https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi#Written_test))), maybe up to a hundred thousand characters for all historic texts.

> We’ll get to it soon but to acknowledge the elephant in the room: Unicode has made things much better but it made things much worse at first, and it had to come from somewhere!

**GB2312**, introduced in 1980, was a list of 6,763 Chinese characters plus alphabets/syllabaries for Greek, Russian, and Japanese.

It uses one or two bytes for each character. Like UTF-8, it is ASCII-compatible: if a byte is between 0x00 and 0x80, then it must be ASCII. If a byte was greater than 0x80, it was a part of a 2-byte character; unlike UTF-8, you don’t know whether it was the first byte or the second byte.

In practice, GB 2312 used 0xA0 to 0xFF: `(255 - 160)**2` = 9025. With some private use area (PUA), you get the ≈7000 characters.

Derived from the Chinese *telegraph* code, whose “codebook … shows one-to-one correspondence between Chinese characters and four-digit numbers from 0000 to 9999. Chinese characters are arranged and numbered in dictionary order according to their radicals and strokes [counts]. Each page of the book shows 100 pairs of a Chinese character and a number in a 10×10 table. The most significant two digits of a code matches the page number, the next digit matches the row number, and the least significant digit matches the column number.” ([Wikipedia](https://en.wikipedia.org/wiki/Chinese_telegraph_code))

---

### How are these input?

<video controls><source src="https://fasiha.github.io/cjk-2021/toshiba.mp4" type="video/mp4"></video>

Notes:

Toshiba typewriter, produced 1940–1954. 1172 total characters ([YouTube](https://www.youtube.com/watch?v=JZcui85b4EE); [Virtual Typewriter Museum](http://www.typewritermuseum.org/collection/brands/index.php3?machine=toshiba&cat=il))

---

#### Use phonetics—IME

Bopomofo is an alphabet for Mandarin and related dialects (as in, real dialects), encoding consonants and vowels and tones, developed in the early 1910s during the Republic of China years. Popular in Taiwan.

<img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/Bopomofo.jpg">

Note:
Image: Taiwanese cell phone [Source](https://commons.wikimedia.org/wiki/File:Bopomofo.jpg)

---

|      |      |       |       |      |
| ---- | ---- | ----- | ----- | ---- |
| bㄅ  | pㄆ  | mㄇ   | fㄈ   |      |
| dㄉ  | tㄊ  | nㄋ   | lㄌ   |      |
| gㄍ  | kㄎ  | hㄏ   |       |      |
| jㄐ  | qㄑ  | tㄒ   |       |      |
| zhㄓ | chㄔ | shㄕ  | rㄖ   |      |
| zㄗ  | cㄘ  | sㄙ   |       |      |
| aㄚ  | oㄛ  | eㄜ   | ehㄝ  |      |
| aiㄞ | eiㄟ | auㄠ  | ouㄡ  |      |
| anㄢ | enㄣ | angㄤ | engㄥ | erㄦ |
| iㄧ  | uㄨ  | iuㄩ  |       |      |

---

Symbols are chunks of “normal” Chinese characters:

`b` ➜ ㄅ, from 勹, which in 包 is pronounced “bāo” (🥟)

`p` ➜ ㄆ, from 攵, which in 攴 is pronounced “pū” (“to tap”)

`m` ➜ ㄇ, which is 冖, pronounced “mì”, the cover radical

`f` ➜ ㄈ, which is 匚, pronounced “fāng”, the right open box radical


---

Pinyin is also an alphabet for Mandarin, encoding consonants and vowels and tones, but developed in the 1950s by the People’s Republic of China, and so had to use entirely different characters: Latin letters.

Easy for English speakers to learn!

|     |                          |
| --- | ------------------------ |
| Q   | “ch” (like Qin dynasty)  |
| C   | “ts” (like Tsai Ing-Wen) |
| X   | “sh 😊” (like Xinjiang)   |
| Sh  | “sh ☹️” (like Shanghai)   |
| Zh  | “j 😊” (like Guangzhou)   |
| J   | “j ☹️”                    |

---

<video controls><source src="https://fasiha.github.io/cjk-2021/chinese-ios.mp4" type="video/mp4"></video>

Notes:

Video: [Fluent in Mandarin](https://www.youtube.com/watch?v=AU3zaoj5_e4)

Due to the high amount of homophony in Mandarin, IME tends to be slower than using non-phonetic input. You type in a string of sounds and usually your smartphone gets the characters right (sentence context, usage history, global patterns), but if not you have to select which character you meant.

This has been a major problem with React and other browser frameworks that want to own text input fields.

- [#3926](https://github.com/facebook/react/issues/3926) complains, “any Chinese characters inputted by Chinese pinyin input method would fire too many renders”. FB dev responds, “this is not a high priority for us right now” (2015, right around when React 0.14.0 was released; still open).
- “some software keyboards on mobile devices also fire composition events for **autocomplete suggestions**. Note that this is even with *normal English input* (latin characters), so the general problem isn’t necessarily restricted to just Chinese Japanese etc IME composition.” (Emphasis in original, [2018](https://github.com/facebook/react/issues/8683#issuecomment-359769270), closed and merged with #3926 by Dan Abramov)

---

#### Use “writing” for input

<img src="https://fasiha.github.io/cjk-2021/radicals.png">

Notes: 

If you’re familiar with *writing* a character (something increasingly rare after leaving school), you can specify its *component pieces* for rapid lookup of a character.

Image: Lunde, *CJKV Information Processing*.

---

<img src="https://fasiha.github.io/cjk-2021/Wubi_keyboard-cut.jpg" height="300px">

Notes:

Image: a Wubi keyboard. [Source](https://commons.wikimedia.org/wiki/File:Wubi_keyboard-cut.png)

There’s only so many of these components, and Each key on a QWERTY keyboard maps to a certain set of character components (often themselves characters).

You type the components in the same order that you write them (stroke order being fixed, and heavily drilled in school)

You’re not limited by homophony: almost all characters have a unique representation with four or fewer keystrokes

Faster typing but it’s a skill that needs practice

---

#### Handwriting recognition

<video controls><source src="https://fasiha.github.io/cjk-2021/handwriting.mp4" type="video/mp4"></video>

Notes:

Video: [Fluent in Mandarin](https://www.youtube.com/watch?v=AU3zaoj5_e4) again

Introduced mid-2008 with iOS 2.0 (recall copy-paste was added iOS 3.0, mid-2009).

Rather than develop phonetic pinyin-to-characters libraries for the many languages of the Sinosphere—Cantonese, Shanghaiese, Fujianese, Hakka, etc.—handwriting recognition allows all these speakers to readily enter text.

Most recently: speech-to-text.

> Simplified vs traditional?—hold on to that question, it’s wierder than you think

---

## Japanese 日本語

<img src="https://upload.wikimedia.org/wikipedia/commons/7/71/Koku_Saitcho_shounin.jpg">

Notes:

Image: *Cry for the Noble Saichō* by Emperor Saga on the death of Saichō, circa 822 CE. Saichō and a fellow Buddhist monk Kūkai are said to have introduced tea to Japan from China. [Source](https://en.wikipedia.org/wiki/File:Koku_Saitcho_shounin.jpg)

### Chinese characters (kanji)

Japanese as a spoken language is totally unrelated to Chinese!

But Japan was a cultural vassal of China for much of the last 1500 years, like all nations that orbited the Middle Kingdom (“middle” as in, middle of the world), so it adopted (and adapted!) *both* Chinese characters *and* those characters’ Chinese pronunciation.

---

<img src="https://fasiha.github.io/cjk-2021/kirin.jpg">

麒麟 = “qí lín” vs “ki rin” — “🦒”

漢字 = “hàn zì” vs“kan ji” — “Chinese character”

天使 = “tiān shǐ” vs “ten shi” — “👼”

Notes:

Image: [MIKI Yoshihito](https://www.flickr.com/photos/mujitra/2392215954/)

As characters were imported from China over the Tang and Song and later dynasties, some were used to write native Japanese words, but many represented totally new concepts lacking native equivalents (e.g., Buddhist terms), and Japanese scholars pronounced these the same as the Middle Chinese.

Over the last thousand years, Chinese loanwords have been thoroughly Japanified: the majority of Chinese characters have both a Chinese-derived pronunciation and a Japanese-native pronunciation.

A gentle analogy may be—English often has a more learned French/Latin-derived term for something and a down-to-earth Norse-derived equivalent: inquire/ask, commence/begin, purchase/buy ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Germanic_and_Latinate_equivalents_in_English) has a ton of these!).

Students begin learning to write Chinese characters in first grade, and by the time they finish high school, they are tested on mastery of 2,136 characters’ readings. These are an integral part of Japanese writing but not the whole story.

---

<img src="https://fasiha.github.io/cjk-2021/Murasaki_Shikibu_Komatsuken.jpg">

Notes:

Image: Murasaki Shikibu finished *The Tale of Genji* circa 1012 CE. Though very popular, the earliest extant manuscript is from more than 200 years later. It is likely to have been written in both kanji and hiragana. Woodblock print by Komatsuken in 1765. [Source](https://collections.mfa.org/objects/233977)

### Japanese syllabaries

Over a thousand years ago, Japanese men and women developed their own syllabaries, like bopomofo, that encode the sounds of spoken Japanese with simplified Chinese characters.

Heian court ladies developed hiragana: ひらがな (“hiragana” in hiragana; in katakana: ヒラガナ). More rounded and smooth, even when written with a brush.

Buddhist monks developed katakana: カタカナ (“katakana” in katakana; in hiragana: かたかな): sharp and angular.

Each has 46 symbols (encoding the 5×10 combinations of 5 vowels and 10 basic consonants, less some obsolete pairings), and are fully interchangeable.

---

|     | ａｉｕｅｏ | ａｉｕｅｏ |
| --- | ---------- | ---------- |
| ∅   | あいうえお | アイウエオ |
| k   | かきくけこ | カキクケコ |
| s   | さしすせそ | サシスセソ |
| t   | たちつてと | タチツテト |
| n   | なにぬねの | ナニヌネノ |
| h   | はひふへほ | ハヒフヘホ |
| m   | まみむめも | マミムメモ |
| y   | や・ゆ・よ | ヤ・ユ・ヨ |
| r   | らりるれろ | ラリルレロ |
| w   | わ・・・を | ワ・・・ヲ |
| n   | ん         | ン         |

Notes:

Each of these has very specific usage in modern Japanese orthography. 

- Hiragana is used for many words lacking Chinese characters and to “fill in” the pronunciation of a word that is spelled only partly with a Chinese character.
- Katakana is used for more recent loan words from English, and for emphasis.
- Combined with Latin letters (“rōmaji”), any given Japanese sentence will have *four* scripts.

---

- 走る (read “hashiru”, “to run”) = 
  - 走 (Chinese character pronounced “hashi”) +
  - る (hiragana, “ru”)
- 話す (read “hanasu”, “to speak”) = 
  - 話 (Chinese character pronounced “hana”) + 
  - す (hiragana, “su”)

・・・

ブルームバーグ (“Burūmubāgu” for “Bloomberg”),

---

<video width="500px" controls><source src="https://fasiha.github.io/cjk-2021/flick.mp4" type="video/mp4"></video>

Notes:

### Flick input

Because Japanese has five vowels per consonants, and there are ten-ish consonants, a rather elegant solution is
- use a keypad-like layout for consonants, where each consonant 
- unfolds into a north/south/east/west choice to pick the vowel.

If you hold down the consonant long enough, you see the four directional vowels to choose from via a swipe, with the fifth being “no swipe”.

Typing fast, you don’t need to wait for the vowel menu to unfold, you just “flick”.

Same efficiency hit as pinyin/bopomofo: usually the auto-suggestion has the Chinese characters you want but sometimes you have to stop and help it break homophony.

---

<img src="https://fasiha.github.io/cjk-2021/ios-english.jpg">

Notes:

[Ben Kuhn](https://twitter.com/benskuhn/status/1361736200734855171) quotes *Creative Selection* by Ken Kocienda on this early design for the iPhone keyboard: “tap to get the top letter, swipe left/right to get the bottom letters”.

---

### Natural language processing

<img src="https://fasiha.github.io/cjk-2021/ln.jpg">

Notes:

Image: Makoto Shinkai, 君の名は。 (*Your Name.*) light novel.

Japanese, like Chinese, doesn’t use spaces to separate words. This makes segmentation a challenging machine-learning-intensive pre-processing step to natural language processing (NLP)

When you double-click Japanese text on desktop or long-press on mobile, the app usually does an ok job selecting what you think of as a “word”: Safari, Chrome, Word, etc., have built-in dictionaries to decide word boundaries.

Some (Firefox, Notepad) just select runs of adjacent hiragana/katakana/Chinese characters. 

Others though ([VS Code](https://github.com/Microsoft/vscode/issues/50045)) just select the whole line 😢.

---

## Korean 朝鮮語

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Hunminjeongum.jpg">

Notes:

Image: opening page of 訓民正音 (훈민정음, “hun min jeong eum” in Korean, “kun min sei on” in Japanese, “Instructions to the nation for correct pronunciation”) by Sejong the Great, 1446. [Source](https://commons.wikimedia.org/wiki/File:Hunminjeongum.jpg)

Korean is linguistically *another* totally different language from Japanese and from Chinese, but due to millenia of cultural diffusion with China and unfortunately decades of occupation and colonization by Japan, a lot of vocabulary has transferred to it from both of these.

Like Japanese, Korean’s upper register is filled with words imported from Chinese during ancient times.

### Chinese characters (hanja)

---

Examples

- 人間
  - “nin gen” (Japanese)
  - “in gan” (Korean)
  - “rén jiān” in modern Mandarin
  - “ngìn kiên” in Hakka (means “human”, as opposed to a nine-tailed fox)
- 約束
  - “yaku soku” (Japanese), 
  - “yak sok” (Korean)
  - “yuē shù” in modern Mandarin
  - “yok suk” in Hakka (means “promise”)

---

### Hangul

<img src="https://fasiha.github.io/cjk-2021/sejong.jpg">

Notes:

Image: 9.5 meter tall statue of Sejong the Great installed in 2009 in Seoul. [Republic of Korea](https://www.flickr.com/photos/koreanet/4273003660)

However, unlike in Japanese, the Koreans have *hangul*, a phonetic writing system. This is a Big Deal.

King Sejong the Great is said to have personally perfected hangul in 1443 and encouraged its spread despite the learned elite’s dislike. (He is also a perennial star and side character in Korean dramas.)

Hangul Day is a national holiday in both Koreas.

It’s a matter of national pride that this writing system is “perfect”: it’s logical, compact, easy to learn, and maps to the sounds of Korean very well.

---

ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ

ㅏ ㅑ ㅓ ㅕ ㅗ ㅛ ㅜ ㅠ ㅡ ㅣ

Notes:

Hangul is made up of twenty-four symbols (called *jamo*): fourteen consonants (ㄱㄴㄷㄹㅁ…) and ten vowels (ㅏㅑㅓㅕㅗ…), plus several pairs of two-consonant and two-vowel combinations.

These symbols’ shapes are said to mimic the shape of the mouth when producing them.

---

<img src="https://fasiha.github.io/cjk-2021/hangul-placement.png">

Notes:

Image: excerpt from a much more detailed chart of Hangul letter order from [Wikipedia](https://commons.wikimedia.org/wiki/File:Hangeul_letter_order.svg).

But the cool thing is, you don’t write these out linearly like bopomofo or hiragana or Latin—rather, these jamo combine into syllables in *two dimensions*.

This can happen because Korean morphemes (the smallest unit of meaning) are invariably made up of 
- an *initial* consonant (single or doubled),
- a *medial* vowel (or diphthong), and
- optionally, a *final* consonant or consonant cluster. 

These snap together like Legos, following straightforward rules depending on the length of the morpheme.

Hangul did not replace Chinese characters (hanja), then or now. Hangul only became official due to nationalism in the late 1800s. 

Today, even high schoolers only learn Chinese characters in elective courses.

Newspapers of record tend to have ~5% Chinese characters, with political news often having (much) more.

Korean tends to be written with spaces so front-end NLP is easier than Chinese or Japanese.

---

## Ⓤ🅽ℐ𝗖𝕆𝖉𝙴

Let’s talk about Unicode.

Notes:

A monumental achievement, today with Unicode 13 containing >140,000 code points.

But it’s driven by committees of experts, who are falliable.

### The hangul trainwreck

Unicode 1.0 released in 1991 had 2,350 hangul syllables and jamo. This is far fewer than the full set of syllables that can be constructed. The rest were assumed to be typed and rendered by combining individuals, following the design of the Korean character set (KS X 1001) that Unicode followed.

Unicode 1.1 in 1993 added 4,300 more syllables, following KS X 1002 and another partial set, again far fewer than needed by modern Korean.

Unicode 1.0 was never an official or national standard, and 1.x were tentative. Both are obsolete.

Unicode 2.0 in in 1996 finally threw out all ~6,500 hangul characters and created the Hangul Syllables block in a totally different part of the plane containing all ~11,000 hangul and jamo used today. The obsolete hangul code points are now used for rare Chinese characters…

We give each full hangul syllable its own code point because, in UTF-8, 훯 (“hwolh”) is three bytes, and each of its combining components, ᄒ (“h”) and ᅯ (“wo”) and ᆶ (“lh”), is also three bytes.

In fact, try copy-pasting these three simpler hangul and then removing the spaces between them: ᄒ / ᅯ / ᆶ. Your operating system will seamlessly combine them into the larger Unicode code point (party trick via [Gernot Katzer](http://www.gernot-katzers-spice-pages.com/var/korean_hangul_unicode.html)).

---

### “Han Unification”

<img src="https://fasiha.github.io/cjk-2021/Source_Han_Sans_Version_Difference.svg">

Notes:

---

<img src="https://fasiha.github.io/cjk-2021/cjkv-table-3-99.png">

Notes:

Image: Lunde, *CJKV Information Processing*.

Unicode 2.0 also added ~21,000 Chinese characters; 3.0 in 1999 added ~6,500; 3.1 in 2001 added another ~43,000 (Table 3-82 in *CJKV Information Processing*).

From the beginning, their goal was to “unify all ideographs from the many CJKV national character set standards into a single set of ideographs” (Lunde, p. 155) and this came to have the problematic name, “Han unification”.

“Unification” sought to tame the bewildering amount of variation of characters across East and Southeast Asia such that characters that had the same
1. meaning and
2. abstract shape,

but varied by typeface (font) were assigned to a single Unicode point.

But this turned out to be a hard problem, from many linguistic and historical perspectives. Lunde: “Unfortunately, early standards were inconsistent in their encoding models for ideographs, and some still are” (p. 159).

At various points Unicode incorrectly failed to unify characters *and* was incorrectly too eager to unify.

---

- 辶 can look like
- ⻌ (PRC—simplified Chinese characters),
- ⻍ (Japan, Korea), or
- ⻎ (Taiwan, Hong Kong—traditional Chinese characters).

All four of these are their own Unicode code points, and there’s a unified code point, 辶.

Notes:

Via [@ken_lunde](https://twitter.com/ken_lunde/status/540136581407834113)

Unification has been erratic even for characters that the PRC simplified in the 1950s and 1960s.

---

We haven’t talked about ⥌[vertical scripts](https://netflixtechblog.com/implementing-japanese-subtitles-on-netflix-c165fbe61989)⥍, [fonts](https://monocle.com/radio/shows/monocle-on-design/extra-236/) 🆃, [emoji](https://www.youtube.com/watch?v=9BaLTBTqHmw) (^‿^), or [waffles](https://www.theverge.com/21327599/how-to-make-emoji-yawning-face-waffle-proposal-unicode) 🥞.
