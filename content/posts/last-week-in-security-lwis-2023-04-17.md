Title: Last Week in Security (LWiS) - 2023-04-17
Date: 2023-04-17 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-04-17
Author: Erik
Summary: PDF RCE (<a href="https://twitter.com/sigabrt9" target="_blank">@sigabrt9</a>), more PersistAssist (<a href="https://twitter.com/FortyNorthSec" target="_blank">@FortyNorthSec</a>), 5x SMM vulns (<a href="https://twitter.com/uffeux" target="_blank">@uffeux</a>), PRTG XSS 0day (<a href="https://twitter.com/SkylightCyber" target="_blank">@SkylightCyber</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-04-10 to 2023-04-17.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2023/04/announcing-depsdev-api-critical.html" target="_blank">Announcing the deps.dev API: critical dependency data for secure supply chains</a>.  5 million packages and more than 50 million versions from the Go, Maven, PyPI, npm, and Cargo ecosystems have been documented by Google and are available via an API for you.</li>
<li><a href="https://www.vice.com/en/article/y3wddv/much-hyped-water-plant-hack-wasnt-a-hack-was-actually-user-error-official-says" target="_blank">Much-Hyped Water Plant Hack Wasn't a Hack, Was Actually User Error, Official Says</a>. In this edition of "attribution is hard..." (alternative theory: the attackers were so good the FBI couldn't find any trace, but ya know, <a href="https://en.wikipedia.org/wiki/Occam%27s_razor" target="_blank">Occam's razor</a>).</li>
<li><a href="https://aws.amazon.com/codewhisperer/" target="_blank">Amazon CodeWhisperer</a>. GitHub Copilot X price got you down? Feed your code into <span class="strike">a different megacorp</span> Amazon for free and get code completion suggestions from an AI. At least this one tells you the license of the code <span class="strike">you're stealing</span> it got inspiration from.</li>
<li><a href="https://blog.thinkst.com/2023/04/birds-at-tailscale.html" target="_blank">Birds at (Tail)scale</a>. Now you can one-click deploy a honeypot to your tailscale network. I have yet to see a better signal to noise ratio for any detection technology.</li>
<li><a href="https://www.fortinet.com/blog/threat-research/are-internet-macros-dead-or-alive" target="_blank">Are Internet Macros Dead or Alive?</a>. <a href="https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines" target="_blank">Betteridge</a> never fails. Some good lure/prompt images to borrow for red teaming in this article. The template location lure would work against up to date Word installs.</li>
<li><a href="https://eu-symbols.rizin.re/" target="_blank">Rizin Silhouette Server</a>. The Rizin team is running a public symbol server!</li>
<li><a href="https://blog.redteam-pentesting.de/2023/rooting-printer/" target="_blank">Rooting a Common-Criteria Certified Printer to Improve OPSEC</a>. Some serious dedication to privacy. But why print the reports in the first place?</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://offsec.almond.consulting/ghostscript-cve-2023-28879.html" target="_blank">Shell in the Ghost: Ghostscript CVE-2023-28879 writeup</a>. "This write-up details how CVE-2023-28879 - an RCE in Ghostscript - was found and exploited. Due to the prevalence of Ghostscript in PostScript processing, this vulnerability may be reachable in many applications that process images or PDF files (e.g. ImageMagick, PIL, etc.), making this an important one to patch and look out for."</li>
<li><a href="https://codewhitesec.blogspot.com/2023/04/java-exploitation-restrictions-in.html" target="_blank">Java Exploitation Restrictions in Modern JDK Times</a>. With lots of enterprise software still being written in Java, the exploitation isn't slowing down, just adapting.</li>
<li><a href="https://fortynorthsecurity.com/blog/extending-and-detecting-persistassist-act-ii/" target="_blank">Extending (and Detecting) PersistAssist: Act II</a>. Write some C# to persist with WMI event subscriptions.</li>
<li><a href="https://fortynorthsecurity.com/blog/autofunkt/" target="_blank">Introducing AutoFunkt: Automated Cloud Redirector Generation</a>. Cloud functions are very useful for redirecting C2 traffic through high reputation domains, but they can be a pain to set up - until now!</li>
<li><a href="https://gynvael.coldwind.pl/?id=766" target="_blank">On self-healing code and the obvious issue</a>. It's like command injection, but you get to write it in plain english.</li>
<li><a href="https://labs.jumpsec.com/butting-heads-with-a-threat-actor-on-an-engagement/" target="_blank">Butting Heads with a Threat Actor on an Engagement</a>. Now ask what would happen if the actor cleaned up properly, and then patched the vulnerability (or at least mitigated it). Detection must have layers!</li>
<li><a href="https://research.nccgroup.com/2023/04/11/stepping-insyde-system-management-mode/" target="_blank">Stepping Insyde System Management Mode</a>. It's a bit wild that as a result of a code leak Insyde got a free audit and 5 vulnerabilities found.</li>
<li><a href="https://offensivedefence.co.uk/posts/dinvoke-105/" target="_blank">D/Invoke v1.0.5</a>. A few new functions to make your C# tooling a bit more ergonomic.</li>
<li><a href="https://www.pentagrid.ch/de/blog/multiple-vulnerabilities-in-aten-PE8108-power-distribution-unit/" target="_blank">Multiple vulnerabilities in Aten PE8108 power distribution unit</a>. Even your PDU is trying to get you pwned.</li>
<li><a href="https://malicious.link/post/2023/simple-php-webshell-with-php-filter-chains/" target="_blank">Simple PHP webshell with php filter chains</a>. In memory PHP webshell!?</li>
<li><a href="https://www.reversemode.com/2023/04/losing-control-over-schneiders.html" target="_blank">Losing control over Schneider's EcoStruxure Control Expert</a>. Unauthenticated RCE, this time in your SCADA workstation.</li>
<li><a href="https://kentindell.github.io/2023/04/03/can-injection/" target="_blank">CAN Injection: keyless car theft</a>. Woah. You wouldn't download a car exploit?</li>
<li><a href="https://skylightcyber.com/2023/04/18/popping-tags/" target="_blank">Popping Tags: Exploiting Template Injections in PRTG Network Monitor</a>. Currently an 0day. Careful what links your PRTG admin is clicking.</li>
<li><a href="https://www.trustedsec.com/blog/hacking-your-cloud-tokens-edition-2-0/" target="_blank">Hacking Your Cloud: Tokens Edition 2.0</a>. A great post on Azure/Office tokens and how to pivot them to more access.</li>
<li><a href="https://slashparity.com/?p=938" target="_blank">GCP Pentesting Guide</a>. Some Google specific cloud hacking.</li>
<li><a href="https://www.fo-sec.com/articles/10-defender-bypass-methods" target="_blank">Bypassing Windows Defender (10 Ways)</a>. Nothing novel here but a nice collection of techniques.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/VoldeSec/PatchlessCLRLoader" target="_blank">PatchlessCLRLoader</a> - .NET assembly loader with patchless AMSI and ETW bypass. Also comes in BOF form: <a href="https://github.com/VoldeSec/PatchlessInlineExecute-Assembly" target="_blank">PatchlessInlineExecute-Assembly</a>.</li>
<li><a href="https://github.com/zwclose/KillerVuln2" target="_blank">KillerVuln2</a> - Files for PoC of vulnerability in Intel Killer Performance Suite</li>
<li><a href="https://github.com/t3l3machus/PowerShell-Obfuscation-Bible" target="_blank">PowerShell-Obfuscation-Bible</a> - A collection of techniques, examples and a little bit of theory for manually obfuscating PowerShell scripts to achieve AV evasion, compiled for educational purposes. The contents of this repository are the result of personal research, including reading materials online and conducting trial-and-error attempts in labs and pentests.</li>
<li><a href="https://github.com/MellowNight/2D-Injector" target="_blank">2D-Injector</a> - Hiding unsigned DLL inside a signed DLL.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/thecyberneh/scriptkiddi3" target="_blank">scriptkiddi3</a> - Streamline your recon and vulnerability detection process with SCRIPTKIDDI3, A recon and initial vulnerability detection tool built using shell script and open source tools.</li>
<li><a href="https://github.com/improsec/BackupOperatorToolkit" target="_blank">BackupOperatorToolkit</a> - contains different techniques allowing you to escalate from Backup Operator to Domain Admin</li>
<li><a href="https://github.com/hay-kot/homebox" target="_blank">homebox</a> - Homebox is the inventory and organization system built for the Home User.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 338 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
