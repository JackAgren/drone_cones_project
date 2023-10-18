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


## Installing PostgreSQL

**IMPORTANT** You will be unable to run the django migrations until you have completed this installation.

Go to https://www.postgresql.org/download/ and download the correct version for your computer. You now have the postgres server installed along with a program called PGadmin, which gives a nice GUI to see the status of your database.


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

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
