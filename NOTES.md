Please make notes here to clarify any decisions taken that you wish to communicate, and capture any URLs you used in solving the problems at hand.
* I didn't want .DS_Store to be added to my repo so I just added it to the .gitignore file
* I notice that `run.sh` is not mentioned in the the README instructions. I did try `./run.sh` to run the Flask app, but I encountered an issue ("ImportError: cannot import name 'escape' from 'jinja2'"), but since using a web application framework isn't mentioned in the exercise instructions, I chose not to prioritize solving this issue.
* I added comments for clarity and put the contents of the `else` block (which currently handles displaying the input string and its length) in its own function in anticipation of it becoming long & messy
* I used https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/ to remind me of Python dictionary syntax and how to iterate over them (for finding the most frequent character and count)
* I realized a string like "hheelloo" has a highest char frequency of 2, and 'h', 'e', 'l', and 'o' should be printed, so I amended my code.
* Ignored punctuation by storing it in a string and checking that each char wasn't in the string. Looked at https://www.digitalocean.com/community/tutorials/python-string-module and saw this.
* Used same logic for finding most frequent character(s) in a dictionary to find most popular word(s)
* For the longest string(s) feature, I am not prioritizing it now, but I realize that if a user enters a string with weird spacing or newlines or end with punctuation, then the way it's printed to the terminal may look off and you may not be able to tell if it's just one string or multiple and where one string ends and another starts.
* I decided to try storing whatever the stats are for a run of the application at the end of the session in a separate textfile with timestamps.
* To remember how to output to a file in Python, I referenced https://docs.python.org/3/tutorial/inputoutput.html
* I would have to redo a handful of what I wrote in order to output to a file instead so I am deciding to scrap it for the sake of time. However I will print out to the file the list of inputted strings with a timestamp since that functionality is already complete.



