Title: Last Week in Security (LWiS) - 2023-10-03
Date: 2023-09-25 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-10-03
Author: Erik
Summary: Nighthawk update (<a href="https://twitter.com/mdseclabs" target="_blank">@MDSecLabs</a>), Teams external splash bypass, MSI LPEs, and Zip+LNKs (<a href="https://twitter.com/pfiatde" target="_blank">@pfiatde</a>), SCCM takeover (<a href="https://twitter.com/_Mayyhem" target="_blank">@_Mayyhem</a>), .NET obfuscation (<a href="https://twitter.com/eversinc33" target="_blank">@eversinc33</a>), JonMon (<a href="https://twitter.com/jsecurity101" target="_blank">@jsecurity101</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-09-19 to 2023-10-03.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/" target="_blank">From ScreenConnect to Hive Ransomware in 61 hours</a>. Solid write-up of how <a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">traitorware</a> wreaks havoc.</li>
<li><a href="https://www.mdsec.co.uk/2023/09/nighthawk-0-2-6-three-wise-monkeys/" target="_blank">Nighthawk 0.2.6 - Three Wise Monkeys</a>. The C2 wars continue. New Nighthawk version introduces API call stack masking.</li>
<li><a href="https://www.ic3.gov/Media/News/2023/230927.pdf" target="_blank">[PDF] People's Republic of China-Linked Cyber Actors Hide in Router Firmware</a>. Cisco vuln leads to firmware backdoors by PRC. The decision to not share the actual trigger packet is unfortunate for defenders.</li>
<li><a href="https://blog.cloudflare.com/announcing-encrypted-client-hello/" target="_blank">Encrypted Client Hello - the last puzzle piece to privacy</a>. A wise man once said <a href="https://youtu.be/TDg092qe50g" target="_blank">Domain fronting is dead, long live domain fronting</a>. This is very similar to my 2020 talk, except all sites share the cloudflare-ech.com unencrypted SNI value vs being able to spoof it.</li>
<li><a href="https://azure.microsoft.com/en-us/updates/default-outbound-access-for-vms-in-azure-will-be-retired-transition-to-a-new-method-of-internet-access/" target="_blank">Default outbound access for VMs in Azure will be retired — transition to a new method of internet access</a>. This is how AWS has always worked - you need a NAT gateway.</li>
<li><a href="https://blog.cloudflare.com/turnstile-ga/" target="_blank">Cloudflare is free of CAPTCHAs; Turnstile is free for everyone</a>. Let the cat-and-mouse bot vs anti-bot wars continue!</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.foxio.io/ja4-network-fingerprinting-9376fe9ca637" target="_blank">JA4+ Network Fingerprinting</a>. The evolution of the JA3, JA3S, and JARM fingerprints. Break out <a href="https://github.com/cbeuw/Cloak" target="_blank">Cloak</a> to blend in. You're proxying your C2 traffic via legitimate web servers to blend in already right?</li>
<li><a href="https://hackerone.com/reports/2107680" target="_blank">AWS keys and user cookie leakage via uninitialized memory leak in outdated librsvg version in Basecamp</a>. Pretty cool report/find!</li>
<li><a href="https://www.linkedin.com/pulse/bypass-two-factor-authentication-facebook-accounts-25300-bazzoun/" target="_blank">Bypass Two-Factor Authentication of Facebook Accounts ($25,300)</a>. In todays episode of crazy bug...</li>
<li><a href="https://medium.com/mitre-engenuity/summiting-the-pyramid-level-up-your-analytics-b6f12efd9133" target="_blank">Summiting the Pyramid: Level Up Your Analytics</a>. New methodology for detection engineering. "...This methodology shifts the advantage to defenders, even as adversaries evolve, and allows us to change the game on the adversary."</li>
<li><a href="https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/active-directory-hardening-series-part-1-disabling-ntlmv1/ba-p/3934787" target="_blank">Active Directory Hardening Series - Part 1 - Disabling NTLMv1</a> - Last week we reported that SMB NTLM is able to be disabled in the latest insiders builds of Windows 11, now Microsoft is pushing this. Relay those NTLM hashes while you still can!</li>
<li><a href="https://posts.specterops.io/sccm-hierarchy-takeover-41929c61e087" target="_blank">SCCM Hierarchy Takeover</a>. "...if an attacker gains control of any primary site, they gain control of the entire SCCM hierarchy." SCCM has been a huge are of domain privilege escalation on recent assessments. Due to its complexity, I wager that more attacks will come out of it in the coming months.</li>
<li><a href="https://badoption.eu/blog/2023/09/27/teams4.html" target="_blank">Teams external participant splash screen bypass</a>. Teams external participant splash screen can be bypassed.</li>
<li><a href="https://www.synacktiv.com/en/publications/introducing-ntdissector-a-swiss-army-knife-for-your-ntdsdit-files" target="_blank">Introducing ntdissector, a swiss army knife for your NTDS.dit files</a>. Blog post to a <a href="https://github.com/synacktiv/ntdissector/" target="_blank">tool release</a>. The tool convert an NTDS file to well formatted JSON objects.</li>
<li><a href="https://ptr0x1.com/posts/edr-evasion-part-ii-scarecrow/" target="_blank">EDR Evasion Part II: Your very own Scarecrow</a>. A guide on what are some changes you can make to <a href="https://github.com/Tylous/ScareCrow" target="_blank">Scarecrow</a> to evade EDRs. <a href="https://ptr0x1.com/posts/edr-evasion-part-i-understanding-scarecrow/" target="_blank">Part one</a> of this series did a good job of walking through the capabilities of ScareCrow.</li>
<li><a href="https://0xdarkvortex.dev/c2-infra-on-azure/" target="_blank">A Thousand Sails, One Harbor - C2 Infra on Azure</a>. Operational guidance on using Azure to hide your C2. Domain fronting in Azure is back on the menu!</li>
<li><a href="https://www.r-tec.net/r-tec-blog-net-assembly-obfuscation-for-memory-scanner-evasion.html" target="_blank">.NET Assembly Obfuscation for Memory Scanner Evasion</a>. Having an automated way to obfuscate your payloads is becoming expected for moderately advanced red teams. How does your pipeline compare?</li>
<li><a href="https://assume-breach.medium.com/home-grown-red-team-lnk-phishing-revisited-in-2023-364daf70a06a" target="_blank">Home Grown Red Team: LNK Phishing Revisited In 2023</a>. Threat actors are using lnks with some truly gross command lines to great effect. This post has some alternative techniques for lnk based initial access.</li>
<li><a href="https://starlabs.sg/blog/2023/09-sharepoint-pre-auth-rce-chain/" target="_blank">[P2O Vancouver 2023] SharePoint Pre-Auth RCE chain (CVE-2023-29357 &amp; CVE-2023-24955)</a>. Wow. Makes you wonder what else has unauth RCE waiting to be discovered.</li>
<li><a href="https://starlabs.sg/blog/2023/09-nftables-adventures-bug-hunting-and-n-day-exploitation/" target="_blank">nftables Adventures: Bug Hunting and N-day Exploitation (CVE-2023-31248)</a>. More good exploitation content from Star Labs; this time a nice Linux 6.2 LPE.</li>
<li><a href="https://www.praetorian.com/blog/pwn-request-hacking-microsoft-github-repositories-and-more/" target="_blank">Long Live the Pwn Request: Hacking Microsoft GitHub Repositories and More</a>. GitHub actions and other types of CI/CD can be setup to run on pull requests or other actions where others control the code. Make sure they are appropriately locked down!</li>
<li><a href="https://badoption.eu/blog/2023/10/03/MSIFortune.html" target="_blank">MSIFortune - LPE with MSI Installers</a>. Some excellent LPE ideas and even initial access ideas in this post.</li>
<li><a href="https://badoption.eu/blog/2023/09/28/ZipLink.html" target="_blank">ZipLink - Combine Zips and Lnk for fun and profit</a>. If the above was giving you ideas for initial access, check this post. A few clicks (zip + pop up), but not bad!</li>
<li><a href="https://blog.scrt.ch/2023/09/25/exploiting-stale-adidns-entries/" target="_blank">Exploiting stale ADIDNS entries</a>. Some fun DNS based tricks for domain compromise.</li>
<li><a href="https://blog.washi.dev/posts/popping-calcs-in-dnspy/" target="_blank">A problem with .NET Self-Contained Apps and how to pop calculators in dnSpy</a>. Update your dnSpy or get pop'd in the NK's next campaign targeting security researchers.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/p0dalirius/ExtractBitlockerKeys" target="_blank">ExtractBitlockerKeys</a> -  Post-ex script to automatically extract the bitlocker recovery keys from a domain.</li>
<li><a href="https://gist.github.com/EspressoCake/f3588fc339b5b681002d06df41c7e977" target="_blank">transitiveObjectControl.py</a> - Given transitive object control: output info on last hop, chain length, and type.</li>
<li><a href="https://github.com/Maldev-Academy/MaldevAcademyLdr.1" target="_blank">MaldevAcademyLdr.1</a> - The team at Maldev Academy drop their first "openly released" loader.</li>
<li><a href="https://github.com/CTI-Driven/LOLBins" target="_blank">LOLBins</a>-  The LOLBins CTI-Driven (Living-Off-the-Land Binaries Cyber Threat Intelligence Driven) is a project that aims to help cyber defenders understand how LOLBin binaries are used by threat actors during an intrusion in a graphical and digestible format for the TIPs platform using the STIX format.</li>
<li><a href="https://github.com/hlldz/misc/tree/main/proxy_calls" target="_blank">proxy_calls</a> - Proof of Concept - Custom Call Stack for LoadLibrary with TrySubmitThreadpoolCallback/TpSimpleTryPost.</li>
<li><a href="https://github.com/p0dalirius/LDAPWordlistHarvester" target="_blank">LDAPWordlistHarvester</a> - A tool to generate a wordlist from the information present in LDAP, in order to crack passwords of domain accounts.</li>
<li><a href="https://github.com/g0h4n/REC2" target="_blank">REC2</a> - New rust-based C2 (Yes another C2). Uses VirusTotal and Mastodon APIs.</li>
<li><a href="https://github.com/M01N-Team/HeaderLessPE" target="_blank">HeaderLessPE</a> - A memory PE loading technique using HVNC.</li>
<li><a href="https://github.com/Chocapikk/CVE-2023-29357" target="_blank">CVE-2023-29357</a>- Patched June 2023 but... Microsoft SharePoint Server priv esc.</li>
<li><a href="https://github.com/jsecurity101/JonMon" target="_blank">JonMon</a> - <a href="https://twitter.com/jsecurity101" target="_blank">@jsecurity101</a> with a tool drop for defenders/attackers. "...collection of open-source telemetry sensors designed to provide users with visibility into the operations and activity of their Windows systems". Add this to your maldev boxes to see what defenders could be collecting on your actions.</li>
<li><a href="https://github.com/Mazars-Tech/AD_Miner" target="_blank">AD_Miner</a> - Use your existing neo4j DB to find some quick wins (may not work well against large environments based on our testing).</li>
<li><a href="https://gitlab.com/illwill/sub7" target="_blank">Sub7</a> - Source code for SubSeven 2.1.3 (if you're feeling nostalgic).</li>
<li><a href="https://github.com/gergelykalman/CVE-2023-32364-macos-app-sandbox-escape" target="_blank">CVE-2023-32364-macos-app-sandbox-escape</a> - Exploit for CVE-2023-32364.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://scorpiosoftware.net/2023/09/24/windows-hook-events/" target="_blank">Windows Hook Events</a>. Short read by Mr. Yosifovich. Discusses the SetWinEventHook API in Windows for intercepting and processing user interface-related events.</li>
<li><a href="https://github.com/pwnwriter/haylxon" target="_blank">haylxon</a>. Gowitness replacement? Blazing-fast tool to grab screenshots of your domain list right from terminal.</li>
<li><a href="https://github.com/hmgle/graftcp" target="_blank">graftcp</a>. A flexible tool for redirecting a given program's TCP traffic to SOCKS5 or HTTP proxy.</li>
<li><a href="https://github.com/W01fh4cker/VcenterKit" target="_blank">VcenterKit</a>. vCenter Comprehensive Penetration and Exploitation Toolkit.</li>
<li><a href="https://github.com/vulncheck-oss/go-exploit" target="_blank">go-exploit</a>. A Go-based Exploit Framework.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 356 (+2)</p>
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
