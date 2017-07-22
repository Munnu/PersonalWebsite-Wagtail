# This is not for you, it's for me, and get off my lawn

July 15, 2017

I should have made the diary earlier, but haven't so I'm going off what I'm able to remember while hangry. I plan to use a diary to remember my progress on projects. 

What I've clearly noticed is that Wagtail is all about abstraction. I have a good feeling that if I really want to exercise class inheritcance, extending, and overriding based on my website goals, this is the place where I'll be implementing those things a bunch.

------
**Entry - July 22, 2017**
### Adding and tweaking <img> tag via templating language
Wagtail adds some extra functionality to the templating structure. One of them is `img`. Instead of doing `<img src="x" ... >`, Wagtail provides `{% image [image] [resize-rule] %}` to use images in templates. 

Changing img by adding a class or id or overriding the alt tag can be done by something like this: `                        {% image main_image class="img-responsive" alt=post.title %}` where class is added, and alt is overrided from the Wagtail default.

source: [http://docs.wagtail.io/en/v0.7/core_components/images/index.html](http://docs.wagtail.io/en/v0.7/core_components/images/index.html)

### The Wagtail Gotcha - Adding Categories to choose within a page type
I totally forgot this bamboozled me. When adding the category row in models, there will be an empty column at first. In order to populate category types, go to the Wagtail /admin/ page, then upon logging in, look at the left pane and select Snippets, from there do
**Snippets > Name_Of_Page_Type_That_Has_Category_Table** to add categories.

------
**Entry - July 15, 2017
**
### Wagtail/Google Recaptcha
I'm still trying to understand how to get wagtail recaptcha to work for me. I'm a little stuck on `SSL: CERTIFICATE_VERIFY_FAILED` when trying to use Google NoCaptcha. 

Security is a little new to me and so are networking concepts. That being said, I don't understand the implications behind why this message is generated. I'm currently forced to use ReCaptcha v1.0 for this reason. Not sure if this would work on production if it isn't working locally.

I've tried remedying this using the tools in the **ssl_security_tools** folder. Tried using Stunnel, ngrok, and I think some built-in django tool to do the job and I still get the error. So far the hardest part for me has been doing the email form for this website. How in the world could this website be such a challenge for me is beyond me.

### Overriding Wagtail Email Functionality
Another aspect of the contact form I figured out is how to override the email sending functionality in Wagtail. I noticed that based on the documentation, my emails would not naturally contain a user-inputted subject line, but rather no subject or a default subject I'd input. Another thing I noticed is that the emails would default to my email address. 

I was banging my head on this for a bit to realize that in my current setup, despite overriding the send_mail function, gmail will always use my personal email as the to and from email. I can't change a thing. Later, I will inspect other methods so that I won't have to copy and paste email addresses from contact form submissions.

[Stackoverflow](https://stackoverflow.com/questions/8418905/how-to-override-the-from-address-in-django-email-sent-through-gmail?rq=1) proves this, and so does the Google Documentation (not linked, forgot where it was). The world sees Stackoverflow as a deity, so it's all good, right? I do fear that SO is a total programming crutch, though. Besides RTFM on answers, there's more of a reliance on SO without understanding where or why someone came up to the conclusion they did.

---
---

## My current todo

**Develop the portfolio gallery (portfolio-page)
**

- ~~I assume this will need to be developed similarly to the images section in the Wagtail tutorial, mixed with an index page that contains icons.~~
- I want to be able to create categories: **Engineering | Art | ... | Misc | All** within portfolio gallery for a user to choose which part of the portfolio gallery is of interest to them. (See below)

** Creating a wagtail portfolio-item section **

- ~~If I'm not mistaken, I have not made it to creating the page that would be linked from the main gallery that goes into detail about a single personal project done.~~
- ~~This shouldn't be too much to do as it emulates the Wagtail tutorial. I think this is why it was overlooked.~~

**Make the search functionality better**

- ~~Maybe based on the search functionality like Open Canada. I'll hold off on this one, it is not important.~~
- Wait, currently the search feature is broken.

**Clean up my wagtail project
**

- Because I went head-first into it and did the demo concurrent to the web app development. There's a lot of demo/experimentation in this. Maybe after I'm done, it's best to create a demo fork and then clean up `master`.
- This would entail having separate sections
    - ~~Like linking the pages to each other~~
    - Creating sections: ~~Home~~, ~~About~~, ~~Resume~~, Portfolio (Portfolio Gallery, ~~Portfolio long description page~~), ~~Blog~~, ~~Contact~~.
    
**Designer Edits**

- Though this belongs on the HTML/CSS version and it has nothing to do with me, there will most likely be designer edits. I think I have found a collaborator for the first time in my life.

### Other Todos, Portfolio-specific
- Minor fixes needed in portfolio gallery html
url example: [https://munnu.github.io/PersonalWebsite/portfolio-page.html](https://munnu.github.io/PersonalWebsite/portfolio-page.html)

	I haven't investigated but I believe that `<div class="thumb-overlay">`needs fixing. If I don't have a lot of content that will push the overlay to the maximum width, then it will stop where the content ends + margin value.

	There's also a thing that around **`screen width≈767`**, the whitespace around each `<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 thumb">` looks asthetically unpleasing. I didn't notice this before because I used an image with a white background. I now need to think of a way to make this look more pleasing around this screen size. Maybe an image fade? Speak to designer.

- Adding a way to display all categories available and filtering on categories. 
	- All | Engineering | Art | Music | Misc