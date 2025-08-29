St. John's College, a [Great Books school](https://www.nytimes.com/2018/09/11/opinion/contrarian-college-stjohns.html), has a class that spans four years called Seminar.

It consists entirely of reading and talking about books in the Western "canon" — or, at least, one conception of that canon.

This graph shows all the times each author mentions another in the texts we read.
  
---

Homer——85——>Plato should be read as "Homer is mentioned by Plato 85 times in the seminar books."
Hovering over an edge in .svg should show you more information about that edge.


  ---

I wrote a Python program to read the texts, count the word frequencies for each text, find author matches and finally generate the graph with pygraphviz. I am more familiar with C-family languages than Python, so apologies for any non-pythonic idioms.
  
---
There were many false positives. For example, Chaucer mentions "Bacon", but he means the food, not the seminar author Francis Bacon. But Marx refers to both the food and the philosopher. Swift is such a common word that I didn't even try with him. Adam Smith I had to do manually.
I relied largely on my memory of these texts to find and resolve the false positives, so it's likely that I missed some. Hence, this graph is **not intended to serve as a reference.**

Instead, it's a bird's eye view of how thinkers (in one tradition of thought) built on each other over time, creating one interconnected edifice of the mind.

---

The reading list is based off of Annapolis 24-25. I used the entire texts except where the selections were explicitly stated (for Plutarch's Lives, for example).
I did not include The Bible, since it's hard to ascribe an "author" to the books in it.

Not all the books I used are in this repo since many are copyrighted, or their translations are.
