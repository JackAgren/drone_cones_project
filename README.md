# project-cone-by-drone

## Git
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

## Merge Conflicts

I'll get to this later


## Using PostgreSql

**IMPORTANT** You will be unable to run the django migrations until you have completed this installation.

1. Go to https://www.postgresql.org/download/ and download the correct version for your computer. You now have the postgres server installed along with a program called PGadmin, which gives a nice GUI to see the status of your database.

2. Using your prefered python package manager, install 'psychopg2'. This gives an easy way to use python with postgres.

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.cs.usu.edu/drone-cones/project-cone-by-drone.git
git branch -M master
git push -uf origin master
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.cs.usu.edu/drone-cones/project-cone-by-drone/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

## Image & Icon Attribution

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

