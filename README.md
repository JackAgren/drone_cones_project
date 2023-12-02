# project-cone-by-drone

## How to set up

### Setting up the backend server
0. Make sure you have pulled the most recent version from GitLab.

1. Go to https://www.postgresql.org/download/ and download the correct version for your computer. You now have the postgres server installed along with a program called PGadmin, which gives a nice GUI to see the status of your database. If running macOS run ```brew install postgresql@15```.
    
    * If in PGadmin there is no server but you have installed postgresql you need to register a new server.
    * Start PostgreSql. If using mac ```run brew services start postgresql@15``` or ```psql```
    * Right click databases and then click "Register"
    * Set name to DroneConesServer
    * Set host to localhost
    * Now we need to create a DB
    * Right click databases and select create -> database
    * Name it DroneConesDB

2. Install the django rest framework with `pip install djangorestframework`

3. Navigate to `backend/api` and run `python manage.py makemigrations` followed by `python manage.py migrate`. If you get errors here please let me know.
    * Be sure postgresql is running and confirm by looking at connection status through PGadmin
    * If ModuleNotFoundError: No module named 'corsheaders', try running `pip install django-cors-headers`

4. run `python manage.py runserver`. You will get some output telling you the port the server is running on (usually localhost:8000).

5. Since the tables are empty, you can go to `http://localhost:8000/inventory/get_inventory` to add some items by filling out the form at the bottom of the page.

**As of 26 Oct**
You can now perfore `GET` requests from the inventory by the description, or simply get a list. You can fetch from `http://localhost:8000/inventory/get_inventory` to get JSON of all items in the inventory, or `http://localhost:8000/inventory/get_inventory/<description>` to get a specific item.


### CORs Dependencies
Make sure to pip install the following:

pip install django-cors-headers

This has code to circumvent CORs issues.

### settings.py
Ensure for your local machine that you set the password value (found under DATABASES) in the settings.py file found within backend/api/api/settings.py matches the password set in the database found in pgAdmin4.  As of writing this, the default value of the password value is 'password'.


# Image & Icon Attribution

### `/dashboard`
* <a href="https://www.flaticon.com/free-icons/food-and-restaurant" title="food and restaurant icons">Food and restaurant icons created by Freepik - Flaticon</a>
* Drone: Modeled by Benjamin Ricks
* <a href="https://www.flaticon.com/free-icons/binoculars" title="binoculars icons">Binoculars icons created by smashingstocks - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/money" title="money icons">Money icons created by vectorsmarket15 - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/dollar" title="dollar icons">Dollar icons created by Freepik - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/pay" title="pay icons">Pay icons created by Freepik - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/inventory" title="inventory icons">Inventory icons created by IconBaandar - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/user" title="user icons">User icons created by Freepik - Flaticon</a>

### `/customer/history`
* <a href="https://www.flaticon.com/free-icons/shopping-cart" title="shopping cart icons">Shopping cart icons created by Vectors Market - Flaticon</a>

### `/customer/track-order`
* Drone: Modeled by Benjamin Ricks

### `/customer/arrived`
* <a href="https://www.flaticon.com/free-icons/hello" title="hello icons">Hello icons created by Freepik - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/ice-cream" title="ice cream icons">Ice cream icons created by Freepik - Flaticon</a>
* Drone: Modeled by Benjamin Ricks

### `customer/menu`
* Featured 0: https://www.pinterest.com/pin/74872412544956633/
* Featured 1: https://www.stlmag.com/dining/the-dish-ices-plain-fancy/
* Featured 2: https://practicallyhomemade.com/strawberry-crunch-cheesecake-cones/
* Featured 3: https://pintsizedbaker.com/peanut-butter-ice-cream/
* <a href="https://www.flaticon.com/free-icons/waffle" title="waffle icons">Waffle icons created by iconixar - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/bowl" title="bowl icons">Bowl icons created by Roundicons - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/ice-cream-cone" title="ice cream cone icons">Ice cream cone icons created by Freepik - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/cone" title="cone icons">Cone icons created by Nikita Golubev - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/cookie" title="cookie icons">Cookie icons created by Smashicons - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/sprinkles" title="sprinkles icons">Sprinkles icons created by Freepik - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/oreo" title="oreo icons">Oreo icons created by LAFS - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/syrup" title="syrup icons">Syrup icons created by Freepik - Flaticon</a>
* Ice cream scoop (all flavors): created by Emma Lynn

# Git
Here is are a few git commands that will be used very often when collaborating

*   `git clone git@gitlab.com:sodo-launch-pad/raptor/raptor.git`
    *   In order to clone the repo via SSH, you must have a functioning SSH key on the GitLab. 
*   `git checkout -b <YourBranchNameHere>`
    *   If the specified branch doesn't exist, it will be created. The specified branch will then be checked out and all uncommitted changes will be brought to this branch
*   `git add .`
    *   All changes will be moved to staged
*   `git commit -am "<Commit Message>"`
    *   Moves all tracked files to staged and them commits them
*   `git push --set-upstream <RemoteName> <BranchName>`
    *   When pushing up a branch for the first time you need to establish which remote to push to. The **RemoteName = origin**, and BranchName is the name of the branch you have checked out and are attempting to push. This command only needs to be used the first a branch is pushed, after that `git push` can be used.
*   `git push`
    *   Will push all your local and committed changes to the remote repo.

## Merge Requests

It is important to know that it is impossible to push to master. The master branch is considered production ready, so the only way to change/add code are through merge requests. 
Pushing up a new branch will automatically give a prompt to create a merge request on GitLab. Merge requests can also be manually created on GitLab. 
Once created, merge requests can be reviewed and then merged by the current team lead on GitLab. Add the current team lead to the Assignee so they will be notified of the request, and add the current sprint as the Milestone so it will be tracked properly.

Through the GitLab merge requests page, the team lead can add comments and suggestions to the code. You do not need to create multiple merge requests if changes need to be made. Pushing up changes to the branch associated with the merge request will automatically update the request. Once code is deemed sufficeint, the team lead can click the merge button on GitLab and the code will be merged with master. Merging two branches that are not master can also be done this way, but it is not required.  