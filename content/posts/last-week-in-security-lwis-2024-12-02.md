Title: Last Week in Security (LWiS) - 2024-12-02
Date: 2024-12-02 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-12-02
Author: Erik
Summary: Windows LPE (<a href="https://x.com/SecuriTeam_SSD" target="_blank">@SecuriTeam_SSD</a>), Nighthawk 0.3.3 (<a href="https://x.com/MDSecLabs" target="_blank">@MDSecLabs</a>), Advanced Cobalt Strike Usage (<a href="https://x.com/_RastaMouse" target="_blank">@_RastaMouse</a>), Webcam LED control (<a href="https://x.com/andreyknvl" target="_blank">@andreyknvl</a>), AI/ML attacks (<a href="https://x.com/olivier_boschko" target="_blank">@olivier_boschko</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-11-25 to 2024-12-02.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/newsroom/news/intel-chips-act.html#gs.ir3x3h" target="_blank">Intel, Biden-Harris Administration Finalize $7.86 Billion Funding Award Under US CHIPS Act</a> - Apparently <a href="https://www.intel.com/content/www/us/en/newsroom/news/intel-ceo-news-dec-2024.html" target="_blank">not enough to save Intel CEO Pat Gelsinger's job</a>.</li>
<li><a href="https://www.mdsec.co.uk/2024/11/nighthawk-0-3-3-evanesco/" target="_blank">Nighthawk 0.3.3 - Evanesco</a> - The team at MDSec has stepped up their in-memory evasion techniques with this new release. With the new Python API and ability to register custom commands, Nighthawk is becoming a contender to dethrone Cobalt Strike.</li>
<li><a href="https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/" target="_blank">RomCom exploits Firefox and Windows zero days in the wild</a> - Two 0days led to Firefox/Windows compromise without user interaction - browse to page, get exploited. These kinds of 0-click exploits are becoming rarer as browsers and operating systems become increasingly sandboxed/hardened.</li>
<li><a href="https://blog.thinkst.com/2024/12/its-baaack-credit-card-canarytokens-are-now-on-your-consoles.html" target="_blank">It's Baaack… Credit Card Canarytokens are now on your Consoles</a> - Probably not a concern for redteamers (are you trying credit card numbers?), but defenders may want to consider dropping some canarytoken cards in their databases. Hopefully other canarytokens have fired long before the cards, but defense in depth is always a good idea.</li>
<li><a href="https://www.raspberrypi.com/products/raspberry-pi-pico-2/" target="_blank">Raspberry Pi Pico 2</a> - The chip that powered the DEF CON badges this year is now available in a $5 microcontroller ($7 if you want WiFi and Bluetooth).</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul><li><a href="https://ssd-disclosure.com/ssd-advisory-ksthunk-sys-integer-overflow-pe/" style="color: #3bd267;" target="_blank">SSD Disclosure Advisory - ksthunk.sys Integer Overflow (Windows LPE)</a> <span class="m-label m-flat m-success">Sponsored</span> - A vulnerability in the ksthunk.sys driver allows a local attacker to exploit an Integer Overflow vulnerability and gain elevated privileges on Windows (PoC provided). Microsoft states it has been patched, but it still works on the latest Windows 11. Have an exploit you want to disclose? Check out <b><a href="https://ssd-disclosure.com/" style="color: #3bd267;" target="_blank">SSD Secure Disclosure</a></b> to know more.</li></ul><ul>
<li><a href="https://embracethered.com/blog/posts/2024/deepseek-ai-prompt-injection-to-xss-and-account-takeover/" target="_blank">DeepSeek AI: From Prompt Injection To Account Takeover</a> - With web frontends and code generation, LLMs can be used to generate cross site scripting (XSS) payloads that get executed in the browser.</li>
<li><a href="https://research.checkpoint.com/2024/gaming-engines-an-undetected-playground-for-malware-loaders/" target="_blank">Gaming Engines: An Undetected Playground for Malware Loaders</a> - Using a game engine to load malware is a clever technique to evade detection. The use of the 3D renderer to check for sandboxed environments is a nice touch.</li>
<li><a href="https://certitude.consulting/blog/en/exploring-anti-phishing-measures-in-microsoft-365-pt-2/" target="_blank">Exploring Anti-Phishing Measures in Microsoft 365 - Pt. 2</a> - The arms race of phishing warnings implemented in HTML/CSS continues. Since senders can determine the style of their emails, they can modify the styles of the warnings that Microsoft 365 displays to hide them - mostly.</li>
<li><a href="https://blog.christophetd.fr/pkce-aws-sso/" target="_blank">The New PKCE Authentication in AWS SSO Brings Hope (Mostly)</a> - Device Code phishing <em>should</em> be a thing of the past, but Amazon still has it enabled and there is no way to disable it. The post includes details about PKCE (Proof Key for Code Exchange) and helpful hints on how to hunt for device code authentications.</li>
<li><a href="https://decoder.cloud/2024/11/26/group-policy-nightmares-pt2/" target="_blank">Group Policy Security Nightmares pt2</a> - Loving this series on Group Policy. Each post is a short explanation of a vulnerable Group Policy and how it can be abused.</li>
<li><a href="https://blog.exodusintel.com/2024/12/02/windows-sockets-from-registered-i-o-to-system-privileges/" target="_blank">Windows Sockets: From Registered I/O to SYSTEM Privileges</a> - A Windows local privilege escalation via a vulnerability patched in August 2024 that uses a heap spray is detailed here. This <a href="https://github.com/Nephster/CVE-2024-38193" target="_blank">PoC</a>  is not affiliated with the post, be careful.</li>
<li><a href="https://blog.nviso.eu/2024/11/26/wake-up-and-smell-the-bitlocker-keys/" target="_blank">Wake up and Smell the BitLocker Keys</a> - Another post on BitLocker key extraction. Without a second factor, consider BitLocker an annoyance to moderately sophisticated attackers, not a security feature.</li>
<li><a href="https://rastamouse.me/udrl-sleepmask-and-beacongate/" target="_blank">UDRL, SleepMask, and BeaconGate</a> - Cobalt Strike has evolved quite a bit over the last few years. This post breaks down the User-Defined Reflective Loader (UDRL), SleepMask, and BeaconGate.</li>
<li><a href="https://boschko.ca/adversarial-ml/" target="_blank">Breaking Down Adversarial Machine Learning Attacks Through Red Team Challenges</a> - Learn how to craft and understand adversarial attacks on AI/ML models through hands-on challenges.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/xairy/lights-out" target="_blank">lights-out</a> - Tools for controlling webcam LED on ThinkPad X230. See the <a href="https://powerofcommunity.net/poc2024/Andrey%20Konovalov,%20Lights%20Out%20-%20Covertly%20turning%20off%20the%20ThinkPad%20webcam%20LED%20indicator.pdf" target="_blank">[PDF] slides</a> for more fuel to tape over your webcams.</li>
<li><a href="https://github.com/Friends-Security/ShadowHound" target="_blank">ShadowHound</a> - PowerShell scripts for alternative SharpHound enumeration, including users, groups, computers, and certificates, using the ActiveDirectory module (ADWS) or System.DirectoryServices class (LDAP).</li>
<li><a href="https://github.com/ioncodes/SilentLoad" target="_blank">SilentLoad</a> - Loads a drivers through NtLoadDriver by setting up the service registry key directly. To be used in engagement for Bring Your Own Vulnerable Driver (BYOVD), where service creation creates an alert. Could also be useful with WinDivert/<a href="https://github.com/praetorian-inc/PortBender" target="_blank">PortBender</a>.</li>
<li><a href="https://github.com/Octoberfest7/Enumprotections_BOF" target="_blank">Enumprotections_BOF</a> - A BOF to enumerate system process, their protection levels, and more.</li>
<li><a href="https://github.com/Kudaes/Eclipse" target="_blank">Eclipse</a> - Activation Context Hijack.</li>
<li><a href="https://github.com/Censys-Research/censeye" target="_blank">censeye</a> - This tool is designed to help researchers identify hosts with characteristics similar to a given target. The tool can discover useful pivots in Censys host data and (optionally) crawl related hosts using data from those discoveries.</li>
<li><a href="https://github.com/decoder-it/KrbRelayEx" target="_blank">KrbRelayEx</a> - KrbRelayEx is a tool designed for performing Man-in-the-Middle (MitM) attacks by relaying Kerberos AP-REQ tickets. It listens for incoming SMB connections and forwards the AP-REQ to the target host, enabling access to SMB shares or HTTP ADCS (Active Directory Certificate Services) endpoints on behalf of the targeted identity.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://gergelykalman.com/badmalloc-CVE-2023-32428-a-macos-lpe.html" target="_blank">badmalloc (CVE-2023-32428) - a macOS LPE</a> - A file race condition in macOS leads to a local privilege escalation. Apple does not handle the bug bounty well, sadly.</li>
<li><a href="https://github.com/D3Ext/Hooka" target="_blank">Hooka</a> - Shellcode loader generator with multiples features.</li>
<li><a href="https://github.com/projectdiscovery/urlfinder" target="_blank">urlfinder</a> - A high-speed tool for passively gathering URLs, optimized for efficient and comprehensive web asset discovery without active scanning.</li>
<li><a href="https://github.com/MythicAgents/Hannibal" target="_blank">Hannibal</a> - A Mythic Agent written in PIC C.</li>
<li><a href="https://github.com/mistweaverco/bananas" target="_blank">bananas</a> - Bananas🍌, Cross-Platform screen 🖥️ sharing 📡 made simple ⚡.</li>
<li><a href="https://github.com/0xthirteen/reg_snake" target="_blank">reg_snake</a> - Python tool to interact with WMI StdRegProv.</li>
<li><a href="https://github.com/Cyb3rWard0g/floki" target="_blank">floki</a> - Agentic Workflows Made Simple.</li>
<li><a href="https://github.com/PShlyundin/GPOHunter" target="_blank">GPOHunter</a> - A security assessment tool for analyzing Active Directory Group Policy Objects (GPOs) to identify misconfigurations and vulnerabilities.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 441 (+0)</p>
<p>Blogs monitored: 397 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
