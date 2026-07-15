Title: Last Week in Security (LWiS) - 2025-09-08
Date: 2025-09-08 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-09-08
Author: Erik
Summary: Metamorphic compilation (<a href="https://x.com/tijme" target="_blank">@tijme</a>), Windows Secure Calls (<a href="https://x.com/33y0re" target="_blank">@33y0re</a>), macOS race condition exploit (<a href="https://x.com/patch1t" target="_blank">@patch1t</a>), NTLM relaying (<a href="https://x.com/elad_shamir" target="_blank">@elad_shamir</a>), iOS zero-click RE (<a href="https://x.com/quarkslab" target="_blank">@quarkslab</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-09-02 to 2025-09-08.</p>
<section id="news">
<h2>News</h2>
<ul><li><p><a href="https://specterops.io/specter-bash/?_gl=1*1kj5qw5*_up*MQ..*_ga*MjY5MDYzMDg2LjE3NTYyMzE0NDY.*_ga_53SGLN9EBJ*czE3NTYyMzE0NDUkbzEkZzAkdDE3NTYyMzE0NDUkajYwJGwwJGgw" style="color: #3bd267;" target="_blank">Specter Bash 2025 – October 6–9, 2025 | Denver, CO</a>  is SpecterOps' annual training event with a Halloween twist. Over four days, participants take part in SpecterOps courses on Red Team Operations, Tradecraft Analysis, Identity-driven Offensive Tradecraft, and Detection, led by the team behind BloodHound. When classes wrap up, evening sessions and community gatherings keep the energy going and give plenty of opportunities to connect with one another. Can’t attend in person? They have virtual options too! Last Week in Security readers get an exclusive <b>25% discount</b> with code <code>LWIS</code>. Get the full details and register <a href="https://specterops.io/specter-bash/?_gl=1*1kj5qw5*_up*MQ..*_ga*MjY5MDYzMDg2LjE3NTYyMzE0NDY.*_ga_53SGLN9EBJ*czE3NTYyMzE0NDUkbzEkZzAkdDE3NTYyMzE0NDUkajYwJGwwJGgw/" style="color: #3bd267;" target="_blank">here</a>. <span class="m-label m-flat m-success">Sponsored</span></p></li></ul><ul>
<li><a href="https://blog.cloudflare.com/unauthorized-issuance-of-certificates-for-1-1-1-1/" target="_blank">Addressing the unauthorized issuance of multiple TLS certificates for 1.1.1.1</a> - I'm a bit surprised a company as security focused as Cloudflare didn't notice a rogue certificate for their service for 7 months, and reported to them three separate times, two of them being mistriaged. Even if an attacker had the certificates, they would still need to intercept traffic to decrypt/respond to it.</li>
<li><a href="https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack" target="_blank">npm Author Qix Compromised via Phishing Email in Major Supply Chain Attack</a> - Supply chain attacks have been ramping up, and this attack on JavaScript's Node Package Manager (NPM) looks to be one of the biggest to date in terms of potential impact. Good news is the payload was just a cryptocurrency stealer. Imagine if it had been ransomware, or a stealthy APT.</li>
<li><a href="https://blog.mozilla.org/futurereleases/2025/09/05/firefox-32-bit-linux-support-to-end-in-2026/" target="_blank">Firefox 32-bit Linux Support to End in 2026</a> - This lines up with, <a href="https://support.mozilla.org/en-US/kb/firefox-users-windows-7-8-and-81-moving-extended-support" target="_blank">Firefox users on Windows 7, 8 and 8.1 moving to Extended Support Release</a> also ending support in 2026, despite the operating systems having no support from Microsoft since January 2023.</li>
<li><a href="https://arstechnica.com/gadgets/2025/07/bankrupt-futurehome-suddenly-makes-its-smart-home-hub-a-subscription-service/" target="_blank">Futurehome smart hub owners must pay new $117 subscription or lose access</a> - This is ransomware and should be illegal.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://connormcgarr.github.io/secure-calls-and-skbridge/" target="_blank">Windows Internals: Secure Calls - The Bridge Between The NT Kernel and Secure Kernel</a> - "This post will be taking a look at the architecture which allows NT, which is in a completely isolated region of physical memory from the Secure Kernel, to “hand off” execution to the Secure Kernel, as well as showcase some of the common patterns NT and SK use in regards to copying and encapsulating parameters and output from VTL 0 &lt;-&gt; VTL 1 and VTL 1 &lt;-&gt; VTL 0." Connor's posts are always worth the read, and he dropped <a href="https://github.com/connormcgarr/Vtl1Mon" target="_blank">Vtl1Mon</a> (Virtual Trust Level (VTL 1) secure call tracing), to explore on your own.</li>
<li><a href="https://jhftss.github.io/Exploiting-the-Impossible/" target="_blank">Exploiting the Impossible: A Deep Dive into A Vulnerability Apple Deems Unexploitable</a> - Deep in Apple's file-copy API there was a race condition which Apple said was unexploitable. Spoiler: <a href="https://www.youtube.com/watch?v=lrAUbRon0SY" target="_blank">it was exploitable</a> and required two patches to finally fix.</li>
<li><a href="https://blog.quarkslab.com/patch-analysis-of-Apple-iOS-CVE-2025-43300.html" target="_blank">Reverse engineering of Apple's iOS 0-click CVE-2025-43300: 2 bytes that make size matter</a> - How about some more deep technical Apple exploitation? Parsing user generated content continues to be a hard problem, and this one was likely worth up to <a href="https://www.crowdfense.com/exploit-acquisition-program/" target="_blank">$7 million USD</a>.</li>
<li><a href="https://www.netspi.com/blog/executive-blog/web-application-pentesting/vibe-coding-a-pentesters-dream/" target="_blank">Vibe Coding: A Pentester’s Dream</a> - Some real world examples of AI-created code being confidently insecure. Our jobs are safe, for now.</li>
<li><a href="https://specterops.io/wp-content/uploads/sites/3/2025/04/SPO_NTLM_WhitePaper_Updated.pdf" target="_blank">[PDF] The Renaissance of NTLM Relay Attacks: Everything You Need to Know</a> - NTLM relay attack continue to be effective, and even disabling NTLM doesn't save you from relaying as Kerberos can be relayed in some instances.</li>
<li><a href="https://blog.trailofbits.com/2025/09/03/subverting-code-integrity-checks-to-locally-backdoor-signal-1password-slack-and-more/" target="_blank">Subverting code integrity checks to locally backdoor Signal, 1Password, Slack, and more</a> - Integrity checks are only as good as the content they check, and in Electron apps, the checks don't cover the whole app. This post introduces "snapshot tampering."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul><li><p><a href="https://bloodhound.specterops.io/opengraph/ocip" style="color: #3bd267;" target="_blank">BloodHound OpenGraph Challenge</a> - OpenGraph is live in BloodHound 8.0, and SpecterOps wants to see what you can do with it. Share your research, writeups, or talks for a chance at challenge coins, swag, and even SpecterOps training or a trip to SO-CON 2026. Submit your work <a href="https://bloodhound.specterops.io/opengraph/ocip" style="color: #3bd267;" target="_blank">here</a>. <span class="m-label m-flat m-success">Sponsored</span></p></li></ul><ul>
<li><a href="https://github.com/tijme/dittobytes" target="_blank">dittobytes</a> - Metamorphic cross-compilation of C++ &amp; C-code to PIC, BOF &amp; EXE.</li>
<li><a href="https://github.com/magisterquis/sneaky_remap" target="_blank">sneaky_remap</a> - A C and Go /proc/pid/maps cloak of invisibility for shared object files.</li>
<li><a href="https://github.com/basecamp/once-campfire" target="_blank">once-campfire</a> - Campfire is web-based chat application. [Formally a $299 product by basecamp]</li>
<li><a href="https://github.com/f0rw4rd/tls-preloader" target="_blank">tls-preloader</a> - LD_PRELOAD library to bypass TLS certificate verification for debugging and testing. See more at, <a href="https://f0rw4rd.github.io/posts/tls-noverify-bypass-all-the-things/" target="_blank">TLS NoVerify: Bypass All The Things</a>.</li>
<li><a href="https://github.com/TierZeroSecurity/killerPID-BOF" target="_blank">killerPID-BOF</a> - Kill a process by specifying its PID. Short post <a href="https://tierzerosecurity.co.nz/2025/09/08/killerPID-BOF.html" target="_blank">here</a> .</li>
<li><a href="https://github.com/deriv-security/MeetC2" target="_blank">MeetC2</a> - (MeetC2 a.k.a Meeting C2) - A framework abusing Google Calendar APIs.</li>
<li><a href="https://github.com/Workday/raw-disk-parser" target="_blank">raw-disk-parser</a> - A tool to interact with Windows drivers to perform a raw disk read and parse out target files without calling standard Windows file APIs.</li>
<li><a href="https://github.com/almounah/orsted" target="_blank">orsted</a> - Orsted C2 Framework.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://links.plex.tv/s/vb/Vn7XtnwDSSaqqDUYoHu1P57ZgZ1FsHgTO2PTIBl6jEOUiHBH3LGmI3nLdDfopQa54PatUwZQhT0Bz8rKAi--jTM4ATdsBHpe4c1Yljr89VkoCOavEGH5wn5Fi_filLNeOMo-lnNqLSLpJpI/lOe98S8UWKdmPnp9StQz9R1-kOSTpWhr/12" target="_blank">Plex security incident</a> - <a href="https://jellyfin.org/" target="_blank">Jellyfin</a> is looking better and better every day.</li>
<li><a href="https://github.com/bijomaru78/eccm" target="_blank">eccm</a> - Ethernet Cable Connection Manager.</li>
<li><a href="https://github.com/Secrover/Secrover" target="_blank">Secrover</a> - Open-source security reports — no paywalls, just actionable insights.</li>
<li><a href="https://ffmpegs.pages.dev/" target="_blank">FFmpegs Pages</a> - Simple media processing for everyone.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 458 (+0)</p>
<p>Blogs monitored: 424 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
