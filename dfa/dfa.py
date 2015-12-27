#!/usr/bin/python2
# -*- coding: utf-8 -*-

# a finite set of states (Q)
# a finite set of input symbols called the alphabet (Σ)
# a transition function (δ : Q × Σ → Q)
# a start state (q0 ∈ Q)
# a set of final/accept states (F ⊆ Q)

from sets import Set

class DFA():
    def __init__(self):
        self.states = Set()
        self.alphabet = Set()
        self.transition_table = {}
        self.accept_states = Set()
        self.start_state = None
        self.state_id = 0

    def get_start_state(self):
        return self.start_state

    def accept_p(self, state):
        return state in self.accept_states

    def transition(self, state, symbol):
        return self.transition_table.get((state, symbol))

    def add_state(self):
        self.states.add(self.state_id)
        self.state_id += 1
        return self.state_id - 1

    def add_n_state(self, n):
        for _ in xrange(n):
            self.add_state()

    def add_transition(self, from_state, symbol, to_state):
        self.alphabet.add(symbol)
        self.transition_table[(from_state, symbol)] = to_state
        return self

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.add(state)

class DFA_Matcher():
    def __init__(self, dfa):
        self.dfa = dfa
        self.current_state = dfa.get_start_state()

    def reset(self):
        self.current_state = self.dfa.get_start_state()

    def match(self, symbol_list):
        for each in symbol_list:
            self.apply_symbol(each)
        return self.dfa.accept_p(self.current_state)

    def apply_symbol(self, symbol):
        self.current_state = self.dfa.transition(self.current_state, symbol)
        return self.current_state

    def success_p(self):
        return self.dfa.accept_p(self.current_state)
