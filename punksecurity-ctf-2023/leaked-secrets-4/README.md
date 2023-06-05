# Leaked Secrets - 4
Category: Leaked Secrets

## Description
You have access to a small lambda project where the developer wasn't taking too much care with their repository hygiene...

Your goal is to find and extract the flag.

## Write-up
- As we enter the environment, we notice a `.git` directory in our current working directory.
- By running the command `git log`, we can see the commit history and the changes made to files in each commit.
- We can go through the commits one by one by using `git reset --hard HEAD~1` to reset to the previous commit and review the changes using `git log -p`.
- During this process, we found the flag in one of the file changes.

Flag: `punk_{JR6LD3FHAUR1JFSL}`
