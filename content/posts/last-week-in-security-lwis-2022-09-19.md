Title: Last Week in Security (LWiS) - 2022-09-19
Date: 2022-09-19 23:50
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-09-19
Author: Erik
Summary: CloudFox (<a href="https://twitter.com/sethsec" target="_blank">@sethsec</a> + <a href="https://twitter.com/cvendramini2" target="_blank">@cvendramini2</a>), MiraclePtr in Chrome, Jetty hacking (<a href="https://twitter.com/m1ke_n1" target="_blank">@m1ke_n1</a>), ExternalC2 myths (<a href="https://twitter.com/RET2_pwn" target="_blank">@RET2_pwn</a>), NTLMv1 attacks (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a> + <a href="https://twitter.com/an0n_r0" target="_blank">@an0n_r0</a>), Golden Ticket patches soon (<a href="https://twitter.com/varonis" target="_blank">@varonis</a>), plaintext Citrix passwords (<a href="https://twitter.com/gentilkiwi" target="_blank">@gentilkiwi</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-09-05 to 2022-09-19.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.uber.com/newsroom/security-update" target="_blank">Security update (Uber)</a>. The Uber hack made headlines last week, and for good reason. Looks like a single social engineering success (MFA push is <a href="https://www.vice.com/en/article/5d35yd/the-uber-hack-shows-push-notification-2fa-has-a-downside-its-too-annoying" target="_blank">too annoying</a>?) plus some share drive spelunking allowed the attacker to achieve widespread system compromise. I wish this was surprising. It looks like they're <a href="https://www.reddit.com/r/ProgrammerHumor/comments/xijske/uber_hiring_security_engineers/" target="_blank">hiring security engineers</a> now.</li>
<li><a href="https://letsencrypt.org/2022/09/07/new-life-for-crls.html" target="_blank">A New Life for Certificate Revocation Lists</a>. Interesting thoughts from Scott <a href="https://twitter.com/Scott_Helme/status/1567561115088846849" target="_blank">on twitter</a>.</li>
<li><a href="https://www.vice.com/en/article/88q5wv/twitter-whistleblower-says-there-was-at-least-one-chinese-spy-working-at-the-company" target="_blank">Twitter Whistleblower Says There Was at Least One Chinese Spy Working at the Company</a>. Mudge's rumored $7MM severance and non-disclosure didn't cover congressional hearing it seems. Look's like someone is trying to <a href="https://www.newyorker.com/news/news-desk/the-search-for-dirt-on-the-twitter-whistle-blower" target="_blank">dig up dirt on him</a>.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/gta-6-source-code-and-videos-leaked-after-rockstar-games-hack/" target="_blank">GTA 6 source code and videos leaked after Rockstar Games hack</a>. This looks like a "legitimate" insider as opposed to the Uber hack.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.synacktiv.com/en/publications/traces-of-windows-remote-command-execution.html" target="_blank">Traces of Windows remote command execution</a>. The quieter you become, the more... you know the joke. This post shows the artifacts left behind from a variety of "RCE" techniques (lateral movement) on Windows.</li>
<li><a href="https://bishopfox.com/blog/introducing-cloudfox" target="_blank">Introducing: CloudFox</a>. <a href="https://github.com/BishopFox/cloudfox" target="_blank">Cloudfox</a> helps you gain situational awareness in unfamiliar cloud environments. It's a command line tool created to help penetration testers and other offensive security professionals find exploitable attack paths in cloud infrastructure.</li>
<li><a href="https://security.googleblog.com/2022/09/use-after-freedom-miracleptr.html" target="_blank">Use-after-freedom: MiraclePtr</a>. Google's quest to prevent memory corruption exploits continues with a novel C++ add-on to Chrome for Windows and Android as of Chrome 102. Props to the team for <a href="https://chromium-review.googlesource.com/c/chromium/src/+/3305132" target="_blank">pushing</a> this out despite a tiny performance hit.</li>
<li><a href="https://swarm.ptsecurity.com/jetty-features-for-hacking-web-apps/" target="_blank">Jetty Features for Hacking Web Apps</a>. Some neat tricks specific to Jetty in this post.</li>
<li><a href="https://xret2pwn.github.io/Myths-About-External-C2/" target="_blank">Myths About External C2</a>. This post shows the basics of External C2 using a mock teamserver and agent (python).</li>
<li><a href="https://blog.syss.com/posts/bloodhound-blindspots/" target="_blank">The Blind Spots of BloodHound</a>. Nice attack graph you have there; it'd be a shame if something... happened to it...</li>
<li><a href="https://www.trustedsec.com/blog/practical-attacks-against-ntlmv1/" target="_blank">Practical Attacks against NTLMv1</a>. Or check out the <a href="https://twitter.com/an0n_r0/status/1571598587439775745" target="_blank">tweet-length-summary</a>. TLDR: disable NTLMv1 everywhere!</li>
<li><a href="https://www.varonis.com/blog/pac_requestor-and-golden-ticket-attacks" target="_blank">Fighting Golden Ticket Attacks with Privileged Attribute Certificate (PAC)</a>. PAC enforcement is scheduled for October 2022, are your golden ticket tools ready? The table at the end of the article is worth the price of admission.</li>
<li><a href="https://www.bugcrowd.com/resources/levelup/a-basic-guide-to-ios-testing-in-2022/" target="_blank">A Basic Guide to iOS Testing in 2022</a>. Enough to get you started!</li>
<li><a href="https://mrd0x.com/stealing-tokens-from-office-applications/" target="_blank">Stealing Access Tokens From Office Desktop Applications</a>. Your apps authenticate to MS services as you, and so the authentication material is in memory. This post shows you how to extract and use it - to read Outlook emails for example.</li>
<li><a href="https://cube0x0.github.io/Relaying-YubiKeys/" target="_blank">Relaying YubiKeys</a>. Hardware FIDO2 keys are the answer to all phishing right? Right!? Well if an attacker has your PIN and you don't have "touch to sign" enabled, then yes, its just another annoying step. "Touch to sign" is what keeps this from being practical, as the attacker would then also have to trick the user into touching the key for every blob they wanted to sign. Could always skip all that and use <a href="https://github.com/bulwarkid/virtual-fido" target="_blank">virtual-fido</a> to nullify all the benefits of a hardware security device.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://twitter.com/gentilkiwi/status/1571892686130642946" target="_blank">Mimikatz update</a>. Now you can dump plaintext Citrix passwords from memory. Best part is you don't even need elevated rights for the current use context! If anyone has this as a BOF, DM me!</li>
<li><a href="https://github.com/lkarlslund/ldapnomnom" target="_blank">ldapnomnom</a> - Anonymously bruteforce Active Directory usernames from Domain Controllers by abusing LDAP Ping requests (cLDAP).</li>
<li><a href="https://github.com/MaherAzzouzi/CVE-2022-37706-LPE-exploit" target="_blank">CVE-2022-37706-LPE-exploit</a> - A reliable exploit + write-up to elevate privileges to root. (Tested on Ubuntu 22.04) - NOTE: only for enlightenment window manager (Tizen based TVs and... thats it?).</li>
<li><a href="https://github.com/D1rkMtr/MasqueradingPEB" target="_blank">MasqueradingPEB</a> - Maquerade any legitimate Windows binary by changing some fields in the PEB structure.</li>
<li><a href="https://cve-north-stars.github.io/" target="_blank">CVE North Stars</a> - Leveraging CVEs as North Stars in vulnerability discovery and comprehension.</li>
<li><a href="https://github.com/D1rkMtr/ExecRemoteAssembly" target="_blank">ExecRemoteAssembly</a> - Execute Remote Assembly with args passing and with AMSI and ETW patching.</li>
<li><a href="https://github.com/xRET2pwn/Teamsniper" target="_blank">Teamsniper</a> is a tool for fetching keywords in a Microsoft Teams such as (passwords, emails, database, etc.).</li>
<li><a href="https://github.com/slyd0g/DylibHijackTest" target="_blank">DylibHijackTest</a> - Discover DYLD_INSERT_LIBRARIES hijacks on macOS.</li>
<li><a href="https://github.com/Accenture/Codecepticon" target="_blank">Codecepticon</a> is a .NET application that allows you to obfuscate C#, VBA/VB6 (macros), and PowerShell source code, and is developed for offensive security engagements such as Red/Purple Teams. What separates Codecepticon from other obfuscators is that it targets the source code rather than the compiled executables, and was developed specifically for AV/EDR evasion.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/evilashz/CheeseOunce" target="_blank">CheeseOunce</a> - Coerce Windows machines auth via MS-EVEN. Will we ever run out of coercion techniques?</li>
<li><a href="https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/" target="_blank">How we built Pingora, the proxy that connects Cloudflare to the Internet</a>. Some companies are large enough where the milliseconds matter. I hope Pingora is opensourced soon!</li>
<li><a href="https://github.com/Ge0rg3/requests-ip-rotator" target="_blank">requests-ip-rotator</a> - A Python library to utilize AWS API Gateway's large IP pool as a proxy to generate pseudo-infinite IPs for web scraping and brute forcing.</li>
<li><a href="https://diffusionbee.com/" target="_blank">DiffusionBee - Stable Diffusion GUI App for M1 Mac</a>. DiffusionBee is the easiest way to run Stable Diffusion (AI image generation) locally on your M1 Mac. Comes with a one-click installer. No dependencies or technical knowledge needed.</li>
<li><a href="https://github.com/soufianetahiri/CitrixSecureAccessAuthCookieDump" target="_blank">CitrixSecureAccessAuthCookieDump</a> - Dump Citrix Secure Access auth cookie from the process memory.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 420 (+0)</p>
<p>Blogs monitored: 323 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
