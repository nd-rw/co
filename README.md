# .co
personal website

<b>backend</b>: flask + python scripts autoscheduled by cron OR gohugo(https://gohugo.io/getting-started/quick-start/)

<b>frontend</b>: html/css/js + choo (https://github.com/choojs/choo) / other potential framework?
                 **css frameworks:**
                  - https://github.com/tachyons-css/tachyons
                  -https://github.com/nd-rw/uikit

<b>js/ect libraries</b>: https://github.com/xtianmiller/emergence.js
  - https://github.com/hughsk/web-audio-analyser/ (for audio wave viz)

<b>goals</b>:
  
  <i>function</i>

      - responsive
      - fast

  <i>form:</i>

    - nier colour pallette + ascii art styling
    - font-family: Consolas, monaco, monospace, gt zirkon, Nocturno
    https://www.typotheque.com/fonts/nocturno/buy?bc[pack]=0

<b>Development steps</b>:
  
  - install and sync git on server to this repo. https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-16-04#how-to-set-up-git
  
  - use pocket API to pull latest archived articles to generate a list of "recently read"
  
  - use goodreads API to pull "books read" and "currently reading" to display both.
  
  - apple music API for currently listenting to? or plain-text alternative
  
  - pull favourite movies and movies I want to watch from imdb RSS feeds.
  
  - github api to document changes to the website in a changelog format
  
  - pull latest instagram posts as plain images

  - seperate inspiration image feed based on direct image upload or url upload
  
  - input page to update "currently reading/watching/playing" 
      - Album Search(https://github.com/alastair/python-musicbrainzngs/issues/197
      - Games Search (Giant Bomb wiki)
      - Movies Search (IMDB or equiv)
      - all entries need a date and historicals need to be stored.
  
  - markdown to html workflow for uploading articles/pages, automatically apply minimal css to new markdown files in "article" github repository. (https://github.com/Python-Markdown/markdown/blob/master/docs/reference.md)
  
  - create python scripts that create json file and update json based on API calls described above (schedule the python scripts to run on a decided interval (once a day?) using cron). More serverside processing = faster page loads.
  
  - use javascript to produce a html table with the json stored on the server (possibly duplicate these json files on a CDN (eg: aws ect ect) for security reasons so visitors are not privy to any primary server files or connections).


<b>inspiration</b>
- https://observablehq.com/
- http://brutalistwebsites.com/
- http://wiki.xxiivv.com/
- https://jon-kyle.com/entries/2018-05-26-trans-catalina
- http://www.gt-zirkon.com/#
- https://brandur.org/interfaces (BIG MOOD)
