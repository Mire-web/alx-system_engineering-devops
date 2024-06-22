![BOOM BOOM](https://media.giphy.com/media/eK17Q8JUz2DHWtb2IY/giphy.gif)


# AND THE SERVER WENT BOOM 💥💥
This is the postmortem of the incident which sadly frustrated our users for an entire hour and thirty minutes on friday 21st June, 2024.

## ISSUE SUMMARY:
Duration: 1hour 30mins from 19:30 to 21:00 WAT
Impact: The entire web server was down causing requests to our website to return a 500 Internal error for the time duration, 87% of users were affected as the backup web server is not scaled enough to handle such large traffic.
ROOT CAUSE: An infinite loop 😭, a recent change that was committed to enhance speed of transaction, turned out halt transactions💔.

## TIMELINE:
- 19:30 Monitor Alerts went off
- 19:35 on-call engineer arrived on site
- 19:45 engineer escalated the problem
- 20:15 Senior engineer arrived on site
- 20:20 Problem detected
- 20:25 Changes Rollback to before recent commit
- 20:35 Rollback Failed as system resources were almost completely used
- 20:38 Hard reboot performed on server
- 20:45 Server ready for configuration
- 20:55 Commit fixed and Configuration done, proceeds to reboot server to ensure full working condition.
- 21:00 Systems fully back online

## ROOT CAUSE AND RESOLUTION
Recently our system had a spike in user activity, system administrator realized transactions were slowing down as the user base grew, and since it was almost the weekend, the engineers agreed to do the full scaling over the weekend, as a quick fix, a commit was to be made to act as a make shift virtual RAM to speed up transactions temporarily, How dumb we were🤦‍♂️. During the commit an unsuspecting loop sneaked past and got into production, Yes we didn't test the patch before committing as the chances of failure was really low, if only we knew how wrong we were 😂.
With the help of our robust monitoring system, the on call engineer was able to escalate the situation in time to have the problem fixed by the senior engineer, who resolved to rollback changes and ultimately hard reboot the server to restore nominal operations🎉🎉.

## CORRECTIVE AND PREVENTATIVE MEASURES:
- Scale the current infrastructure to accomodate the growing user base
- Never deploy without test
- Scale the backup server for injury time
