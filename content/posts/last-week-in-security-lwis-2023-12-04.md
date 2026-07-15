Title: Last Week in Security (LWiS) - 2023-12-04
Date: 2023-12-04 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-12-04
Author: Erik
Summary: O365 Phishing infra (<a href="https://twitter.com/pfiatde" target="_blank">@pfiatde</a>), EvilSlackbot (<a href="https://twitter.com/infosec_drewze" target="_blank">@infosec_drewze</a>), Sonos jailbreak (<a href="https://twitter.com/alexjplaskett" target="_blank">@alexjplaskett</a>), DNS attacks (<a href="https://twitter.com/timolongin" target="_blank">@timolongin</a>), DNS rebinding attack (<a href="https://twitter.com/_danielthatcher" target="_blank">@_danielthatcher</a>), and more!

<aside class="m-note m-warning">
<h3>year += 1</h3>
<p>This will be the last LWiS of 2023. See you next year!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-11-27 to 2023-12-04.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://support.apple.com/en-us/HT214031" target="_blank">About the security content of iOS 17.1.2 and iPadOS 17.1.2</a>. Two webkit vulnerabilities may have been exploited in the wild. Not to be outdone, <a href="https://chromereleases.googleblog.com/2023/11/stable-channel-update-for-desktop_28.html" target="_blank">Chrome</a> patched their sixth 0day this year. Browsers are where the data is and the most frequent way users execute untrusted code, so its where the high value exploitation is as well.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://sec-consult.com/blog/detail/taking-over-a-country-kaminsky-style/" target="_blank">TRAP; RESET; POISON; - Taking over a country Kaminsky style</a>. A CGNAT device allows for "Kaminsky style" DNS attacks.</li>
<li><a href="https://github.blog/2023-11-30-securing-our-home-labs-home-assistant-code-review/" target="_blank">Securing our home labs: Home Assistant code review</a>. A detailed write up of a few nice bugs in Home Assistant.</li>
<li><a href="https://badoption.eu/blog/2023/12/03/PhishingInfra.html" target="_blank">O365 Phishing infrastructure</a>. "Last year, mails sent by Dev Tenants got immediately flagged, but something changed." Oh boy. If there isn't a fix for this soon it <em>will</em> be abused.</li>
<li><a href="https://www.ambionics.io/blog/owncloud-cve-2023-49103-cve-2023-49105" target="_blank">Owncloud: details about CVE-2023-49103 and CVE-2023-49105</a>. Full details on the owncloud vulnerabilities from last week.</li>
<li><a href="https://research.nccgroup.com/2023/12/04/shooting-yourself-in-the-flags-jailbreaking-the-sonos-era-100/" target="_blank">Shooting Yourself in the .flags - Jailbreaking the Sonos Era 100</a>. Some U-boot and hardware hacking of a smart speaker.</li>
<li><a href="https://www.intruder.io/research/we-hacked-ourselves-with-dns-rebinding" target="_blank">We Hacked Ourselves With DNS Rebinding</a>. A very neat usecase for DNS rebinding which is often a theoretical attack. I also like that the author didn't stop investigating when the change to IMDSv2 was made which prevented the outcome, but didn't solve the original "vulnerability."</li>
<li><a href="https://www.hunters.security/en/blog/delefriend-a-newly-discovered-design-flaw-in-domain-wide-delegation-could-leave-google-workspace-vulnerable-for-takeover" target="_blank">DeleFriend: Severe design flaw in Domain Wide Delegation could leave Google Workspace vulnerable for takeover</a>. Juciy potential privesc for Google Workspace. They even included a nice tool: <a href="https://github.com/axon-git/DeleFriend/" target="_blank">DeleFriend</a>.</li>
<li><a href="https://github.com/research-virus/stuxnet" target="_blank">stuxnet</a> - Public open-source code of malware Stuxnet (aka MyRTUs).</li>
<li><a href="https://therealunicornsecurity.github.io/Tricard/" target="_blank">Tricard - Malware sandboxes fingerprinting</a>. Create binaries that ship back system fingerprints to find sandboxes!</li>
<li><a href="https://clearbluejar.github.io/posts/decompilation-debugging-pretending-all-binaries-come-with-source-code/#pretend-like-your-binary-comes-with-source" target="_blank">Decompilation Debugging</a>. Amazing post about how to debug complex code without source (they use the Windows RPC server as a target) using Ghidra.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Drew-Sec/EvilSlackbot" target="_blank">EvilSlackbot</a> -  A Slack bot phishing framework for Red Teaming exercises. There is a <a href="https://drew-sec.github.io/EvilSlackbot/" target="_blank">blog post</a> about its use as well.</li>
<li><a href="https://github.com/BlackSnufkin/GhostDriver" target="_blank">GhostDriver</a> - yet another AV killer tool using BYOVD.</li>
<li><a href="https://github.com/xforcered/ADOKit" target="_blank">ADOKit</a> -  Azure DevOps Services Attack Toolkit.</li>
<li><a href="https://github.com/gregoryc/standardlib" target="_blank">standardlib</a> -  A complete standardlib for c for once.</li>
<li><a href="https://github.com/weaselsec/ClickOnce-AppDomain-Manager-Injection" target="_blank">ClickOnce-AppDomain-Manager-Injection</a> - ClickOnce + AppDomain Manager Injection.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/ergrelet/windiff" target="_blank">windiff</a> - Web-based tool that allows comparing symbol, type and syscall information of Microsoft Windows binaries across different versions of the OS.</li>
<li><a href="https://github.com/Tw1sm/PySQLRecon" target="_blank">PySQLRecon</a> - Offensive MSSQL toolkit written in Python, based off SQLRecon.</li>
<li><a href="https://github.com/dotnet/Kerberos.NET" target="_blank">Kerberos.NET</a> -  A Kerberos implementation built entirely in managed code.</li>
<li><a href="https://github.com/B64-Cryptzo/Scudo" target="_blank">Scudo</a> is a C++ class that encrypts and dynamically executes functions. This open-source repository offers a concise solution for securing and executing encrypted functions in your codebase.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 364 (+2)</p>
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
