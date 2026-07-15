Title: Last Week in Security (LWiS) - 2024-02-26
Date: 2024-02-26 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-02-26
Author: Erik
Summary: ConnectWise Vulnerabilities, open buckets (<a href="https://twitter.com/PfiatDe" target="_blank">@pfiatde</a>), SCCM takeover (<a href="https://twitter.com/garrfoster" target="_blank">@garrfoster</a>), cloud to on-prem pivot (<a href="https://twitter.com/chiragsavla94" target="_blank">@chiragsavla94</a>), WMI persistence (<a href="https://twitter.com/Gr1mmie" target="_blank">@Gr1mmie</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-02-19 to 2024-02-26.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><p>ConnectWise ScreenConnect Vulnerabilities - What is there to say about this except 🤦.</p>
<blockquote>
<ul>
<li><a href="https://www.horizon3.ai/attack-research/red-team/connectwise-screenconnect-auth-bypass-deep-dive/" target="_blank">ConnectWise ScreenConnect: Authentication Bypass Deep Dive</a></li>
<li><a href="https://github.com/rapid7/metasploit-framework/pull/18870" target="_blank">Unauthenticated RCE exploit module for ConnectWise ScreenConnect (CVE-2024-1709)</a></li>
<li><a href="https://www.huntress.com/blog/a-catastrophe-for-control-understanding-the-screenconnect-authentication-bypass" target="_blank">A Catastrophe For Control: Understanding the ScreenConnect Authentication Bypass</a></li>
</ul>
</blockquote>
</li>
<li><p><a href="https://krebsonsecurity.com/2024/02/feds-seize-lockbit-ransomware-websites-offer-decryption-tools-troll-affiliates/" target="_blank">Feds Seize LockBit Ransomware Websites, Offer Decryption Tools, Troll Affiliates</a> - LockBit is now the third major ransomware takedown. Love to see it.</p>
</li>
<li><p><a href="https://krebsonsecurity.com/2024/02/new-leak-shows-business-side-of-chinas-apt-menace/" target="_blank">New Leak Shows Business Side of China's APT Menace</a> - This is about the i-SOON leak from last week (which has been removed from GitHub...). See also: <a href="https://risky.biz/SRB67/" target="_blank">Srsly Risky Biz: China's free market espionage machine</a> and <a href="https://www.sentinelone.com/labs/unmasking-i-soon-the-leak-that-revealed-chinas-cyber-operations/" target="_blank">Unmasking I-Soon</a>.</p>
</li>
<li><p><a href="https://signal.org/blog/phone-number-privacy-usernames/" target="_blank">Keep your phone number private with Signal usernames</a>. "You will still need a phone number to register for Signal." <a href="https://simplex.chat/" target="_blank">SimpleX</a> is still the winner when it comes to fully anonymous chat/audio/video calls.</p>
</li>
<li><p><a href="https://therecord.media/avast-fine-ftc-alleged-browser-data-sales" target="_blank">FTC hits Avast with $16.5 million fine over allegations of selling users' browsing data</a> - "extremely detailed re-identifiable data". This is interesting coming from an endpoint security vendor who's business is consumer based.</p>
</li>
<li><p><a href="https://security.apple.com/blog/imessage-pq3/" target="_blank">iMessage with PQ3: The new state of the art in quantum-secure messaging at scale</a> - Apple continues to up its game with security. Do <a href="https://www.reuters.com/technology/cybersecurity/governments-spying-apple-google-users-through-push-notifications-us-senator-2023-12-06/" target="_blank">push notifications</a> next please.</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://badoption.eu/blog/2024/02/20/buckets.html" target="_blank">Cloud storage - never fails to surprise</a> - Some truly horrific finds in the world of open bucket storage.</li>
<li><a href="https://labs.watchtowr.com/double-k-o-rce-in-ibm-operation-decision-manager/" target="_blank">“To live is to fight, to fight is to live! - IBM ODM Remote Code Execution</a> - Java deserialization and JNDI Injection, classics.</li>
<li><a href="https://simonwillison.net/2023/Oct/14/multi-modal-prompt-injection/" target="_blank">Multi-modal prompt injection image attacks against GPT-4V</a> - Prompt injections come for images and soon, video.</li>
<li><a href="https://pluralistic.net/2024/02/05/cyber-dunning-kruger/" target="_blank">Pluralistic: How I got scammed (05 Feb 2024)</a> - Don't ever get too cocky and thing it can't happen to you just because you work in security. Cory literally writes books on scams. At least it wasn't <a href="https://www.thecut.com/article/amazon-scam-call-ftc-arrest-warrants.html" target="_blank">$50,000 in a shoe box</a>.</li>
<li><a href="https://posts.specterops.io/sccm-hierarchy-takeover-with-high-availability-7dcbd3696b43" target="_blank">SCCM Hierarchy Takeover with High Availability</a> - SCCM is the gift that keeps on giving.</li>
<li><a href="https://vulncheck.com/blog/zyxel-cve-2023-33012" target="_blank">re: Zyxel VPN Series Pre-auth Remote Command Execution</a> - At least this SSL VPN pre-auth RCE is "limited" to an "unusual configuration."</li>
<li><a href="https://whiteknightlabs.com/2024/02/21/pivoting-from-microsoft-cloud-to-on-premise-machines/" target="_blank">Pivoting from Microsoft Cloud to On-Premise Machines</a> - This is the opposite direction of the typical lateral movement path, but as everything goes "cloud-first" it may become the more common path.</li>
<li><a href="https://www.blackhillsinfosec.com/initial-access-operations-part-1/" target="_blank">Initial Access Operations Part 1: The Windows Endpoint Defense Technology Landscape</a> - Looking forward to this series. Initial access is certainly one of the fastest moving targets for the offsec community.</li>
<li><a href="https://blog.talosintelligence.com/google-cloud-run-abuse/" target="_blank">Astaroth, Mekotio &amp; Ousaban abusing Google Cloud Run in LATAM-focused malware campaigns</a> - Serverless infrastructure being used by TAs to deliver payloads? Ya don't say.... Great write-up by Talos. Appreciate the statistics on how often they're seeing this.</li>
<li><a href="https://dfir.ch/posts/aws_ransomware/" target="_blank">AWS Ransomware</a> - Moving ransomeware operations to cloud infrastructure. Let the cycle continue!</li>
<li><a href="https://grimmie.net/extending-and-detecting-persistassist-act-ii/" target="_blank">Extending (and Detecting) PersistAssist: Act II</a> - WMI event subscriptions are usually not as detected as more popular persistence mechanisms on Windows in my experience.</li>
<li><a href="https://decoder.cloud/2024/02/26/hello-im-your-adcs-server-and-i-want-to-authenticate-against-you/" target="_blank">Hello: I'm your ADCS server and I want to authenticate against you</a> - A fresh potato drop (<a href="https://github.com/decoder-it/ADCSCoercePotato/" target="_blank">ADCSCoercePotato</a>) and new coercion method. Mind the limitations, as DFSCoerce will likely be more applicable, but good to have options!</li>
<li><a href="https://itm4n.github.io/peap-credentials-wired-connections/" target="_blank">Extracting PEAP Credentials from Wired Network Profiles</a> - A deep dive into DPAPI and even some Ghidra reversing to extract wired PEAP credentials from Windows.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/chaudharyarjun/RepoReaper" target="_blank">RepoReaper</a> - RepoReaper is an automated tool crafted to meticulously scan and identify exposed .git repositories within specified domains and their subdomains.</li>
<li><a href="https://community.openvpn.net/openvpn/wiki/CVE-2023-7235" target="_blank">CVE-2023-7235: OpenVPN 2.x GUI privilege escalation possible if installed outside default installation path on Windows</a> - Less commonly seen than "enterprise" VPNs, OpenVPN is still prevalent.</li>
<li><a href="https://github.com/Helixo32/CrimsonEDR" target="_blank">CrimsonEDR</a> - Simulate the behavior of AV/EDR for malware development training.</li>
<li><a href="https://github.com/x90skysn3k/brutespray" target="_blank">brutespray</a> - Bruteforcing from various scanner output - Automatically attempts default creds on found services.</li>
<li><a href="https://github.com/rasta-mouse/SpawnWith" target="_blank">SpawnWith</a> - An experimental Beacon Object File (BOF) that provides an alternative to the spawnas and inject commands.</li>
<li><a href="https://github.com/olafhartong/BHCEupload" target="_blank">Bloodhound CE JSON Uploader</a> - A small go tool to upload JSON files to the BloodHound community edition API.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/xaitax/SploitScan" target="_blank">SploitScan</a> - is a sophisticated cybersecurity utility designed to provide detailed information on vulnerabilities and associated proof-of-concept (PoC) exploits.</li>
<li><a href="https://github.com/GreenmaskIO/greenmask" target="_blank">greenmask</a> - PostgreSQL dump and obfuscation tool.</li>
<li><a href="https://adamobeng.com/wddbfs-mount-a-sqlite-database-as-a-filesystem/" target="_blank">wddbfs</a> - Mount a sqlite database as a filesystem.</li>
<li><a href="https://github.com/mtth-bfft/adeleg" target="_blank">ADeleg</a> -  Active Directory delegation management tool</li>
<li><a href="https://scorpiosoftware.net/2024/02/20/projected-file-system/" target="_blank">Projected File System</a> - Solid write up on the ProjFS provider which provides various types of data to access with I/O APIs.</li>
<li><a href="https://github.com/soteria-security/365Inspect" target="_blank">365Inspect</a> -  A PowerShell script that automates the security assessment of Microsoft Office 365 environments.</li>
<li><a href="https://github.com/jfjallid/go-secdump" target="_blank">go-secdump</a> -  Tool to remotely dump secrets from the Windows registry</li>
<li><a href="https://github.com/Moopinger/smugglefuzz" target="_blank">SmuggleFuzz</a> -  A customizable and rapid HTTP downgrade smuggling scanner written in Go.</li>
<li><a href="https://github.com/SureStacks/AzureAssess" target="_blank">AzureAssess</a> - "...gain a comprehensive understanding of your Azure resources and their security configurations."</li>
<li><a href="https://github.com/Stratus-Security/Subdominator" target="_blank">Subdominator</a> - "The Internets #1 Subdomain Takeover Tool"</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 368 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
