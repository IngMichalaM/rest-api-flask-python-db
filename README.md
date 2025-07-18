# REST API with Flask and Python in 2025
**Jose Salvatiera, Udemy**

Covers the lectures 52-60 - Section 3: Your first REST API. 
Lessons before were a Python refresher.
Data are saved only locally using a list (stores and items). Everything gets deleted when the app stops.
Storing of the data will be modified in the next lectures, as well as use of Marshmallow, Flask-Smorest and Flask-blueprints.

## Install requirements.txt
 `pip install -r requirements.txt`
 
## Run Flask
`flask run`

## Create docker image
 `docker build -t rest-api-flask-python .`
 - -t - tag
 - rest-api-flask-python - name
 - . location of tje Dockerfile - current directory

## Problems with docker authentication
0. `docker logout`
1. `docker login -u <docker username>`
2. At the password prompt, enter the personal access token.

## Run docker from command line
 `docker run -p 5000:5000 rest-api-flask-python`

## Bruno
- flask_python_db contains the collection for the BE test using Bruno

# GIT
>> Jose + Colt**
>> - current course (Jose Salvatiera) - Section 10
>> - The Git and Github Bootcamp - Colt Steele

- log: `git log` (escape :q) 
  - without pages and only one line commits: `git --no-pager log --oneline`
  - without: `--no-pager` we stay on the page - to quite, type `q`.
  - limit number of displayed commits: `--max-count=X`
- add: `git add <file name>`
- commit: `git commit -m "<message>"`
- move files from the staging area to the working area: `git rm --cached <filenames>`
- correct commit message (interactive rebase): 
  - `git rebase -i HEAD~X` - X how many commits back to show
    - reword - edit commit message
    - fixup - like squash, but discard commit's tag (put two commits together, keeping the older commit message)
- tags: 
  - `git tag <tag name> <commit hash>`
  - list of tags: `git tag`
- rebase
  - merging main into feature branch, to have cleaner order of commits (first commits from main, then commits from feature) `git rebase main`
  - reduce merge noise after pulling the changes from remote `git pull --rebase`
- differences: 
  - diff between two branches: `git diff branch1..branch2`
  - without skipping some changes: `git --no-pager diff branch1..branch2`

## git config 
Each git repository has a .git folder and within a config file (plus there is a global config file in the home directory). In the config, among others, one can save its own aliases:
```
[alias] 
  mylog = log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate
```
or with the `--no-pager`
```
[alias] 
  mylog = !git --no-pager log --pretty=format:\"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]\" --decorate
```
## branches
- create new branch 
  - create new branch, but stay in the current branch `git branch <branch name>`
  - create new branch and switch to it 
    - `git checkout -b <branch name>`
    - `git switch -c <branch name>`
- delete local branch
  - `git branch -d <branch-name>`
  - force-delete, when there are unmerged changes `git branch -D <branch-name>`
- delete remote branch 
  - `git push origin --delete <branch-name>`
  
# bashrc
The .bashrc file is a shell script that is executed whenever a new terminal session is started in interactive mode in the Bash shell
Usually located in the home directory. A script can be placed directly there, or reference `source ~/playaround/bash_aliases.sh` ->
bash_aliases.sh contains a new command for cd+ls :-) 
``` 
cdl() {
  cd "$1" && ls
}
```