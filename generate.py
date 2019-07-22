import os

def get_symbols(line):
    codepoints = line.split(';')[0].strip().split()
    keywords = ' '.join(line.split('#')[1].strip().split(' ')[1:])
    return (codepoints, keywords)


def get_emoji(codepoint):
    return chr(int("0x" + codepoint, 16))


def format_line(codepoints, desc):
    return "{}|{}".format(desc, ''.join([get_emoji(x) for x in codepoints])).lower()


with open("emoji-test.txt") as f:
    emoji_file = f.read()

emoji = [x for x in emoji_file.split('\n') if not x.startswith("#") and x]

emoji_list = [get_symbols(x) for x in emoji]

path = os.path.join(os.environ["HOME"], '.config/emoji')
if not os.path.exists(path):
    open(path, 'x').close()

with open(path, 'w') as f:
    for emoji in emoji_list:
        f.write(format_line(*emoji) + "\n")
