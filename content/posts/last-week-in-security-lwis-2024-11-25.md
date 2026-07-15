Title: Last Week in Security (LWiS) - 2024-11-25
Date: 2024-11-25 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-11-25
Author: Erik
Summary: Sitecore Exploit (<a href="https://x.com/assetnote" target="_blank">@assetnote</a> + <a href="https://x.com/plopz0r" target="_blank">@plopz0r</a>), CI/CD CTF (<a href="https://x.com/magisterquis" target="_blank">@MagisterQuis</a>), new Mythic agent (<a href="https://x.com/silentwarble" target="_blank">@silentwarble</a>), cmake based win32 shellcode template (<a href="https://x.com/ilove2pwn_" target="_blank">@ilove2pwn_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-11-18 to 2024-11-25.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Learn Azure and on-prem Red Teaming with 20% OFF</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Start your Red Team training with us! <a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Altered Security</a> offers multiple Red Team course with affordable and enterprise-like hands-on labs.
Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more.
Our courses and labs are designed by experts who have more than a decade's experience of training and speaking at Black Hat USA, DEF CON and other respected conferences.
Join more than 30K professionals from 130+ countries.</p>
<p>Enjoy <strong>20% OFF</strong> on all courses and instructor-led bootcamps to be held in Q1 and Q2 2025. <strong>No coupon code required.</strong> Discount ends on 2nd December 2024.</p>
</aside><ul>
<li><a href="https://www.cisa.gov/resources-tools/resources/phishing-resistant-multi-factor-authentication-mfa-success-story-usdas-fast-identity-online-fido" target="_blank">Phishing-Resistant Multi-Factor Authentication (MFA) Success Story: USDA’s Fast IDentity Online (FIDO) Implementation</a> - A big win! If USDA can roll out FIDO multi-factor authentication that is phishing resistant, so can you!</li>
<li><a href="https://pagedout.institute/download/PagedOut_005.pdf" target="_blank">[PDF] Paged Out #5</a> - Your favorite new zine has a fresh issue out!</li>
<li><a href="https://www.404media.co/email/f459caa7-1a58-4f31-a9ba-3cb53a5046a4/" target="_blank">'FYI. A Warrant Isn’t Needed': Secret Service Says You Agreed To Be Tracked With Location Data</a> - Your weekly reminder that the US still does not have a comprehensive data privacy law. At least in the EU they have to <a href="https://therecord.media/how-italy-became-an-unexpected-spyware-hub" target="_blank">deploy spyware</a> instead of just harvesting ad data.</li>
<li><a href="https://26857953.fs1.hubspotusercontent-eu1.net/hubfs/26857953/State%20of%20API%20Exposure%202024%20-%20Escape.pdf" target="_blank">[PDF] Fortune 1000 at Risk: How we discovered 30,000 exposed APIs &amp; 100,000 API issues in the world’s largest organizations</a> - "Exposed" APIs aren't necessarily bad (how else would use use them?) but over 1,800 critical vulnerabilities including criticals, exposed dev instances, and secrets being leaked is bad.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.qualys.com/2024/11/19/needrestart/needrestart.txt" target="_blank">LPEs in needrestart (CVE-2024-48990, CVE-2024-48991, CVE-2024-48992, CVE-2024-10224, and CVE-2024-11003)</a> - These old school Qualys reports are always amazing. From the technical analysis to the song lyrics, it's the must read post of the week. I hope Qualys leadership continues to allow this kind of work, and to allow it to be published as a text file. Never change.</li>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-326a" target="_blank">Enhancing Cyber Resilience: Insights from CISA Red Team Assessment of a US Critical Infrastructure Sector Organization</a> - These reports from CISA are always a great read. The CISA red team is doing real adversary emulation (90 day+ assessements) with no advanced notice to defenders (only "Trusted Agents" know about the assessment).</li>
<li><a href="https://labs.watchtowr.com/pots-and-pans-aka-an-sslvpn-palo-alto-pan-os-cve-2024-0012-and-cve-2024-9474/" target="_blank">Pots and Pans, AKA an SSLVPN - Palo Alto PAN-OS CVE-2024-0012 and CVE-2024-9474</a> - This is hopefully the last of the Palo Alto CVE news for a while, but these were the bugs discussed over the last two weeks and boy are they bad. The first allows you disable auth by sending a header asking auth to be disabled (yes, seriously). The second is basic command injection.</li>
<li><a href="https://shells.systems/extracting-plaintext-credentials-from-palo-alto-global-protect/" target="_blank">Extracting Plaintext Credentials from Palo Alto Global Protect</a> - Dump some potentially useful credentials out of memory on Windows with <a href="https://github.com/t3hbb/PanGP_Extractor" target="_blank">PanGP_Extractor</a>.</li>
<li><a href="https://www.synacktiv.com/en/publications/relaying-kerberos-over-smb-using-krbrelayx" target="_blank">Relaying Kerberos Over SMB Using Krbrelayx</a> - Without signing enabled, and with the ability to set DNS entries in an environment, you can in fact relay kerberos over SMB. Consider an environment where a vulnerable service only allows authentication via kerberos, and you have your use case.</li>
<li><a href="https://www.trellix.com/blogs/research/when-guardians-become-predators-how-malware-corrupts-the-protectors/" target="_blank">When Guardians Become Predators: How Malware Corrupts the Protectors</a> - Another example of <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">traitorware</a> in action.</li>
<li><a href="https://neodyme.io/en/blog/wazuh_rce/#the-target-wazuh" target="_blank">From Guardian to Gateway: The Hidden Risks of EDR Vulnerabilities</a> - More <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">traitorware</a>, this time with two exploits for the popular open source endpoint detection and response (EDR) Wazuh.</li>
<li><a href="https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html" target="_blank">Leveling Up Fuzzing: Finding more vulnerabilities with AI</a> - Google uses LLMs to find real bugs. AI in cybersecurity isn't <em>100%</em> hype.</li>
<li><a href="https://posts.specterops.io/azure-key-vault-tradecraft-with-bark-24163abc8de3" target="_blank">Azure Key Vault Tradecraft with BARK</a> - As users move to the cloud, so will the attackers. <a href="https://github.com/BloodHoundAD/BARK" target="_blank">BARK</a> recently added some new functions to help attack the Azure Key Vault service.</li>
<li><a href="https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/" target="_blank">The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access</a> - You may think your WiFi or other systems are only vulnerable to physical proximity attacks when an adversary visits in person, but Russia was attacking targets via compromised neighboring WiFi networks. Physical proximity attacks without the "physically being there" part.</li>
<li><a href="https://unit42.paloaltonetworks.com/unique-popular-techniques-lateral-movement-macos/" target="_blank">Lateral Movement on macOS: Unique and Popular Techniques and In-the-Wild Examples</a> - The Remote Apple Events (RAE) lateral movement technique was a new one to me.</li>
<li><a href="https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform/" target="_blank">Finding vulnerabilities in ClipSp, the driver at the core of Windows’ Client License Platform</a> - Windows licensing is done in the kernel, and there were flaws!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><p><a href="https://github.com/silentwarble/Hannibal" target="_blank">Hannibal</a> is a x64 Windows Agent written in fully position independent C (plus a tiny bit of C++). Details in <a href="https://silentwarble.com/posts/making-monsters-1/" target="_blank">Making Monsters - Part 1</a>.</p>
</li>
<li><p><a href="https://www.zerodayinitiative.com/advisories/ZDI-24-1532/" target="_blank">7-Zip Zstandard Decompression Integer Underflow Remote Code Execution Vulnerability</a> - New initial access exploit?</p>
</li>
<li><p>Sitecore Exploit</p>
<blockquote>
<ul>
<li><a href="https://www.assetnote.io/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x" target="_blank">Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.x</a> - Sitecore is a content management system/site builder; think WordPress or Adobe Experience Manager. It's used by some large companies for quick marketing sites (among other uses). It had some remote code execution vulnerabilities that were patched in August and disclosed last week.</li>
<li><a href="https://blog.scrt.ch/2024/11/25/arbitrary-web-root-file-read-in-sitecore-before-v10-4-0-rev-010422/" target="_blank">Arbitrary web root file read in Sitecore before v10.4.0 rev. 010422</a> - It's interesting to compare this with the previous as, "our analysis and attack vectors are actually slightly different [than Assetnote's]."</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://github.com/realoriginal/shellcode-template" target="_blank">shellcode-template</a> - A cmkr based win32 shellcode template for a unified build platform and more production friendly structure/testing.</p>
</li>
<li><p><a href="https://github.com/magisterquis/wtrtdtmlb/tree/master" target="_blank">wtrtdtmlb</a> "Kinda realisticish CI/CD server" but without pointing fingers that trades realism for illustration. Use this to demonstrate/practice linux hacking. See the slides <a href="https://docs.google.com/presentation/d/1jg3IHtXxMkbiQq935PzRmc8brnBKgAvxrpSzKluz0Io/edit#slide=id.g31701c584a3_0_200" target="_blank">here</a>.</p>
</li>
<li><p><a href="https://github.com/hfiref0x/WinDepends" target="_blank">WinDepends</a> is a rewrite of the Dependency Walker utility which for a long time was a "must have" tool when it comes to Windows PE files analysis and building hierarchical tree diagram of all dependent modules.</p>
</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://rt-solar.ru/solar-4rays/blog/4861/" target="_blank">The Elusive GoblinRAT - The Story Behind the Most Secretive and Mysterious Linux Backdoor Found in Government Infrastructures</a> - Some pretty well done Linux tradecraft in Russia.</li>
<li><a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python" target="_blank">patchright-python</a> - Patchright is a patched and undetected version of the Playwright Testing and Automation Framework. It can be used as a drop-in replacement for Playwright.</li>
<li><a href="https://github.com/roadwy/DefenderYara" target="_blank">DefenderYara</a> - Extracted Yara rules from Windows Defender mpavbase and mpasbase</li>
<li><a href="https://github.com/0xf005ba11/vmplex-ws" target="_blank">vmplex-ws</a> - A modern, tabbed UI for Hyper-V.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 442 (+1)</p>
<p>Blogs monitored: 398 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
