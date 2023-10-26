# project-cone-by-drone

## Git
Here is are a few git commands that will be used very often when collaborating

*   `git clone git@gitlab.com:sodo-launch-pad/raptor/raptor.git`
    *   In order to clone the repo via SSH, you must have a functioning SSH key on the GitLab. 
*   `git checkout -b <YourBranchNameHere>`
    *   If the specified branch doesn't exist, it will be created. The specified branch will then be checked out and all uncommited changes will be brought to this branch
*   `git add .`
    *   All changes will be moved to staged
*   `git commit -am "<Commit Message>"`
    *   Moves all tracked files to staged and them commits them
*   `git push --set-upstream <RemoteName> <BranchName>`
    *   When pushing up a branch for the first time you need to establish which remote to push to. The **RemoteName = origin**, and BranchName is the name of the branch you have checked out and are attempting to push. This command only needs to be used the first a branch is pushed, after that `git push` can be used.
*   `git push`
    *   Will push all your local and commited changes to the remote repo.

## Merge Requests

It is important to know that it is impossible to push to master. The master branch is considered production ready, so the only way to change/add code are through merge requests. 
Pushing up a new branch will automatically give a prompt to create a merge request on GitLab. Merge requests can also be manually created on GitLab. 
Once created, merge requests can be reviewed and then merged by the current team lead on GitLab. Add the current team lead to the Assignee so they will be notified of the request, and add the current sprint as the Milestone so it will be tracked properly.

Through the GitLab merge requests page, the team lead can add comments and suggestions to the code. You do not need to create multiple merge requests if changes need to be made. Pushing up changes to the branch associated with the merge request will automatically update the request. Once code is deemed sufficeint, the team lead can click the merge button on GitLab and the code will be merged with master. Merging two branches that are not master can also be done this way, but it is not required.  

## Merge Conflicts

I'll get to this later


## Using PostgreSql

**IMPORTANT** You will be unable to run the django migrations until you have completed this installation.

1. Go to https://www.postgresql.org/download/ and download the correct version for your computer. You now have the postgres server installed along with a program called PGadmin, which gives a nice GUI to see the status of your database.

## Running the backend server
0. Make sure you have pulled the most recent version from GitLab.

1. Go to https://www.postgresql.org/download/ and download the correct version for your computer. You now have the postgres server installed along with a program called PGadmin, which gives a nice GUI to see the status of your database.

2. Install the django rest framework with `pip install djangorestframework`

3. Navigate to `backend/api` and run `python manage.py makemigrations` followed by `python manage.py migrate`. If you get errors here please let me know.

4. run `python manage.py runserver`. You will get some output telling you the port the server is running on (usually localhost:8000).

5. Since the tables are empty, you can go to `http://localhost:8000/inventory/get_inventory` to add some items by filling out the form at the bottom of the page.

**As of 26 Oct**
You can now perfore `GET` requests from the inventory by the description, or simply get a list. You can fetch from `http://localhost:8000/inventory/get_inventory` to get JSON of all items in the inventory, or `http://localhost:8000/inventory/get_inventory/<description>` to get a specific item.

