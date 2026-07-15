Title: Last Week in Security (LWiS) - 2020-07-27
Date: 2020-07-27 06:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-07-27
Author: Erik
Summary: NTLM relaying via Citrix Workspace by <a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>, access the entire AD database via Exchange with a new tool from <a href="https://twitter.com/_mohemiv" target="_blank">@_mohemiv</a>, a new Go based C2/Agent from <a href="https://twitter.com/paragonsec" target="_blank">@paragonsec</a> and team, phishing tips from <a href="https://twitter.com/lorentzenman" target="_blank">@lorentzenman</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-07-20 to 2020-07-27.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<aside class="m-note m-warning">
<h3>DEF CON Talk</h3>
<p>I will be virtually presenting <a href="https://defcon.org/html/defcon-safemode/dc-safemode-speakers.html#Hunstad" target="_blank">research</a> on TLS 1.3 and what it means for domain fronting on Thursday, August 6th at 1630 Pacific Time (2330 UTC).</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.bbc.com/news/technology-53528329" target="_blank">Blackbaud hack: More UK universities confirm breach</a>. Software supply chain hits Blackbaud and therefore many of its customers. It turns out extortionware (ransomware + stealing data) was used to get Blackbaud to pay the ransom/extortion and once the hackers had been paid, they had given "confirmation that the copy [of data] they removed had been destroyed". Unfortunately there is no way to verify that, and any data that was taken has to be assumed lost.</li>
<li><a href="https://www.theregister.com/2020/07/21/twilio_javascript_sdk_code_injection/" target="_blank">Twilio: Someone waltzed into our unsecured AWS S3 silo, added dodgy code to our JavaScript SDK for customers</a>. This is scary for anyone who uses an SDK or third party software (everyone). The software supply chain is vulnerable, and there are no great solutions to both update third party code quickly and stay secure. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1195/002/" target="_blank">T1195.002 Supply Chain Compromise: Compromise Software Supply Chain</a>]</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.scrt.ch/2020/07/15/engineering-antivirus-evasion-part-ii/" target="_blank">Engineering antivirus evasion (Part II)</a>. Scrt shows how it is possible to accurately replace function calls in C/C++ code-bases without using regexes to hide API import and allow meterpreter to bypass ESET Nod32.</li>
<li><a href="https://www.pentestpartners.com/security-blog/raining-system-shells-with-citrix-workspace-app/" target="_blank">Raining SYSTEM Shells with Citrix Workspace app</a>. <a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a> uses NTLM relaying with Citrix workspace to get SYTEM shells. Poc is <a href="https://github.com/CCob/PoC/blob/master/CVE-2020-8207/citrix_workspace.py" target="_blank">here</a>.</li>
<li><a href="https://inside.battelle.org/blog-details/battelle-publishes-open-source-binary-visualization-tool" target="_blank">Battelle Publishes Open Source Binary Visualization Tool</a>. CantorDust enables the rapid visualization of unknown binary data with Ghidra, allowing for rapid visual inspection of unknown binaries.</li>
<li><a href="https://swarm.ptsecurity.com/attacking-ms-exchange-web-interfaces/" target="_blank">Attacking MS Exchange Web Interfaces</a>. <a href="https://twitter.com/_mohemiv" target="_blank">@_mohemiv</a> drops serious knowledge, providing an overview of current Exchange attacks, and introducing a <a href="https://github.com/ptswarm/impacket" target="_blank">new tool</a> to allow the lookup of Distinguished Name Tags from the domain controller using Exchange RPC. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1087/002/" target="_blank">T1087.002 Account Discovery: Domain Account</a>]</li>
<li><a href="https://redteaming.co.uk/2020/07/22/to-click-or-not-to-click/" target="_blank">To Click or Not to Click?</a>. Step up your phishing game with these tips from <a href="https://twitter.com/lorentzenman" target="_blank">@lorentzenman</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1566/002/" target="_blank">T1566.002 Phishing: Spearphishing Link</a>]</li>
<li><dl>
<dt>Malware Analysis - These in-depth posts show some current campaigns and the techniques they are using. If you are in adversary emulation, be sure to add them to your assessments.</dt>
<dd><ul>
<li><a href="https://blog.malwarebytes.com/threat-analysis/2020/07/chinese-apt-group-targets-india-and-hong-kong-using-new-variant-of-mgbot-malware/" target="_blank">Chinese APT group targets India and Hong Kong using new variant of MgBot malware</a></li>
<li><a href="https://newtonpaul.com/analysing-fileless-malware-cobalt-strike-beacon/" target="_blank">Analysing Fileless Malware: Cobalt Strike Beacon</a></li>
<li><a href="https://blog.trendmicro.com/trendlabs-security-intelligence/updates-on-thiefquest-the-quickly-evolving-macos-malware/" target="_blank">Updates on ThiefQuest, the Quickly-Evolving macOS Malware</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://secfault-security.com/blog/chain3.html" target="_blank">Writing an iOS Kernel Exploit from Scratch</a>. If you ever want to do iOS exploit development, this is required reading. All the nitty gritty steps from setting up the environment to analyzing the bug and finally writing the exploit are covered.</li>
<li><a href="https://awaraucom.wordpress.com/2020/07/19/house-of-io-remastered/" target="_blank">House of Io – Remastered</a>. This post describes a mechanism for bypassing the Safe-Linking heap mitigating in GLibc 2.32 and greater under specific circumstances.</li>
<li><a href="https://iwantmore.pizza/posts/PEzor.html" target="_blank">Designing and Implementing PEzor, an Open-Source PE Packer</a>. Phra walks through the process of writing a robust (syscall inlining, user-land hook removal, LLVM obfuscation, polymophic generation, etc) PE loader. Excellent work.</li>
<li><a href="https://dirkjanm.io/abusing-azure-ad-sso-with-the-primary-refresh-token/" target="_blank">Abusing Azure AD SSO with the Primary Refresh Token</a>. The AD whisperer himself Dirk-jan (<a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>) is back to drop valuable knowledge. Here he explains how SSO works with Primary Refresh Tokens, and what some of the implicit risks are of using SSO. He demonstrates how attackers can abuse this if they have access to a device which is Azure AD joined or Hybrid joined to obtain long-lived tokens which can be used independently of the device and which will in most cases comply with even the stricter Conditional Access policies. Dirk-jan also kindly released a tool to help you do all this: <a href="https://github.com/dirkjanm/ROADtoken" target="_blank">ROADtoken</a>.</li>
<li><a href="https://research.nccgroup.com/2020/07/22/depthcharge/" target="_blank">Tool Release: Sinking U-Boots with Depthcharge</a>. This is a very cool tool from nccgroup for physical assessments against devices running the U-boot bootloader.</li>
<li><a href="https://srcincite.io/blog/2020/07/20/sharepoint-and-pwn-remote-code-execution-against-sharepoint-server-abusing-dataset.html" target="_blank">SharePoint and Pwn :: Remote Code Execution Against SharePoint Server Abusing DataSet</a>. SharePoint continues to deserialize all kinds of data and deserialization continues to deliver shells.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/paranoidninja/Boomerang" target="_blank">Boomerang</a> is a tool to expose multiple internal servers to web/cloud. This project is in early stages, and has no authentication or encryption, but may provide a good base if you are looking to write your own tunneling agent with Go.</li>
<li><a href="https://github.com/sailay1996/RpcSsImpersonator" target="_blank">RpcSsImpersonator</a> is an Administrator or Network Service to SYSTEM privilege exploit for Windows.</li>
<li><a href="https://github.com/NtRaiseHardError/Antimalware-Research/tree/master/Malwarebytes/v4.0.4.49" target="_blank">Malwarebytes-Disabler</a> injects shellcode into a malwarebytes process which allows a user to disable "Malware Protection" even if the Malwarebytes administrator has set a password to protect this setting from being changed. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1562/001/" target="_blank">T1562.001 Impair Defenses: Disable or Modify Tools</a>]</li>
<li><a href="https://github.com/Mr-B0b/SpaceRunner" target="_blank">SpaceRunner</a> enables the compilation of a C# program that will execute arbitrary PowerShell code, without launching PowerShell processes through the use of runspace and includes AMSI patching. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1562/006/" target="_blank">T1562.006 Impair Defenses: Indicator Blocking</a>]</li>
<li><a href="https://github.com/intrepidtechie/KITT-O365-Tool" target="_blank">KITT-O365-Tool</a> is a tool designed to make working O365 Business Email Compromise investigations easier and more efficient for DFIR and SOC analysts by pairing the power of PowerShell cmdlets with the ease of use of a GUI.</li>
<li><a href="https://github.com/DeimosC2/DeimosC2" target="_blank">DeimosC2</a>  is a post-exploitation Command &amp; Control (C2) tool that leverages multiple communication methods in order to control machines that have been compromised. DeimosC2 server and agents works on, and has been tested on, Windows, Darwin, and Linux. It is entirely written in Golang with a front end written in Vue.js. This is a very impressive 1.0 release!</li>
<li><a href="https://github.com/jamesmcm/vopono" target="_blank">vopono</a> is a tool to run applications through VPN tunnels via temporary network namespaces. This allows you to run only a handful of applications through different VPNs simultaneously, whilst keeping your main connection as normal.</li>
<li><a href="https://github.com/hlldz/dazzleUP" target="_blank">dazzleUP</a> is a tool that detects the privilege escalation vulnerabilities caused by misconfigurations and missing updates in the Windows operating systems. It uses the Windows Update Agent API instead of WMI (like others) when finding missing patches, and comes with a CobaltStrike cna script. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://github.com/cpandya2909/CVE-2020-15778" target="_blank">CVE-2020-15778</a> is a simple command injection in openssh &lt;= 8.3p1. If you have access to a linux host without shell access but only scp access, you just got shell access.</li>
<li><a href="https://github.com/checkymander/Carbuncle" target="_blank">Carbuncle</a> is a tool for interacting with outlook interop during red team engagements; enumerate, read, monitor, and send email.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
