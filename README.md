# blog_hosting_using_flask_jinja_templating

## Description

This is a simple flask app that is hosting few blog posts. Data for the blogs is fetched using **https://www.npoint.io/**. When the application is run, it will display three blog posts rendered using HTML/CSS styles and showing title and subtitles. It also displays the link to read the complete blog post. After clicking on this link, it will show the complete blog post.

We have used two HTML files: 
1) for displaying the main blog post page with titles and subtitles 
2) the body page of each blog post after clicking on the URL on the first page

Since Jinja template is used to loop over the JSON blog data from npoint API, if number of blogs change in future, it should still work.

### Dependencies

* These modules are prerequisite : requests, flask

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program

```
* clone the repo
* open in an IDE/code editor and execute *main.py*
* click on the URL in the output to take to main blog post page. Click on the URL of any of the blog post to view the complete blog
```
