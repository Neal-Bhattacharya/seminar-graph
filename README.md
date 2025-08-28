St. John's College, a small liberal arts college, has a class that spans four years called "Seminar"
It consists entirely of reading and talking about books in the Western "canon" — at least, one conception of that canon.
This graph shows all the times each author mentions another in the texts we read.
The reading list is based off Annapolis 24-25. I used the entire texts except where the selections were explicitly stated (in Plutarch, for example).
I did not include The Bible, since it hard to ascribe one "author" (God?) to the books in it.

Homer——85——>Plato should be read as "Homer is mentioned by Plato 85 times in the seminar books."
Hovering over an edge in .svg should show you more information about that edge.

I made a python program to read the texts, count the word frequencies for each text, and find author matches. See `Processor.predicate()`

There were many false positives. For example, Chaucer mentions "Bacon", but he means the food, not the seminar author Roger Bacon. Swift is such a common word that I didn't even try with him. Adam Smith I had to do manually.
I relied largely on my memory of these texts to find and resolve these, so it's likely that I missed some. Hence, this graph IS NOT INTENDED TO SERVE AS A REFERENCE

Instead, it's a bird's eye view of how thinkers (in one tradition of thought) built on each other over time, creating one interconnected edifice of the mind.

Note: Not all the books are in this repo since many are copyrighted, or their translations are.
