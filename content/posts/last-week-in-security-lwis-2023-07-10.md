Title: Last Week in Security (LWiS) - 2023-07-10
Date: 2023-07-10 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-07-10
Author: Erik
Summary: LPEs for Windows and Linux, Mastodon TooRoot, tons of web app hacking, and a bunch of new tools, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-06-26 to 2023-07-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2023/06/gmail-client-side-encryption-deep-dive.html" target="_blank">Gmail client-side encryption: A deep dive</a>. People continue to glue on things to a protocol (email) that was never intended to be secure or private. This implementation looks pretty seamless (unlike PGP) actually.</li>
<li><a href="https://bishopfox.com/blog/cve-2023-27997-exploitable-and-fortigate-firewalls-vulnerable" target="_blank">CVE-2023-27997 Is Exploitable, and 69% of FortiGate Firewalls Are Vulnerable</a>. Firewall, you had one job...</li>
<li><a href="https://zetter.substack.com/p/sec-targets-solarwinds-ciso-for-possible" target="_blank">SEC Targets SolarWinds' CISO for Rare Legal Action Over Russian Hack</a>. 🌶️🌶️🌶️</li>
<li><a href="https://support.apple.com/en-us/HT213825" target="_blank">About the security content of Rapid Security Responses for macOS Ventura 13.4.1</a>. I believe this is the second deployment of the "Rapid Security Response" from Apple.</li>
<li><a href="https://arstechnica.com/security/2023/07/mastodon-fixes-critical-tootroot-vulnerability-allowing-node-hijacking/" target="_blank">Mastodon fixes critical “TootRoot” vulnerability allowing node hijacking</a>. The attention from the social media wars is a good thing for Mastodon. More eyes make shallow bugs.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://offsec.almond.consulting/windows-msiexec-eop-cve-2020-0911.html" target="_blank">Windows Installer arbitrary content manipulation Elevation of Privilege (CVE-2020-0911)</a>. While the CVE is a bit aged, the write up is high quality.</li>
<li><a href="https://www.shielder.com/blog/2023/07/aws-codebuild--s3-privilege-escalation/" target="_blank">AWS CodeBuild + S3 == Privilege Escalation</a>. The cloud is just someone else's <span class="strike">computer</span> foot guns.</li>
<li><a href="https://blog.assetnote.io/2023/06/29/binary-reversing-citrix-xss/" target="_blank">Reversing Citrix Gateway for XSS</a>. These gateways are everywhere in enterprise, I wonder how many are still vulnerable... Check the vulnerable versions in the <a href="https://blog.assetnote.io/2023/06/29/citrix-xss-advisory/" target="_blank">advisory</a>.</li>
<li><a href="https://www.archcloudlabs.com/projects/gdb-debugging-1/" target="_blank">Debugging with gdb - Fixing a NULL Pointer Dereference in dhcpcd</a>. Some good basic gdb triage.</li>
<li><a href="https://www.mdsec.co.uk/2023/06/cve-2023-26258-remote-code-execution-in-arcserve-udp-backup/" target="_blank">CVE-2023-26258 - Remote Code Execution in ArcServe UDP Backup</a>. "Within minutes of analysing the code, a critical authentication bypass was discovered." 😬 The disclosure timeline is also... interesting.</li>
<li><a href="https://posts.specterops.io/sowing-chaos-and-reaping-rewards-in-confluence-and-jira-7a90ba33bf62" target="_blank">Sowing Chaos and Reaping Rewards in Confluence and Jira</a>. Comes with a new tool: <a href="https://github.com/werdhaihai/AtlasReaper" target="_blank">AtlasReaper</a> - A command-line tool for reconnaissance and targeted write operations on Confluence and Jira instances.</li>
<li><a href="https://www.trustedsec.com/blog/chaining-vulnerabilities-to-exploit-post-based-reflected-xss/" target="_blank">Chaining Vulnerabilities to Exploit POST Based Reflected XSS</a>. Comes with its own learning lab!</li>
<li><a href="https://whiteknightlabs.com/2023/07/06/developing-winsock-communication-in-malware/" target="_blank">Developing Winsock Communication in Malware</a>. Tired: named pipes. Inspired: Winsock over TCP.</li>
<li><a href="https://whiteknightlabs.com/2023/07/06/mockingjay-memory-allocation-primitive/" target="_blank">Mockingjay Memory Allocation Primitive</a>. Some good code examples linked.</li>
<li><a href="https://www.wiz.io/blog/linux-rootkits-explained-part-1-dynamic-linker-hijacking" target="_blank">Linux rootkits explained - Part 1: Dynamic linker hijacking</a>. Covers the first of the three major types of rootkits: LD_PRELOAD (the others being kernel modules and eBPF).</li>
<li><a href="https://labs.withsecure.com/publications/executing-arbitrary-code-executables-in-read-only-filesystems" target="_blank">Executing Arbitrary Code &amp; Executables in Read-Only FileSystems</a>. As everything moves to k8s as a service, its only a matter of time before you land in a read-only file system.</li>
<li><a href="https://blog.assetnote.io/2023/07/04/citrix-sharefile-rce/" target="_blank">Encrypted Doesn't Mean Authenticated: ShareFile RCE (CVE-2023-24489)</a>. Another great writeup from assetnote.</li>
<li><a href="https://www.rcesecurity.com/2023/07/patch-diffing-cve-2023-28121-to-compromise-a-woocommerce/" target="_blank">Patch Diffing CVE-2023-28121 to Compromise a WooCommerce</a>. Lots of web app hacking this week!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/lem0nSec/ShellGhost" target="_blank">ShellGhost</a> - A memory-based evasion technique which makes shellcode invisible from process start to end.</li>
<li><a href="https://github.com/lrh2000/StackRot" target="_blank">StackRot</a> - CVE-2023-3269: Linux kernel privilege escalation vulnerability.</li>
<li><a href="https://github.com/fortra/CVE-2023-28252" target="_blank">CVE-2023-28252</a> - Common Log File System (CLFS) LPE for Windows patched in April 2023.</li>
<li><a href="https://github.com/fin3ss3g0d/evilgophish" target="_blank">evilgophish</a> - evilginx + gophish. Bow with evilginx3 support!</li>
<li><a href="https://github.com/bitquark/shortscan" target="_blank">shortscan</a> - An IIS short filename enumeration tool.</li>
<li><a href="https://github.com/xforcered/BOFMask" target="_blank">BOFMask</a> is a proof-of-concept for masking Cobalt Strike's Beacon payload while executing a Beacon Object File (BOF).</li>
<li><a href="https://github.com/D00Movenok/BounceBack" target="_blank">BounceBack</a> - ↕️🤫 Stealth redirector for your red team operation security.</li>
<li><a href="https://github.com/Octoberfest7/TeamsPhisher" target="_blank">TeamsPhisher</a> - Send phishing messages and attachments to Microsoft Teams users.</li>
<li><a href="https://github.com/serpapi/clauneck" target="_blank">clauneck</a> - A tool for scraping emails, social media accounts, and much more information from websites using Google Search Results.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/CERT-Polska/Artemis" target="_blank">Artemis</a> - A modular web reconnaissance tool and vulnerability scanner.</li>
<li><a href="https://github.com/ustayready/golddigger" target="_blank">golddigger</a> is a simple tool used to help quickly discover sensitive information in files recursively. Originally written to assist in rapidly searching files obtained during a penetration test.</li>
<li><a href="https://github.com/axllent/mailpit" target="_blank">mailpit</a> - An email and SMTP testing tool with API for developers.</li>
<li><a href="https://github.com/folkertvanheusden/multitail/" target="_blank">multitail</a> - Tail on steroids.</li>
<li><a href="https://github.com/RedTeamPentesting/kbtls" target="_blank">kbtls</a> - Establishes mutually trusted TLS connections based on a pre-shared connection key.</li>
<li><a href="https://github.com/blackhillsinfosec/skyhook" target="_blank">skyhook</a> - A round-trip obfuscated HTTP file transfer setup built to bypass IDS detections.</li>
<li><a href="https://github.com/adnanh/webhook" target="_blank">webhook</a> is a lightweight incoming webhook server to run shell commands.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 348 (+0)</p>
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
