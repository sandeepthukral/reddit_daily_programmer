import unittest


wordlist = set(open("enable", "r").read().split())


def remove_char(i, string):
    return string[:i] + string[i + 1:]


def substrings(string):
    results = set()
    for index in range(len(string)):
        results.add(remove_char(index, string))
    return results


def funnel(string1, string2):
    if len(string2) != len(string1) - 1:
        return False
    elif string2 in substrings(string1):
        return True
    else:
        return False


def bonus1(string, words):
    candidates = substrings(string)
    results = []
    for candidate in candidates:
        if candidate in words:
            results.append(candidate)
    return results


def bonus2(words):
    words = set([x for x in words if len(x) > 3])

    max_length = max(len(word) for word in words)
    length_sets = []
    for length in range(4, max_length + 1):
        length_set = set()
        for word in words:
            if len(word) == length:
                length_set.add(word)
        length_sets.append(length_set)

    results = []
    for index, length_set in enumerate(length_sets):
        if index == 0:
            continue
        else:
            for word in length_set:
                if len(bonus1(word, length_sets[index - 1])) == 5:
                    results.append(word)
    return results


class TestWordFunnel(unittest.TestCase):
    """Given two strings of letters, determine whether the second can be made
    from the first by removing one letter. The remaining letters must stay in
    the same order."""

    def test_examples(self):
        self.assertTrue(funnel("leave", "eave"))
        self.assertTrue(funnel("leaves", "leave"))
        self.assertTrue(funnel("reset", "rest"))
        self.assertTrue(funnel("dragoon", "dragon"))
        self.assertFalse(funnel("eave", "leave"))
        self.assertFalse(funnel("sleet", "lets"))
        self.assertFalse(funnel("skiff", "ski"))

    def test_bonus1(self):
        self.assertEqual(sorted(bonus1("dragoon", wordlist)), sorted(["dragon"]))
        self.assertEqual(sorted(bonus1("boats", wordlist)), sorted(["oats", "bats", "bots", "boas", "boat"]))
        self.assertEqual(sorted(bonus1("affidavit", wordlist)), sorted([]))

    def test_bonus2(self):
        self.assertEqual(len(bonus2(wordlist)), 28)


if __name__ == "__main__":
    unittest.main()