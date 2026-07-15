Title: How we built Hamiltix.net for less than $1 a month on AWS
Date: 2018-03-01 11:40
Category: AWS
Tags: Gitlab, DevOps, Python, AWS, Lambda
Slug: how-we-built-hamiltixnet-for-less-than-1-a-month-on-aws
Author: Erik
Summary: The details of running a complex ticket ranking site for under a dollar a month on AWS

<aside class="m-note m-warning">
<h3>Ok not quite $1...</h3>
<p>After the free-tier expires it will be less than $5, but the fact remains: it's crazy cheap.</p>
</aside>
<section id="background">
<h2>Background</h2>
<p>Hamilton the musical is hot. <a href="http://variety.com/2017/legit/news/hamilton-ticket-prices-1202648756/" target="_blank">Really hot</a>.
With crazy high ticket prices, finding the best deal should be easy, especially if you live in New York City, Chicago,
or a city on the US Tour. You just go to a major ticket resale site, and search across all the dates you are
able to attend and... wait... no site supports ranking tickets across dates? And their "deal rankings" don't take into
account the intricacies of each theatre (viewing obstructions, etc)!? I guess we'll have to build it ourselves!</p>
<p>For a full background on the motivations behind <a href="https://www.hamiltix.net/" target="_blank">hamiltix.net</a> checkout the <a href="https://blog.hamiltix.net/welcome-to-hamiltix.html" target="_blank">hamiltix.net
blog</a>.</p>
</section>
<section id="from-simple-script-to-legitimate-website">
<h2>From simple script to legitimate website</h2>
<p>Being a python programmer it didn't take long to scrape the major ticket sites and rank all the tickets with a custom
algorithm. This turned up some interesting results, and it was easy to compare the best tickets for any dates, sections,
and theaters we wanted. This was great for personal use, but not very accessible to an average Hamilton-goer (and
despite <a href="https://arstechnica.com/tech-policy/2017/08/court-rejects-linkedin-claim-that-unauthorized-scraping-is-hacking/" target="_blank">being perfectly legal</a> it
may draw the irk of the sites we are scraping). Time to legitimize our data collection and make it presentable.</p>
<p>This lead to a long slog through the secondary ticket market, which was actually quite interesting, and will be detailed
on the hamiltix.net blog. The end state was we connected with a "ticket broker" network
and are able to access their inventory (spoiler: nearly all secondary ticket sites share the same inventory). With live
tickets at our fingertips the question became how do we process all the data and present it on the cheap?</p>
</section>
<section id="aws-power-complexity-affordability">
<h2>AWS - Power, Complexity, Affordability</h2>
<p>Enter Amazon Web Services (AWS). AWS is the cloud service provider that powers may of the biggest names on the internet
so lets see how it does with a simple static site and backend.</p>
<aside class="m-note m-danger">
<h3>Warning!</h3>
<p>The following architecture design choices were made for the purposes of cost savings as well as a chance to learn new
technologies. I make no claim they are the best choices for the given tasks. In many cases, there are much better
technologies that make more sense!</p>
</aside>
<p>Normally, the first step for this kind of project is to start up a linux server, but <a href="https://www.cloudtp.com/doppler/rise-of-serverless-computing-operational-security-financial-considerations/" target="_blank">serverless computing is on the
rise</a>.
We've never dealt with Lambda or any other "serverless" technology before so lets give it a shot.</p>
<p>The overall design of hamiltix looks like this:</p>
<figure class="m-figure">
<img alt="Hamiltix AWS Diagram" src="images/hamiltix-on-the-cheap/hamiltix-aws.png"/>
<figcaption>The Hamiltix.net AWS stack</figcaption>
</figure>
<p>As you can see, Lambda is the star of the show. If you haven't heard of Lambda before, you can think of it as a service
that will run a function (however complex) on a trigger (there are too many to list, basically any AWS service can
trigger a lambda). Lambda offers Node.js, Python (2.7 and 3.6), Java (8+), C# (.NET Core), and Go environments.
Since we already had the ranking module in Python, we stuck with Python (3 of course) for the rest of the functions as
well.</p>
<p>Cloudwatch event rules kick off any Lambdas that need to run on intervals (getting and ranking tickets), and API
Gateway fires any "dynamic" content for the website like advanced search, or the actual ticket purchasing.</p>
<p>We also made the decision to not use a javascript framework for the front end, mostly because they are incredebly
complex and some people suggest <a href="https://medium.com/@mattburgess/all-javascript-frameworks-are-terrible-e68d8865183e" target="_blank">they are all terrible</a> (or
<a href="https://medium.com/@mattburgess/javascript-frameworks-are-great-2df4a3f0b24d" target="_blank">maybe great?</a>). Could be use React with
a static site? Sure, but that also means dealing with animated routes, custom routing, GraphQL, Redux, Sass or Less,
JSX... I'm already exhausted. We just want to present tickets cleanly to users, not build the next Facebook.
<a href="https://jquery.com/" target="_blank">jQuery</a>, <a href="https://sweetalert2.github.io/" target="_blank">SweetAlert2</a>,
<a href="https://semantic-ui.com/" target="_blank">Semantic-ui</a>, <a href="https://momentjs.com/" target="_blank">Moment.js</a>, and
<a href="https://dubrox.github.io/Multiple-Dates-Picker-for-jQuery-UI/" target="_blank">MutliDatesPicker</a> are the only external javascript
libraries used on hamiltix.net.</p>
<p>Without the need for a server hosting the site, it can be stored on S3 and distributed by Cloudfront. Setting up a
static site with AWS
<a href="https://medium.com/@sbuckpesch/setup-aws-s3-static-website-hosting-using-ssl-acm-34d41d32e394" target="_blank">is fairly simple</a>. Any
<code>ajax</code> calls in the site's javascript are sent to the API Gateway which in turn calls the correct lambda function to
handle whatever task is requested. With hamilton ticket prices as high as they are, we set up a staging environment that
uses our ticket broker's sandbox API to test all functions on each commit to master. For this to work, you need two
separate environments in API Gateway, and the corresponding aliases for your lambda functions (don't forget to publish
the changes in API Gateway!).</p>
<img alt="The two API Gateway stages for hamiltix" class="m-image m-custom-image" src="images/hamiltix-on-the-cheap/api-stages.png"/>
<p>While in the API Gateway, you have to point the lambda handler to the function alias that corresponds to either staging
or prod. This can be done with a <code>stageVariable</code> when setting up the endpoint in the Resources screen of API Gateway.
You'll need to allow API Gateway permissions to access each alias you use, but AWS provides a nice aws-cli command
for you when you set up the Lambda proxy integration.</p>
<img alt="The stageVariable setup on the Resources screen" class="m-image m-custom-image" src="images/hamiltix-on-the-cheap/stage-variable.png"/>
<p>Then in the Stages screen, ensure that each stage as an appropriate Stage Variable.</p>
<img alt="The stageVariable setup on the Stages screen" class="m-image m-custom-image" src="images/hamiltix-on-the-cheap/actual-stage-variables.png"/>
<p>Now the staging and prod APIs will call the <code>Staging</code> and <code>Prod</code> lambda aliases respectively. Setting up staging and prod
lambda aliases is not difficult, and is handled by Gitlab's CI/CD pipeline.</p>
<section id="ci-cd">
<h3>CI/CD</h3>
<p>If you've read <a href="https://blog.badsectorlabs.com/pelican-gitlab-cicd-docker-aws-awesome-static-site.html">my first post</a>
you know I'm a big fan of Gitlab and its built in CI/CD. The hamiltix repo is set up with each lambda as a
<a href="https://git-scm.com/book/en/v2/Git-Tools-Submodules" target="_blank">submodule</a> because Gitlab currently <a href="https://gitlab.com/gitlab-org/gitlab-ce/issues/18157" target="_blank">does not support</a> more than one <code>.gitlab-ci.yml</code> file for a repo. The
<code>gitlab-ci.yml</code> files for each lambda are nearly identical (on purpose!), only the variables section at the top and
the additional <code>cp</code> statements for custom directories (if needed) change between lambda functions. Strict
<a href="https://12factor.net/build-release-run" target="_blank">twelve-factor</a> followers will notice that the build and release stages are
combined. It is certianlly possible to break the build step out and pass the zip as an artifact, but the stage is so
fast we haven't done this yet.</p>
<pre class="m-code"><span class="nt">variables</span><span class="p">:</span>
<span class="w">  </span><span class="c1">#  Set git strategy</span>
<span class="w">  </span><span class="nt">GIT_STRATEGY</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">clone</span>
<span class="w">  </span><span class="nt">GIT_SUBMODULE_STRATEGY</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">recursive</span>
<span class="w">  </span><span class="c1"># Keys and secrets are defined in the project CI settings and exposed as env variables</span>
<span class="w">  </span><span class="nt">AWS_ACCESS_KEY_ID</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">$AWS_ACCESS_KEY_ID</span>
<span class="w">  </span><span class="nt">AWS_SECRET_ACCESS_KEY</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">$AWS_SECRET_ACCESS_KEY</span>
<span class="w">  </span><span class="nt">AWS_DEFAULT_REGION</span><span class="p">:</span><span class="w"> </span><span class="s">"us-east-1"</span>
<span class="w">  </span><span class="nt">NAME</span><span class="p">:</span><span class="w"> </span><span class="s">"MyFunction"</span>
<span class="w">  </span><span class="nt">FILENAME</span><span class="p">:</span><span class="w"> </span><span class="s">"MyFunction.py"</span>
<span class="w">  </span><span class="nt">HANDLER</span><span class="p">:</span><span class="w"> </span><span class="s">"MyFunction.lambda_handler"</span>
<span class="w">  </span><span class="nt">RUNTIME</span><span class="p">:</span><span class="w"> </span><span class="s">"python3.6"</span>
<span class="w">  </span><span class="nt">ROLE</span><span class="p">:</span><span class="w"> </span><span class="s">"arn:aws:iam::XXXXXXXXXXXXX:role/XXXXXXXXXX"</span>
<span class="w">  </span><span class="nt">FILE</span><span class="p">:</span><span class="w"> </span><span class="s">"fileb://deploy_$CI_COMMIT_REF_NAME.zip"</span>

