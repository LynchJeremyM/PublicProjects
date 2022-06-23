#README

PURPOSE
The primary purpose of the project is to expand my working knowledge of overall application development. It also serves to improve my python skills, and eventually will branch into
other domains such as JavaScript and SQL. This project also serves as a demonstration of how I personally process information and create solutions. As such, it will have additional 
notes and comments written directly into files, and likely more official documentation of the process later in development.

PROJECT CRITERIA
Create a order processing application. This application should, at minimum -
    - Sort items into an optimal pull order
    - List alternative options for locations 
    - Consider inventory of items when sorting
    - Allow for user (the person pulling the order) to cancel or change items if needed

This project will heavily evolve overtime as I implement new functions and expand overall goals. The design is also likely to change as new problems arise.
For example, I currently assume when sorting that aisles are always closest to their numeric counterparts (IE 1 is close to 2). However, what happens if a 
store has multiple sections with different labeling? Or, what if 2 aisles are not actually close to each other despite their labeling? Many factors can change
the desired output.

Currently the items in a list are randomly generated, but I would also like add the ability for a user(s) to "create" an order and create a batch from that. Having 
a database with "actual" items is also a future goal, to better simulate a store or warehouse environment.

END