Title: Last Week in Security (LWiS) - 2022-05-02
Date: 2022-05-02 23:30
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-05-02
Author: Erik
Summary: GitHub OAuth token hack, security.txt RFC (<a href="https://twitter.com/EdOverflow" target="_blank">@EdOverflow</a>), channel binding bypass for LDAP (<a href="https://twitter.com/lowercase_drm" target="_blank">@lowercase_drm</a>), #ExtraReplica (<a href="https://twitter.com/sagitz_" target="_blank">@sagitz_</a>, <a href="https://twitter.com/shirtamari" target="_blank">@shirtamari</a>, <a href="https://twitter.com/nirohfeld" target="_blank">@nirohfeld</a>, <a href="https://twitter.com/ronenshh" target="_blank">@ronenshh</a>), Windows kernel driver fun (<a href="https://twitter.com/_xpn_/" target="_blank">@_xpn_</a>), prefetch on Apple Silicon (<a href="https://twitter.com/jose_vicarte" target="_blank">@jose_vicarte</a> and team), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-04-25 to 2022-05-02.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9116" target="_blank">RFC 9116: A File Format to Aid in Security Vulnerability Disclosure</a>. The security.txt file for security disclosure is an official RFC!</li>
<li><a href="https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/" target="_blank">Security alert: Attack campaign involving stolen OAuth user tokens issued to two third-party integrators</a>. A breach is bad, but having GitHub have to tell you about your breach is even worse. Good on GitHub for identifying the malicious use of "legitimate" OAuth tokens from a Heroku and Travis CI.</li>
<li><a href="https://msrc-blog.microsoft.com/2022/04/28/azure-database-for-postgresql-flexible-server-privilege-escalation-and-remote-code-execution/" target="_blank">Azure Database for PostgreSQL Flexible Server Privilege Escalation and Remote Code Execution</a>. AWS last week, Azure this week. This one is much worse as you could gain access to other customer's databases. Full details <a href="https://www.wiz.io/blog/wiz-research-discovers-extrareplica-cross-account-database-vulnerability-in-azure-postgresql/" target="_blank">here</a>.</li>
<li><a href="https://www.newsblur.com/newsletters/story/8592555:688341" target="_blank">$90 million stolen from DeFi platforms over the weekend</a>. The early adopter phase has a really steep entrance fee.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.doyensec.com//2022/04/26/vbox-fuzzing.html" target="_blank">Introduction to VirtualBox security research</a>. "This article introduces VirtualBox research and explains how to build a coverage-based fuzzer, focusing on the emulated network device drivers."</li>
<li><a href="https://offsec.almond.consulting/bypassing-ldap-channel-binding-with-starttls.html" target="_blank">Bypassing LDAP Channel Binding with StartTLS</a>. Even if you have "LDAP server channel binding token requirements: Always" set as a GPO, if authentication is started unencrypted and then upgrade via StartTLS, channel binding is bypassed!</li>
<li><a href="https://xret2pwn.github.io/Building-Token-Vault-Part0x02/" target="_blank">Access Token Manipulation Part 0x02</a>. Build a token vault in memory to store stolen tokens!</li>
<li><a href="https://posts.specterops.io/learning-machine-learning-part-2-attacking-white-box-models-1a10bbb4a2ae" target="_blank">Learning Machine Learning Part 2: Attacking White Box Models</a>. A very detailed look at attacking ML models.</li>
<li><a href="https://www.prefetchers.info/" target="_blank">Augury: Using Data Memory-Dependent Prefetchers to Leak Data at Rest</a>. Prefetch vulnerabilities arrive on Apple Silicon. No one is immune to this vulnerability class it seems.</li>
<li><a href="https://www.microsoft.com/security/blog/2022/04/26/microsoft-finds-new-elevation-of-privilege-linux-vulnerability-nimbuspwn/" target="_blank">Microsoft finds new elevation of privilege Linux vulnerability, Nimbuspwn</a>. Directory traversal (CVE-2022-29799) and a time-of-check-time-of-use (TOCTOU) race condition (CVE-2022-29800) in networkd-dispatcher lead to LPE.</li>
<li><a href="https://www.trustedsec.com/blog/g_cioptions-in-a-virtualized-world/" target="_blank">g_CiOptions in a Virtualized World</a>. This post explores some ways to get your code running in the Windows kernel with Virtualization Based Security (VBS) enable but no Hypervisor Code Integrity (HVCI).</li>
<li><a href="https://www.gosecure.net/blog/2022/04/26/evasive-phishing-techniques-threat-actors-use-to-circumvent-defense-mechanisms/" target="_blank">Evasive Phishing Techniques Threat Actors Use to Circumvent Defense Mechanisms</a>. If phishing is part of your assessment procedures, it's good to read up on what the real adversaries are up to. To that end, <a href="https://blog.nviso.eu/2022/04/29/analyzing-vsto-office-files/" target="_blank">VSTO</a> files are in right now.</li>
<li><a href="https://modexp.wordpress.com/2022/05/02/shellcode-risc-v-linux/" target="_blank">Shellcode: Linux on RISC-V 64-Bit</a>. One day you will b only be popping shells on ARM and RISC-V machines, mark my words. You can use <a href="https://github.com/TheThirdOne/rars" target="_blank">rars</a> to get started.</li>
<li><a href="https://www.mandiant.com/resources/tracking-apt29-phishing-campaigns" target="_blank">Trello From the Other Side: Tracking APT29 Phishing Campaigns</a>. Hosting your own payloads and C2 is so 2020.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EspressoCake/BeaconDownloadSync" target="_blank">BeaconDownloadSync</a> is a fine-tuned control mechanism for syncing files from the Cobalt Strike Downloads entries in the data model.</li>
<li><a href="https://github.com/SecIdiot/minbeacon" target="_blank">minbeacon</a> is a work in progress of constructing a minimal http(s) beacon for Cobalt Strike.</li>
<li><a href="https://github.com/trustedsec/CS-Remote-OPs-BOF" target="_blank">CS-Remote-OPs-BOF</a> is an addition to TrustedSec's <a href="https://github.com/trustedsec/CS-Situational-Awareness-BOF" target="_blank">CS-Situational-Awareness-BOFs</a> that modify systems (injection, persistence, etc).</li>
<li><a href="https://github.com/cedowens/Dylib_Runner" target="_blank">Dylib_Runner</a> is Swift code to run a dylib on disk.</li>
<li><a href="https://github.com/cedowens/okta-sprayer" target="_blank">okta-sprayer</a> is a Python3 Script to perform a password spray against an okta instance.</li>
<li><a href="https://github.com/d4rckh/nimc2" target="_blank">nimc2</a> is a c2 fully written in nim.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/pyscript/pyscript" target="_blank">pyscript</a>. Python directly in HTML (via a WASM shim).</li>
<li><a href="https://github.com/paranoidninja/O365-Doppelganger" target="_blank">O365-Doppelganger</a> is a quick handy script to harvest credentials off of a user during a Red Team and get execution of a file from the user.</li>
<li><a href="https://github.com/ehids/ecapture#ecapture-user-manual" target="_blank">ecapture</a> can capture SSL/TLS text content without CA cert using eBPF.</li>
<li><a href="https://github.com/boltgolt/howdy" target="_blank">howdy</a> is Windows Hello™ style facial authentication for Linux.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 416 (+1)</p>
<p>Blogs monitored: 304 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
