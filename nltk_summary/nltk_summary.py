import argparse

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict


"""
This module uses NLTK to create a summarizer with a sentence count limit to summarize a text.

Example:
    CLI query to run this tokenizer:

        $ python nltk_summary.py airline.txt

Module does the following:
1) sanitizes the text by removing unnecessary spaces and paragraph breaks
2) tokenizes the text into words and sentences, and then rank orders sentences by highest frequency of both
3) summarizes the text by listing the top sentences, given the sentence count limit (set at 4 for default)
"""



def main():
    args = parse_arguments()
    content = read_file(args.filepath)
    content = sanitize_input(content)
    sentence_tokens, word_tokens = tokenize_content(content)
    sentence_ranks = score_tokens(word_tokens, sentence_tokens)

    return summarize(sentence_ranks, sentence_tokens, 2)

def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.read()

    except IOError as e:
        print("Fatal Error: File ({}) could not be located or is not readable.".format(path))


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='File name of text to summarize')
    parser.add_argument('-l', '--length', default=4, help='Number of sentences to return')
    args = parser.parse_args()

    return args


def sanitize_input(data):
    """Function to clean up text.

        Removes unneeded paragraphs, tabs, scpaces.

        Args:
            param1 (str): The text

        Returns:
            str: The cleaned up text
        """
    replace = {
        ord('\f') : ' ',
        ord('\t') : ' ',
        ord('\n') : ' ',
        ord('\r') : None
    }

    return data.translate(replace)


def tokenize_content(content):
    """Function to find the stop words, and then use these to word and sentence tokenize

        Removes unneeded stop words, makes all words lowercase, then sentence tokenizes and word tokenizes all

        Args:
            content (str): The sanitized text

        Returns:
            filterd_words: list of all words
            sentence_tokens: list of all sentences
        """
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(content.lower())

    return [
        sent_tokenize(content),
        [word for word in words if word not in stop_words]
    ]


def score_tokens(filterd_words, sentence_tokens):
    """Function to score the word tokens

        Tells you what words happen most, and then rank the sentences.
        The value of ranking will then contain key values of the sentence’s numeric position, and their score.

        Args:
            filterd_words: list of all words
            sentence_tokens: list of all sentences

        Returns:
            ranking: a dict with all the sentences ranked based on word frequency:
        """
    word_freq = FreqDist(filterd_words)

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]

    return ranking


def summarize(ranks, sentences, length):
    """Function to construct our summary from the N highest scoring sentences where N is our desired length.


        Args:
            ranks (list): sentence rank list
            sentences (dict): sentence tokens
            length (integer): How many sentences to output
        Returns:
            str: The summary - top sentences joined together
        """
    if int(length) > len(sentences):
        print("Error, more sentences requested than available. Use --l (--length) flag to adjust.")
        exit()

    indexes = nlargest(length, ranks, key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indexes)]
    return ' '.join(final_sentences)


if __name__ == "__main__":
    print(main())