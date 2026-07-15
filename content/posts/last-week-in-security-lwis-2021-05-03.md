Title: Last Week in Security (LWiS) - 2021-05-03
Date: 2021-05-03 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-05-03
Author: Erik
Summary: Policy change (<a href="https://twitter.com/github" target="_blank">@github</a>), Marauder's map (<a href="https://twitter.com/Jean_Maes_1994" target="_blank">@Jean_Maes_1994</a>), Null byte injection in GoAhead (<a href="https://mobile.twitter.com/luker983" target="_blank">@luker983</a>), in-mem DLL loader (<a href="https://twitter.com/scythe_io" target="_blank">@scythe_io</a>), Firebase fronting (<a href="https://twitter.com/shantanukhande" target="_blank">@shantanukhande</a>), Source Engine client RCE (<a href="https://twitter.com/4lpine" target="_blank">@4lpine</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-04-26 to 2021-05-03.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://github.blog/2021-04-29-call-for-feedback-policies-exploits-malware/" target="_blank">A call for feedback on our policies around exploits and malware</a>. The Microsoft owned GitHub has taken down a few exploits in the past (all against Microsoft products I believe). While there are lots of hot takes on infosec twitter about how this is the end of hosting exploits on GitHub, from my reading GitHub is being about as reasonable as a Microsoft owned company can be at this stage. If we see projects being removed at a higher rate after this, perhaps those hot takes will be warranted. I find it somewhat ironic that git was built as a way to share code peer-to-peer (decentralized) and we as a community have turned to one centralized git host for nearly all our code.</li>
<li><a href="https://www.vice.com/en/article/k78a53/the-irs-wants-help-hacking-cryptocurrency-hardware-wallets" target="_blank">The IRS Wants Help Hacking Cryptocurrency Hardware Wallets</a>. I find it interesting the IRS is looking for "repeatable, consistent" process to break hardware devices designed to store secrets and launches <a href="https://news.bloombergtax.com/daily-tax-report/irss-operation-hidden-treasure-focusing-on-crypto-fraud" target="_blank">Operation Hidden Treasure</a>, while there are maybe other <a href="https://itep.org/fact-sheet-apple-and-tax-avoidance/" target="_blank">issues</a> <a href="https://www.propublica.org/article/filing-taxes-could-be-free-simple-hr-block-intuit-lobbying-against-it" target="_blank">to</a> <a href="https://en.wikipedia.org/wiki/Panama_Papers" target="_blank">focus</a> <a href="https://www.investopedia.com/stock-analysis/2013/investing-news-for-jan-29-hsbcs-money-laundering-scandal-hbc-scbff-ing-cs-rbs0129.aspx" target="_blank">on</a>.</li>
<li><a href="https://blog.appcensus.io/2021/04/27/why-google-should-stop-logging-contact-tracing-data/" target="_blank">Why Google Should Stop Logging Contact-Tracing Data</a>. After all the cryptographic work to ensure contract-tracing apps would preserve privacy, Google goes and dumps all the temporary identifiers into logs readable by phone manufacturers and other "privileged" apps. Who would have thought that a massive surveillance system on every smartphone would be potentially abused (<em>surprised-pickachu.jpg</em>).</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.nviso.eu/2021/04/27/i-solemnly-swear-i-am-up-to-no-good-introducing-the-marauders-map/" target="_blank">I Solemnly Swear I Am Up To No Good. Introducing the Marauders Map</a>. Jean-Francois makes good points about developing your own tools, or at least <a href="https://www.offensive-security.com/offsec/understanding-pentest-tools-scripts/" target="_blank">understanding the tools/scripts you use in a Pentest</a>. He has created an internal attack toolkit that can run C# binaries from the internet. This is useful for constrained environments like Citrix desktops or other machines with limited access to applications beyond MS Office, as you can run them from Macros.</li>
<li><a href="https://luker983.github.io/blog/2021-04-26-Embedded-Webserver-Null-Byte-Injection/" target="_blank">Discovering Null Byte Injection Vulnerability in GoAhead</a>. This article goes to show that sometimes CTFs turn out real vulnerabilities!</li>
<li><a href="https://labs.jumpsec.com/burp-suite-python-scripter/" target="_blank">Overcoming Issues Using Custom Python Scripts with Burp Suite Professional</a>. Burp Suite Professional is a great tool, and one of the best features is the ability to add your own features! Using the Python Scripter extension you are able to modify all requests, even from the active scanner, to get better results against custom web applications.</li>
<li><a href="https://www.pentagrid.ch/de/blog/password-reset-code-brute-force-vulnerability-in-AWS-Cognito/" target="_blank">Password reset code brute-force vulnerability in AWS Cognito</a>. While there were limits on password reset tokens (6-digit numbers), the researchers in this post managed to use Turbo Intruder and simultaneous TCP connections to get a 0.32% chance of guessing a Cognito reset token. Not bad if you have a big list of users.</li>
<li><a href="https://talosintelligence.com/vulnerability_reports/TALOS-2020-1211" target="_blank">Linux Kernel /proc/pid/syscall information disclosure vulnerability</a>. While not super useful on its own, if you have a Linux bug that requires an information disclosure to defeat ASLR, this might be for you.</li>
<li><a href="https://www.redteam.cafe/red-team/domain-front/firebase-domain-front-hiding-c2-as-app-traffic" target="_blank">Firebase Domain Front - Hiding C2 as App traffic</a>. While Azure has killed classic domain fronting, these "function" based fronts will continue to work because the ability to run arbitrary code as a "function" is their core purpose.</li>
<li><a href="https://ctf.re/source-engine/exploitation/2021/05/01/source-engine-2/" target="_blank">Exploiting the Source Engine (Part 2) - Full-Chain Client RCE in Source using Frida</a>. This very detailed post shows how Frida and x32dbg were used to get an RCE by modifying a Team Fortress 2 server to send malformed traffic.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/xinbailu/DripLoader" target="_blank">DripLoader</a> is an evasive shellcode loader for bypassing event-based injection detection, without necessarily suppressing event collection, but does use direct syscalls. By using "standard" looking allocations and APIs, along with delays, DripLoader makes it difficult of EDRs to detect malicious activity during loading. It may be worth borrowing some of these techniques for your own custom loader.</li>
<li><a href="https://github.com/d4rckh/vaf" target="_blank">vaf</a> is a "very advanced fuzzer" written in Nim. While not as featured as <a href="https://github.com/ffuf/ffuf" target="_blank">ffuf</a> I enjoy seeing more Nim projects.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/SharpNamedPipePTH" target="_blank">SharpNamedPipePTH</a> is a C# version of the tool to use Pass-the-Hash for authentication on a local Named Pipe for user Impersonation. There is a <a href="https://s3cur3th1ssh1t.github.io/Named-Pipe-PTH/" target="_blank">blog post</a> for explanation (from LWiS 2020-04-19).</li>
<li><a href="https://github.com/scythe-io/memory-module-loader" target="_blank">memory-module-loader</a>  is an implementation of a Windows loader that can load dynamic-link libraries (DLLs) directly from memory. The loader exposed by the Windows operating system can only load modules from disk via LoadLibrary or LoadLibraryEx. However, it is entirely possible to load libraries from memory instead. This is one such implementation. This loader supports loading resources as well.</li>
<li><a href="https://github.com/Cr4sh/MicroBackdoor" target="_blank">MicroBackdoor</a> is a C2 tool for Windows targets with an easily customizable codebase and small footprint. Micro Backdoor consists of a server, client, and dropper. It wasn't designed as replacement for your favorite post-exploitation tools but rather as really minimalistic thing with all of the basic features in less than 5000 lines of code.</li>
<li><a href="https://github.com/Ben0xA/DoUCMe" target="_blank">DoUCMe</a> leverages the NetUserAdd Win32 API to create a new computer account. This is done by setting the usri1_priv of the USER_INFO_1 type to 0x1000. The primary goal is to avoid the normal detection of new user created events (4720). This will hide the user in the Control Panel and the lusrmgr.msc Snap In. It will show up in the Group Listing, but not as a user.</li>
<li><a href="https://github.com/projectdiscovery/interactsh" target="_blank">interactsh</a> is an open-source solution for out of band data extraction, A tool designed to detect bugs that cause external interaction (blind SQLi, blind CMDi, SSRF, etc). Interactsh is an alternative to Burp Collaborator with potential to tie into other tools (i.e. nuclei).</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/KCarretto/paragon" target="_blank">paragon</a> is a red team engagement platform with the goal of unifying offensive tools behind a simple UI. This project looks really cool, and does a ton of the heavy lifting that everyone who has though, "I'll write my own implant/c2" has run into. I'm surprised this hasn't gotten more press (or maybe I've just missed it?).</li>
<li><a href="https://github.com/GemGeorge/SniperPhish" target="_blank">SniperPhish</a> is a phishing platform that has a few more features than the favorite <a href="https://getgophish.com/" target="_blank">Gophish</a>, like an advanced web page builder to customize credential harvesting. I have yet to find a phishing platform that allows for "inbox management" (i.e. replying to emails via the web interface).</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
