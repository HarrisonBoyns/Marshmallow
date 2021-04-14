# flask-sql-alchemy

marshmallow is a library used for serialisation and deserialization of data 

what is serialisation?

Look up Black for formatting code --> install black to the dev packages
pipenv install -d black 
Then run it with pipenv black somepath one desires to format

write all constants now on the top of the page 

use classmethods when possible ( class methods pass the cls for you automatically 
make it therefore better than static methods). If it doesn't use "self" good 
argument to use a class method --> purely stylistic. Good form and thus more 
correct. Main reason most of flask uses self but this way is better. Stylistically 
more correct. When to use class or static. Typically use class when the method 
interacts with the class or just always use class over static. Whats the difference? 
Instance methods --> python passes the object as an argument (self) to the method.
Class methods --> python passes the class as an argument (cls) to the method.
Static methods --> python does not do anything. Must pass the class as the first argument. 

classmethods must be the first decorator :). 

After one deletes a method / variable ensure that it is no longer in use 
command shift F --> find the variable 

remember linting and creating complex types. Can also use current class

pipenv basically allows one to keep a closer track of what has been 
installed and what versions may be install for future uses. 

Ensures others install the exact same version. Adds a layer of security. 
Every dependency installed by pipenv is hashed and that hash is stored in a Pipfile.lock.
( basically the requirements.txt)
pipenv then compares what someone has downloaded to the hashes of what is in the lock file
if different an error is thrown == problem ( security - > someone would have 
changed it without changing the version number therefore prolly malware)
also simplifies working with virtual environments. Takes care of a bunch of shit.

packages --> used to deploy 
dev packages --> used for testing 