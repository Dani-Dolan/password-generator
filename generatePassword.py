#/usr/bin/env python3
import argparse
import random
import re
import string

def get_args():
    "command-line arguments"

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        metavar='num_passwords',
                        type=int,
                        default=3,
                        help='Number of Passwords to Generate')

    parser.add_argument('-w',
                        '--num_words',
                        metavar='num_words',
                        type=int,
                        default=4,
                        help='Number of Words for Password')

    parser.add_argument('-m',
                        '--min_lengthWord',
                        metavar='minimum',
                        type=int,
                        default=3,
                        help='Minimum Word Length')

    parser.add_argument('-x',
                        '--max_lengthWord',
                        metavar='maximum',
                        type=int,
                        default=6,
                        help='Maximum Word Length')

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        help='Random Seed')

    parser.add_argument('-l',
                        '--leetSpeak',
                        action='store_true',
                        help='Leet Speak Letters')

    return parser.parse_args()

def main():
    args = get_args()
    random.seed(args.seed)
    words = set()

    def lengthWord(word):
        return args.min_lengthWord <= len(word) <= args.max_lengthWord

    for count in args.file:
        for line in count:
            for word in filter(lengthWord, map(removeNonWord, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = [
        ''.join(random.sample(words, args.num_words)) for _ in range(args.num)
    ]

    if args.leetSpeak:
        passwords = map(leetSpeak, passwords)

    print('\n'.join(passwords))


def removeNonWord(word):
    "Remove non-word characters"

    return re.sub('[^a-zA-Z]', '', word)


def leetSpeak(text):
    """leetSpeak"""

    text = randomtxt(text)
    xform = str.maketrans({
        'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'
    })
    return text.translate(xform) + random.choice(string.punctuation)


def randomtxt(text):

    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text))


if __name__ == '__main__':
    main()