<span class="nt">stages</span><span class="p">:</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">test</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">deploy</span>

<span class="nt">test</span><span class="p">:</span>
<span class="w">  </span><span class="nt">stage</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">test</span>
<span class="w">  </span><span class="nt">image</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">badsectorlabs/code-checking:latest</span><span class="w"> </span><span class="c1"># This is a docker image that contains a lot of code checking tools</span>
<span class="w">  </span><span class="nt">script</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cpd --minimum-tokens 100 --language python --files .</span>
<span class="w">    </span><span class="c1"># pylint output is good to look at, but not worth breaking the build over</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">pylint -d bad-continuation -d line-too-long -d import-error -d missing-docstring $FILENAME || true</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">flake8 --max-line-length 120 --ignore=E722,W503 .</span><span class="w"> </span><span class="c1"># You must pass flake8 (W503 is wrong, pep8 changed)</span>

<span class="nt">deploy-staging</span><span class="p">:</span>
<span class="w">  </span><span class="nt">stage</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">deploy</span>
<span class="w">  </span><span class="nt">image</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">badsectorlabs/aws-compress-and-deploy:latest</span>
<span class="w">  </span><span class="nt">variables</span><span class="p">:</span>
<span class="w">    </span><span class="nt">ALIAS</span><span class="p">:</span><span class="w"> </span><span class="s">"Staging"</span>
<span class="w">    </span><span class="nt">DESC</span><span class="p">:</span><span class="w"> </span><span class="s">"Staging</span><span class="nv"> </span><span class="s">build,</span><span class="nv"> </span><span class="s">commit:</span><span class="nv"> </span><span class="s">$CI_COMMIT_SHA"</span>
<span class="w">  </span><span class="nt">script</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">virtualenv -p /usr/bin/python3.6 env</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">source env/bin/activate</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">pip install -r requirements.txt</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">mkdir dist</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cp $FILENAME dist</span><span class="w"> </span><span class="c1"># copy all files needed to dist</span>
<span class="w">    </span><span class="c1"># Copy any other directories (modules, etc) here</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cp -rf env/lib/python3.6/site-packages/* dist</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cd dist</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">zip -r9 ../deploy_$CI_COMMIT_REF_NAME.zip .</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cd ..</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">deactivate</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">ls -lart</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo Creating or updating $NAME</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="p p-Indicator">&gt;</span><span class="w"> </span><span class="c1"># This captures the code hash for the updated/created lambda function; -r is needed with jq to strip the quotes</span>
<span class="w">      </span><span class="no">CODE_SHA_256=$(aws lambda update-function-code --function-name $NAME --zip-file $FILE | jq -r ."CodeSha256" || aws lambda create-function</span>
<span class="w">      </span><span class="no">--function-name $NAME --runtime $RUNTIME --role $ROLE --handler $HANDLER --zip-file $FILE | jq -r ."CodeSha256")</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo Publishing LATEST, CodeSha256=$CODE_SHA_256, as 'Staging'</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">VERSION=$(aws lambda publish-version --function-name $NAME --description "$DESC" --code-sha-256 $CODE_SHA_256 | jq -r ."Version")</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo "Published LATEST as version $VERSION"</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="p p-Indicator">&gt;</span>
<span class="w">      </span><span class="no">aws lambda update-alias --function-name $NAME --name $ALIAS --function-version $VERSION || aws lambda create-alias</span>
<span class="w">      </span><span class="no">--function-name $NAME --name $ALIAS --description "Staging" --function-version $VERSION</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo Successfully updated $NAME:$ALIAS</span>
<span class="w">  </span><span class="nt">environment</span><span class="p">:</span>
<span class="w">    </span><span class="nt">name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">master-staging</span>
<span class="w">  </span><span class="nt">only</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">master</span>

