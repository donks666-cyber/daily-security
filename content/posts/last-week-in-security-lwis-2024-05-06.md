Title: Last Week in Security (LWiS) - 2024-05-06
Date: 2024-05-06 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-05-06
Author: Erik
Summary: Entra to on-prem (<a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>), new bloodhound edges (<a href="https://twitter.com/Jonas_B_K" target="_blank">@Jonas_B_K</a> ), Chrome type confusion (<a href="https://twitter.com/_manfp" target="_blank">@_manfp</a>), GitHub RCE via actions (<a href="https://twitter.com/Creastery" target="_blank">@Creastery</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-04-29 to 2024-05-06.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://krebsonsecurity.com/2024/04/fcc-fines-major-u-s-wireless-carriers-for-selling-customer-location-data/" target="_blank">FCC Fines Major U.S. Wireless Carriers for Selling Customer Location Data</a> - The real question is how much did these companies profit from this data before they were caught?</li>
<li><a href="https://www.theguardian.com/technology/2024/apr/28/bbc-presenters-likeness-used-in-advert-after-firm-tricked-by-ai-generated-voice" target="_blank">BBC presenter's likeness used in advert after firm tricked by AI-generated voice</a> - It's happening. Deep-phishing perhaps is the term? Are you/your customers ready? Can you simulate this attack?</li>
<li><a href="https://jfrog.com/blog/attacks-on-docker-with-millions-of-malicious-repositories-spread-malware-and-phishing-scams/" target="_blank">JFrog Security research discovers coordinated attacks on Docker Hub that planted millions of malicious repositories</a> - "nearly 20% of these public repositories (almost three million repositories!) actually hosted malicious content." :grimacing"</li>
<li><a href="https://sign.dropbox.com/blog/a-recent-security-incident-involving-dropbox-sign" target="_blank">A recent security incident involving Dropbox Sign</a> - Where the juciy data goes, so go the attackers. This was an acquisition (HelloSign) from 2019, no it should have been fully integrated into DropBox's security practice.</li>
<li><a href="https://www.justice.gov/opa/pr/sodinokibirevil-affiliate-sentenced-role-700m-ransomware-scheme" target="_blank">Sodinokibi/REvil Affiliate Sentenced for Role in $700M Ransomware Scheme</a> - A Ukrainian national was sentenced today to 13 years and seven months in prison and ordered to pay over $16 million in restitution for his role in conducting over 2,500 ransomware attacks and demanding over $700 million in ransom payments. A rare conviction in the ransomware scene.</li>
<li><a href="https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025" target="_blank">What's new in Windows Server 2025 (preview)</a> - Microsoft has decided to change the default on #pre2k computer accounts and has removed the checkbox entirely in upcoming server releases.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://dirkjanm.io/lateral-movement-and-hash-dumping-with-temporary-access-passes-microsoft-entra/" target="_blank">Lateral movement and on-prem NT hash dumping with Microsoft Entra Temporary Access Passes</a> - Per usual, amazing post by Dirk-Jan. Passwordless persistence and Entra-ID &lt;-&gt; On-Prem tradecraft. Must read.</li>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations/" target="_blank">Uncharmed: Untangling Iran's APT42 Operations</a> - Tradecraft details including their use of social engineering for initial access and credential harvesting. NGOs and journalists are being targeted.</li>
<li><a href="https://www.guidepointsecurity.com/blog/sccm-exploitation-compromising-network-access-accounts/" target="_blank">SCCM Exploitation: Compromising Network Access Accounts</a> - An article on how fruitful Network Access Accounts are along with some mitigation and detection guidance. Even comes with wazuh and elastic parsers and rules! Thorough work.</li>
<li><a href="https://posts.specterops.io/adcs-attack-paths-in-bloodhound-part-2-ac7f925d1547" target="_blank">ADCS Attack Paths in BloodHound — Part 2</a> - New edges introduced with ADCS support in bloodhound.</li>
<li><a href="https://observationsinsecurity.com/2024/04/25/how-i-hacked-into-googles-internal-corporate-assets/" target="_blank">How I hacked into Google's internal corporate assets</a> - Spoiler alert: dependency confusion. Has anyone used technique on a red team?</li>
<li><a href="https://www.zerodayinitiative.com/blog/2024/5/2/cve-2024-2887-a-pwn2own-winning-bug-in-google-chrome" target="_blank">CVE-2024-2887: A Pwn2own Winning Bug in Google Chrome</a> - Type confusion in web assembly leads to shellcode execution in the V8 sandbox.</li>
<li><a href="https://labs.jumpsec.com/why-sneak-when-you-can-walk-through-the-front-door/" target="_blank">Why sneak when you can walk through the front door - A Love letter to Password Spraying against M365 in Red Team Engagements</a> - Great advice on performing a responsible password spray. The internal phish post-access is especially deadly.</li>
<li><a href="https://posts.specterops.io/manual-ldap-querying-part-2-8a65099e12e3" target="_blank">Manual LDAP Querying: Part 2</a> - Be careful with these (and Sharphound) as mature defenders will detect strange queries (like the SPN query).</li>
<li><a href="https://blog.stratumsecurity.com/2024/04/29/code-injection-to-rce-with-net/" target="_blank">Code Injection to RCE with .NET</a> - A real-life write up on a web app .NET injection and how it was turned into RCE.</li>
<li><a href="https://whiteknightlabs.com/2024/04/30/sleeping-safely-in-thread-pools/" target="_blank">Sleeping Safely in Thread Pools</a> - A new-to-red-teams (seen in the wild) technique to protect sleeping treads with thread pools.</li>
<li><a href="https://revflash.medium.com/its-morphin-time-self-modifying-code-sections-with-writeprocessmemory-for-edr-evasion-9bf9e7b7dced" target="_blank">It's Morphin' Time: Self-Modifying Code Sections with WriteProcessMemory for EDR Evasion</a> - This post introduces a novel self-injection technique for EDR evasion.</li>
<li><a href="https://www.0ffset.net/reverse-engineering/identifying-xrefs-with-capstone/" target="_blank">Identifying Cross References with Capstone Disassembler and PEFile</a> - Learn how to programmatically identify cross-references in malware code using Capstone Disassembler and PEFile in Python.</li>
<li><a href="https://zeronetworks.com/blog/leash-the-hounds-stop-ldap-recon-attacks" target="_blank">Leash the Hounds: How to Stop LDAP Recon Attacks</a> - Strategies to mitigate LDAP reconnaissance attacks using the LDAP Firewall for enhanced security and efficient auditing. <a href="https://github.com/zeronetworks/ldapfw" target="_blank">ldapfw</a> is the tool.</li>
<li><a href="https://swisskyrepo.github.io/Drink-Love-Share-Rump/" target="_blank">DLS 2024 - RedTeam Fails - "Oops my bad I ruined the operation"</a> - Examples of basic OPSEC mistakes during red team assessments.</li>
<li><a href="https://ynwarcs.github.io/Win11-24H2-CFG" target="_blank">CFG in Windows 11 24H2</a> - Explore how Windows 11's 24H2 update integrates Control Flow Guard with hotpatching to enhance system security and efficiency.</li>
<li><a href="https://sabotagesec.com/tale-of-code-integrity-driver-loads/" target="_blank">Tale of Code Integrity &amp; Driver Loads</a> - The article discusses how the Core Isolation user setting in Windows affects the process of driver loading, particularly focusing on Virtualization-based Security (VBS) and Hypervisor-Protected Code Integrity (HVCI).</li>
<li><a href="https://starlabs.sg/blog/2024/04-sending-myself-github-com-environment-variables-and-ghes-shell/" target="_blank">Send()-ing Myself Belated Christmas Gifts - GitHub.com's Environment Variables &amp; GHES Shell</a> - 2MB of env variables from production Github.com and RCE. What a bug!</li>
<li><a href="https://nickb.website/blog/virtualizing-ios-on-apple-silicon" target="_blank">Virtualizing iOS on Apple Silicon</a> - Some impressive low level hacking.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/CCob/okta-terrify" target="_blank">okta-terrify</a> - Okta Verify and Okta FastPass Abuse Tool.</li>
<li><a href="https://github.com/padok-team/cognito-scanner" target="_blank">cognito-scanner</a> - A simple script which implements different Cognito attacks such as Account Oracle or Privilege Escalation.</li>
<li><a href="https://github.com/floesen/KExecDD" target="_blank">KExecDD</a> - Admin to Kernel code execution using the KSecDD driver.</li>
<li><a href="https://github.com/JCSteiner/Python-Beacon" target="_blank">Python-Beacon</a> - Python files to aide with shellcode execution.</li>
<li><a href="https://github.com/TheOfficialFloW/PPPwn" target="_blank">PPPwn</a> - PPPwn - PlayStation 4 PPPoE RCE.</li>
<li><a href="https://github.com/mlcsec/SharpGraphView" target="_blank">SharpGraphView</a> - Microsoft Graph API post-exploitation toolkit.</li>
<li><a href="https://github.com/0vercl0k/symbolizer-rs" target="_blank">symbolizer-rs</a> - A fast execution trace symbolizer for Windows that runs on all major platforms and doesn't depend on any Microsoft libraries.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/void-stack/Hypervisor-Detection" target="_blank">Hypervisor-Detection</a> - Detects virtual machines and malware analysis environments.</li>
<li><a href="https://github.com/erebe/wstunnel" target="_blank">wstunnel</a> - Tunnel all your traffic over Websocket or HTTP2 - Bypass firewalls/DPI - Static binary available.</li>
<li><a href="https://github.com/HeyPuter/puter" target="_blank">puter</a> - 🌐 The Internet OS! Free, Open-Source, and Self-Hostable.</li>
<li><a href="https://github.com/Installomator/Installomator" target="_blank">Installomator</a> - Installation script to deploy standard software on Macs.</li>
<li><a href="https://github.com/owasp-dep-scan/blint" target="_blank">blint</a> - BLint is a Binary Linter to check the security properties, and capabilities in your executables. Since v2, blint is also an SBOM generator for binaries.</li>
<li><a href="https://trufflesecurity.com/blog/postman-carries-lots-of-secrets" target="_blank">(The) Postman Carries Lots of Secrets</a> Don't sleep on Postman secrets!</li>
<li><a href="https://github.com/P1sec/QCSuper" target="_blank">QCSuper</a> - QCSuper is a tool communicating with Qualcomm-based phones and modems, allowing to capture raw 2G/3G/4G radio frames, among other things.</li>
<li><a href="https://github.com/bluet/proxybroker2" target="_blank">proxybroker2</a> - The New (auto rotate) Proxy [Finder | Checker | Server]. HTTP(S) &amp; SOCKS 🎭.</li>
<li><a href="https://github.com/hoodoer/JS-Tap" target="_blank">JS-Tap</a> - JavaScript payload and supporting software to be used as XSS payload or post exploitation implant to monitor users as they use the targeted application. Also includes a C2 for executing custom JavaScript payloads in clients.</li>
<li><a href="https://github.com/dunderhay/git-rotate" target="_blank">git-rotate</a> - Leveraging GitHub Actions to rotate IP addresses during password spraying attacks to bypass IP-Based blocking.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 426 (+0)</p>
<p>Blogs monitored: 379 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
