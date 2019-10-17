# .co
[![Netlify Status](https://api.netlify.com/api/v1/badges/8f32b96f-9015-45e7-a795-acbcf3791553/deploy-status)](https://app.netlify.com/sites/unruffled-bose-1c2551/deploys)

personal website

<h3>backend</h3>

`python code` that:

 - interprets information (folder structures, markdown, css and javascript files)
 - updates data based on API calls or personal online data stores
 - minifies/packages up all of the above in a suitable format to be deployed for netlify.
 
 
<b>python packages:</b>
- https://github.com/juancarlospaco/css-html-js-minify


<h3>frontend</h3>

minified html/css/js

<h4>css frameworks:</h4>

 - https://github.com/tachyons-css/tachyons (good style but may be too opinionated when writing creative/expressive css)
 - https://github.com/kbrsh/wing
 - https://github.com/louismerlin/concrete.css
 - investigate other lightweight, minimalist css frameworks


<h3>js/ect libraries</h3>:
- http://bl.ocks.org/KoGor/8160770 - technical drawing of a turbocharger animated using this code.
- https://github.com/xtianmiller/emergence.js
- https://github.com/hughsk/web-audio-analyser/ (for audio wave viz)

<h2>goals:</h2>
  
  <h3>function</h3>
  
      - responsive
      - fast

  <h3>form:</h3>

    - nier colour pallette + ascii art styling
    - font-family: Consolas, monaco, monospace, gt zirkon, Nocturno
    https://www.typotheque.com/fonts/nocturno/buy?bc[pack]=0

<h2>Development steps</h2>:
  
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


<h3>inspiration</h3>

- https://callumflack.design/the-littoral-line

- https://observablehq.com/

- http://brutalistwebsites.com/

- http://wiki.xxiivv.com/

- https://jon-kyle.com/entries/2018-05-26-trans-catalina

- http://www.gt-zirkon.com/#

- https://brandur.org/interfaces (BIG MOOD)

- 90s sci-fi/cyberpunk-ish anime computer interfaces (Cowboy Bebop, Evangellion, Akira)


