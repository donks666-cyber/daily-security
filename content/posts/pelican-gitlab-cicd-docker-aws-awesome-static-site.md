Title: Pelican + Gitlab CI/CD + Docker + AWS = Awesome Static Site
Date: 2018-02-26 12:04
Category: DevOps
Tags: Gitlab, DevOps, Python
Slug: pelican-gitlab-cicd-docker-aws-awesome-static-site
Author: Erik
Summary: How I leverage Gitlab CI/CD and Pelican to create a static blog hosted on AWS S3

<p>All the code referenced in this post (and even this post itself) is available
<a href="https://gitlab.com/badsectorlabs/blog" target="_blank">on gitlab</a>.</p>
<section id="choosing-a-static-site-generator">
<h2>Choosing a static site generator</h2>
<p>Setting out to start a blog, there are tons of options. The classic <a href="https://wordpress.com/" target="_blank">Wordpress</a>,
the upstart <a href="https://ghost.org/" target="_blank">ghost</a> or the many static site generators like
<a href="https://jekyllrb.com/" target="_blank">jeckyll</a>, <a href="https://gohugo.io/" target="_blank">Hugo</a>, <a href="http://octopress.org/" target="_blank">Octopress</a> (abandoned), and
<a href="https://blog.getpelican.com/" target="_blank">Pelican</a>.  After looking at each option, I settled on pelican because I wanted a static
site (one less server to deal with), it's written in Python (one of my preferred languages) and it has an <a href="http://www.pelicanthemes.com/" target="_blank">extensive
library of themes</a> to use as a base. I decided on the <a href="http://mcss.mosra.cz/" target="_blank">m.css theme</a> because I liked its dark theme and lack of javascript (shout out to anyone reading this via
the Tor browser) and it has great support for code. I've only had to make a few small tweaks to m.css to make it my own.</p>
<p>Getting started with Pelican is simple, follow the m.css <a href="http://mcss.mosra.cz/pelican/#quick-start" target="_blank">quickstart</a>.</p>
<p>Pelican has a cool feature which makes tweaking themes or writing content easy - the devserver.</p>
<pre class="m-code">$<span class="w"> </span><span class="nb">cd</span><span class="w"> </span>/dir/of/pelican/blog
$<span class="w"> </span>make<span class="w"> </span>devserver
&lt;lots<span class="w"> </span>of<span class="w"> </span>output&gt;
Pelican<span class="w"> </span>and<span class="w"> </span>HTTP<span class="w"> </span>server<span class="w"> </span>processes<span class="w"> </span>now<span class="w"> </span>running<span class="w"> </span><span class="k">in</span><span class="w"> </span>background.
$</pre>
<p>Now Pelican is watching your files for changes, and will re-compile articles when you save a change. Keep an eye on the
terminal running the devserver though, if a change causes an error in Pelican it will show up there and your browser
will not see anything new.</p>
<p>Creating content is as easy as writing a <a href="http://docutils.sourceforge.net/rst.html" target="_blank">reStructuredText</a> document in the
<code>content</code>  directory. reStructuredText is awesome, and if you've used Markdown (Pelican also supports Markdown if you
prefer) before, it has the same general feel. The m.css
<span class="raw-html"><em><a href="http://mcss.mosra.cz/pelican/writing-content/" target="_blank">writing content</a></em></span> guide is a great primer
on reST. The only issue I have with reST is that markup can't be nested, so italicising a link is not as simple as
wrapping it in <code>*</code>. For instance, you would think that last <em>writing content</em> link would be written as</p>
<pre class="m-code"><span class="ge">*`writing content &lt;http://mcss.mosra.cz/pelican/writing-content/&gt;`_*</span></pre>
<p>But that is not allowed, so you have to define a directive at the top of the document to allow raw HTML and use it
in-line later, as so:</p>
<pre class="m-code"><span class="c">.. At the top of the document before any content</span>
<span class="p">..</span> <span class="ow">role</span><span class="p">::</span> raw-html(raw)
     <span class="nc">:format:</span> html
