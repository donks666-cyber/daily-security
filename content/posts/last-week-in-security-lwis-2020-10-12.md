Title: Last Week in Security (LWiS) - 2020-10-12
Date: 2020-10-12 23:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-10-12
Author: Erik
Summary: DLL Hijacking persistence by <a href="https://twitter.com/duff22b" target="_blank">@duff22b</a>, Unauth RCE against HP Device Manager from <a href="https://twitter.com/nickstadb" target="_blank">@nickstadb</a>, Linux package manager persistence by <a href="https://twitter.com/pwnshift" target="_blank">@pwnshift</a>, malware unpacking techniques from <a href="https://twitter.com/Marco_Ramilli" target="_blank">@Marco_Ramilli</a>, criticals in Apple infra by <a href="https://twitter.com/samwcyo" target="_blank">@samwcyo</a>, DLL hijacking for lateral movement by <a href="https://twitter.com/domchell" target="_blank">@domchell</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-10-05 to 2020-10-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://docs.python.org/3.9/whatsnew/3.9.html" target="_blank">Python 3.9 is out</a> which brings new features like dictionary merging (<cite>dict1 | dict2</cite>), dictionary updates (<cite>dict1 |= dict2</cite>) , type hinting, and a new parser.</li>
<li><a href="https://www.virtuallyghetto.com/2020/10/esxi-on-arm-fling.html" target="_blank">ESXi on Arm Fling is LIVE!</a>. Teased at VMworld Europe 2018, the ARM variant of ESXi is finally here. It can run on a Raspberry Pi 4 (8GB highly recommended) and can act as a vSAN witness in a two node cluster (not officially supported).</li>
<li><a href="https://googleprojectzero.blogspot.com/2020/10/enter-the-vault-auth-issues-hashicorp-vault.html" target="_blank">Enter the Vault: Authentication Issues in HashiCorp Vault</a>. Two vulnerabilities in HashiCorp Vault could allow an attacker to bypass authentication checks in Amazon Web Services (AWS) and Google Cloud Platform (GCP) configurations.</li>
<li><a href="https://krebsonsecurity.com/2020/10/report-u-s-cyber-command-behind-trickbot-tricks/" target="_blank">Report: U.S. Cyber Command Behind Trickbot Tricks</a>. Some entity was sending Trickbot configs with a new C2 address of 127.0.0.1 as well as spamming the bot registration endpoints to flood Trickbot operators with bad data. This article claims it was USCYBERCOM.</li>
<li><a href="https://samcurry.net/hacking-apple/" target="_blank">We Hacked Apple for 3 Months: Here’s What We Found</a>. <a href="https://twitter.com/samwcyo" target="_blank">@samwcyo</a> and friends spent a few months tearing through everything Apple dropping criticals along the way. This write up is very well done, and is worth the read. They will likely cross $500,000 in bounties once all are paid.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://pwnshift.github.io/2020/10/01/persistence.html" target="_blank">Persistence Via Linux Package Managers</a>. This post explores using python to wait and execute commands when a package manager has finished its update. This way, you can re-backdoor programs after they are updated to maintain your persistence.</li>
<li><a href="https://riccardoancarani.github.io/2020-10-10-donut-crumbs/" target="_blank">Following Donut Crumbs</a>. <a href="https://github.com/TheWover/donut" target="_blank">Donut</a> is an incredibly useful tool, but like every tool it has its signatures. This post shows a few to give defenders ideas on how to detect it as well as operators ideas on what to modify.</li>
<li><a href="https://chadduffey.com/2020/10/10/edgegdi.html" target="_blank">edgegdi.dll for persistence</a>. Windows 10 2004 is missing a DLL that nearly every process attempts to call. Writing a well crafted stand in can be used for persistence (requires Administrator access). Note that the code presented in this post will BSOD on reboot, and fixes are an exercise left for the reader (I would grab a copy from older windows and use <a href="https://github.com/Cybereason/siofra" target="_blank">siofra</a>). If this technique sounds familiar, the basic discovery of edgegdi.dll was discussed in <a href="https://windows-internals.com/faxing-your-way-to-system/" target="_blank">Faxing Your Way to SYSTEM — Part Two</a>.</li>
<li><a href="https://nickbloor.co.uk/2020/10/05/hp-device-manager-cve-2020-6925-cve-2020-6926-cve-2020-6927/" target="_blank">HP Device Manager – CVE-2020-6925, CVE-2020-6926, CVE-2020-6927</a>. This is a great post on how persistence pays off as <a href="https://twitter.com/nickstadb" target="_blank">@nickstadb</a> manages to get SYSTEM on any Windows machine that is running the HP Device Manager. Excellent work!</li>
<li><a href="https://marcoramilli.com/2020/10/09/how-to-unpack-malware-personal-notes/" target="_blank">How To Unpack Malware: Personal Notes</a>. This post explores some different techniques to get started with unknown packed malware samples.</li>
<li><a href="https://www.guardicore.com/2020/10/wareztheremote-turning-remotes-into-listening-devices/" target="_blank">WarezTheRemote: Turning Remotes into Listening Devices</a>. In the smart world even remotes have firmware and microphones. This post complete with demo video and great graphics shows how an attacker on the same network as one of these remotes could "update" it and use it as a persistent listening device. This specific remote has been patched with firmware validity checks.</li>
<li><a href="https://www.cyberark.com/resources/threat-research-blog/anti-virus-vulnerabilities-who-s-guarding-the-watch-tower" target="_blank">Anti-Virus Vulnerabilities: Who’s Guarding the Watch Tower?</a>. Directory permissions issues are widespread and even affect anti-virus products.</li>
<li><a href="https://unit42.paloaltonetworks.com/cve-2020-14386/" target="_blank">CVE-2020-14386: Privilege Escalation Vulnerability in the Linux kernel</a>. This CVE affects a lot of default installs (i.e. Ubuntu) and is an up to 10 byte heap overflow in packet processing. At this time, only a <a href="https://github.com/cgwalters/cve-2020-14386" target="_blank">crash PoC</a> is available.</li>
<li><a href="https://www.praetorian.com/blog/inside-mimikatz-part1" target="_blank">Inside the Mimikatz Pass-the-Hash Command (Part 1)</a>. This is a very detailed look into the complex systems involved in Windows authentication.</li>
<li><a href="https://www.mdsec.co.uk/2020/10/i-live-to-move-it-windows-lateral-movement-part-3-dll-hijacking/" target="_blank">I Like to Move It: Windows Lateral Movement Part 3: DLL Hijacking</a>. While DLL hijacking is a common technique used for persistence and privilege escalation, in certain circumstances it can be used for lateral movement as well (planting a DLL via SMB and executing the program that loads it via WMI or DCOM).</li>
<li><a href="https://teamhydra.blog/2020/10/12/in-process-execute-assembly-and-mail-slots/" target="_blank">In Process Execute Assembly and Mail Slots</a>. When executing .Net assemblies in your own process, the CLR must be loaded and unless you modify the executables they will print to standard out. This post shows how to use mail slots to run unmodified .Net binaries and get the output back over mailslots which your implant can ship back to you via your C2. PoC <a href="https://github.com/N4kedTurtle/ExecuteAssembly_Mailslot" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/linhlhq/TinyAFL/tree/TinyAFL-MacOS" target="_blank">TinyAFL</a> is a fuzzer designed for macOS usermode applications even if source code is not available.</li>
<li><a href="https://github.com/EncodeGroup/UAC-SilentClean" target="_blank">UAC-SilentClean</a> implements a DLL planting technique to bypass UAC Always Notify and execute code in a high integrity process. The SilentCleanup technique has been known for quite some time, and Microsoft has made no attempt to fix it, so this will likely continue to work until the scheduled task is changed for some other reason unrelated to security.</li>
<li><a href="https://github.com/EncodeGroup/BOF-RegSave" target="_blank">BOF-RegSave</a> will acquire the necessary privileges and dump SAM - SYSTEM - SECURITY registry keys for offline parsing and hash extraction.</li>
<li><a href="https://github.com/wallarm/jwt-secrets/" target="_blank">jwt-secrets</a> is a collection of many public-available JWT secrets from code samples that may be used in production. It is the list used in the new Burp app <a href="https://github.com/wallarm/jwt-heartbreaker" target="_blank">jwt-heartbreaker</a> (more details <a href="https://lab.wallarm.com/meet-jwt-heartbreaker-a-burp-extension-that-finds-thousands-weak-secrets-automatically/" target="_blank">here</a>).</li>
<li><a href="https://github.com/liamg/gitjacker" target="_blank">gitjacker</a> downloads git repositories and extracts their contents from sites where the .git directory has been mistakenly uploaded. It will still manage to recover a significant portion of a repository even where directory listings are disabled.</li>
<li><a href="https://github.com/luisfontes19/CSRFER" target="_blank">CSRFER</a> is a tool to generate csrf payloads based on vulnerable requests.</li>
<li><a href="https://github.com/screego/server" target="_blank">screego server</a> allows you to share your screen with good quality and low latency. Screego is an addition to existing software and only helps to share your screen. This is useful for code reviews where the quality of Teams/Meet/Zoom doesn't cut it.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/devanshbatham/FavFreak" target="_blank">FavFreak</a> matches favicon hashes to their services using a large fingerprint dictionary. This can be a quick win when identifying web technologies on a large attack surface.</li>
<li><a href="https://github.com/pwndoc/pwndoc" target="_blank">pwndoc</a> is similar to <a href="https://github.com/GhostManager/Ghostwriter" target="_blank">Ghostwriter</a> allowing multiple users to collaborate on assessment or vulnerability reports and generate a customized Docx report.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
