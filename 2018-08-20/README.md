## Challenge

Given two strings of letters, determine whether the second can be made from the first by removing one letter. The remaining letters must stay in the same order.

##Examples

```
funnel("leave", "eave") => true
funnel("reset", "rest") => true
funnel("dragoon", "dragon") => true
funnel("eave", "leave") => false
funnel("sleet", "lets") => false
funnel("skiff", "ski") => false
```

## Optional bonus 1
Given a string, find all words from the enable1 word list that can be made by removing one letter from the string. If there are two possible letters you can remove to make the same word, only count it once. Ordering of the output words doesn't matter.

```
bonus("dragoon") => ["dragon"]
bonus("boats") => ["oats", "bats", "bots", "boas", "boat"]
bonus("affidavit") => []
```

## Optional bonus 2
Given an input word from enable1, the largest number of words that can be returned from bonus(word) is 5. One such input is "boats". There are 28 such inputs in total. Find them all.

Ideally you can do this without comparing every word in the list to every other word in the list. A good time is around a second. Possibly more or less, depending on your language and platform of choice - Python will be slower and C will be faster. The point is not to hit any specific run time, just to be much faster than checking every pair of words.


## My notes
I found it easy to solve the main challenge and the bonus. I did them rather the same way as done in the community.

For bonus 3, I did what I could. But it was pathetically slow.
Then when I looked at this community solutioon, I realized how it has been filtered down to make the comparison much faster.
So if I have a letter on length n, you can make n words of length n-1.
So if my input is of length n, I should compare it only with words of size n-1 from the complete list.
That optimization saves the day.