<span class="c">.. In-line</span>
<span class="na">:raw-html:</span><span class="nv">`&lt;em&gt;&lt;a href="http://mcss.mosra.cz/pelican/writing-content/"&gt;writing content&lt;/a&gt;&lt;/em&gt;`</span></pre>
</section>
<section id="hosting-a-static-site">
<h2>Hosting a static site</h2>
<p>Just like static site generators, there are a few static site hosts to choose from:
<a href="https://cloud.google.com/storage/docs/hosting-static-website" target="_blank">Google</a>, <a href="https://pages.github.com/" target="_blank">GitHub Pages</a>,
<a href="https://about.gitlab.com/features/pages/" target="_blank">GitLab Pages</a>, and <a href="https://aws.amazon.com/s3/" target="_blank">Amazon's S3</a>.</p>
<p>I choose S3, mostly because I am already familiar with AWS and am using it extensively for another project
(<a href="https://www.hamiltix.net" target="_blank">hamiltix.net</a>) which will be detailed in a future post. For the first 12 months on AWS you
get 5GB of S3 storage free, as well as 20k get requests and 2k put requests per month. Combine this with
<a href="https://aws.amazon.com/cloudfront/" target="_blank">Cloudfront</a> (AWS's CDN) and even if reddit tries to hug you to death you should
have no issues keeping your site up. In fact, if you want to use SSL/TLS with your S3 static site (hint:
<a href="https://security.googleblog.com/2016/09/moving-towards-more-secure-web.html" target="_blank">you do</a>) you <em>have</em> to use Cloudfront.</p>
<p>Instead of walking through another S3 and Cloudfront setup, just follow the <a href="https://medium.com/@sbuckpesch/setup-aws-s3-static-website-hosting-using-ssl-acm-34d41d32e394" target="_blank">same guide I used</a>.</p>
</section>
<section id="ci-cd-putting-it-all-together-automatically">
<h2>CI/CD - Putting it all together, automatically</h2>
<p>This is where the magic happens. On every push to master, your static site should build, minify, upload, and invalidate
the Cloudfront cache. This way you can write a post in a feature branch, and when you merge it into master your blog
updates without any additional actions! Gitlab is my git host of choice because it can be self-hosted and is very
powerful. Additionally, Gitlab.com offers unlimited free private repos with unlimited collaborators. But my favorite
feature of Gitlab is its built-in CI/CD. No longer do you need a seperate service to test/build/deploy your code, it's
all built right into your version control. Layer docker on top of this and you get easy, reporducable builds and all it
takes is one yaml file in the root of your repo!</p>
<p>Getting started with Gitlab CI/CD can be a little intimidating, and I've found using other projects <code>gitlab-ci.yml</code>
files as templates is the best way to get started. For instance, here is the <code>gitlab-ci.yml</code> file for this blog
(if you're on mobile, sorry in advance; there is no good way to show code on mobile without wrapping which kills
context):</p>
<pre class="m-code"><span class="nt">variables</span><span class="p">:</span>
<span class="w">  </span><span class="c1"># Set git strategy, recursive in case there are submodules</span>
<span class="w">  </span><span class="nt">GIT_STRATEGY</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">clone</span>
<span class="w">  </span><span class="nt">GIT_SUBMODULE_STRATEGY</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">recursive</span>
<span class="w">  </span><span class="c1"># Keys and secrets are defined in the project CI settings and exposed as env variables</span>
<span class="w">  </span><span class="nt">AWS_ACCESS_KEY_ID</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">$AWS_ACCESS_KEY_ID</span>
<span class="w">  </span><span class="nt">AWS_SECRET_ACCESS_KEY</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">$AWS_SECRET_ACCESS_KEY</span>
<span class="w">  </span><span class="nt">AWS_DEFAULT_REGION</span><span class="p">:</span><span class="w"> </span><span class="s">"us-east-1"</span>

<span class="c1"># Define two stages, if the site fails to build it will not be deployed</span>
<span class="nt">stages</span><span class="p">:</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">build</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">deploy</span>

<span class="nt">build</span><span class="p">:</span>
<span class="w">  </span><span class="nt">stage</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">build</span>
<span class="w">  </span><span class="nt">image</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">apihackers/pelican</span><span class="w">  </span><span class="c1"># This image contains everything needed to build a static pelican site</span>
<span class="w">  </span><span class="nt">artifacts</span><span class="p">:</span><span class="w">  </span><span class="c1"># artifacts are files that will be passed to the next CI stage and can be downloaded from the GitLab web</span>
<span class="w">              </span><span class="c1"># frontend as zips</span>
<span class="w">    </span><span class="nt">paths</span><span class="p">:</span>
<span class="w">      </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">output</span><span class="w">  </span><span class="c1"># This is the directory we want to save and pass to the next stage</span>
<span class="w">    </span><span class="nt">expire_in</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">1 week</span><span class="w">  </span><span class="c1"># Keep it around for a week in case we need to roll back</span>
<span class="w">  </span><span class="nt">script</span><span class="p">:</span><span class="w">  </span><span class="c1"># The script block is the series of commands that will be run in the container defined in `image`</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">pelican content -o output -s publishconf.py</span><span class="w">  </span><span class="c1"># Build the site using the publish config into the output directory</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">ls -lart output</span>
<span class="w">  </span><span class="nt">only</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">master</span><span class="w">  </span><span class="c1"># Only run this step on the master branch. No reason to spend resources on incomplete feature branches</span>


<span class="nt">deploy-prod</span><span class="p">:</span>
<span class="w">  </span><span class="nt">stage</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">deploy</span>
<span class="w">  </span><span class="nt">image</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">badsectorlabs/aws-compress-and-deploy</span><span class="w">  </span><span class="c1"># This is a custom image for minifying and working with AWS</span>
<span class="w">  </span><span class="nt">variables</span><span class="p">:</span><span class="w">  </span><span class="c1"># You can set per-stage variables like this</span>
<span class="w">    </span><span class="nt">DESC</span><span class="p">:</span><span class="w"> </span><span class="s">"Prod</span><span class="nv"> </span><span class="s">build,</span><span class="nv"> </span><span class="s">commit:</span><span class="nv"> </span><span class="s">$CI_COMMIT_SHA"</span><span class="w">  </span><span class="c1"># There are tons of built in env variables during the CI process</span>
<span class="w">    </span><span class="nt">S3_BUCKET</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">blog.badsectorlabs.com</span>
<span class="w">    </span><span class="nt">CLOUDFRONT_DISTRIBUTION_ID</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">$CLOUDFRONT_DISTRIBUTION</span><span class="w">  </span><span class="c1"># Again, the secrets are stored in GitLab, not in the code!</span>
<span class="w">  </span><span class="nt">script</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">cd output</span><span class="w"> </span><span class="c1"># Assumes the static site is in 'output' which is automatically created because the last step had</span>
<span class="w">                </span><span class="c1"># 'output' as an artifact</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo [+] ls before minification</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">ls -lart .</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo "$DESC" &gt; version.html</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo [+] minifying HTML</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">find . -iname \*.html | xargs -I {} htmlminify -o {} {}</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo [+] minifying CSS</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">find . -iname \*.css | xargs -I {} uglifycss --output {} {}</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo [+] minifying JS</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">find . -iname \*.js | xargs -I {} uglifyjs -o {} {}</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo [+] ls after minification</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">ls -lart .</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo [+] Syncing all files to $S3_BUCKET</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">aws s3 sync . s3://$S3_BUCKET --region us-east-2</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">echo [+] Invalidating Cloudfront cache</span><span class="w">  </span><span class="c1"># This step is necessary or you wont see the changes until the TTL expires</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DISTRIBUTION_ID --paths '/*'</span>
<span class="w">  </span><span class="nt">environment</span><span class="p">:</span><span class="w">  </span><span class="c1"># environments are just ways to control what is deployed where, for a simple blog straight to prod is ok</span>
<span class="w">    </span><span class="nt">name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">master-prod</span>
<span class="w">  </span><span class="nt">only</span><span class="p">:</span>
<span class="w">    </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">master</span>
<span class="w">  </span><span class="nt">when</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">manual</span><span class="w">  </span><span class="c1"># This causes GitLab to wait until you click the run button before executing this stage</span></pre>
<aside class="m-block m-success">
<h3>Success!</h3>
<p>And there you have it. A clean, static, no-javascript blog with posts you can write in reST and deploy with a git
push.</p>
<p>Questions or comments?
blog (at) badsectorlabs.com</p>
</aside>
</section>
