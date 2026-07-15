Title: Handling Fatal Errors in Production on a Saturday Night
Date: 2018-04-30 11:40
Category: AWS
Tags: DevOps, Python, AWS, Lambda
Slug: handling-fatal-errors-in-production-on-a-saturday-night
Author: Erik
Summary: The tale of a tricky bug and the tools used to quicky find and fix it

<aside class="m-block m-success">
<h3>TLDR</h3>
<p>Designing notifications, analytics, and proper logging into your web application allows the weekend critical errors
to be triaged and fixed fast enough to keep everything running smoothly.</p>
</aside>
<aside class="m-note m-warning">
<h3>Affiliate Link</h3>
<p>The link to  <a href="https://logrocket.com/?cid=badsectorlabs1" target="_blank">LogRocket</a> is an affiliate link. As they don't have an
official affiliate program I'm not sure if anything will come of it, but for transparency I am disclosing my affiliation here.
There are many alternatives, but LogRocket has been great and offers a free tier!</p>
</aside>
<section id="background">
<h2>Background</h2>
<p>In my <a href="https://blog.badsectorlabs.com/how-we-built-hamiltixnet-for-less-than-1-a-month-on-aws.html">last post</a> I
described the way we instrumented all our AWS Lambda functions on <a href="https://www.hamiltix.net/" target="_blank">hamiltix.net</a> so any
unhandled error was sent as a Pushover notification with a full stack trace. While some were concerned this would lead
to a flood of messages, it has been nearly silent except for purchase notifications and a few minor bugs which were
corrected. Everything had been running smoothly for a while, until...</p>
</section>
<section id="the-error">
<h2>The Error</h2>
<p>It was Saturday, 8:21 P.M. I'd just returned home when I got a Pushover notification.</p>
<img alt="[FATAL] Error in TheMoneyLambda" class="m-image m-custom-image" src="images/handling-fatal-errors-in-production-on-a-saturday-night/pushover.jpeg"/>
<p>The few error notifications we have gotten are in a query or other part of the website that is a "first step" of the user
experience. By the time a user gets to the point where they are interacting with "TheMoneyLambada" the order is complete
(hence the name). What this means is that a user was trying to purchase tickets when this occurred. Priority: Critical.</p>
<p>I sit down at my laptop and open the CloudWatch dashboard. All Lambda standard out or logging messages are captured by
CloudWatch, so this should show exactly what caused the error. Immediately I saw the error, "Invalid Ticket Group Quantity."
Like all tricky bugs I immediately thought, "That's impossible!" The details of the order are all checked with the broker
immediately before purchase. TheMoneyLambda should never be handling an order that hasn't been checked for correctness.
The check is handled by a separate lambda, so flipping over to those logs I see that it was checked successfully. About
this time I get another error notification, same as first. Worried the customer is getting error messages and attempting
to buy the tickets multiple times, I fire off a quick email (captured at checkout) to them letting them know I am
looking into the issue.</p>
<p>The pressure was on now. I have no idea how this bug was possible and I'm about to loose a customer. With a grand total
of $0 spent on marketing, word of mouth and this blog is the only driver of sales. A bad customer experience
could torpedo the whole project.</p>
</section>
<section id="the-secret-weapon">
<h2>The Secret Weapon</h2>
<p>With the contradiction of the Lambda logs leading no where, I turned to a tool that I added to the site more for fun than
anything. <a href="https://logrocket.com/?cid=badsectorlabs1" target="_blank">LogRocket</a> is a javascript snippet that you can add to any page
and it hooks user interactions and logging and presents it back in a timeline view. From time to time I would use it to
see how people interacted with the site (my friend calls this "watching film" - like we are a sports team). While we include
LogRocket on the checkout page, we explicitly tell it NOT to capture any of the credit card fields. In the renders they
just don't appear (as if the element was deleted) which keeps us from accidentally storing any payment data.</p>
<p>In LogRocket I pick out the session right away and watch the user interaction from the beginning. Every thing looks
normal, except the ajax calls to API Gateway (and therefore Lambda) fail. Then I see it. LogRocket helpfully
captures all the details about ajax calls, and I notice the duration is about 15 seconds.</p>
<figure class="m-figure">
<img alt="LogRocket session showing the failed AJAX request" src="images/handling-fatal-errors-in-production-on-a-saturday-night/logrocket.png"/>
<figcaption>15 Seconds, why is that familiar?</figcaption>
</figure>
<p>Besides <a href="https://www.nngroup.com/articles/response-times-3-important-limits/" target="_blank">being an eternity online</a>, 15.957 seconds
is awfully close to the default 15 seconds execution limit on Lambada functions. Switching back to the CloudWatch logs
I scroll up past the two errors I initially fixated on to see this:</p>
<img alt="Apparently a successful order" class="m-image m-custom-image" src="images/handling-fatal-errors-in-production-on-a-saturday-night/cloudwatch.png"/>
<p>No errors, no traceback. Apparently a successful order. In my initial haste to find the issue I was focused on the errors
and missed the fact they were preceded by a successful order. The function must have timed out just before sending the
successful order notification and returning a 200 status to the front end. For some reason the broker's API took ten
seconds to respond, which in turn caused our Lambda function to hit its time limit of 15 seconds, but not before actually
processing the order! The user saw an error on the site, while at the same time getting a confirmation email. I
communicated the issue to the customer, who was really great about everything, and immediately increased the execution
time limit for TheMoneyLambda. With Lambda aliases, you have to make the change in the Lambda's dashboard then push a
new version to all aliases you want changed. This prevents you from accidentally changing a parameter or environment
variable that a current alias requires when updating a function. With the GitLab pipelines described in my <a href="https://blog.badsectorlabs.com/how-we-built-hamiltixnet-for-less-than-1-a-month-on-aws.html">previous post</a> its as simple as
re-running the deploy stage.</p>
<p>If the broker API had failed completely, or was a little faster this error wouldn't be possible. It was <em>just</em> slow
enough to succeed on the back end while failing on the front end.</p>
</section>
<section id="lessons-learned">
<h2>Lessons Learned</h2>
<ul>
<li>Instrumenting business critical functions to receive instant error notification is key to knowing there is a problem.</li>
<li>Quick communication with affected customers can help smooth over an otherwise bad experience.</li>
<li>During testing, ensure you test less-than-optimal conditions to include very slow responses.</li>
<li>Sometimes the stars align to serve you a tricky bug on a Saturday night. Welcome to the startup life =)</li>
</ul>
<p>In the market for Hamilton the Musical tickets? Find a better ticket search, alert, and buying experience
at <a href="https://www.hamiltix.net/" target="_blank">hamiltix.net</a>.</p>
<p>Questions or comments?
blog (at) badsectorlabs.com</p>
</section>