<span class="nt">deploy-prod</span><span class="p">:</span>
<span class="w">  </span><span class="nt">stage</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">deploy</span>
<span class="w">  </span><span class="nt">image</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">badsectorlabs/aws-compress-and-deploy:latest</span>
<span class="w">  </span><span class="nt">variables</span><span class="p">:</span>
<span class="w">    </span><span class="nt">ALIAS</span><span class="p">:</span><span class="w"> </span><span class="s">"Prod"</span>
<span class="w">    </span><span class="nt">DESC</span><span class="p">:</span><span class="w"> </span><span class="s">"Prod</span><span class="nv"> </span><span class="s">build,</span><span class="nv"> </span><span class="s">commit:</span><span class="nv"> </span><span class="s">$CI_COMMIT_SHA"</span>
<span class="w">  </span><span class="nt">script</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">virtualenv -p /usr/bin/python3.6 env</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">source env/bin/activate</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">pip install -r requirements.txt</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">mkdir dist</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cp $FILENAME dist</span><span class="w"> </span><span class="c1"># copy all files needed to dist</span>
<span class="w">    </span><span class="c1"># Copy any other directories (modules, etc) here</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cp -rf env/lib/python3.6/site-packages/* dist</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cd dist</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">touch PROD</span><span class="w"> </span><span class="c1"># This is the canary that will tell the lambda function to use the PROD secrets</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">zip -r9 ../deploy_$CI_COMMIT_REF_NAME.zip .</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cd ..</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">deactivate</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">ls -lart</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo Creating or updating $NAME</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="p p-Indicator">&gt;</span><span class="w"> </span><span class="c1"># This captures the code hash for the updated/created lambda function; -r is needed with jq to strip the quotes</span>
<span class="w">      </span><span class="no">CODE_SHA_256=$(aws lambda update-function-code --function-name $NAME --zip-file $FILE | jq -r ."CodeSha256" || aws lambda create-function</span>
<span class="w">      </span><span class="no">--function-name $NAME --runtime $RUNTIME --role $ROLE --handler $HANDLER --zip-file $FILE | jq -r ."CodeSha256")</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo Publishing LATEST, CodeSha256=$CODE_SHA_256, as 'Prod'</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">VERSION=$(aws lambda publish-version --function-name $NAME --description "$DESC" --code-sha-256 $CODE_SHA_256 | jq -r ."Version")</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo "Published LATEST as version $VERSION"</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="p p-Indicator">&gt;</span>
<span class="w">      </span><span class="no">aws lambda update-alias --function-name $NAME --name $ALIAS --function-version $VERSION || aws lambda create-alias</span>
<span class="w">      </span><span class="no">--function-name $NAME --name $ALIAS --description "Prod" --function-version $VERSION</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo Successfully updated $NAME:$ALIAS</span>
<span class="w">  </span><span class="nt">environment</span><span class="p">:</span>
<span class="w">    </span><span class="nt">name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">master-prod</span>
<span class="w">  </span><span class="nt">only</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">master</span>
<span class="w">  </span><span class="nt">when</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">manual</span></pre>
<p>Using this CI setup, the lambda can check for <code>PROD</code> with <code>if os.path.exists('PROD'):</code> and if so read in env
variables for the production environment, and otherwise use staging variables. Note that both staging and production
variables must be defined in the lambda settings (aliases take a snapshot of the lambda settings to prevent a setting
change from breaking aliases that already exist).</p>
<p>The CI setup for pushing the static site assets looks nearly identical to the <a href="https://gitlab.com/badsectorlabs/blog/blob/master/.gitlab-ci.yml" target="_blank">setup for this blog</a>.</p>
</section>
<section id="logging-and-monitoring">
<h3>Logging and Monitoring</h3>
<p>Once you have some lambdas working away for you, it becomes necessary to monitor them. By default the lambdas will log
any standard out to Cloudwatch, which is nice if you need to go back and see what caused an issue, but doesn't help
alert you when an issue occurs. There are many ways to solve this issue, including many that would leverage AWS services
but I already had a lifetime <a href="https://pushover.net/" target="_blank">Pushover</a> account, so decided to use it for instant push
notifications on any unhandled lambda error.</p>
<pre class="m-code"><span class="k">def</span> <span class="nf">send_pushover</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">title</span><span class="p">,</span> <span class="n">sound</span><span class="o">=</span><span class="s1">'pushover'</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Send a pushover message</span>
<span class="sd">    :param message: string; the message to send</span>
<span class="sd">    :param title: string; the title of the message</span>
<span class="sd">    :param sound: string; one of the keys of {'pushover': 'Pushover (default)', 'bike': 'Bike', 'bugle': 'Bugle',</span>
<span class="sd">                          'cashregister': 'Cash Register', 'classical': 'Classical', 'cosmic': 'Cosmic',</span>
<span class="sd">                          'falling': 'Falling', 'gamelan': 'Gamelan', 'incoming': 'Incoming',</span>
<span class="sd">                          'intermission': 'Intermission', 'magic': 'Magic', 'mechanical': 'Mechanical',</span>
<span class="sd">                          'pianobar': 'Piano Bar', 'siren': 'Siren', 'spacealarm': 'Space Alarm', 'tugboat': 'Tug Boat',</span>
<span class="sd">                          'alien': 'Alien Alarm (long)', 'climb': 'Climb (long)', 'persistent': 'Persistent (long)',</span>
<span class="sd">                          'echo': 'Pushover Echo (long)', 'updown': 'Up Down (long)', 'none': 'None (silent)'}</span>
<span class="sd">    :return: None</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">pushover</span> <span class="kn">import</span> <span class="n">init</span> <span class="k">as</span> <span class="n">pushover_init</span> <span class="c1"># install with `pip3 install python-pushover`</span>
    <span class="kn">from</span> <span class="nn">pushover</span> <span class="kn">import</span> <span class="n">Client</span>
    <span class="c1"># Send Pushover notification via the API (this is the hamiltix key)</span>
    <span class="n">pushover_init</span><span class="p">(</span><span class="s1">'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'</span><span class="p">)</span>
    <span class="n">client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="s1">'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'</span><span class="p">)</span>
    <span class="n">client</span><span class="o">.</span><span class="n">send_message</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">sound</span><span class="o">=</span><span class="n">sound</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">lambda_handler</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">context</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">main</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'[FATAL] Caught exception: </span><span class="si">{}</span><span class="s1">'</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
        <span class="kn">import</span> <span class="nn">traceback</span>
        <span class="n">error_trace</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">format_exc</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">error_trace</span><span class="p">)</span>
        <span class="n">error_title</span> <span class="o">=</span> <span class="s1">'Error in [LambdaFunctionName]'</span>
        <span class="n">send_pushover</span><span class="p">(</span><span class="n">error_trace</span><span class="p">,</span> <span class="n">error_title</span><span class="p">,</span> <span class="n">sound</span><span class="o">=</span><span class="s1">'falling'</span><span class="p">)</span>
        <span class="k">raise</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>  <span class="c1"># Make sure the lambda function returns a 500</span></pre>
