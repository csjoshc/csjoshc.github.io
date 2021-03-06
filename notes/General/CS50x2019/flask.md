<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to General topics portal</a>

<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

# MVC

* Controller - business and functional logic (Python)
* View - aesthetics that is user-facing 
* Model - a database that handles requests

# Frameworks

Frameworks are a way to have a web app dynamically generate content. This would be instead of using a BaseHTTPRequestHandler and writing HTML through Python line by line, such as adding `<!DOCTYPE HTML>`, `<body>text</body>` tags and so on. Also necessary is setting the server_address as `("0.0.0.0", 8080)`. Flask is an example of such a framework. It abstracts away the line-by-line. 

# webapp example

```python
from flask import Flask, render_template, request, jsonify

# turn this .py file into a webapp
app = Flask(__name__)

namelist=[] # persistent data structure - before db

# listen for a forward slash
@app.route("/")

# call the following when a user requests 
# the forward slash (e.g. the root dir)
def index():
    return "hello world"
```

Then, on the command line you just use the following lines. The first two are required only the first time the application is run. The below is for Linux:

```bash
export FLASK_APP=application.py
export FLASK_DEBUG=1
flask run
```

Alternatively, on windows it would be

```shell
set FLASK_APP=application.py
set FLASK_DEBUG=1
flask run
```

Alternative - the index.html is in a /templates folder by convention. 

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        `<title>hello</title>
    </head>
    <body>
        hello {{ name }}
        <form action="/nextpage" method="post">//post will send info 
            <input autofocus name="name" placeholder="Name" type="text">
            <input type="submit" value="Enter">
        </form>    
    </body>
</html>
```

```python
def index(): 
    name = request.args.get("name", "default_name") # default if none
    # this comes from the ?name=myname in the url
    return render_template("index.html", name=name)
```

Then, in the browser you would append a ?name=myname to the url to simulate a GET request - and this would dynamically update the website to use that name. 

For other requests, such as the submission, we can implement separate request listeners. You can also set methods to allow both GET and POST, and include a if switch in the associated method to handle the page load or submission, respectively. 

```python
@app.route("/nextpage", methods=["POST"])
def nextpage_func():
    # what to do with a name submission? this comes from the form submission
    name = request.form.get("name")
    if not name:
        return "failure"
    namelist.append(name)
    return render_template("good_job.html")
```

# HTML templates

Flask also allows placeholders for chunks of html. In a `layouts.html` file inside a templates directory:

```html
<body>
{% raw %}{% block body %}{% endblock %}{% endraw %}
</body>
```

Then, in other HTML files that are based off this layouts file, we can get rid of the doctype, html/lang and header tags. We can just include the HTML that is **specific** to the particular page. This might be an exampel of "good_job.html" that I used above:

```html
{% raw %}
{% extends "layout.html" %}
{% block body %}

    <h1>Good job!</h1>
    // unique stuff here
{% endblock %}
{% endraw %}
```

# Displaying persistent data

Now that we have a namelist that gets appended to with each submission, we can also have a page dynamically updated with that list. Update the nextpage_func() to redirect to another page and add another function to handle the generating of that redirected page:


```python
@app.route("/nextpage", methods=["POST"])
def nextpage_func():
    # what to do with a name submission? this comes from the form submission
    name = request.form.get("name")
    if not name:
        return "failure"
    namelist.append(name)
    # redirect to the names.html page using the route
    return redirect("/displaynames")

@app.route("/displaynames")
def enterednames_func():
    return render_template("names.html", namelist=namelist)
```

Then, in names.html in templates directory:

```html
{% raw %}
{% extends "layout.html" %}
{% block body %}
    <ul> //list 
        {% for name in namelist %}
            <li>{{ name }}</li?
        {% endfor %}
    </ul>
{% endblock %}
{% endraw %}
```

You can also set up the entered_names() function to save the file at the same time the page loads, and to display a link to the file as a href as a download link. 
`<a href="/myfiles.zip">Download</a>`

# Javascript error checking

For checking user input, it would be good to check it on the client side. 

```html
<script>
document.querySelector('form').onsubmit = function(){
    if(!document.querySelector('input').value){
        alert('You must enter a name');
        return false;
    }
    return true;
}
</script>
```

For fancier checking, you can use bootstrap to check user input without generating alert popups. 

#  jQuery 

jQuery can enable calling a function using `$` notation with a `.get()` function to load snippets of HTML after a page is already loaded. Under an input field, reactive output can be shown using a javascript snippet. This changes the contents inside the `<ul></ul>` tags in reaction to user input

```html
<ul></ul>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script>
    let input = document.querySelector("input");
    input.onkeyup = function(){
        $.get('/search?q=' + input.value, function(data) {
            document.querySelector('ul').innerHTML=data;
        });

    };
</script>
```

On the server side there is a app route for the jQuery script that returns a JSON of the matching entries. 

```python
@app.route("/search")
def search():
    q = request.args.get("q")
    words = [w for w in words if q and w.startswith(q)]
    return jsonify(words)
```

Finally, its possible to replace server side Python with JavaScript and implement lookup using a .js array loaded into the browser. 

```html
<script>
    
    let input = document.querySelector('input');
    input.onkeyup = function() {
        let html = '';
        if (input.value) {
            for (word of WORDS) {
                if (word.startsWith(input.value)) {
                    html += '<li>' + word + '</li>';
                }
            }
        }
        document.querySelector('ul').innerHTML = html;
    };

</script>
```