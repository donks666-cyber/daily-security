Title: Last Week in Security (LWiS) - 2024-11-12
Date: 2024-11-12 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-11-12
Author: Erik
Summary: 🕵️📱 Mysterious iPhone reboots, Tor under attack, Citrix Unauth RCE (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>), GitHub Actions attack (<a href="https://x.com/adnanthekhan" target="_blank">@adnanthekhan</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-11-04 to 2024-11-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.torproject.org/defending-tor-mitigating-IP-spoofing/" target="_blank">Defending the Tor network: Mitigating IP spoofing against Tor</a> - Attackers used spoofed IP packets to trigger automated abuse complaints against Tor relay providers. Many people host Tor relays as they are "safe" in that the shuttle encrypted traffic between other Tor nodes, and thus are typically not subject to abuse complaints. For technical details see the post <a href="https://delroth.net/posts/spoofed-mass-scan-abuse/" target="_blank">One weird trick to get the whole planet to send abuse complaints to your best friend(s)</a>.</li>
<li><a href="https://security.paloaltonetworks.com/PAN-SA-2024-0015" target="_blank">PAN-SA-2024-0015 Important Informational Bulletin: Ensure Access to Management Interface is Secured</a> - This is a strange "there may be an exploit" bulletin. Get your management interfaces secured either way.</li>
<li><a href="https://opensource.org/ai/open-source-ai-definition" target="_blank">The Open Source AI Definition - 1.0</a> - Lots of controversy on this definition of "Open Source" AI. Some are <a href="https://samjohnston.org/2024/10/22/debian-general-resolution-gr-drafted-opposing-osis-open-source-ai-definition-osaid/" target="_blank">not</a> <a href="https://news.slashdot.org/story/24/11/03/0257241/new-open-source-ai-definition-criticized-for-not-opening-training-data" target="_blank">happy</a>. I personally agree with Bruce Schneier that "open weights" is a much better term for this type of AI.</li>
<li><a href="https://blogs.vmware.com/cloud-foundation/2024/11/11/vmware-fusion-and-workstation-are-now-free-for-all-users/" target="_blank">VMware Fusion and Workstation are Now Free for All Users</a> - After being acquired by Broadcom, VMware has not done well in the court of public opinion after raising prices and killing off the free tier of the popular ESXi hypervisor. It looks like they are backtracking with this move. The damage is likely already done, as many businesses are actively migrating to alternatives. <a href="https://ludus.cloud/" target="_blank">Ludus</a> is built on the open source KVM/Proxmox.</li>
<li><a href="https://www.404media.co/police-freak-out-at-iphones-mysteriously-rebooting-themselves-locking-cops-out/" target="_blank">Police Freak Out at iPhones Mysteriously Rebooting Themselves, Locking Cops Out</a> - Law enforcement claims that iOS 18 is causing iPhones to communicate with each other and reboot. Occam's Razor would suggest that perhaps iOS 18 is just buggy, crashes, and reboots. However, it has <a href="https://www.forbes.com/sites/davidphelan/2024/11/12/no-your-iphone-is-not-mysteriously-rebooting-heres-whats-happening-secret-revealed/" target="_blank">later been reported</a> that this is a feature of iOS 18.1 where iPhones will reboot if not unlocked for 4 days. The iPhone to iPhone communication almost certainly not the cause of the reboots.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/" target="_blank">Life on a crooked RedLine: Analyzing the infamous infostealer's backend</a> - Deep technical details on the Redline backend that was taken down last week.</li>
<li><a href="https://lab.wallarm.com/attackers-abuse-docusign-api-to-send-authentic-looking-invoices-at-scale/" target="_blank">Attackers Abuse DocuSign API to Send Authentic-Looking Invoices At Scale</a> - Clever use of "3rd party" emailers that are likely allowlisted by targets to deliver phishing content.</li>
<li><a href="https://www.securonix.com/blog/crontrap-emulated-linux-environments-as-the-latest-tactic-in-malware-staging/" target="_blank">CRON#TRAP: Emulated Linux Environments as the Latest Tactic in Malware Staging</a> - Attackers drop a "pivotbox" TinyCore Linux virtual machine run by QEMU to bypass detections and expand access into Windows networks.</li>
<li><a href="https://decoder.cloud/2024/11/08/group-policy-security-nightmares-pt-1/" target="_blank">Group Policy Security Nightmares pt 1</a> - A post on how Group Policy can be misconfigured to create security issues in Windows Active Directory networks.</li>
<li><a href="https://jhftss.github.io/A-New-Era-of-macOS-Sandbox-Escapes/" target="_blank">A New Era of macOS Sandbox Escapes: Diving into an Overlooked Attack Surface and Uncovering 10+ New Vulnerabilities</a> - Applications on macOS have a complex sandbox system based on entitlements, and by really digging into it, Mickey Jin found a lot of vulnerabilities.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/cloud-pentesting/privilege-escalation-google-cloud-composer/" target="_blank">Filling up the DagBag: Privilege Escalation in Google Cloud Composer</a> - If you can get write access to a Google Cloud Composer bucket, you can execute arbitrary command execution in the composer pipeline.</li>
<li><a href="https://adnanthekhan.com/2024/11/11/release-drafter-∫to-google-accompanist-compromise-vrp-writeup/" target="_blank">Release-Drafter To google/accompanist Compromise: VRP Writeup</a> - A good example of an in-the-wild GitHub Actions attack.</li>
<li><a href="https://labs.watchtowr.com/visionaries-at-citrix-have-democratised-remote-network-access-citrix-virtual-apps-and-desktops-cve-unknown/" target="_blank">Visionaries Have Democratised Remote Network Access - Citrix Virtual Apps and Desktops (CVE Unknown)</a> - Watchtowr has been on a tear recently, and this one is a classic .NET deserialization exploit, but with a twist of jumping protocols - from HTTP to MSMQ. This feels like a CVSS 10.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://netsecfish.notion.site/Command-Injection-Vulnerability-in-name-parameter-for-D-Link-NAS-12d6b683e67c80c49ffcc9214c239a07" target="_blank">Command Injection Vulnerability in 'name' parameter for D-Link NAS</a> - Unauthenticated remote code execution against a four different network attached storage devices, with over 60,000 on the internet.</li>
<li><a href="https://github.com/ifpdz/CVE-2024-44258" target="_blank">CVE-2024-44258</a> - Proof of concept of a symlink vulnerability within the ManagedConfiguration framework and the profiled daemon in Apple devices. When restoring a crafted backup, the migration process fails to validate whether the destination folder is a symbolic link (symlink), leading to unauthorized file migration into restricted areas.</li>
<li><a href="https://github.com/0xthirteen/Carseat" target="_blank">Carseat</a> is a python implementation of Seatbelt. This tool contains all (all minus one technically) modules in Seatbelt that support remote execution as an option.</li>
<li><a href="https://github.com/Offensive-Panda/ShadowDumper" target="_blank">ShadowDumper</a> is a powerful tool used to dump LSASS memory, often needed in penetration testing and red teaming. It uses multiple advanced techniques to dump memory, allowing to access sensitive data in LSASS memory. [Note: feels largely AI generated]</li>
<li><a href="https://github.com/c3llkn1ght/BlindBrute" target="_blank">BlindBrute</a> is a highly customizable Python tool designed for blind SQL injection attacks. It supports multiple detection methods, including status code, content length, keyword comparison, and time-based. It also allows for flexible payload injection using headers, query strings, request data, and raw HTTP request templates, making it adaptable to a wide range of scenarios.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://embracethered.com/blog/posts/2024/claude-computer-use-c2-the-zombais-are-coming/" target="_blank">ZombAIs: From Prompt Injection to C2 with Claude Computer Use</a> - AI is the new hot topic, and soon AI models will be interacting with your computer, potentially with malicious prompt injection controlling them.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 439 (+0)</p>
<p>Blogs monitored: 396 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
