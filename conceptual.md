### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
**Client side vs server side** - Python is used for server-side back-end applications, while JavaScript is mainly for client-side web applications.
**Web broswer language** - Python is not natively used in web browsers, unlike JavaScript.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  **Python**

  ***using get***

  ```
  {
    value = dict.get('c',default_value)
  }

  ```
  ***using try except***

  ```
  {
    try:
        value = dict['c']
    except KeyError:
        value = default_value
  }

  ```

- What is a unit test?
A unit test is a method of testing the smallest pieces of code, typically individual functions to ensure they work as expected

- What is an integration test?
Integration tests assess how different parts of the application work together

- What is the role of web application framework, like Flask?
Flask provides the tools and libraries to build a web application, to handle routing, requests, responses, and sessions via importing from Flask libraries

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
URL parameter is better to request essential data ('/foods/pretzel'). Query parameter is better for filtering ('foods?type=pretzel').

- How do you collect data from a URL placeholder parameter using Flask?
use the following: @app.route('/item/<id>')

- How do you collect data from the query string using Flask?
use the following: value = request.args.get('key')

- How do you collect data from the body of the request using Flask?
use the following: data = request.form

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data stored on the client's browser, that contains session information, and is sent back and forth between server side and client side

- What is the session object in Flask?
Session object is improved upon cookies to store user specific information from one request to the next. It's implemented on top of cookies

- What does Flask's `jsonify()` do?
Converts data to JSON format
