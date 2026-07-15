Title: Last Week in Security (LWiS) - 2021-04-19
Date: 2021-04-19 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-04-19
Author: Erik
Summary: 0 to RCE against a CMS (<a href="https://twitter.com/ultrayoba" target="_blank">@ultrayoba</a>), tcpip.sys patch diffing for N-days (<a href="https://twitter.com/0vercl0k" target="_blank">@0vercl0k</a>), detecting stagers (<a href="https://twitter.com/DidierStevens" target="_blank">@DidierStevens</a>), named pipe PTH (<a href="https://twitter.com/ShitSecure" target="_blank">@ShitSecure</a>), URI-based 1-click RCEs (<a href="https://twitter.com/positive_sec" target="_blank">@positive_sec</a>), FDE bypass [Airstrike attack] (<a href="https://twitter.com/breakfix" target="_blank">@breakfix</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-04-12 to 2021-04-19.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://labs.nettitude.com/blog/poshc2-introducing-native-macos-implants/" target="_blank">PoshC2 – Introducing Native macOS Implants</a>. As more businesses adopt macOS, red teamers have started to build tooling to support engagements against them.</li>
<li><a href="https://www.cyberscoop.com/nsa-microsoft-exchange-server-vulnerabilities/" target="_blank">NSA says it found new critical vulnerabilities in Microsoft Exchange Server</a>. Like many big bugs, once one is exposed lots of researches take aim. Exchange is the latest target, falling at the recent Pwn2Own and now multiple vulnerabilities being reported by the NSA. How many more remain unreported?</li>
<li><a href="https://www.vice.com/en/article/y3dmjg/fbi-removes-web-shells-microsoft-exchange" target="_blank">FBI Accesses Computers Around Country to Delete Microsoft Exchange Hacks</a>. The warrant and its attachments authorize "the use of remote access techniques to search the electronic media" of the targeted Exchange servers. While it also states that it does not authorize any seizure or copying of content (besides the webshells themselves) and no alteration of functionality, the FBI still had access to your mail server. I suppose it's a good idea to patch to keep everyone out, not just the "bad guys."</li>
<li><a href="https://github.com/disclose/research-threats" target="_blank">research-threats</a> is a collection of legal threats against good faith Security Researchers; vulnerability disclosure gone wrong and is a continuation of work started by <a href="https://twitter.com/attritionorg" target="_blank">@attritionorg</a>. Hopefully it will encourage companies to act better toward researchers trying to help them.</li>
<li><a href="https://krebsonsecurity.com/2021/04/did-someone-at-the-commerce-dept-find-a-solarwinds-backdoor-in-aug-2020/" target="_blank">Did Someone at the Commerce Dept. Find a SolarWinds Backdoor in Aug. 2020?</a>. This is an interesting post that also brings up blue team OPSEC. While Virus Total and other similar services are great, what are you telling the world by uploading samples with accounts or information that tie back to your organization?</li>
<li><a href="https://googleprojectzero.blogspot.com/2021/04/policy-and-disclosure-2021-edition.html" target="_blank">Policy and Disclosure: 2021 Edition</a>. Google Project Zero is often used as an example of how to do responsible disclosure, and they have taken that role seriously. In 2021 they are implementing a "90+30" model that give a 30 day grace period after a bug is fixed within 90 days to allow better patch adoption before technical details are released. As N-day authors get faster and faster, this grace period becomes more important.</li>
<li><a href="https://www.forescout.com/company/resources/namewreck-breaking-and-fixing-dns-implementations/" target="_blank">NAME:WRECK Breaking and fixing DNS implementations</a>. Many IoT and industrial control OS's DNS implementations are bad. So bad, in fact, that you can get remote code execution with a specially crafted DNS response. This exploit requires an attacker to be able to respond to DNS requests - some form of man-in-the-middle.</li>
<li><a href="https://www.securityweek.com/codecov-bash-uploader-dev-tool-compromised-supply-chain-hack" target="_blank">Codecov Bash Uploader Dev Tool Compromised in Supply Chain Hack</a>. The year of the supply chain attack is well underway. This one targets a tool developers use to generate code coverage often used in CI. Who is affected? <a href="https://grep.app/search?q=https%3A//codecov.io/bash" target="_blank">Lots of projects</a>.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://swarm.ptsecurity.com/rce-cockpit-cms/" target="_blank">From 0 to RCE: Cockpit CMS</a>. This post shows a few ways to exploit blind NoSQL injection, authenticated account takeover, and even remote code execution in the MongoLite library.</li>
<li><a href="https://sensepost.com/blog/2021/duo-two-factor-authentication-bypass/" target="_blank">Duo Two-factor Authentication Bypass</a>. An issue where 2FA authentication state wasn't tied to a session allowed an attacker one the same Duo deployment to redirect 2FA prompts to their own device. This is a narrow use case, and Duo even did incident response and determined it had never been exploited - except by the researchers. A reminder that 2FA isn't always a dead end!</li>
<li><a href="https://doar-e.github.io/blog/2021/04/15/reverse-engineering-tcpipsys-mechanics-of-a-packet-of-the-death-cve-2021-24086/" target="_blank">Reverse-engineering tcpip.sys: mechanics of a packet of the death (CVE-2021-24086)</a>. The <a href="https://github.com/0vercl0k/CVE-2021-24086" target="_blank">PoC</a> has been out for two weeks (it was in LWiS) but this post shows how it was discovered and created. If you have an interest in patch diffing or N-day exploitation, read this post. Another post that leverages patch diffing was also released last week: <a href="https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1647.html" target="_blank">CVE-2021-1647: Windows Defender mpengine remote code execution</a></li>
<li><a href="https://redteamer.tips/basic-operational-security-when-dropping-to-disk/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=basic-operational-security-when-dropping-to-disk" target="_blank">Basic operational security when dropping to disk</a>. Despite all the in memory voodoo, if you want to persist in a network, you'll have to write something to disk at some point. This post includes some tips to blend in better. Pro tip: the <a href="https://github.com/optiv/ScareCrow/blob/main/limelighter/limelighter.go" target="_blank">limelighter.go from ScareCrow</a> has the versioninfo and signing all in one (vs the official <a href="https://github.com/Tylous/Limelighter" target="_blank">Limelighter</a>).</li>
<li><a href="https://s3cur3th1ssh1t.github.io/Named-Pipe-PTH/" target="_blank">Named Pipe Pass-the-Hash</a>. Ever have access to a Windows box, and want to run a command as a different low privileged user (whose NTLM hash you have) on the same machine, but that target user is not logged in or running any processes? This post describes the process of creating a tool to do just that. The tool: <a href="https://github.com/S3cur3Th1sSh1t/NamedPipePTH" target="_blank">NamedPipePTH</a>.</li>
<li><a href="https://positive.security/blog/url-open-rce" target="_blank">Allow arbitrary URLs, expect arbitrary code execution</a>. Lots of desktop apps are vulnerable to 1-click exploitation via URL handlers. These issues affect Windows and Linux, across lots of app types. Be careful what you click, and perhaps leverage these on your next phishing engagement.</li>
<li><a href="https://shenaniganslabs.io/2021/04/13/Airstrike.html" target="_blank">Airstrike Attack - FDE bypass and EoP on domain joined Windows workstations (CVE-2021-28316)</a>. Domain joined Windows machines would leak a MSCHAPv2 challenge response hash to a rogue access point which can be used to recover an NTLM hash and forge a Kerberos Silver ticket and gain full access to the locked computer's hard drive. This vulnerability was patched in the April 2021 security update for Windows.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://isc.sans.edu/forums/diary/Finding+Metasploit+Cobalt+Strike+URLs/27204/" target="_blank">Finding Metasploit &amp; Cobalt Strike URLs</a>. The great forensic tool creator DidierStevens has a new script to find likely metasploit or Cobalt Strike's 8bit checkums. Don't stage your payloads if you are worried about OPSEC. The tool is available <a href="https://github.com/DidierStevens/Beta/blob/master/metatool.py" target="_blank">here</a>.</li>
<li><a href="https://ssd-disclosure.com/ssd-advisory-overlayfs-pe/" target="_blank">SSD Advisory – OverlayFS PE</a>. Ubuntu 14.04-20.10 were vulnerable to an issue with file capabilities (think setuid-bit, but slightly different) where an OverlayFS could set arbitrary capabilities on files in an outer namespace/mount. A full exploit is included.</li>
<li><a href="https://github.com/ars3n11/MineSweeper" target="_blank">MineSweeper</a> is a lightweight (17-18kb) binary for Windows user-land hook manipulation. This will be useful for EDR research.</li>
<li><dl>
<dt>macOS Post-Exploitation</dt>
<dd><ul>
<li><a href="https://github.com/antman1p/JXA_Proc_Tree" target="_blank">JXA_Proc_Tree</a> is a JXA script for enumerating running processes, printed out in a json, parent-child tree. For use with a macOS JXA agent (i.e. <a href="https://github.com/its-a-feature/Mythic" target="_blank">Mythic</a>).</li>
<li><a href="https://github.com/cedowens/Add-To-TCC-DB" target="_blank">Add-To-TCC-DB</a> is a JXA script that leverages sqlite3 API calls to add items to the user's TCC (Transparency, Consent, and Control) database.</li>
<li><a href="https://github.com/antman1p/PrintTCCdb" target="_blank">PrintTCCdb</a> is a JXA script for Mythic that prints the TCC.db.</li>
<li><a href="https://github.com/cedowens/Persistent-Swift" target="_blank">Persistent-Swift</a> is a Swift port of some of the original PersistentJXA projects by D00MFist. Original <a href="https://github.com/D00MFist/PersistentJXA" target="_blank">PersistentJXA</a> repo.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/JoelGMSec/Invoke-Stealth" target="_blank">Invoke-Stealth</a> is a Simple &amp; Powerful PowerShell Script Obfuscator. This tool helps you to automate the obfuscation process of any script written in PowerShell with different techniques. You can use any of them separately, together or all of them sequentially with ease, from Windows or Linux.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Porchetta-Industries/pyMalleableC2" target="_blank">pyMalleableC2</a> is a python interpreter for Cobalt Strike Malleable C2 Profiles. It allows you to parse, build and modify them programmatically. Unlike other simple parsers, this one actually uses an abstract syntax tree and should handle complex profiles much better.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