<p>Getting a push alert any time there is an error helps us respond to issues as soon as they come up. The same
<code>send_pushover()</code> is used to alert on other things as well, like any time a ticket is purchaced (with the cash
register sound naturally).</p>
</section>
</section>
<section id="cost">
<h2>Cost</h2>
<p>So how much does it cost to run hamiltix.net? Right now we are still in the 12 month AWS "free-tier" and monthly cost is
stable at around $0.60, of which $0.50 is Route53 (one hosted zone) and the rest is S3 and taxes. After the "free-tier"
expires our S3 costs will increase slightly, API Gateway will be $0.09 per GB of data transferred out, and Cloudfront
will be $0.085 for the first 10TB a month but Lambda, DynamoDB, and Cloudwatch will remain free (unless we get really
popular!), and <span class="strike">costs should remain under $1</span>. <a href="https://www.reddit.com/r/programming/comments/816mbu/how_we_built_hamiltixnet_for_less_than_1_a_month/dv17bbj/" target="_blank">Reddit</a> has
correced my error, and API Gateway has a base fee of $3.50 for the first 1 million requests. After the free-tier expires
costs should remain under $5. If we wanted to bring this down even more, moving the domain to Google
Domains (or similar) would reduce our current costs by 80%!</p>
<aside class="m-block m-success">
<h3>TLDR</h3>
<p>The combination of AWS and Gitlab allows for incredibly inexpensive yet powerful hosting solution with CI/CD and
monitoring that enables quick response to issues and automated building and deployment; all for under $1 a month!</p>
<p>Questions or comments?
blog (at) badsectorlabs.com</p>
</aside>
</section>
