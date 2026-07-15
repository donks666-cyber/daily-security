Title: Last Week in Security (LWiS) - 2024-12-16
Date: 2024-12-16 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-12-16
Author: Erik
Summary: LDAP RCE 😵, worst.fit (<a href="https://x.com/orange_8361" target="_blank">@orange_8361</a> + <a href="https://x.com/_splitline_" target="_blank">@_splitline_</a>) Grok AI vulns (<a href="https://x.com/wunderwuzzi23" target="_blank">@wunderwuzzi23</a>), automating exploits (<a href="https://x.com/FuzzySec" target="_blank">@FuzzySec</a> + <a href="https://x.com/chompie1337" target="_blank">@chompie1337</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-12-09 to 2024-12-16.</p>
<aside class="m-note m-success">
<h3>Holiday Break</h3>
<p>Last Week in Security will return 2025-01-06. Enjoy the holidays!</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.centerforcybersecuritypolicy.org/insights-and-research/a-partial-win-for-ai-red-teaming-from-the-copyright-office" target="_blank">A Partial Win for AI Red-Teaming from the Copyright Office</a> - "Common AI research techniques do not violate DMCA Section 1201," where common techniques are: prompt injection, creating accounts to bypass bans, and bypassing rate limits. But don't worry, there's still the Computer Fraud and Abuse Act (CFAA) that will be thrown at researchers.</li>
<li><a href="https://techcrunch.com/2024/12/16/blackberry-sells-cylance-for-160m-a-fraction-of-the-1-4b-it-paid-in-2018/" target="_blank">BlackBerry sells Cylance for $160M, a fraction of the $1.4B it paid in 2018</a> - Cylance was one of the first "AI" powered endpoint detection vendors, but has struggled to stay relevant under BlackBerry. For their efforts, BlackBerry is taking a $1.24 billion hit on the deal vs the acquisition price in 2018.</li>
<li><a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49112" target="_blank">Windows Lightweight Directory Access Protocol (LDAP) Remote Code Execution Vulnerability NewRecently updated - CVE-2024-49112</a> - We don't usually post a CVE without a blog post or proof of concept, but unauthenticated remote code execution on a Domain Controller is pretty wild. CVSS 9.8 tells you how serious it is. Someone even built a <a href="https://github.com/tnkr/poc_monitor" target="_blank">poc_monitor</a>.</li>
<li><a href="https://letsencrypt.org/2024/12/11/eoy-letter-2024/" target="_blank">6 Day TLS Certificates coming from Let's Encrypt next year</a> - Get those clocks in sync, and certificate systems automated! 90 day certificates will still be supported.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.deepinstinct.com/blog/forget-psexec-dcom-upload-execute-backdoor" target="_blank">Forget PSEXEC: DCOM Upload &amp; Execute Backdoor</a> -- This novel lateral movement technique uses only DCOM to write a  DLL and execute it on a remote machine. There are limited requirements (both machines in the same domain/forest, etc), and I suspect this will go undetected for quite some time.</li>
<li><a href="https://embracethered.com/blog/posts/2024/security-probllms-in-xai-grok/" target="_blank">Security ProbLLMs in xAI's Grok: A Deep Dive</a> - AI security research is heating up, and Johann Rehberger keeps cranking out solid posts with detailed methodology.</li>
<li><a href="https://github.com/FuzzySecurity/H2HC-2024/blob/main/H2HC2024_The_Kernel_Hackers_Guide_to_the_Galaxy.pdf" target="_blank">The Kernel Hacker's Guide to the Galaxy - Automating Exploit Engineering Workflows</a> - Beyond the great case studies from two of the best researchers in the game, this is one of the best looking decks I've seen.</li>
<li><a href="https://googleprojectzero.blogspot.com/2024/12/qualcomm-dsp-driver-unexpectedly-excavating-exploit.html" target="_blank">The Qualcomm DSP Driver - Unexpectedly Excavating an Exploit</a> - From just crash logs to 6 exploits is impressive, especially when it was a third party driver to blame. I wonder how much of the move for <a href="https://www.pcmag.com/news/apple-to-produce-modem-chips-for-iphones-in-house" target="_blank">Apple to launch its own modems in 2025</a>, is security vs licensing/cost.</li>
<li><a href="https://labs.watchtowr.com/cleo-cve-2024-50623/" target="_blank">Cleo Harmony, VLTrader, and LexiCom - RCE via Arbitrary File Write (CVE-2024-50623)</a> - These "managed file transfer" (MFT) programs are in use by the biggest enterprises, but have shockingly little security research done against them, likely because they are hard to get your hands on (no trials, free versions, and very expensive). As this exploit is still unpatched and the details are out, if you even recognize the name Cleo you should start incident response.</li>
<li><a href="https://securitylabs.datadoghq.com/articles/mut-1244-targeting-offensive-actors/" target="_blank">Getting a taste of your own medicine: Threat actor MUT-1244 targets offensive actors, leaking hundreds of thousands of credentials</a> - If you're testing tools off GitHub and not using a sandbox like <a href="https://ludus.cloud/" target="_blank">Ludus</a>, you're putting your customers at risk.</li>
<li><a href="https://www.oasis.security/resources/blog/oasis-security-research-team-discovers-microsoft-azure-mfa-bypass" target="_blank">Oasis Security Research Team Discovers Microsoft Azure MFA Bypass</a> - Azure allowed time based tokens to be valid for 3 minutes, not the 30 seconds they claimed. Add in the fact that there were no rate limits for guessing, with 24 token requests, that gives a roughly 50% of a correct guess. Microsoft now blocks attempts after a number of failures for around half a day.</li>
<li><a href="https://deluks2006.github.io/posts/snowy-days-and-the-malware-packing-ways/" target="_blank">Snowy Days &amp; The Malware Packing Ways</a> - A post on packers/crypters. Plenty of theory, code snippets, and resources.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/web-application-pentesting/uncovering-a-critical-vulnerability-through-chained-findings/" target="_blank">From Informational to Critical: Chaining &amp; Elevating Web Vulnerabilities</a> - Some nice escalation of a lower threat vulnerabilities into a serious finding in web apps hosted on the same domain.</li>
<li><a href="https://worst.fit/assets/EU-24-Tsai-WorstFit-Unveiling-Hidden-Transformers-in-Windows-ANSI.pdf" target="_blank">Unveiling Hidden Transformers in Windows ANSI!</a> - Awesome research by Orange Tsai &amp; Spitline Huang which also came with a <a href="https://worst.fit/#" target="_blank">list of all executables vulnerable to the WorstFit Attack!</a></li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/NtDallas/KrakenMask" target="_blank">KrakenMask</a> - Sleep obfuscation.</li>
<li><a href="https://github.com/safedv/RustSoliloquy" target="_blank">RustSoliloquy</a> - A Rust implementation of Internal-Monologue — retrieving NetNTLM hashes without touching LSASS, leveraging SSPI for NTLM negotiation and indirect NTAPIs for core operations.</li>
<li><a href="https://github.com/nbaertsch/Shrike" target="_blank">Shrike</a> - Hunting and injecting RWX 'mockingjay' DLLs in pure nim</li>
<li><a href="https://github.com/wetw0rk/Sickle" target="_blank">Sickle</a> - Payload development framework.</li>
<li><a href="https://github.com/dreadnode/burpference" target="_blank">burpference</a> - A research project to add some brrrrrr to Burp.</li>
<li><a href="https://github.com/deepinstinct/DCOMUploadExec" target="_blank">DCOMUploadExec</a> - DCOM Lateral movement POC abusing the IMsiServer interface - uploads and executes a payload remotely.</li>
<li><a href="https://github.com/n0tspam/delepwn" target="_blank">delepwn</a> - DelePwn is a security assessment tool designed to identify and demonstrate the risks associated with Google Workspace Domain-Wide Delegation (DWD) misconfigurations in Google Cloud Platform (GCP) environments. This tool helps security professionals and administrators evaluate their organization's exposure to potential DWD-based attacks.</li>
<li><a href="https://github.com/NtDallas/Svartalfheim" target="_blank">Svartalfheim</a> - Stage 0 Shellcode to Download a Remote Payload and Execute it in Memory.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/mrmtwoj/apache-vulnerability-testing" target="_blank">apache-vulnerability-testing</a> - Apache HTTP Server Vulnerability Testing Tool | PoC for CVE-2024-38472 , CVE-2024-39573 , CVE-2024-38477 , CVE-2024-38476 , CVE-2024-38475 , CVE-2024-38474 , CVE-2024-38473 , CVE-2023-38709.</li>
<li><a href="https://github.com/djackreuter/rustlualoader" target="_blank">rustlualoader</a> - Shellcode loader that executes embedded Lua from Rust.</li>
<li><a href="https://github.com/Oliver-1-1/SmmInfect" target="_blank">SmmInfect</a> - The project aims to bring the capabilities of SMM x86-64(System Management Mode) to usermode through a backdoor.</li>
<li><a href="https://github.com/cmprmsd/cinelog" target="_blank">cinelog</a> - Comprehensive logging of all terminal input and output for each session based on Asciinema and wild zsh + Python scripting.</li>
<li><a href="https://github.com/kleprevost/saladcat" target="_blank">saladcat</a> - A distributed hashcat implementation using Salad Cloud and Hashtopolis</li>
<li><a href="https://github.com/microsoft/markitdown" target="_blank">markitdown</a> - Python tool for converting files and office documents to Markdown.</li>
<li><a href="https://github.com/secureworks/pytune" target="_blank">pytune</a> - Pytune is a post-exploitation tool for enrolling a fake device into Intune with mulitple platform support.</li>
<li><a href="https://github.com/7h30th3r0n3/Evil-M5Core2" target="_blank">Evil-M5Core2</a> - Evil-M5Project is an innovative tool developed for ethical testing and exploration of WiFi networks. It's compatible with Cardputer, Atoms3, Fire, core2. You can scan, monitor, and interact with WiFi networks in a controlled environment. This project is designed for educational purposes, aiding in understanding network security and vulnerabilities.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 441 (+0)</p>
<p>Blogs monitored: 400 (+0)</p>
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
