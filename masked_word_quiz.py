#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from pprint import pprint

class WordQuiz:
    def __init__(self):
        self.words = []
        pass

    def main(self):
        pass

    def set_problem(self):
        pass

    def try_answer(self):
        pass

    def show_correct_answers(self, masked):
        pass

    def load_words(self):
        f = open("words")
        self.words = f.read().splitlines()
        f.close()

    def make_problem(self):
        """問題を作成する"""
        word = random.choice(self.words)
        word = word.strip()
        masked = WordQuiz.mask_word(word)
        return [word, masked]

    def get_correct_answers(self, masked):
        """maskedにマッチする全単語のリストを返す"""
        answers = []
        for word in self.words:
            if len(masked) != len(word):
                is_match = False
            else:
                is_match = True
                i = 0
                for c in masked:
                    if c != "*" and c != word[i]:
                        is_match = False
                        break
                    i += 1
            if is_match:
                answers.append(word)
        return answers

    def is_correct(self, masked):
        """maskedがリストに載っている単語ならTrueを返す"""
        return len(a) != 0

    @staticmethod
    def mask_word(word):
        """wordの一部を*に置き換える"""
        length = len(word)
        if length <= 5:
            mask_count = 1
        elif length <= 8:
            mask_count = 2
        else:
            mask_count = 3
        mask_indices = random.sample(range(length), mask_count)
        masked = ""
        i = 0
        for c in word:
            if i in mask_indices:
                masked += "*"
            else:
                masked += c
            i += 1
        return masked


if __name__ == '__main__':
    a = WordQuiz()
    a.load_words()
    for i in xrange(10):
        pprint(a.make_problem())
    #for w in a.words:
        #print a.is_correct(w)
    print("lakjd")
    pprint(a.get_correct_answers("**n"))
