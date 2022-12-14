# IFrame Split Screen View

A common request we hear is how to create a split screen display, where the screen is broken up into 2 or 4 panels displaying different content using iFrames. The HTML app allows you to input raw HTML into the app and it will render it onto the TV screen, In which case you can easily create a table full of iframes of embedded web pages split into panels.

See the provided example in `index.html` of a working split screen display, using a website that permits iframe embedding

## Why This May Not Work

10 years ago, this would of worked just fine, however modern day browsers and web server configuration will not permit this for security reasons and to prevent clickjacking in most cases due to how the `X-Frame-Options` and `Content-Security-Policy` headers work.

You can read more about these here:

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy

You can check if a website has enabled `X-Frame-Options` by using cURL and looking for the specific header

```
curl -IL www.google.com | grep -i x-frame
```

In this case, you will see `X-Frame-Options: SAMEORIGIN` which means only the domain `google.com` can embed content from google.com in an iframe. You will not be able to embed this into a VuePilot HTML app.

It is possible however if you are using smaller web app tools or internal web tools that are not public facing, they won't have these security policies in place and it may work. There are also ledgitimate reasons why some websites may not implement these policies, ie where they allow external iframe embedding on other sites, such as video or dashboard style websites.

## Usage

Open and edit `index.html` with your own URLs, copy the HTML and paste into a HTML app.
