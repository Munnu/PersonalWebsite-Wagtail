# This is not for you, it's for me, and get off my lawn

July 15, 2017

I should have made the diary earlier, but haven't so I'm going off what I'm able to remember while hangry. I plan to use a diary to remember my progress on projects. 

What I've clearly noticed is that Wagtail is all about abstraction. I have a good feeling that if I really want to exercise class inheritcance, extending, and overriding based on my website goals, this is the place where I'll be implementing those things a bunch.

------
**Entry - July 29, 2017**
### Search Functionality
Kpeeing this entry short. I created a successful Search section that can search on Page titles successfully, see commit ([c2ef7b4](https://github.com/Munnu/PersonalWebsite-Wagtail/commit/c2ef7b4f3777f83ebe902f315927bdf410925e1a)).

I created a new branch (new_search) to work on a search functionality that includes all of the other pages. It's pretty crude. What I'd like to do is have all pages that contain the searched criteria to display if they're on the main website (no subdomain) and blog subdomain, and not any other subdomains. This is where I'm stuck, somewhat.

In the new version, I get the functionality desired, but I assume there is a better way to code it without manually importing all of my Page types into my search.view module.

**Entry - July 22, 2017**
### Adding and tweaking <img> tag via templating language
Wagtail adds some extra functionality to the templating structure. One of them is `img`. Instead of doing `<img src="x" ... >`, Wagtail provides `{% image [image] [resize-rule] %}` to use images in templates. 

Changing img by adding a class or id or overriding the alt tag can be done by something like this: `                        {% image main_image class="img-responsive" alt=post.title %}` where class is added, and alt is overrided from the Wagtail default.

source: [http://docs.wagtail.io/en/v0.7/core_components/images/index.html](http://docs.wagtail.io/en/v0.7/core_components/images/index.html)

### The Wagtail Gotcha - Adding Categories to choose within a page type
I totally forgot this bamboozled me. When adding the category row in models, there will be an empty column at first. In order to populate category types, go to the Wagtail /admin/ page, then upon logging in, look at the left pane and select Snippets, from there do
**Snippets > Name_Of_Page_Type_That_Has_Category_Table** to add categories.

### Filtering Blog Tags on current subdomain

Original Glitch:

- I needed to fix the 'tags' section, as it's linking to another subdomain. Not really sure what's going on here yet. Unrelated but likely necessary: I also have not created a tags page for the blog subdomain.

- Now the other half of the issue is making blog-tags not go to the other subdomain when listing all the tags.

Solutions to Glitch:

- I figured out that I have to create a new tags page, give it a slug (I called it blog-tag). Go into the blog_page.html template, change the slugurl to look for blog-tag. 
- The other half has something to do with handling an empty request from the model's end and also specifically filtering on current domain. See commit: [87dad77](https://github.com/Munnu/PersonalWebsite-Wagtail/commit/85dad7702e3afb0bdf3baa54aadc6d180b8395b5)

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

- ~~I assume this will need to be developed similarly to the images section in the Wagtail tutorial, mixed with an index page that contains icons.~~ Yes, confirmed and completed.
- I want to be able to create categories: **Engineering | Art | ... | Misc | All** within portfolio gallery for a user to choose which part of the portfolio gallery is of interest to them. (See below under 'Other Todos')

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
- Copied again from below:
 
	There's also a thing that around `screen width≈767`, the whitespace around each `<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 thumb">` looks asthetically unpleasing. I didn't notice this before because I used an image with a white background. I now need to think of a way to make this look more pleasing around this screen size. Maybe an image fade? Speak to designer for ideas.

### Other Todos, Portfolio-specific
- Minor fixes needed in portfolio gallery html
url example: [https://munnu.github.io/PersonalWebsite/portfolio-page.html](https://munnu.github.io/PersonalWebsite/portfolio-page.html)

	~~I haven't investigated but I believe that `<div class="thumb-overlay">`needs fixing. If I don't have a lot of content that will push the overlay to the maximum width, then it will stop where the content ends + margin value.~~ 
	
	Eh, bullcrap workaround, use a bunch of non-breaking spaces. It's a really minor todo, so I'll leave it.

	There's also a thing that around **`screen width≈767`**, the whitespace around each `<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 thumb">` looks asthetically unpleasing. I didn't notice this before because I used an image with a white background. I now need to think of a way to make this look more pleasing around this screen size. Maybe an image fade? Speak to designer.

- Adding a way to display all categories available and filtering on categories. 
	- All | Engineering | Art | Music | Misc
	- Idea: Maybe use Tag functionality instead of Categories. I think Categories are more for searching purposes. It's also possible to have to consider a hybrid.

### Todo WYSIWYG Wagtail Editor

Lower priority, but 

- Add codeblock functionality. I think they call these Streamfields.
	- I think this might be of use: [https://gist.github.com/frankwiles/74a882f16704db9caa27](https://gist.github.com/frankwiles/74a882f16704db9caa27)
	- More google fun [extra links on the topic](https://www.google.com/search?q=wagtail+code+block+addition&rlz=1C5CHFA_enUS690US690&oq=wagtail+code+block+addition&aqs=chrome..69i57.4987j0j4&sourceid=chrome&ie=UTF-8)
	
### Todo TL;DR
I've found myself repeating things above, so in summary

- ~~Recreate /portfolio/ to be tag-based to accomodate for filtering~~ Good enough
- ~~Fix the search bar, extra bonus if the search bar has better search capabilities than the one in the Wagtail tutorial~~ Good enough
- Add codeblock functionality. I don't want to reinvent the wheel, so are there snippets that have things I'd like?
- When things are all done, update to the latest version of Wagtail.

### Things to Learn

- Learn WSGI and also Django Models
	- Like how to join things (filter on this subdomain and another subdomain, filter on this but exclude this subset) 

References
[https://docs.djangoproject.com/en/1.11/ref/models/fields/#model-field-types](https://docs.djangoproject.com/en/1.11/ref/models/fields/#model-field-types) - Model data types

[https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups) - Field lookups: gte, lte, ecetera.

ex: `Entry.objects.get(id__exact=None)`

[https://docs.djangoproject.com/en/1.11/ref/models/querysets/#methods-that-return-new-querysets](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#methods-that-return-new-querysets) - queryset methods

[https://docs.djangoproject.com/en/1.11/topics/db/models/#field-types](https://docs.djangoproject.com/en/1.11/topics/db/models/#field-types)

[https://tutorial.djangogirls.org/en/django_orm/](https://tutorial.djangogirls.org/en/django_orm/)

[Wagtail Core Tests - Good for understanding how to use Page QuerySets](https://github.com/wagtail/wagtail/blob/master/wagtail/wagtailcore/tests/test_page_queryset.py)
