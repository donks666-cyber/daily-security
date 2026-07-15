Title: Last Week in Security (LWiS) - 2025-04-07
Date: 2025-04-07 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-04-07
Author: Erik
Summary: 2 weeks worth of news, techniques, tools and exploits!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-03-24 to 2025-04-07.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Celebrate the 'Month of Azure Red Teaming' with Altered Security</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Start your Azure Red Team training with us! Altered Security offers multiple Red Team courses with affordable and enterprise-like hands-on labs. Each course comes with an industry-recognized certification. We are the creators of the popular Azure Red Team certifications - CARTP and CARTE. Our courses and labs are designed by experts who have more than a decade's experience of training and speaking at Black Hat USA, DEF CON and other respected conferences. Join more than 40K professionals from 130+ countries.</p>
<p>We are celebrating April 2025 as 'Month of Azure Red Teaming'. Enjoy 20% OFF on all Azure courses (on-demand, bootcamps and learning path) using <strong>'AZURE20OFF'</strong> from April 2 to April 11 2025. <strong><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://blog.cloudflare.com/open-sourcing-openpubkey-ssh-opkssh-integrating-single-sign-on-with-ssh/" target="_blank">Open-sourcing OpenPubkey SSH (OPKSSH): integrating single sign-on with SSH</a> - SSO enabled SSH is now as easy as two lines in your sshd configuration file. <a href="https://github.com/openpubkey/opkssh/" target="_blank">opkssh</a> - opkssh (OpenPubkey SSH) is the open source tool compatible with Google, Microsoft/Azure, and Gitlab OpenID Providers</li>
<li><a href="https://security.googleblog.com/2025/04/google-launches-sec-gemini-v1-new.html" target="_blank">Google announces Sec-Gemini v1, a new experimental cybersecurity model</a> - The second cybersecurty focused model from a big company after Tred Micro's <a href="https://newsroom.trendmicro.com/2025-03-19-Trend-Micro-to-Open-source-AI-Model-and-Agent-to-Drive-the-Future-of-Agentic-Cybersecurity" target="_blank">Cybertron</a> dropped last month.</li>
<li><a href="https://www.troyhunt.com/a-sneaky-phish-just-grabbed-my-mailchimp-mailing-list/" target="_blank">A Sneaky Phish Just Grabbed my Mailchimp Mailing List</a> - A good reminder that it can happen to <em>anyone</em>. Don't get complacent, and put in technical controls to prevent yourself from attacks (hardware multi-factor).</li>
<li><a href="https://citizenlab.ca/2025/03/a-first-look-at-paragons-proliferating-spyware-operations/" target="_blank">Virtue or Vice? A First Look at Paragon’s Proliferating Spyware Operations</a> - More great research out of Citizen Lab. 0days for messaging apps exist and are being used to target a variety of targets.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://medium.com/@adan.alvarez/github-actions-and-the-pinning-problem-what-100-security-projects-reveal-54a3a9dcc902" target="_blank">GitHub Actions and the Pinning Problem: What 100 Security Projects Reveal</a> - Github project dependencies and transitive dependencies are one of the highest risks to the internet right now. This research should serve as an eye opener of this issue. TLDR - Pin your github actions and minimize third-parties that do not.</li>
<li><a href="https://xbz0n.sh/blog/social-engineering-redteam" target="_blank">Social Engineering in Red Team Operations: Technical Setup and Tools</a> - A technical overview on modern phishing infrastructure and considerations. Tactical knowledge of evasion techniques along the tools you can use are also provided. Good write up.</li>
<li><a href="https://www.wiz.io/blog/ingress-nginx-kubernetes-vulnerabilities" target="_blank">IngressNightmare: CVE-2025-1974 - 9.8 Critical Unauthenticated Remote Code Execution Vulnerabilities in Ingress NGINX</a> - A critical unauthenticated remote code execution vulnerabilities in Ingress NGINX Controller for Kubernetes that affect approximately 43% of cloud environments.</li>
<li><a href="https://trustedsec.com/blog/mcp-an-introduction-to-agentic-op-support" target="_blank">MCP: An Introduction to Agentic Op Support</a> - A good introduction to what a lot of infosec is talking about these days: how to implement AI agents that leverage Large Language Models (LLMs) alongside common tools to autonomously achieve goals (offensive and defensive)</li>
<li><a href="https://tx0actical.github.io/posts/ss-bypass/" target="_blank">Bypassing SmartScreen (Domain-Wide) using DNS Sinkholing</a> - While not a commonly acceptable configuration change in client environments during pentests/red teams, this post warrants discussion regarding how adversaries might impair the defensive capabilities of your environment once they gain privileges to do so. How can we emulate/simulation this at scale? What happens when an attacker escalates privileges in your network and deploys an applocker policy to kill your EDR processes?</li>
<li><a href="https://starlabs.sg/blog/2025/03-cimfs-crashing-in-memory-finding-system-kernel-edition/" target="_blank">CimFS: Crashing in memory, Finding SYSTEM (Kernel Edition)</a> - The bugs are over a year old, but the techniques are timeless.</li>
<li><a href="https://posts.specterops.io/an-operators-guide-to-device-joined-hosts-and-the-prt-cookie-bcd0db2812c4" target="_blank">An Operator’s Guide to Device-Joined Hosts and the PRT Cookie</a> - How an operator can perform reconnaissance prior to making an Entra ID token request and how tokens can be used once they are obtained.</li>
<li><a href="https://blog.quarkslab.com/ccleaner_lpe_macos.html" target="_blank">CCleaner Local Privilege Escalation Vulnerability on macOS</a> - Weak protections on inter-process communication lead to privilege escalation in an old version of CCleaner.</li>
<li><a href="https://labs.watchtowr.com/xss-to-rce-by-abusing-custom-file-handlers-kentico-xperience-cms-cve-2025-2748/" target="_blank">XSS To RCE By Abusing Custom File Handlers - Kentico Xperience CMS (CVE-2025-2748)</a> - Always fun to see cross site scripting (XSS) converted to full on remote code execution (RCE).</li>
<li><a href="https://eshard.com/posts/emulating-ios-14-with-qemu" target="_blank">Emulating an iPhone in QEMU</a> - A journey to build your own <a href="https://www.corellium.com/" target="_blank">Corellium</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/boku7/Loki" target="_blank">Loki</a> - 🧙‍♂️ Node JS C2 for backdooring vulnerable Electron applications.</li>
<li><a href="https://github.com/LaurieWired/GhidraMCP/" target="_blank">GhidraMCP</a> - MCP Server for Ghidra.</li>
<li><a href="https://github.com/MorDavid/BloodHound-MCP-AI" target="_blank">BloodHound-MCP-AI</a> - BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.</li>
<li><a href="https://github.com/atomicchonk/roadrecon_mcp_server" target="_blank">roadrecon_mcp_server</a> - Claude MCP server to perform analysis on ROADrecon data.</li>
<li><a href="https://github.com/Friends-Security/sharefiltrator" target="_blank">sharefiltrator</a> - Tool for enumeration &amp; bulk download of sensitive files found in SharePoint environments.</li>
<li><a href="https://github.com/AmitMoshel1/PatchGuardEncryptorDriver" target="_blank">PatchGuardEncryptorDriver</a> - An improved version of Patch Guard that I implemented, that includes integrity checks and other protection mechanisms I added.</li>
<li><a href="https://github.com/azurekid/blackcat" target="_blank">blackcat</a> - BlackCat is a PowerShell module designed to validate the security of Microsoft Azure. It provides a set of functions to identify potential security holes.</li>
<li><a href="https://github.com/dmcxblue/AzureFunctionRedirector" target="_blank">AzureFunctionRedirector</a> - Code and tutorial on using Azure Functions as your redirector. Careful, Microsoft has been known to close subscriptions if they detect nefarious use.</li>
<li><a href="https://github.com/EricEsquivel/Inline-EA" target="_blank">Inline-EA</a> - Cobalt Strike BOF for evasive .NET assembly execution.</li>
<li><a href="https://github.com/thisis0xczar/FrogPost" target="_blank">FrogPost</a> - postMessage Security Testing Tool.</li>
<li><a href="https://github.com/ricardojoserf/NativeNtdllRemap" target="_blank">NativeNtdllRemap</a> - Remap ntdll.dll using only NTAPI functions with a suspended process.</li>
<li><a href="https://github.com/ricardojoserf/NativeTokenImpersonate" target="_blank">NativeTokenImpersonate</a> - Impersonate Tokens using only NTAPI functions.</li>
<li><a href="https://github.com/Slowerzs/KeyJumper" target="_blank">KeyJumper</a> - This project demonstrates arbitrary kernel code execution on a Windows 11 system with kCET enabled, to create a keylogging tool by mapping kernel memory to userland. You can find a blogpost about it <a href="https://blog.slowerzs.net/posts/keyjumper/" target="_blank">here</a> for more information.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/mordavid/dcsynchound" target="_blank">DCSyncHound</a> - This script analyzes the DCSync output file from several tools (such as Mimikatz, Secretsdump and SharpKatz).</li>
<li><a href="https://github.com/vari-sh/RedTeamGrimoire" target="_blank">RedTeamGrimoire</a> - 🔥📜 Forbidden collection of Red Team sorcery 📜🔥.</li>
<li><a href="https://github.com/nullenc0de/Internal_Pentest" target="_blank">Internal_Pentest</a> - Scripts that automate portions of pentests.</li>
<li><a href="https://github.com/gildas-lormeau/SingleFile" target="_blank">SingleFile</a> - Web Extension for saving a faithful copy of a complete web page in a single HTML file.</li>
<li><a href="https://github.com/adanalvarez/MyScripts/tree/main/GitHub" target="_blank">GitHub Actions Dependency Scanner</a> - Python script that recursively scans a GitHub repository’s workflows to uncover unpinned or unpinnable dependencies in your GitHub Actions usage.</li>
<li><a href="https://posts.specterops.io/getting-the-most-value-out-of-the-oscp-the-pen-200-labs-81ea65f29c0e" target="_blank">Getting the Most Value Out of the OSCP: The PEN-200 Labs</a> - So cool to see a whole section on <a href="https://ludus.cloud/" target="_blank">Ludus</a> in this post!</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 446 (+0)</p>
<p>Blogs monitored: 407 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
