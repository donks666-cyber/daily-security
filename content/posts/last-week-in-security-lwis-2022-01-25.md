Title: Last Week in Security (LWiS) - 2022-01-25
Date: 2022-01-25 21:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-01-25
Author: Erik
Summary: PrinterLogic RCEs (<a href="https://twitter.com/theParanoids" target="_blank">@TheParanoids</a>), Java app analysis (<a href="https://twitter.com/infosec_au" target="_blank">@infosec_au</a>), DCSync from Linux (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), timed race conditions (<a href="https://twitter.com/itscachemoney" target="_blank">@itscachemoney</a>), ManageEngine auth bypass (<a href="https://twitter.com/sourceincite" target="_blank">@sourceincite</a>), Windows driver RE methods (<a href="https://twitter.com/Void_Sec" target="_blank">@Void_Sec</a>), Sliver 1.5 with BOF support (<a href="https://twitter.com/LittleJoeTables" target="_blank">@LittleJoeTables</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-01-18 to 2022-01-25.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/" target="_blank">MoonBounce: the dark side of UEFI firmware</a>. UEFI/SPI firmware malware is very scare, as you can <a href="https://www.youtube.com/watch?v=lb1XDMbQOiM" target="_blank">"Wipe The Drive"</a> but it won't get rid of the malware. Check out this PDF for the <a href="https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/01/19115831/MoonBounce_technical-details_eng.pdf" target="_blank">technical details (PDF)</a> and <a href="https://samples.vx-underground.org/APTs/2022/2022.01.20/" target="_blank">vx-underground</a> for the samples.</li>
<li><a href="https://www.youtube.com/watch?v=dT9y-KQbqi4" target="_blank">How I hacked a hardware crypto wallet and recovered $2 million</a>. Joe Grand found that the particular firmware version of the target Trezor was copying the PIN to RA so he voltage glitched the MCU to bypass the debug disable which allowed the key to be read from RAM.</li>
<li><a href="https://portswigger.net/daily-swig/california-public-office-admits-covid-19-healthcare-data-breach" target="_blank">California public office admits Covid-19 healthcare data breach</a>. Exactly zero people are surprised. Any production database is potentially useful to attackers, this one had lots of personally identifiable information to go after.</li>
<li><a href="https://developer.chrome.com/blog/force-major-version-to-100/" target="_blank">Force Chrome major version to 100 in the User-Agent string</a>. This feels like the exact opposite of <a href="https://0ver.org/" target="_blank">zer0ver</a>.</li>
<li><a href="https://msrc-blog.microsoft.com/2022/01/20/an_armful_of_cheris/" target="_blank">An Armful of CHERIs</a>. Silicon that can enforce memory safety? I'm intrigued.</li>
<li><a href="https://www.lexology.com/library/detail.aspx?g=e45913c8-1f04-4d34-b6da-770dee9a080b" target="_blank">Cyber Risks and Business Interruption Insurance - Merck and International Indemnity v ACE (et al.)</a>. TLDR (too legal didn't read in this case): the cyber insurers for Merck - the shipping giant cripped by NotPetya ransomware - tried to claim that the "War or Hostile Acts" exclusion would apply since Russia was behind the NotPetya attack. The court said nope, pay up!</li>
<li><a href="https://www.mail-archive.com/announce@apache.org/msg07042.html" target="_blank">CVE-2022-23307: Apache Log4j 1.x: A deserialization flaw in the Chainsaw component of Log4j 1 can lead to malicious code execution.</a>. Yes, even the unsupported Log4j 1.x branch was vulnerable. If you were on an unsupported version of Log4j you've definitely upgraded in the last month right?</li>
<li><a href="https://venturebeat.com/2022/01/18/mcafee-enterprise-fireeye-relaunches-as-trellix-aims-to-be-market-leader-in-xdr/" target="_blank">McAfee Enterprise-FireEye relaunches as Trellix, aims to be ‘market leader’ in XDR</a>. RIP McAfee (x2), and also <a href="https://kc.mcafee.com/corporate/index?page=content&amp;id=SB10378" target="_blank">two vulnerabilities</a>.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.printerlogic.com/security-bulletin/" target="_blank">Multiple RCE vulns in PrinterLogic Web Stack versions 19.1.1.13 SP9 and below</a>. Check out the <a href="https://www.yahooinc.com/paranoids/paranoids-vulnerability-research-printerlogic-issues-security-alert/" target="_blank">technical write up</a>, which takes this week's top spot for it's technical merit but also the section on how PrinterLogic was chosen as a research target. Well done Blaine!</li>
<li><a href="https://blog.assetnote.io/2022/01/23/solarwinds-webhelpdesk-hsql-eval-harcoded-creds/" target="_blank">Solarwinds Web Help Desk: When the Helpdesk is too Helpful</a>. This post has some helpful tips on digging into java applications. Who knows, you just might find hard coded credentials!</li>
<li><a href="https://positive.security/blog/video-depixelation" target="_blank">Recovering redacted information from pixelated videos</a>. You've seen static text unbluring, but what about video? If you really want to redact something, black boxes are usually the best answer.</li>
<li><a href="https://www.n00py.io/2022/01/adding-dcsync-permissions-from-linux/" target="_blank">Adding DCSync Permissions from Linux</a>. If you find yourself on a Linux machine but with an AES key to a computer account with WriteDACL over the domain, you might be able to <a href="https://github.com/n00py/DCSync" target="_blank">DCSync</a>.</li>
<li><a href="https://srcincite.io/blog/2022/01/20/zohowned-a-critical-authentication-bypass-on-zoho-manageengine-desktop-central.html" target="_blank">ZohOwned :: A Critical Authentication Bypass on Zoho ManageEngine Desktop Central</a>. Another Java bug chain, this time on critical remote management software.</li>
<li><a href="https://www.trustedsec.com/blog/recovering-randomly-generated-passwords/" target="_blank">Recovering Randomly Generated Passwords</a>. Yes, randomly generated passwords are very hard to crack, but Hans proves you can do better than a full brute force given time constraints.</li>
<li><a href="https://voidsec.com/windows-drivers-reverse-engineering-methodology/" target="_blank">Windows Drivers Reverse Engineering Methodology</a> Paolo sums up his year-long Windows Drivers research and details his methodology for reverse engineering (WDM) Windows drivers. This is a free mini-course on Windows driver RE!</li>
<li><a href="https://www.trustedsec.com/blog/wmi-for-script-kiddies/" target="_blank">WMI for Script Kiddies</a>. Nothing groundbreaking, but if you need a one stop shop of WMI knowledge, this is a good candidate.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/masasron/chrome-bandit" target="_blank">chrome-bandit</a> is a proof of concept to show how your saved passwords on Google Chrome and other Chromium-based browsers can easily be stolen by any malicious program on macOS.</li>
<li><a href="https://github.com/blacklanternsecurity/TREVORproxy" target="_blank">TREVORproxy</a> is a SOCKS proxy written in Python that randomizes your source IP address. Round-robin your evil packets through SSH tunnels or give them billions of unique source addresses!</li>
<li><a href="https://github.com/Cache-Money/chronorace" target="_blank">chronorace</a> is a tool to accurately perform timed race conditions to circumvent application business logic. Well timed race conditions can allow for uncovering all kinds of interesting edge cases. <a href="https://hackerone.com/reports/300305" target="_blank">Here</a> is a good example.</li>
<li><a href="https://github.com/hlldz/RefleXXion" target="_blank">RefleXXion</a> is a utility designed to aid in bypassing user-mode hooks utilised by AV/EPP/EDR etc. In order to bypass the user-mode hooks, it first collects the syscall numbers of the NtOpenFile, NtCreateSection, NtOpenSection and NtMapViewOfSection found in the LdrpThunkSignature array.</li>
<li><a href="https://github.com/BishopFox/sliver/releases/tag/v1.5.0" target="_blank">Sliver v1.5.0</a>. This release has a lot of cool changes. My favorite is BOF support!</li>
<li><a href="https://github.com/Idov31/FunctionStomping" target="_blank">FunctionStomping</a> is a new shellcode injection technique. Given as C++ header or standalone Rust program. Currently undetected by hollows-hunter.</li>
<li><a href="https://github.com/Wra7h/SharpGhosting" target="_blank">SharpGhosting</a> is Process Ghosting (x64 only) in C#.</li>
<li><a href="https://octagon.net/blog/2022/01/22/cve-2021-45467-cwp-centos-web-panel-preauth-rce/" target="_blank">CVE-2021-45467: CWP CentOS Web Panel – preauth RCE</a>. File inclusion + directory traversal = RCE.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://twitter.com/zoph/status/1473991530712952833" target="_blank">A month ago AWS accidentally gave themselves read access to every S3 bucket for 12 hours</a>. I missed this news. Such a big gaff should have been widely reported?</li>
<li><a href="https://github.com/Yavuzlar/VulnLab" target="_blank">VulnLab</a> is a dockerized web vulnerability lab.</li>
<li><a href="https://github.com/liamg/extrude" target="_blank">extrude</a> analyzes binaries for missing security features, information disclosure and more.</li>
<li><a href="https://github.com/Danielv123/serverManager" target="_blank">serverManager</a> is an  IPMI server manager build for Dell 12th gen servers. If you have an R710 or R720 at home you have to give this a try.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
