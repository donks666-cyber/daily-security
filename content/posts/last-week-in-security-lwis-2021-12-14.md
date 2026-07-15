Title: Last Week in Security (LWiS) - 2021-12-14
Date: 2021-12-14 23:15
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-12-14
Author: Erik
Summary: Log4j RCE, sAMAccountName [DA from any user] (<a href="https://twitter.com/exploitph" target="_blank">@exploitph</a>), XLAM tricks (<a href="https://twitter.com/_DaWouw" target="_blank">@_DaWouw</a>), Cobalt Strike 4.5 and MiTM (<a href="https://twitter.com/joevest" target="_blank">@joevest</a>, <a href="https://twitter.com/DidierStevens" target="_blank">@DidierStevens</a>), CVEtrends (<a href="https://twitter.com/simonbyte" target="_blank">@SimonByte</a>), additional Windows kernel tricks (<a href="https://twitter.com/cerbersec" target="_blank">@cerbersec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-12-07 to 2021-12-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2021-44228" target="_blank">log4j logging framework vulnerable to RCE (10.0 CVSS3)</a>. Who knew that the ability to do <a href="https://logging.apache.org/log4j/2.13.0/manual/lookups.html#JndiLookup" target="_blank">Jndi lookups</a> with user supplied data could be such and awful idea. Early reports claimed a recent version of Java and some environment variables would mitigate the vulnerability, but they were <a href="https://twitter.com/marcioalm/status/1470361495405875200" target="_blank">mistaken</a>. Check out this <a href="https://gist.github.com/SwitHak/b66db3a06c2955a9cb71a8718970c592" target="_blank">Blue Team Cheatsheet</a> for links to advisories.</li>
<li><a href="https://www.reddit.com/r/GooglePixel/comments/r4xz1f/pixel_prevented_me_from_calling_911/hnrvsr1/?context=3" target="_blank">Pixel prevented me from calling 911</a>. When you give up control of a core function like dialing to third party apps, in this case Microsoft Teams, bad things can happen.</li>
<li><a href="https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/" target="_blank">Improve kernel security with the new Microsoft Vulnerable and Malicious Driver Reporting Center</a>. You can now submit drivers directly to Microsoft with details about how they are vulnerable or malicious.</li>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-4-5-fork-run-youre-history/" target="_blank">Cobalt Strike 4.5: Fork&amp;Run – you’re "history"</a>. "We dedicated a significant portion of this release to improving controls around product licensing." When your tool is used in nearly all ransomware events, I suspect HelpSystems got a call from someone to put more controls in place. The biggest change in this release for users is the ability to define custom process injection technique as well as increased size limits for sleep mask kit and user reflective loaders. Cobalt Strike continues to innovate and adapt to the changing offensive security landscape - the reason why it is the go to tool in the space.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://exploit.ph/cve-2021-42287-cve-2021-42278-weaponisation.html" target="_blank">CVE-2021-42287/CVE-2021-42278 Weaponisation</a>. With all the log4j hype, this one may have slipped by. Don't let it, as it allows any domain user with the ability to add computer accounts (default 10 per user), can get a ticket as a DC to arbitrary services which allows dcsyncing. Patch is out, but given the season and log4j, this one might have legs into 2022. Be sure to also checkout <a href="https://exploit.ph/more-samaccountname-impersonation.html" target="_blank">more sAMAccountName Impersonation</a>. The switches needed for this attack are <a href="https://github.com/GhostPack/Rubeus/blob/master/CHANGELOG.md#200---2021-08-04" target="_blank">now in Rubeus</a>.</li>
<li><a href="https://outflank.nl/blog/2021/12/09/a-phishing-document-signed-by-microsoft/" target="_blank">A phishing document signed by Microsoft – part 1</a>. The masters of maldocs are back at it. This time using an Excel add-in (XLAM) with modified contents but "valid" Microsoft signature to deliver malicious vbs. Amazing work as always.</li>
<li><a href="https://securitylab.github.com/research/ubuntu-accountsservice-CVE-2021-3939/" target="_blank">Getting root on Ubuntu through wishful thinking</a>. Exploits are hard, even when you get root sometimes you aren't sure why. Adding a sleep to allow the ability to attach a debugger when the process did eventually crash was clever. Full PoC <a href="https://github.com/github/securitylab/tree/b36e194556f956c3ec63bf9d8af454c8f620f33a/SecurityExploits/Ubuntu/accountsservice_CVE-2021-3939" target="_blank">here</a>.</li>
<li><a href="https://blog.didierstevens.com/2021/12/11/mitm-cobalt-strike-network-traffic/" target="_blank">MiTM Cobalt Strike Network Traffic</a>. This relies on having the beacon private keys, but once in hand, network defenders or those in privileged network positions could inject commands into Cobalt Strike traffic.</li>
<li><a href="https://blog.nviso.eu/2021/12/09/kernel-karnage-part-6-last-call/" target="_blank">Kernel Karnage – Part 6 (Last Call)</a>. This series has been great thus far. Let's seen what kernel driver loading tricks they come up with in future posts!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://cvetrends.com/" target="_blank">CVE Trends</a> is a dashboard for <span class="strike">expensive threat intel</span> monitoring twitter without having to learn about <a href="https://tweetdeck.twitter.com/" target="_blank">tweetdeck</a>. This is a really nice site check for the latest log4j RCE or to put up in your NOC.</li>
<li><a href="https://iongion.github.io/podman-desktop-companion/" target="_blank">Podman Desktop</a> is the Docker desktop replacement you may be looking for now that <a href="https://www.docker.com/pricing/faq" target="_blank">Docker Desktop is no longer free for most companies</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/quic/AFLTriage" target="_blank">AFLTriage</a> is a tool to triage crashing input files using a debugger. It is designed to be portable and not require any run-time dependencies, besides libc and an external debugger. It supports triaging crashes generated by any program, not just AFL, but recognizes AFL directories specially, hence the name.</li>
<li><a href="https://github.com/IkerSaint/KingHamlet" target="_blank">KingHamlet</a> is a simple tool, which allows you to perform a <a href="https://www.elastic.co/blog/process-ghosting-a-new-executable-image-tampering-attack" target="_blank">Process Ghosting Attack</a>.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
