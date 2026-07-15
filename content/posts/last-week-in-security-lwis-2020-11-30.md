Title: Last Week in Security (LWiS) - 2020-11-30
Date: 2020-11-30 23:50
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-11-30
Author: Erik
Summary: OffSecOps setup (<a href="https://twitter.com/xenosCR" target="_blank">@xenosCR</a>), direct syscalls in CobaltStrike (<a href="https://twitter.com/brsn76945860" target="_blank">@brsn76945860</a>), VBA DLL linking (<a href="https://twitter.com/rd_pentest" target="_blank">@rd_pentest</a>), advanced red teaming (<a href="https://twitter.com/BorjaMerino" target="_blank">@BorjaMerino</a>), invoking managed code in .NET DLLs (<a href="https://twitter.com/_xpn_" target="_blank">@_xpn_</a>), shellcode execution via PostgreSQL extensions (<a href="https://twitter.com/darkcodersc" target="_blank">@DarkCoderSc</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-11-23 to 2020-11-30.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://twitter.com/qwertyoruiopz/status/1329506451388293129" target="_blank">Exploit PoCs now fetch your crashlogs</a>. Careful with that <a href="https://github.com/ZecOps/FreeTheSandbox_LPE_POC_13.7" target="_blank">new iOS PoC</a>, as it will upload all the crashdumps on your device to ZecOps every time it is run. The PoC is open source, but the analytics code is hidden in a zip.</li>
<li><a href="https://lore.kernel.org/wireguard/X7vGOb0o6SHIvfDc@zx2c4.com/T/#u" target="_blank">WireGuard for Windows 0.3: ARM support, enterprise features, &amp; more</a>. This is a major release for WireGuard. Windows gets "enterprise" features (non-admins can start and stop tunnels if a registry key is set, etc) that will make it much easier to deploy within modern companies that are properly enforcing the principle of least privilege. Documentation <a href="https://git.zx2c4.com/wireguard-windows/about/docs/adminregistry.md" target="_blank">here</a>.</li>
<li><a href="https://www.wired.com/story/tesla-model-x-hack-bluetooth/" target="_blank">This Bluetooth Attack Can Steal a Tesla Model X in Minutes</a>. The cryptographic checks exist to prevent this, but are not enforced! Video of the process <a href="https://www.youtube.com/watch?v=clrNuBb3myE" target="_blank">here</a>.</li>
<li><a href="https://www.bleepingcomputer.com/news/security/drupal-issues-emergency-fix-for-critical-bug-with-known-exploits/" target="_blank">Drupal issues emergency fix for critical bug with known exploits</a>. Another critical Drupal remote code execution vulnerability - this time if the server processes .tar, .tar.gz, .bz2, or .tlz file uploads. Patch and segment your servers!</li>
<li><a href="https://www.macrumors.com/2020/11/27/developer-successfully-virtualizes-windows-on-m1/" target="_blank">Developer Successfully Virtualizes Windows for Arm on M1 Mac</a>. It took some serious QEMU hacks, but Windows for Arm is running on the new Apple Silicon.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.blackarrow.net/hindering-threat-hunting-a-tale-of-evasion-in-a-restricted-environment/" target="_blank">Hindering Threat Hunting, a tale of evasion in a restricted environment</a>. Some great "advanced red team" tactics in this post. From the initial execution via signed binary DLL hijacking, to the C2 via a trusted service (Google Apps Scripts), this engagement put the "A" in APT. I particularly enjoy that none of these techniques are "new" but rather pulled from actual threat actor TTPs (and the link to my <a href="https://github.com/SixGenInc/Noctilucent" target="_blank">Noctilucent</a> project).</li>
<li><a href="https://secureyourit.co.uk/wp/2020/11/28/vbafunctionpointers/" target="_blank">VBA and Function Pointers</a>. Despite its "unique" syntax, VBA is a fully featured programming language and as such, advanced programming techniques like run time dynamic linking of DLLs can be done in pure VBA.</li>
<li><a href="https://www.synacktiv.com//en/publications/dont-fear-the-bark-tsrewrite-to-dodge-the-mark.html" target="_blank">Don't fear the bark, ts_rewrite to dodge the mark</a>. This post shows the process of developing a PostgreSQL WAF bypass using <a href="https://www.postgresql.org/docs/12/textsearch-features.html" target="_blank">ts_rewrite</a> to encode/rewrite queries.</li>
<li><a href="https://br-sn.github.io/Implementing-Syscalls-In-The-CobaltStrike-Artifact-Kit/" target="_blank">Implementing Syscalls In The Cobaltstrike Artifact Kit</a>. This was teased in the BloodHoundGang Slack, and <a href="https://twitter.com/brsn76945860" target="_blank">@brsn76945860</a> does not disappoint. This posts walks through porting Cobalt Strike's Artifact Kit to Windows/Visual Studio and then using <a href="https://github.com/jthuraisamy/Syswhispers" target="_blank">SysWhispers</a> for direct syscalls in Cobalt Strike's beacon. This should help keep detections low for many AV/EDR solutions.</li>
<li><a href="https://blog.xenoscr.net/OffSecOps-Basic-Setup/" target="_blank">OffSecOps Basic Setup</a>. Based on the <a href="https://www.youtube.com/watch?v=XaICChBJMck" target="_blank">SpecterOps Con 2020 talk by Will Schroeder</a>, the post walks through the basics of setting up a "OffSecOps" pipeline with Jenkins on Windows.</li>
<li><a href="https://browninfosecguy.com/Active-Directory-Lab-Setup-Tool" target="_blank">Active Directory Lab Setup Tool</a> does what it says on the tin. For a completely automated solution, check out <a href="https://detectionlab.network/" target="_blank">DetectionLab</a>.</li>
<li><a href="https://blog.xpnsec.com/the-net-export-portal/" target="_blank">The .NET Export Portal</a> walks through the ways code can be exposed in DLL exports, and how to call managed functions without having to mark anything as exported. PoC code <a href="https://gist.github.com/xpn/8af9b78e07b9565ce21949a4438d42bb" target="_blank">here</a>.</li>
<li><a href="https://windows-internals.com/exploiting-a-simple-vulnerability-in-35-easy-steps-or-less/" target="_blank">Exploiting a “Simple” Vulnerability – In 35 Easy Steps or Less!</a> This post shows the work that goes into memory corruption exploits. A great in depth post for anyone interested in exploit development. Windows local privilege escalation PoC <a href="https://github.com/yardenshafir/CVE-2020-1034" target="_blank">here</a>.</li>
<li><a href="https://www.phrozen.io/resources/paper/41df297b-cfe3-43ec-88e8-0686e5548dd5" target="_blank">Postgresql Extension Shellcode Execution</a>. If you can write a DLL to disk and you have SQL execution (perhaps via SQL injection) you can load a custom extension that can execute arbitrary code! Example extension <a href="https://github.com/DarkCoderSc/execute-shellcode-pgext" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/0xdeadbeefJERKY/mythic-deploy" target="_blank">mythic-deploy</a> automates the deployment and configuration of a <a href="https://github.com/its-a-feature/Mythic" target="_blank">Mythic</a> server with Terraform and Ansible. Adapt it to meet your red team's needs.</li>
<li><a href="https://github.com/whickey-r7/grab_beacon_config" target="_blank">grab_beacon_config</a> is a nmap NSE script to parse beacon payloads from cobalt strike servers to show their configurations. Use against your own infrastructure to see what others can tell about your beacons.</li>
<li><a href="https://github.com/KasperskyLab/TinyCheck" target="_blank">TinyCheck</a> is a network IOC scanner for smartphones with a self-contained wifi man in the middle capture ability. Currently it alerts on known stalkerware indicators as well as plain text data exfiltration so don't count on it to find that NSO Group rootkit.</li>
<li><a href="https://github.com/hausec/Set-RBCDBytes" target="_blank">Set-RBCDBytes</a> will set the msds-allowedtoactonbehalfofotheridentity property on the target with the security descriptor for a supplied user or machine that has an SPN. Where would this be useful? Consider an overprovisioned help desk (or similar) account that has GenericAll over every object in the domain and you want to quickly set the msds-allowedtoactonbehalfofotheridentity property on a specific target without importing all of PowerView. This is the script you need! <a href="https://github.com/pkb1s/SharpAllowedToAct" target="_blank">SharpAllowedToAct</a> is the C# variant, and more information on the technique can be found <a href="https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html" target="_blank">here</a>.</li>
<li><a href="https://github.com/BonJarber/SecUtils/tree/master/clean_wordlist" target="_blank">clean_wordlist.sh</a> is great for cleaning up some of the noise from last week's <a href="https://wordlists.assetnote.io/" target="_blank">AssetNote's wordlists</a>.</li>
<li><a href="https://github.com/nccgroup/s3_objects_check" target="_blank">s3_objects_check</a> is a script to check S3 object permissions in order to identify publicly accessible objects. The script requires two accounts, one with read access to S3 and one with no access to S3.</li>
<li><a href="https://github.com/cloudquery/cloudquery" target="_blank">cloudquery</a> transforms your cloud infrastructure into queryable SQL tables for easy monitoring, governance and security. Think <a href="https://www.osquery.io/" target="_blank">osquery</a> for the cloud.</li>
<li><a href="https://github.com/redcode-labs/Neurax" target="_blank">Neurax</a>. Redcode labs keeps the Go based malware libraries coming with Neurax, library for constructing self-spreading binaries.</li>
<li><a href="https://github.com/evilpenguin/NetworkSniffer" target="_blank">NetworkSniffer</a> will log ALL traffic for any iOS application. This includes WKWebView and UIWebView, and no certificate pinning bypass is required! Requires a jailbroken iPhone.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.cnx-software.com/2020/11/12/tigard-open-source-ft2232h-board-hardware-hacking/" target="_blank">Tigard</a> is a one-stop-shop for all your hardware hacking needs.</li>
<li><a href="https://github.com/microsoft/DbgShell" target="_blank">DbgShell</a> is a PowerShell front-end for the Windows debugger engine.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
