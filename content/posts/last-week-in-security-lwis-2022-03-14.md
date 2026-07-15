Title: Last Week in Security (LWiS) - 2022-03-14
Date: 2022-03-14 23:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-03-14
Author: Erik
Summary: Embedded reversing (<a href="https://twitter.com/zi0black" target="_blank">@zi0Black</a>), SQL injection despite prepared statements (<a href="https://twitter.com/Dooflin5" target="_blank">@Dooflin5</a>), AutoWarp Azure token leak (<a href="https://twitter.com/Yanir_" target="_blank">@Yanir_</a>), Viscosity DPAPI defeat (<a href="https://twitter.com/checkymander" target="_blank">@checkymander</a>), password tricks without mimikatz (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), Chakra exploitation (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), rethinking phishing assessments (<a href="https://twitter.com/matterpreter" target="_blank">@matterpreter</a>), and more!

<aside class="m-note m-success">
<h3>2 Years of LWiS</h3>
<p>This is the 104th issue published! If you find LWiS useful, please share it!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-02-28 to 2022-03-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://dirtypipe.cm4all.com/" target="_blank">The Dirty Pipe Vulnerability</a>. Linux 5.8+ was vulnerable to a DirtyCOW-esq bug that allows overwriting data in arbitrary read-only files. It can also be used as a <a href="https://twitter.com/bestswngs/status/1501424056364859392" target="_blank">Docker container escape</a>. PoCs available here: <a href="https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits" target="_blank">CVE-2022-0847-DirtyPipe-Exploits</a>.</li>
<li><a href="https://www.veeam.com/kb4288?ad=in-text-link" target="_blank">Multiple vulnerabilities (CVE-2022-26500, CVE-2022-26501) in Veeam Backup &amp; Replication allow executing malicious code remotely without authentication</a>. Veeam is a very popular virtual machine backup vendor. While hopefully not publically exposed, once inside these vulnerabilities could prove very useful to a red team.</li>
<li><a href="https://blog.cloudflare.com/icloud-private-relay/" target="_blank">iCloud Private Relay: information for Cloudflare customers</a>. An interesting post about Cloudflare's role in "Private Relay." The part that stuck out to me was: '"Private Relay is designed to ensure only valid Apple devices and accounts in good standing are allowed to use the service. Websites that use IP addresses to enforce fraud prevention and anti-abuse measures can trust that connections through Private Relay have been validated at the account and device level by Apple." Because of these advanced device and user authorization steps, you might consider allowlisting Private Relay IP addresses explicitly.' Are burner Apple IDs and Private Relay a quick way to bypass anti-fraud controls?</li>
<li><a href="https://www.cobaltstrike.com/blog/cobalt-strike-roadmap-update/" target="_blank">Cobalt Strike Roadmap Update</a>. Cobalt Strike has continued to grow after the acquisition by HelpSystems, and this post promises to continue that growth. As the most popular adversary simulation tool on the market, Cobalt Strike is the standard that all other C2's and agents are compared to.</li>
<li><a href="https://www.theregister.com/2022/03/05/nvidia_stolen_certificate/" target="_blank">Leaked stolen Nvidia key can sign Windows malware</a>. The Nvidia data has been leaked, and the perpetrators have moved on to <a href="https://www.techspot.com/news/93663-nvidia-hackers-leak-190gb-sensitive-data-samsung.html" target="_blank">Samsung</a>.</li>
<li><a href="https://news.ubisoft.com/en-gb/article/3tSsBh25mhHhlbGSy1xbRw/ubisoft-cyber-security-incident-update" target="_blank">Ubisoft Cyber Security Incident Update</a>. Lapsus$ is a likely culprit. Unconfirmed, but Lapsus$ shared the link on their Telegram with a smirk emoji - that's attribution in 2022 right?.</li>
<li><a href="https://krebsonsecurity.com/2022/03/conti-ransomware-group-diaries-part-i-evasion/" target="_blank">Conti Ransomware Group Diaries</a>. Krebs does a great job digging into the Conti chat log leaks. The Conti group was well financed, and run much like you'd expect a mid size business to run - with all the infighting and drama that entails.</li>
<li><a href="https://blog.shodan.io/introducing-the-internetdb-api/" target="_blank">Introducing the InternetDB API</a>. Free, and no API key required. Information isn't super detailed, but you get open ports, Common Platform Enumeration (CPE), hostnames, tags, and vulnerabilities with a single request.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.shielder.it/blog/2022/03/reversing-embedded-device-bootloader-u-boot-p.1/" target="_blank">Reversing embedded device bootloader (U-Boot) - p.1</a>. Encrypted kernel images for IoT devices can be a pain, and when they use custom encryption it can be even worse. This post shows the struggle of finding the decryption routine for an ARM powered IoT device that boots with U-boot.</li>
<li><a href="https://maxwelldulin.com/BlogPost?post=9185867776" target="_blank">Finding an Authorization Bypass on my Own Website</a>. If you think prepared SQL statements protect you from all SQL injections, this post is for you. Edge cases can be crazy, and lead to auth bypasses!</li>
<li><a href="https://www.hexacorn.com/blog/2022/03/04/good-file-what-is-it-good-for-part-1/" target="_blank">Good file… (What is it good for) Part 1</a>. What PDB paths and GUIDs do your tools use? Maybe time to do some research into good files on your own and reuse "good" elements in your tooling.</li>
<li><a href="https://thalpius.com/2022/03/08/microsoft-defender-for-office-365-identification/" target="_blank">Microsoft Defender for Office 365 Identification</a>. A quick and easy check to see if an organization is using the paid Defender for O365 by sending a single email.</li>
<li><a href="https://msrc-blog.microsoft.com/2022/03/07/13943/" target="_blank">Disclosure of Vulnerability in Azure Automation Managed Identity Tokens</a>. This is the corporate response, but the <a href="https://twitter.com/Yanir_/status/1500863874412724229" target="_blank">simple truth</a> is much more frightening.</li>
<li><a href="https://blog.checkymander.com/red%20team/viscosity/decrypt-viscosity-passwords/" target="_blank">Decrypting Viscosity Passwords</a>. The DPAPI protected credentials for the VPN software are protected with a custom salt that causes common automated DPAPI decryption tools to fail. The use of WinDBG to find the salt is generally applicable and a good trick to stash in your toolbox.</li>
<li><a href="https://www.n00py.io/2022/03/manipulating-user-passwords-without-mimikatz/" target="_blank">Manipulating User Passwords Without Mimikatz</a>. Some excellent attack options that avoid well signatured binaries/tools in this post. The ShadowCredentials trick is a sneaky favorite.</li>
<li><a href="https://connormcgarr.github.io/type-confusion-part-1/" target="_blank">Exploit Development: Browser Exploitation on Windows - CVE-2019-0567, A Microsoft Edge Type Confusion Vulnerability (Part 1)</a>. If you're even remotely curious about browser exploitation, take an hour and read this post. Connor never disapoints and his blog has more knowledge packed into it than 700 level SANS courses.</li>
<li><a href="https://www.synacktiv.com/en/publications/finding-gadgets-like-its-2022.html" target="_blank">Finding gadgets like it's 2022</a>. CodeQL strikes again, this time in a unqiue application - to find gadgets for Java exploits! You have to have the source code of the target app and be able to compile it, but otherwise, this is a neat new technique to find gadget chains.</li>
<li><a href="https://posts.specterops.io/revisiting-phishing-simulations-94d9cd460934" target="_blank">Revisiting Phishing Simulations</a>. I once had a boss tell me "we never will do assumed breach." I hope he reads this. "Given enough time and resources, a motivated and reasonably sophisticated threat actor will eventually gain access to your environment." Purple teams are the way of the future for mature organizations.</li>
<li><a href="https://wojciechregula.blog/post/macos-red-teaming-bypass-tcc-with-old-apps/" target="_blank">macOS Red Teaming: Bypass TCC with old apps</a>. macOS privacy framework (TCC) got you down? Use an old version of an app that is vulnerable to dylib injection, inherit the legitimate TCC permission, and win!</li>
<li><a href="https://snovvcrash.rocks/2022/03/06/abusing-kcd-without-protocol-transition.html" target="_blank">Abusing Kerberos Constrained Delegation without Protocol Transition</a>. There seem to be no end to the ways to can abuse Kerberos in special circumstances.</li>
<li><a href="https://www.trustedsec.com/blog/expanding-the-hound-introducing-plaintext-field-to-compromised-accounts/" target="_blank">Expanding the Hound: Introducing Plaintext Field to Compromised Accounts</a>. Modify the BloodHound database to fit your use cases.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://fortynorthsecurity.com/blog/remove-powershell-comments-whitespace-and-handles/" target="_blank">Removing PowerShell Comments, Whitespace, and Handles</a>. A simple script to help make your Powershell less detectible.</li>
<li><a href="https://github.com/oxagast/oxasploits" target="_blank">oxasploits</a>. All of these exploits are originally coded by oxagast / Marshall Whittaker. Some of them were already known vulnerabilities that they took and re-evaluated then wrote an exploit for them that they thought was more functional or logical in some way. Some of these vulnerabiltiies are partial PoC exploits that will make something crash, but not actually get root. Some will straight drop you at a root shell. None of this code should ever under any circumstances be run in a production environment, or on a system that you do not have express permission to run a penetration test on.</li>
<li><a href="https://github.com/nettitude/RunOF" target="_blank">RunOF</a> is a .NET application that is able to load arbitrary BOFs, pass arguments to them, execute them and collect and return any output. For more details check out <a href="https://labs.nettitude.com/blog/introducing-runof-arbitrary-bof-tool/" target="_blank">Introducing RunOF – Arbitrary BOF tool</a>.</li>
<li><a href="https://github.com/dolevf/graphql-cop" target="_blank">graphql-cop</a> is a small Python utility to run common security tests against GraphQL APIs.</li>
<li><a href="https://gitlab.com/shodan-public/nrich" target="_blank">nrich</a> is a command-line tool to quickly analyze all IPs in a file and see which ones have open ports/ vulnerabilities. Can also be fed data from stdin to be used in a data pipeline.</li>
<li><a href="https://github.com/S4ntiagoP/donut/tree/syscalls" target="_blank">donut</a> this is a donut fork that contains syscall support for AMSI/WDLP patching.</li>
<li><a href="https://github.com/cube0x0/SyscallPack" target="_blank">SyscallPack</a> is a BOF and some shellcode for full DLL unhooking using dynamic syscalls.</li>
<li><a href="https://github.com/klezVirus/SysWhispers3" target="_blank">SysWhispers3</a> is SysWhispers on Steroids - AV/EDR evasion via direct system calls.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/chaitanyakrishna/iocscraper" target="_blank">iocscraper</a> is a python tool that enables you to extract IOCs and intelligence from different data sources.</li>
<li><a href="https://github.com/sec-tools/litefuzz" target="_blank">litefuzz</a> is a multi-platform fuzzer for poking at userland binaries and servers.</li>
<li><a href="https://github.com/op7ic/BlueTeam.Lab#prerequisites" target="_blank">BlueTeam.Lab</a> is a Blue Team detection lab created with Terraform and Ansible in Azure.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 408 (+2)</p>
<p>Blogs monitored: 288 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
