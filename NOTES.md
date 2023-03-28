Please make notes here to clarify any decisions taken that you wish to communicate, and capture any URLs you used in solving the problems at hand.
* I didn't want .DS_Store to be added to my repo so I just added it to the .gitignore file
* I notice that `run.sh` is not mentioned in the the README instructions. I did try `./run.sh` to run the Flask app, but I encountered an issue ("ImportError: cannot import name 'escape' from 'jinja2'"), but since using a web application framework isn't mentioned in the exercise instructions, I chose not to prioritize solving this issue.
* I added comments for clarity and put the contents of the `else` block (which currently handles displaying the input string and its length) in its own function in anticipation of it becoming long & messy
