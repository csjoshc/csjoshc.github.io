<a href="../../../index.html">Go back to index</a>
<a href="../base.html">Go back to General topics portal</a>

<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

# Web basics

A client sends the following content to a host server at a specific host name. www is the subdomain, while myhost.com is the domain (HTTP is the protocol). There will be a status code returned by the host. 

* 200 is ok
* 300s are redirection
* 400s are client errors (doesn't exist, unauthorized, forbidden)
* 500s are server errors (host can't execute request)
  
```
GET / HTTP/1.1
HOST: www.myhost.com
```
Then, the host sends this reply:
```
HTTP/1.1 200 OK
Content-Type: text/html
```

The IP is the machine, while TCP correctly directs the package to the program/service on the receiving machine. A specific host name (like google.com) is mapped to a target IP through a DNS on local servers; furthermore, information is routed successively closer to the destination in a process similar to recursion. TCP also has utility as a packet requester, if certain packets are lost in transmission, since it can request that the sender resend the missing packets. Appending a port number will correctly identify the target service on the host machine. 

# CSS and styling

The basic factoring out of style settings is with a style tag in the document header. Further separation can be done by using the `<link>` tag to apply styling from another document. 

CSS styling can be applied to both built in HTML tag categories, as well as user defined HTML tags with matching class attributes (as shown below). This would allow defining different appearances for the **same** element if the element was nested within different class attributes. 

```html

<!DOCTYPE html>

<html lang="en">
<head>
<style>

.format1
{
    text-align:center;
}
</style>
</head>
<body class="format1">
</body>
</html>
```

# Javascript

Conceptually, JavaScript can be thought of as allowing the website's author to control the html on the user's browser, after the page has already been sent, loaded and rendered. For example, a new email in gmail might cause an update of the table element by adding a new tr (table row) tag for the new email. JavaScript can be put into separate files (like css) and linked using `<script src="my_script.js"> </script>`

If you included a **named** user input tag , you can reuse that input tag's value as a variable in JavaScript, by referencing its unique identifier. Note the easy string concatenation.

```html
<!-- in header...-->
<script>
    function myfunc()
    {
        let my_var = document.querySelector('#uservar').value;
        alert('you entered ' + my_var);
    }
</script>
<!-- inside <body> tag...-->
<form onsubmit="myfunc(); return=false;">
    <input id="uservar" type="text">
    <input type="submit">
</form>
```

Other form types include "password", "radio", "checkbox" and "submit"

## Events

JavaScript has this syntax for further user interactivity - it can be adapted for any of the form types. There are also ways to reference the triggering event to extract its location, associated text, and so on by using `function myfunc (event){my_event = event.srcElement;}`

```html
<!-- inside body-->

<button id="my_button">Text here</button>

<script>
let body = document.querySelector('body');
document.querySelector('#my_button').onclick = function{
    body.style.backgroundColor = 'red';
};
</script>

```

# AJAX

AJAX allows refreshing sections of the page without refreshing the entire page. This is why it is asynchronous - these requests to update sections occur at different times from when the page itself is loaded. 

* Handle this with a XMLHttpRequest, which has 4 ready states. This is commonly implemented with jQuery. 

```javascript
function aj_req(arg){
    var aj = new XMLHttpRequest();
    aj.onreadystatechange=function{
        if(aj.readyState==4 && aj.status==200)
        // execute
    };
    aj.open("GET", /* url */, true);
    aj.send();
}
```

When handling events, use `this` to refer to the value of the HTML submission that triggered the (anonymous) function call in the first place. 