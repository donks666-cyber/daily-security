Title: Last Week in Security (LWiS) - 2024-11-18
Date: 2024-11-18 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-11-18
Author: Erik
Summary: Arc browser RCE (<a href="https://x.com/RenwaX23" target="_blank">@RenwaX23</a>), more Fortinet woes (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>), PowerHuntShares v2 (<a href="https://x.com/_nullbind" target="_blank">@_nullbind</a>), make_token_cert (<a href="https://x.com/freefirex2" target="_blank">@freefirex2</a>), BOFs without DFR (<a href="https://x.com/netbiosX" target="_blank">@netbiosX</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-11-12 to 2024-11-18.</p>
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
<li><a href="https://security.paloaltonetworks.com/CVE-2024-9474" target="_blank">CVE-2024-9474 PAN-OS: Privilege Escalation (PE) Vulnerability in the Web Management Interface</a> - The alert from last week is a full blown CVE this week.</li>
<li><a href="https://blog.eclecticiq.com/inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers" target="_blank">Inside Intelligence Center: Financially Motivated Chinese Threat Actor SilkSpecter Targeting Black Friday Shoppers</a> - Double check the URL before committing to that deal!</li>
<li><a href="https://www.auswaertiges-amt.de/en/newsroom/news/-/2685132" target="_blank">Joint statement by the Foreign Ministers of Finland and Germany on the severed undersea cable in the Baltic Sea</a> - A reminder that the digital world is not immune to physical attacks. "The fact that such an incident immediately raises suspicions of intentional damage speaks volumes about the volatility of our times."</li>
<li><a href="https://www.theverge.com/2024/11/18/24300033/doj-google-monopoly-remedies-search-chrome-android-ai" target="_blank">US lawyers will reportedly try to force Google to sell Chrome and unbundle Android</a> - This feels very <a href="https://en.wikipedia.org/wiki/United_States_v._Microsoft_Corp." target="_blank">United States of America v. Microsoft Corporation</a> (Feb-Jun 2001). It would be ironic if this ends up killing Firefox, as Google is their only <a href="https://fortune.com/2024/08/05/mozilla-firefox-biggest-potential-loser-google-antitrust-search-ruling/" target="_blank">real source of income</a> ($510 of $593 million in revenue in 2022 was from Google search payments).</li>
<li><a href="https://www.justice.gov/opa/pr/phobos-ransomware-administrator-extradited-south-korea-face-cybercrime-charges" target="_blank">Phobos Ransomware Administrator Extradited from South Korea to Face Cybercrime Charges</a> - The Justice Department unsealed criminal charges against Evgenii Ptitsyn, 42, a Russian national, for allegedly administering the sale, distribution, and operation of Phobos ransomware.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html?m=1" target="_blank">Reverse Engineering iOS 18 Inactivity Reboot</a> - Last week we reported that iOS 18.1 devices were rebooting when left idle. This week we have some good data on how this inactivity reboot works. TLDR: The secure enclave tracks time since last unlock, and if it's been more than 3 days, it will reboot the device.</li>
<li><a href="https://labs.watchtowr.com/hop-skip-fortijump-fortijumphigher-cve-2024-23113-cve-2024-47575/" target="_blank">Hop-Skip-FortiJump-FortiJump-Higher - Fortinet FortiManager CVE-2024-47575</a> - "It’s been a tricky time for Fortinet (and their customers) lately - arguably, even more so than usual. Adding to the steady flow of vulnerabilities in appliances recently was a nasty CVSS 9.8 vulnerability in FortiManager, their tool for central management of FortiGate appliances." Once Sina Kheirkhah (<a href="https://x.com/SinSinology" target="_blank">@SinSinology</a>) locks onto your products, you better hope you're security posture is up to par. Fortinet has been on the receiving end of a lot of attention/exploitation lately.</li>
<li><a href="https://medium.com/@renwa/arc-browser-uxss-local-file-read-arbitrary-file-creation-and-path-traversal-to-rce-b439f2a299d1" target="_blank">Arc Browser UXSS, Local File Read, Arbitrary File Creation and Path Traversal to RCE</a> - Looks like some unused functionality in Arc shipped and could be used for remote code execution (RCE).</li>
<li><a href="https://perception-point.io/blog/phishing-by-design-two-step-attacks-using-microsoft-visio-files/" target="_blank">Phishing by Design: Two-Step Attacks Using Microsoft Visio Files</a> - As defenses get better, threats evolve to use trusted sites and multi-step execution. In this case the often overlooked Microsoft Visio (installed as part of the Office suite usually) is used to deliver a two-step phishing attack.</li>
<li><a href="https://www.clearskysec.com/wp-content/uploads/2024/11/Zero-day-cve-2024-4351-report.pdf" target="_blank">[PDF] New Zero-Day Vulnerability Detected: CVE-2024-43451</a> - This is a unique Windows initial access vulnerability that is being actively exploited, as it only requires a single right click, deleting the file, or dragging the file to another folder to execute.</li>
<li><a href="https://unit42.paloaltonetworks.com/privilege-escalation-llm-model-exfil-vertex-ai/" target="_blank">ModeLeak: Privilege Escalation to LLM Model Exfiltration in Vertex AI</a> - While AI is the current buzzword, it's not immune to security issues. This post details how running a malicious model in Vertex AI could compromise the entire AI environment.</li>
<li><a href="https://www.netspi.com/blog/technical-blog/network-pentesting/powerhuntshares-2-0-release/" target="_blank">Hunting SMB Shares, Again! Charts, Graphs, Passwords &amp; LLM Magic for PowerHuntShares 2.0</a> - Like it or not, credentials on SMB shares are a common win for attackers. This tool's v2 update is a great way to automate finding shares configured with excessive privileges, including interesting ile discovery, automated secret extraction, risk scoring, and of course, LLM-based share fingerprinting.</li>
<li><a href="https://secureyourit.co.uk/wp/2024/11/07/local-admin-disconnected-rdp-sessions/" target="_blank">Local Admin + Disconnected RDP Sessions</a> - A demo to show the dangers of disconnected RDP sessions by privileged accounts (Domain Admins). If the computer they are disconnected from is compromised (Local admin), the domain admin session can be used by the attacker.</li>
<li><a href="https://www.akamai.com/blog/security-research/the-definitive-guide-to-linux-process-injection" target="_blank">The Definitive Guide to Linux Process Injection</a> - While Windows gets most of the attention, Linux has lots of techniques for process injection. This is a great overview post that showcases many of them. Note that the code is actually in the repo <a href="https://github.com/akamai/Linux-Process-Injection" target="_blank">Linux-Process-Injection</a>, not the one linked throughout the post (github.com/guardicode) that 404s.</li>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/ai-enhancing-your-adversarial-emulation/?linkId=11719807" target="_blank">Pirates in the Data Sea: AI Enhancing Your Adversarial Emulation</a> - Many of the use cases presented in the article feel a little basic (i.e. could be implemented in a short script), but this is only the beginning...</li>
<li><a href="https://medium.com/@nickvourd/local-admin-in-less-than-60-seconds-part-1-e2a0c0102b99" target="_blank">Local Admin In Less Than 60 Seconds (Part 1)</a> - By default, Domain Controllers have an insecure LDAP signing and channel binding configuration, this does change in server 2025 but you still have time to abuse this.</li>
<li><a href="https://blog.cybershenanigans.space/posts/writing-bofs-without-dfr/" target="_blank">Writing Beacon Object Files Without DFR</a> - Some good tips on how to clean up BOF code to make it more general and thus easier to test outside of a C2.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/scrt/KexecDDPlus" target="_blank">KexecDDPlus</a> - is a Windows tool that relies on Server Silos to access the KsecDD driver directly, without having to inject code into LSASS. This capability therefore allows it to operate even on systems on which LSA Protection is enabled. For more details see <a href="https://blog.scrt.ch/2024/11/11/exploiting-ksecdd-through-server-silos/" target="_blank">Exploiting KsecDD through Server Silos</a> .</li>
<li><a href="https://github.com/scrt/tpm_sniffing_pin" target="_blank">tpm_sniffing_pin</a> is a simple Python PoC to retrieve the VMK through TPM Sniffing by knowing the user's PIN.</li>
<li><a href="https://github.com/nettitude/TokenCert" target="_blank">TokenCert</a> is a C# tool that will create a network token (LogonType 9) using a provided certificate via PKINIT. This way, we can have a make-token functionality using certificates instead of passwords.</li>
<li><a href="https://github.com/trustedsec/CS-Remote-OPs-BOF/tree/bc0cdd7997ebbf37a1cfee26be97eb3faa06ab50/src/Remote/make_token_cert" target="_blank">make_token_cert</a> - A new BOF from Trusted Sec to authenticate using only a .pfx file.</li>
<li><a href="https://github.com/LuemmelSec/Moodle-Scanner" target="_blank">Moodle-Scanner</a> - A Moodle Scanner to check for the version and associated vulns.</li>
<li><a href="https://github.com/MzHmO/Exploit-Street" target="_blank">Exploit-Street</a> - Complete list of LPE exploits for Windows (starting from 2023).</li>
<li><a href="https://github.com/chryzsh/linux_bof" target="_blank">linux_bof</a> - ELF BOFs! This fork has a few more examples than the parent repo from Outflank.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Dor00tkit/CVE-2024-30090" target="_blank">CVE-2024-30090</a> - Microsoft Streaming Service Elevation of Privilege Vulnerability PoC.</li>
<li><a href="https://github.com/charmbracelet/sequin" target="_blank">sequin</a> is a small utility that can help you debug your CLIs and TUIs. It's also great for describing escape sequences you might not understand, and exploring what TUIs are doing under the hood.</li>
<li><a href="https://github.com/jesusprubio/up" target="_blank">up</a> - Troubleshoot problems with your Internet connection based on different protocols and well-known public servers.</li>
<li><a href="https://github.com/awslabs/multi-agent-orchestrator" target="_blank">multi-agent-orchestrator</a> - Flexible and powerful framework for managing multiple AI agents and handling complex conversations.</li>
<li><a href="https://github.com/woodruffw/zizmor" target="_blank">zizmor</a> - A tool for finding security issues in GitHub Actions setups.</li>
<li><a href="https://github.com/Escape-Technologies/graphinder" target="_blank">graphinder</a> - 🕸️ Blazing fast GraphQL endpoints finder using subdomain enumeration, scripts analysis and bruteforce. 🕸️.</li>
<li><a href="https://github.com/Abdenasser/neohtop" target="_blank">neohtop</a> - 💪🏻 htop on steroids.</li>
<li><a href="https://gitlab-com.gitlab.io/gl-security/security-tech-notes/red-team-tech-notes/okta-verify-bypass-sept-2024/" target="_blank">Tech Note - Okta Verify Bypass</a> - Similar to Adam Chesters recent Okta research, the Gitlab red team documents some of their experience with Okta.</li>
<li><a href="https://github.com/ajm4n/TermHound" target="_blank">TermHound</a> - A comprehensive Active Directory security analysis tool that integrates with Neo4j to detect vulnerabilities, analyze attack paths, and identify security misconfigurations.</li>
<li><a href="https://labs.leaningtech.com/blog/webvm-20" target="_blank">WebVM 2.0: A complete Linux Desktop Environment in the browser via WebAssembly</a> - WebVM is a full Linux environment running in the browser, client-side. It has support for persistent data storage, networking, Xorg, and a complete desktop environment.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 441 (+2)</p>
<p>Blogs monitored: 397 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
