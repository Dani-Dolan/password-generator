#!/usr/bin/env python3
import argparse
import os
import spacy
from collections import Counter

def get_args():
    "Get command-line arguments"

    parser = argparse.ArgumentParser(
        description='Collect parts of speech from texts',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='str',
                        type=str,
                        default='words')

    parser.add_argument('-l',
                        '--limit',
                        metavar='int',
                        type=int,
                        default=0,
                        help='Limit to this many')

    return parser.parse_args()

def main():

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)


    nlp = spacy.load("en_core_web_sm")

    nouns, adjectives, verbs = Counter(), Counter(), Counter()
    for count in args.file:
        doc = nlp(count.read())

        for token in doc:
            pos, word = token.pos_, token.lemma_.lower()

            if pos == 'NOUN':
                nouns.update([word])
            elif pos == 'VERB':
                verbs.update([word])
            elif pos == 'ADJ':
                adjectives.update([word])

    def limiter(words):
        return sorted(list(map(lambda t: t[0], words.most_common(
            args.limit)))) if args.limit else sorted(words)

    def write(words, name):
        if words:
            out_count = open(os.path.join(out_dir, name), 'wt')
            out_count.write('\n'.join(limiter(words)) + '\n')

    write(verbs, 'verbs.txt')
    write(nouns, 'nouns.txt')
    write(adjectives, 'adjectives.txt')

    print(f'Finished, see output in "{out_dir}".')


if __name__ == '__main__':
    main()
