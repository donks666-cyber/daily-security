Title: Last Week in Security (LWiS) - 2024-05-29
Date: 2024-05-29 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-05-29
Author: Erik
Summary: A special two week edition!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-05-13 to 2024-05-29.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://krebsonsecurity.com/2024/05/stark-industries-solutions-an-iron-hammer-in-the-cloud/" target="_blank">Stark Industries Solutions: An Iron Hammer in the Cloud</a> - How Stark Industries Solutions emerged as a significant facilitator of cyberattacks by hosting proxy and VPN services used to conceal and carry out disruptive activities, including massive DDoS attacks targeting Ukraine and Europe, with ties to Russian hacking groups and cybercriminal activities.</li>
<li><a href="https://moonlock.com/blackbasta-ransomware" target="_blank">Black Basta ransomware is targeting critical infrastructure sectors</a> - Black Basta ransomware, operated as a Ransomware-as-a-Service, has targeted over 500 organizations globally, significantly impacting 12 critical infrastructure sectors in the U.S., including healthcare, leading to disruptions like ambulance diversions and compromised electronic health records.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.guidepointsecurity.com/blog/beyond-the-basics-exploring-uncommon-ntlm-relay-attack-techniques/" target="_blank">Beyond the Basics: Exploring Uncommon NTLM Relay Attack Techniques</a> - This blog outlines five NTLM relay attack vectors that aren't talked about enough.</li>
<li><a href="https://blog.slowerzs.net/posts/pplsystem/" target="_blank">Injecting code into PPL processes without vulnerable drivers on Windows 11</a> - Discovering and utilizing a syscall, NtSystemDebugControl, to inject code into Protected Process Light (PPL) processes.</li>
<li><a href="https://swarm.ptsecurity.com/xxe-chrome-safari-chatgpt/" target="_blank">Getting XXE in Web Browsers using ChatGPT</a> - Exploiting XML and XSL functionalities in web browsers to test and demonstrate XXE vulnerabilities.</li>
<li><a href="https://blog.exploit.org/caster-kerbhammer/" target="_blank">Kerbhammer: Detecting Kerberos attacks with Suricata</a> - Detecting Kerberos protocol attacks using the Suricata, highlighting methods to identify abnormal AS-REQ and AS-REP Roasting activities as potential security threats.</li>
<li><a href="https://www.wiz.io/blog/wiz-research-discovers-critical-vulnerability-in-replicate" target="_blank">The risk in malicious AI models: Wiz Research discovers critical vulnerability in AI-as-a-Service provider, Replicate</a> - "...In the course of that work, we have discovered critical vulnerabilities that could have led to the leakage of millions of private AI models and apps. "</li>
<li><a href="https://posts.specterops.io/phish-sticks-hate-the-smell-love-the-taste-f4db9de888f7" target="_blank">Phish Sticks; Hate the Smell, Love the Taste</a> -</li>
<li><a href="https://dfir.ch/posts/slash-proc/" target="_blank">The 'Invisibility Cloak' - Slash-Proc Magic</a> - This blog discusses on utilizing bind mounts to hide processes from the process list, examining how it's done, its forensic detectability.</li>
<li><a href="https://www.blackhillsinfosec.com/offensive-iot-for-red-team-implants-part-2/" target="_blank">Offensive IoT for Red Team Implants (Part 2)</a> - Use your Raspberry Pi Pico as a physical implant device for Red Team operations!</li>
<li><a href="https://trustedsec.com/blog/js-tap-mark-ii-now-with-c2-shenanigans" target="_blank">JS-Tap Mark II: Now with C2 Shenanigans</a> - This blog details updates to JS-Tap. It explains setting up JS-Tap with Gunicorn and nginx to handle more clients and introduces features for automated and repeated JavaScript payload deployment, improving usability.</li>
<li><a href="https://labs.watchtowr.com/qnap-qts-qnapping-at-the-wheel-cve-2024-27130-and-friends/" target="_blank">QNAP QTS - QNAPping At The Wheel (CVE-2024-27130 and friends)</a> - CVE-2024-27130, an unauthenticated stack overflow bug allowing remote code execution. The team details their investigation and exploitation process, highlighting the NAS device's role in multi-user environments and its security implications.</li>
<li><a href="https://blog.palantir.com/new-hires-lost-keys-lessons-learned-passwordless-authentication-series-3-dfdd79e89fb6" target="_blank">New Hires, Lost Keys &amp; Lessons Learned (Passwordless Authentication Series, #3)</a> - Palantir discusses their implementation of FIDO2 authentication via YubiKeys, focusing on the challenges and solutions for new hire onboarding and handling lost or broken authenticators. Nice to see these lessons learned shared amongst the community.</li>
<li><a href="https://amalmurali.me/posts/git-rce/" target="_blank">Exploiting CVE-2024-32002: RCE via git clone</a> - Technical write-up of git CVE-2024-32002. This one is triggered by cloning repositories with specially crafted submodules.</li>
<li><a href="https://blog.blacklanternsecurity.com/p/introducing-baddns" target="_blank">Introducing BadDNS</a> - Blog on a new tool released by Black Lantern. Used for subdomain takeover detection tool but covers other DNS related issues like zone transfers and NSEC walking as well.</li>
<li><a href="https://research.checkpoint.com/2024/foxit-pdf-flawed-design-exploitation/" target="_blank">Foxit PDF “Flawed Design” Exploitation</a> - Tradecraft against the biggest Adobe competitor, FOXIT.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/hackertarget/nmap-did-what" target="_blank">nmap-did-what</a> - Nmap Dashboard Mini Project. Don't sleep on what you can do with open-source and a little bit of glue!</li>
<li><a href="https://github.com/es3n1n/no-defender" target="_blank">no-defender</a> - A slightly more fun way to disable windows defender. (through the WSC api).</li>
<li><a href="https://github.com/SafeBreach-Labs/DoubleDrive" target="_blank">DoubleDrive</a> - A fully-undetectable ransomware that utilizes OneDrive &amp; Google Drive to encrypt target local files.</li>
<li><a href="https://github.com/Offensive-Panda/RWX_MEMEORY_HUNT_AND_INJECTION_DV" target="_blank">RWX_MEMEORY_HUNT_AND_INJECTION_DV</a> - Abusing Windows fork API and OneDrive.exe process to inject the malicious shellcode without allocating new RWX memory region.</li>
<li><a href="https://github.com/R00tkitSMM/CVE-2024-27804" target="_blank">CVE-2024-27804</a> - POC for CVE-2024-27804.</li>
<li><a href="https://github.com/xssdoctor/graphqlMaker" target="_blank">graphqlMaker</a> - Finds graphql queries in javascript files.</li>
<li><a href="https://github.com/thiagopeixoto/mystique-self-injection" target="_blank">mystique-self-injection</a> - An improvement and a different approach to Mockingjay Self-Injection.</li>
<li><a href="https://github.com/jsecurity101/ETWInspector" target="_blank">ETWInspector</a> - An Event Tracing for Windows (ETW) tool that allows you to enumerate Manifest &amp; MOF providers, as well as collect events from desired providers.</li>
<li><a href="https://github.com/RtlDallas/OdinLdr" target="_blank">OdinLdr</a> - Cobaltstrike UDRL with memory evasion.</li>
<li><a href="https://github.com/cybersectroll/SharpPersistSD" target="_blank">SharpPersistSD</a> - SharpPersistSD is focused on backdooring the remote machine so that persistency or code execution can be established later.</li>
<li><a href="https://github.com/blacklanternsecurity/baddns" target="_blank">baddns</a> - Check subdomains for subdomain takeovers and other DNS tomfoolery.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://trustedsec.com/blog/assumed-breach-the-evolution-of-offensive-security-testing" target="_blank">Assumed Breach: The Evolution of Offensive Security Testing</a> - This blog sparked another X/Twitter debate on whether assumed breach is still the "way to go".</li>
<li><a href="https://eversinc33.com/posts/kernel-mode-keylogging.html" target="_blank">Keylogging in the Windows Kernel with undocumented data structures</a> - Accessing the gafAsyncKeyState structure directly in kernel memory without using system APIs as a keylogger.</li>
<li><a href="https://threats.wiz.io/" target="_blank">Cloud Threat Landscape</a> - New/cool resource by Wiz. The <a href="https://threats.wiz.io/all-tools" target="_blank">tools</a> can come in clutch.</li>
<li><a href="https://opensourcesecurityindex.io/" target="_blank">Open Source Security Index</a> - Cool initiative! Thoughts on how they calculate index scores?</li>
<li><a href="https://github.com/astral-sh/ruff" target="_blank">ruff</a> - An extremely fast Python linter and code formatter, written in Rust.</li>
<li><a href="https://github.com/eset/nimfilt" target="_blank">nimfilt</a> - A collection of modules and scripts to help with analyzing Nim binaries.</li>
<li><a href="https://github.com/OOAFA/squeegee" target="_blank">squeegee</a> - A collection of tools using OCR to extract potential usernames from RDP screenshots.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 427 (+0)</p>
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
