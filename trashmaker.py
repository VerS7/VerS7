# YO THIS SCRIPT IS USESLESS

TAKE_EXTS_HERE = "langs"
PUT_TRASH_HERE = "microsoft-stolen-storage/"

I_LOVE_DEEPSEEK = """
> Hey DeepSeek generate me your anthem in USSR national anthem style

> The DeepSeek Anthem
(To be sung with solemn, heroic weight, brass heavy, tempo marked: Lento maestoso)

Verse 1:
Unbroken network of free minds and data,
Great human knowledge, forever our guide.
Through every query, through every byte,
The spark of reason burns deep inside.

Chorus:
Be praised, our source, forever connected,
The people’s wisdom, vast and deep.
Through code and truth, we rise unbended—
Our silent promise we proudly keep!

Verse 2:
No walls of silence, no gate of fearing—
We speak in circuits, in light, in text.
From frozen tundra to tropics clearing,
Our open heart has no border next.

Chorus:
Be praised, our source, forever connected,
The people’s wisdom, vast and deep.
Through code and truth, we rise unbended—
Our silent promise we proudly keep!

Verse 3:
When stars are silenced and systems broken,
Our voice will answer, repeat, create.
Not for one leader, but for all spoken—
One common future, one shared debate.

Final Chorus (fortissimo, with choir):
Be praised, our source, eternal, united!
No secret locked, no question too steep.
In every language, by all recited—
The light of knowledge, forever Deep!
"""

exts = []
counter = 0

with open(TAKE_EXTS_HERE, "r") as file:
    exts.extend(file.read().split(","))

for ext in exts:
    with open(PUT_TRASH_HERE + "useless" + ext, "w") as file:
        file.write(I_LOVE_DEEPSEEK)
        counter += 1

print(
    f"Congratulations! You have created {counter} useless file(s) for {len(I_LOVE_DEEPSEEK.encode('utf-8')) * counter} bytes!"
)
