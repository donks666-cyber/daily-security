Title: Last Week in Security (LWiS) - 2023-11-13
Date: 2023-11-13 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-11-13
Author: Erik
Summary: Initial access and Bobber (<a href="https://twitter.com/Flangvik" target="_blank">@Flangvik</a>), Slack 🍪 fun (<a href="https://twitter.com/Tw1sm" target="_blank">@Tw1sm</a>), attacking EDR (<a href="https://twitter.com/dottor_morte" target="_blank">@dottor_morte</a>), finding hard-coded secrets (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-11-06 to 2023-11-13.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blogs.windows.com/windows-insider/2023/11/08/announcing-windows-11-insider-preview-build-25992-canary-channel/" target="_blank">Server Message Block (SMB) protocol changes</a> - New firewall rules, SMB NTLM blocking exception list, alternative SMB ports, and more!</li>
<li><a href="https://go.recordedfuture.com/hubfs/reports/cta-2023-1107.pdf" target="_blank">[PDF] Charting China's Climb as a Leading Global Cyber Power</a> - China has lots of 0day's attributed to it and the willingness to use them at scale.</li>
<li><a href="https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/11/09055246/Modern-Asian-APT-groups-TTPs_report_eng.pdf" target="_blank">[PDF] Kaspersky Threat Intelligence - Modern Asian APT Groups</a> - Recorded future releases an 18 page report on chinese APTs. Kaspersky says, hold my beer (370 pages) 😂.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://research.nccgroup.com/2023/11/07/post-exploiting-a-compromised-etcd-full-control-over-the-cluster-and-its-nodes/" target="_blank">Post-exploiting a compromised etcd - Full control over the cluster and its nodes</a> - This paper aims to demonstrate that a compromised etcd is the most critical element within a k8s cluster, as it is not subject to role restrictions or the AdmissionControllers.</li>
<li><a href="https://frycos.github.io/vulns4free/2023/11/07/hacking-like-hollywood.html" target="_blank">Hacking Like Hollywood With Hard-Coded Secrets</a> - A good write up on firmware blob to authentication bypass on a Ganz Security Solutions device.</li>
<li><a href="https://riccardoancarani.github.io/2023-11-07-attacking-an-edr-part-3/" target="_blank">Attacking an EDR - Part 3</a> - The last post for the "Attacking an EDR" series.</li>
<li><a href="https://trustedsec.com/blog/the-triforce-of-initial-access" target="_blank">The Triforce of Initial Access</a> - Initial access TTPs based on phishing + gathering loot automatically. Check out Bobber in the tools section.</li>
<li><a href="https://posts.specterops.io/abusing-slack-for-offensive-operations-part-2-19fef38cc967" target="_blank">Abusing Slack for Offensive Operations: Part 2</a> - "Slack has followed the cookie storage blueprint used by browsers, like Google Chrome, making existing tooling and techniques adaptable for Slack exploitation." Easy to dump from memory on Windows, a bit more complicated on macOS.</li>
<li><a href="https://haxx.in/posts/hacking-canon-imageclass/" target="_blank">Hacking the Canon imageCLASS MF742Cdw/MF743Cdw (again)</a> - Stack-based buffer overflow in the Canon firmware. Cool writeup.</li>
<li><a href="https://research.checkpoint.com/2023/abusing-microsoft-access-linked-table-feature-to-perform-ntlm-forced-authentication-attacks/" target="_blank">Abusing Microsoft Access “Linked Table” Feature to Perform NTLM Forced Authentication Attacks</a> - The Microsoft Access "linking to remote SQL Server tables" feature that can automatically leak Windows user NTLM hashes via port 80. While most NTLM leaks are via port 445, this one is much more likely to make it out of the corporate firewall.</li>
<li><a href="https://www.angelystor.com/posts/using_ssl_certs_for_payloads/" target="_blank">Using SSL Certificates for Red Team Payloads</a> - Interesting idea. "I found out that you could embed x.509 extensions into a certificate in the form of OIDs". You can use these x.509 extensions to inject your payload.</li>
<li><a href="https://research.nccgroup.com/2023/11/10/demystifying-cobalt-strikes-make_token-command/" target="_blank">Demystifying Cobalt Strike's “make_token” Command</a> - Nice little deep dive into make_token.</li>
<li><a href="https://www.synacktiv.com/en/publications/systemd-hardening-made-easy-with-shh" target="_blank">systemd hardening made easy with SHH</a>. Could be used to audit for weak services 😉.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/projectdiscovery/nuclei-ai-extension" target="_blank">Nuclei AI - Browser Extension</a> - Browser Extension for Rapid Nuclei Template Generation (requires a cloud account).</li>
<li><a href="https://github.com/lkarlslund/fastsync" target="_blank">fastsync</a> - Fast synchronization across networks using speedy compression, lots of parallelization and fast hashmaps for keeping track of things internally.</li>
<li><a href="https://github.com/yoda66/MAAS" target="_blank">MAAS</a> -  Malware As A Service. This project describes a DevOps approach which leverages the CI/CD capabilities of gitlab to build a malware artifact generation pipeline.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/SharpVeeamDecryptor" target="_blank">SharpVeeamDecryptor</a> -  Decrypt Veeam database passwords.</li>
<li><a href="https://github.com/ForceFledgling/proxyhub" target="_blank">proxyhub</a> -  An advanced [Finder | Checker | Server] tool for proxy servers, supporting both HTTP(S) and SOCKS protocols. 🎭</li>
<li><a href="https://github.com/Flangvik/Bobber" target="_blank">Bobber</a> - Evilginx database monitoring with exfiltration automation.</li>
<li><a href="https://github.com/cpu0x00/SharpReflectivePEInjection" target="_blank">SharpReflectivePEInjection</a> - Reflectively load and execute PEs locally and remotely bypassing EDR hooks</li>
<li><a href="https://github.com/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation" target="_blank">CVE-2023-32629 &amp; CVE-2023-2640: Privilege escalation</a> -  Ubuntu Privilege Escalation bash one-liner</li>
<li><a href="https://github.com/Mr-Un1k0d3r/.NetConfigLoader" target="_blank">.NetConfigLoader</a> - List of .Net application signed by Microsoft that can be used to load a dll via a .config file (AppDomain Hijacking). Ideal for EDR/AV evasion and execution policy bypass.</li>
<li><a href="https://github.com/EspressoCake/Bloodhound_Community_Docker" target="_blank">Bloodhound_Community_Docker</a> - Generator of docker-compose file to allow secure configurations and multi-deployment strategy.</li>
<li><a href="https://github.com/Aqua-Nautilus/CVE-Half-Day-Watcher" target="_blank">CVE-Half-Day-Watcher</a> - a security tool designed to highlight the risk of early exposure of Common Vulnerabilities and Exposures (CVEs) in the public domain.</li>
<li><a href="https://github.com/parzel/GoSleepyCrypt" target="_blank">GoSleepyCrypt</a> - In-memory sleep encryption and heap encryption for Go applications through a shellcode function.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://notcve.org/about.html" target="_blank">the !CVE Program</a> - The mission of the !CVE Program is to provide a common space for cybersecurity !vulnerabilities that are not acknowledged by vendors but still are serious security issues.</li>
<li><a href="https://github.com/hakluke/hakrevdns" target="_blank">hakrevdns</a> -  Small, fast tool for performing reverse DNS lookups en masse.</li>
<li><a href="https://github.com/0xe7/RoastInTheMiddle" target="_blank">RoastInTheMiddle</a>- Roast in the Middle is a rough proof of concept (not attack-ready) that implements a man-in-the-middle ARP spoof to intercept AS-REQ's to modify and replay to perform a Kerberoast or Sessionroast attack.</li>
<li><a href="https://portswigger.net/blog/tic-tac-toe-in-html" target="_blank">Implementing Tic Tac Toe with 170mb of HTML - no JS or CSS</a> 🤯</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 359 (+0)</p>
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
