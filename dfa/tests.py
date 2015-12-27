#1/usr/bin/python2
# -*- coding: utf-8 -*-

from dfa import DFA, DFA_Matcher

import unittest

class TestDFAMatch(unittest.TestCase):

    def test_match(self):
        test_dfa = DFA()
        test_dfa.add_n_state(3)
        test_dfa.set_start_state(0)
        test_dfa.add_accept_state(0)
        test_dfa.add_transition(0, 1, 1).add_transition(0, 0, 0)\
                .add_transition(1, 1, 0).add_transition(1, 0, 2)\
                .add_transition(2, 1, 2).add_transition(2, 0, 1)

        matcher = DFA_Matcher(test_dfa)
        accept_tests = \
                [
                    [],
                    [1, 0, 0, 1],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [1, 1]
                ]
        reject_tests = \
                [
                    [1, 0, 1, 1],
                    [0, 0, 1],
                    [1, 1, 1],
                    [1, 0, 0]
                ]


        for each in accept_tests:
            matcher.reset()
            self.assertTrue(matcher.match(each))
        for each in reject_tests:
            matcher.reset()
            self.assertFalse(matcher.match(each))


class TestDFA(unittest.TestCase):

    def test_construction(self):
        test_dfa = DFA()
        test_dfa.add_n_state(3)
        self.assertTrue(0 in test_dfa.states)
        self.assertTrue(1 in test_dfa.states)
        self.assertTrue(2 in test_dfa.states)
        test_dfa.set_start_state(0)
        test_dfa.add_accept_state(0)
        test_dfa.add_transition(0, 1, 1)
        test_dfa.add_transition(0, 0, 0)
        test_dfa.add_transition(1, 1, 0)
        test_dfa.add_transition(1, 0, 2)
        test_dfa.add_transition(2, 1, 2)
        test_dfa.add_transition(2, 0, 1)

        self.assertTrue(test_dfa.accept_p(0))
        self.assertFalse(test_dfa.accept_p(1))
        self.assertFalse(test_dfa.accept_p(2))

        self.assertEqual(test_dfa.transition(0, 1), 1)
        self.assertEqual(test_dfa.transition(1, 1), 0)
        self.assertEqual(test_dfa.transition(1, 1), 0)
        self.assertEqual(test_dfa.transition(1, 0), 2)
        self.assertEqual(test_dfa.transition(2, 0), 1)
        self.assertEqual(test_dfa.transition(2, 0), 1)

if __name__ == '__main__':
    unittest.main()
