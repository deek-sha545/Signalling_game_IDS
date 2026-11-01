#!/usr/bin/env python3
"""
Unit tests for the Bayes belief update of the signaling extension.
Run from src/:   IDS_CONFIG=signaling_toy.conf ../venv/bin/python -m unittest test_signaling_belief -v
"""
import configparser
import math
import unittest

import numpy as np

import signaling as S
from model import Model


def cfg(**over):
    c = configparser.ConfigParser()
    c.read_dict({'signaling': dict({'types': 'noisy,stealthy', 'prior': '0.5,0.5',
                                    'noisy_kind': 'noisy', 'noisy_scale': '2.0', 'noisy_spread': '0.5',
                                    'stealthy_kind': 'stealthy', 'stealthy_scale': '0.5'}, **over)})
    return S.read_type_cfg(c)


class TestBelief(unittest.TestCase):

    def test_likelihood_matches_simulation(self):
        """The exact likelihood P(N | type) must match the frequency of N produced by model.py."""
        g = S.SignalingGame('fraud', 20, 2, cfg())
        alpha = np.array([[0.6, 0.2, 0.3], [0.1, 0.5, 0.4]])
        f = S.BeliefFilter(g, alpha)
        np.random.seed(0)
        target = None
        for k in range(g.K):
            m = g.type_models[k]
            counts = {}
            n = 40000
            for _ in range(n):
                s = Model.State(m)
                s = m.next_state('old', s, [[0] * g.T], list(alpha[k]))
                key = tuple(s.N[0])
                counts[key] = counts.get(key, 0) + 1
            # compare on the 5 most frequent outcomes
            for key, c in sorted(counts.items(), key=lambda x: -x[1])[:5]:
                p_exact = math.exp(f.loglik(np.array(key))[k])
                se = math.sqrt(p_exact * (1 - p_exact) / n)
                self.assertLess(abs(c / n - p_exact), 5 * se + 1e-4, (k, key, c / n, p_exact))

    def test_posterior_is_bayes_rule(self):
        g = S.SignalingGame('fraud', 20, 2, cfg())
        f = S.BeliefFilter(g, [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]])
        N = np.array([12, 50, 40])
        ll = f.loglik(N)
        prior = np.array([0.3, 0.7])
        post, off = f.update(prior, N)
        expect = prior * np.exp(ll - ll.max())
        self.assertFalse(off)
        np.testing.assert_allclose(post, expect / expect.sum(), rtol=1e-8)

    def test_identical_types_keep_prior(self):
        """With separability 0 both types are identical: the belief must not move."""
        g = S.SignalingGame('suricata', 1000, 120, cfg(), separability=0.0)
        f = S.BeliefFilter(g, [[0.2] * g.A, [0.2] * g.A])
        b = g.prior.copy()
        for N in ([7200, 44100, 1600, 7300, 17400, 4000, 10200], [8000, 44000, 2500, 7400, 17400, 4100, 10900]):
            b, _ = f.update(b, np.array(N))
        np.testing.assert_allclose(b, g.prior, atol=1e-9)

    def test_offpath_keeps_belief(self):
        """snort alert type 2 has NO false alerts; an odd count impossible for every type is off-path."""
        g = S.SignalingGame('snort', 1000, 125, cfg())
        f = S.BeliefFilter(g, [[0.5, 0.5], [0.5, 0.5]])
        b0 = np.array([0.4, 0.6])
        b, off = f.update(b0, np.array([10274000, 3]))
        self.assertTrue(off)
        np.testing.assert_allclose(b, b0)

    def test_huge_counts_no_nan_and_converges(self):
        """snort false alerts ~ 10 million per step: no NaN, and belief converges to the true type."""
        g = S.SignalingGame('snort', 1000, 125, cfg())
        alpha = [[0.4, 1.0], [0.4, 1.0]]
        f = S.BeliefFilter(g, alpha)
        for true_k in range(2):
            np.random.seed(true_k)
            m = g.type_models[true_k]
            s = Model.State(m)
            b = g.prior.copy()
            for _ in range(30):
                s = m.next_state('old', s, [[0] * g.T], alpha[true_k])
                b, off = f.update(b, np.array(s.N[0]))
                self.assertTrue(np.all(np.isfinite(b)))
            self.assertGreater(b[true_k], 0.99)

    def test_types_differ(self):
        g = S.SignalingGame('suricata', 1000, 120, cfg())
        noisy = np.array([a.pr_alert for a in g.type_models[0].attack_types]).sum()
        stealthy = np.array([a.pr_alert for a in g.type_models[1].attack_types]).sum()
        self.assertGreater(noisy, stealthy)
        for a0, a1 in zip(g.type_models[0].attack_types, g.type_models[1].attack_types):
            self.assertEqual(a0.loss, a1.loss)
            self.assertEqual(a0.cost, a1.cost)


if __name__ == '__main__':
    unittest.main()
