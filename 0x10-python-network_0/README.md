## Networking Basics README

This README provides an overview of fundamental concepts related to networking, HTTP, and URLs.

## What is a URL?

A URL (Uniform Resource Locator) is a reference to a web resource that specifies its location and how to retrieve it. It consists of several components, including the protocol, domain name, port number, path, query string, and fragment identifier.

## What is HTTP?

HTTP (Hypertext Transfer Protocol) is a protocol used for transmitting data over the internet. It defines how messages are formatted and transmitted, as well as how web servers and browsers should respond to various commands.

## How to Read a URL

A URL is typically structured as follows: protocol://domain:port/path?query#fragment. Each component serves a specific purpose in identifying and retrieving the desired resource.

## The Scheme for an HTTP URL

The scheme for an HTTP URL typically begins with "http://" for unencrypted connections and "https://" for encrypted connections using SSL/TLS.

## What is a Domain Name?

A domain name is a human-readable label that maps to a specific IP address on the internet. It provides a memorable way to access websites and other internet resources.

## What is a Sub-domain?

A sub-domain is a domain that is part of a larger domain. It precedes the main domain name and allows for further organization and categorization of websites.

## How to Define a Port Number in a URL

A port number can be defined in a URL by appending :port after the domain name. If no port is specified, the default port for the given protocol is used (e.g., 80 for HTTP, 443 for HTTPS).

## What is a Query String?

A query string is a part of a URL that contains data to be passed to the web server as parameters. It follows the path component and is preceded by a question mark (?).

## What is an HTTP Request?

An HTTP request is a message sent by a client (such as a web browser) to a server, requesting a specific action or resource. It typically includes information such as the request method, headers, and optional body content.

## What is an HTTP Response?

An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains the requested resource along with status information such as the response status code, headers, and optional body content.

## What are HTTP Headers?

HTTP headers are additional pieces of information sent along with HTTP requests or responses. They contain metadata about the message and provide instructions or constraints to the server or client.

## What is the HTTP Message Body?

The HTTP message body is the content of an HTTP request or response. It can contain data such as form submissions, file uploads, or the requested resource itself.

## What is an HTTP Request Method?

An HTTP request method specifies the desired action to be performed on the identified resource. Common methods include GET, POST, PUT, DELETE, and others.

## What is an HTTP Response Status Code?

An HTTP response status code indicates the outcome of an HTTP request. It provides information about whether the request was successful, encountered an error, or requires further action.

## What is an HTTP Cookie?

An HTTP cookie is a small piece of data sent from a website and stored on the user's device by the web browser. It is commonly used for session management, user authentication, and tracking.

## How to Make a Request with cURL

cURL is a command-line tool for transferring data with URLs. It supports various protocols, including HTTP, HTTPS, FTP, and more. To make an HTTP request with cURL, you can use the curl command followed by the URL and any additional options.

## What Happens When You Type google.com in Your Browser (Application Level)

When you type "google.com" in your browser, the browser initiates an HTTP request to the server hosting the Google website. The server responds with the HTML content of the Google homepage, along with any associated resources such as images, scripts, and stylesheets. The browser then renders the received content and displays the Google homepage to the user.
