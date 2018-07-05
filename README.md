# .co
personal website

<b>backend</b>: flask + python scripts autoscheduled by cron OR gohugo(https://gohugo.io/getting-started/quick-start/)

<b>frontend</b>: html/css/js + choo (https://github.com/choojs/choo) / other potential framework?

<b>js/ect libraries</b>: https://github.com/xtianmiller/emergence.js
  - https://github.com/hughsk/web-audio-analyser/ (for audio wave viz)

<b>goals</b>:
  
  <i>function</i>

      - responsive
      - fast

  <i>form:</i>

    - nier colour pallette + ascii art styling
    - font-family: Consolas, monaco, monospace;

<b>Development steps</b>:
  
  - install and sync git on server to this repo. https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-16-04#how-to-set-up-git
  
  - use pocket API to pull latest archived articles to generate a list of "recently read"
  
  - use goodreads API to pull "books read" and "currently reading" to display both.
  
  - apple music API for currently listenting to? or plain-text alternative
  
  - pull favourite movies and movies I want to watch from imdb RSS feeds.
  
  - github api to document changes to the website in a changelog format
  
  - pull latest instagram posts as plain images

  - seperate inspiration image feed based on direct image upload or url upload
  
  - markdown to html workflow for uploading articles/pages, automatically apply minimal css to new markdown files in "article" github repository. (https://github.com/CouscousPHP/Couscous)
  
  - create python scripts that create csv file and update csv based on API calls described above (schedule the python scripts to run on a decided interval (once a day?) using cron). More serverside processing = faster page loads.
  
  - use javascript to produce a html table with the csv stored on the server (possibly duplicate these csv files on a CDN (eg: aws ect ect) for security reasons so visitors are not privy to any primary server files or connections).


<b>inspiration</b>
- https://observablehq.com/
- http://brutalistwebsites.com/
- http://wiki.xxiivv.com/
- https://jon-kyle.com/entries/2018-05-26-trans-catalina
