Title: Last Week in Security (LWiS) - 2020-03-23
Date: 2020-03-23 10:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-03-23
Author: Erik
Summary: VMWare exploits including a macOS privesc, XPC abuse in macOS, the first WiFi kr00k PoC, and many great new tools like Invoke-SharpLoader in this week's Last Week in Security.

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-03-16 to 2020-03-23.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.webarxsecurity.com/covid-19-cyber-attacks/?ref=producthunt" target="_blank">COVID-19 Cyber Attacks</a> is a up to date tracker of offensive cyber campaigns that have leveraged the COVID-19 pandemic. Stay alert!</li>
<li><a href="https://github.blog/2020-03-16-npm-is-joining-github/" target="_blank">npm is joining GitHub</a> as GitHub becomes the centralized behemoth of the software development world. Microsoft's famous motto of <a href="https://en.wikipedia.org/wiki/Embrace,_extend,_and_extinguish" target="_blank">embrace, extend [you are here], and extinguish</a> is in full force. It remains to be seen if this is a net positive for software development, but I have my doubts.</li>
<li><a href="https://www.vmware.com/security/advisories/VMSA-2020-0004.html" target="_blank">CVE-2020-3947</a> dropped, a use-after-free that allows a guest to execute code on the host in VMWare Workstation, Fusion, Horizon Client, and Remote Console for Windows. No exploit or PoC available yet. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://blogs.vmware.com/vsphere/2020/03/vsphere-7-links-1.html" target="_blank">vSphere 7 – Launch Recap &amp; Links</a> is a run down of the vSphere 7 and related announcements from VMware.</li>
<li><a href="https://research.checkpoint.com/2020/the-inside-scoop-on-a-six-figure-nigerian-fraud-campaign/" target="_blank">The Inside Scoop on a Six-Figure Nigerian Fraud Campaign</a> is a wild ride through the back alleys of the internet as Check Point Research tracks down a Nigerian fraudster.</li>
<li><a href="https://bazaar.abuse.ch/browse/" target="_blank">Malware Bazaar</a> is a new free service by abuse.sh that serves as an alternative to virus total that aims to only categorize malware and where samples are available for free (even for commercial use!).</li>
<li><a href="https://salsa.debian.org/kernel-team/linux/-/commit/9d60411cee4c646fe5006dcd57a1709d0377aaa6" target="_blank">WireGuard enabled in Debian testing</a>. This is a great step for <a href="https://www.wireguard.com/" target="_blank">WireGuard</a>, a VPN protocol many see as the future for VPNs. Ubuntu has had WireGuard available in the default apt repositories since 19.04.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><dl>
<dt><a href="https://www.securing.biz/en/abusing-securing-xpc-in-macos-apps/index.html" target="_blank">Abusing &amp; Securing XPC in macOS apps</a> is a talk by Wojciech Reguła from the macOS conference "Objective by the Sea" that explores the inter-process communication mechanism XPC for local privilege escalation and unsigned dylib injection. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</dt>
<dd><ul>
<li><a href="https://vimeo.com/397568495" target="_blank">Demo</a> of dylib injection and XPC trickery to bypass the LuLu firewall</li>
<li>A <a href="https://github.com/securing/SimpleXPCApp" target="_blank">secure example</a> of a privileged XPC service was provided as well.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://www.sentinelone.com/blog/how-offensive-actors-use-applescript-for-attacking-macos/" target="_blank">How Offensive Actors Use AppleScript For Attacking macOS</a> show examples of how AppleScript can be used for persistence, anti-analysis, browser hijacking, spoofing, and more.</li>
<li><a href="https://blog.grimm-co.com/post/analyzing-suid-binaries/" target="_blank">Analyzing SUID Binaries</a> from Grimm is a great blog on how to find vulnerable SUID binaries on macOS. Grimm used this process to find a <a href="https://github.com/grimm-co/NotQuite0DayFriday/tree/master/2020.03.17-vmware-fusion" target="_blank">local privilege escalation in VMware Fusion</a>. Even with the recent patch, VMware Fusion 11.5.2 is <a href="https://twitter.com/jeffball55/status/1240040767961301003/photo/1" target="_blank">still vulnerable</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://www.mdsec.co.uk/2020/03/hiding-your-net-etw/" target="_blank">Hiding Your .NET – ETW</a> introduces a simple patch for the Event Threading for Windows (ETW) function "EtwEventWrite" to prevent any loaded .NET assemblies from appearing in any ETW stream, to include the properties windows of Process Explorer. Code for <a href="https://gist.github.com/xpn/fabc89c6dc52e038592f3fb9d1374673" target="_blank">unmanaged</a> and managed (in-line in the blog) processes is available for x86. x64 is an exercise left to the reader. Bonus points for patching the ETW functions to only filter out your indicators, or replaying the ETW signatures of known begin Windows .NET assemblies to fool EDR. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1054/" target="_blank">T1054 Indicator Blocking</a>]</li>
<li><a href="https://medium.com/@lampyre.io/whats-wrong-with-this-account-or-how-to-tell-fake-accounts-from-real-ones-720e0f29b34e" target="_blank">What’s Wrong With This Account? Or How To Tell Fake Accounts From Real Ones</a> is a good resource for investigating accounts, but also provides a blue print for red teamers on how to avoid creating accounts that look suspicious for phishing campaigns or other social engineering.</li>
<li><a href="https://github.com/sailay1996/awesome_windows_logical_bugs/blob/master/dir_create2system.txt" target="_blank">Dir create to SYSTEM</a> describes a few methods of using the ability to create directories on Windows to get a code running as SYSTEM. This should help some exploit devs stuck with a dir-create primitive but no way to weaponize it. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/dafthack/MSOLSpray" target="_blank">MSOLSpray</a> is a password spraying tool for Microsoft Online accounts (Azure/O365). The script logs if a user cred is valid, if MFA is enabled on the account, if a tenant doesn't exist, if a user doesn't exist, if the account is locked, or if the account is disabled. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1110/" target="_blank">T1110 Brute Force</a>]</li>
<li><a href="https://github.com/hexway/r00kie-kr00kie" target="_blank">r00kie-kr00kie</a> is the first tool to exploit the Kr00k (<a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-15126" target="_blank">CVE-2019-15126</a>) WiFi attack where many chips set the packet encryption key to all zeros when de-authenticated, but still send all the packets in the send buffer. It is possible to leak a few packets from busy clients each time you de-auth them. Think of it as <a href="https://heartbleed.com/" target="_blank">heart bleed</a> for WiFi, but much more disruptive to the end user. The <a href="https://hexway.io/research/r00kie-kr00kie/" target="_blank">Hexway Blog</a> has a detailed explanation.</li>
<li><a href="https://github.com/ufrisk/MemProcFS" target="_blank">MemProcFS</a> evolves direct memory access (DMA) attacks to their GUI based final form by mounting memory contents as a virtual file system allowing you to use normal tools like hex editors on live memory. It even comes with Python and C/C++ API bindings. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1200/" target="_blank">T1200 Hardware Additions</a>]</li>
<li><a href="https://www.youtube.com/watch?v=9Mv0-PfiXeg" target="_blank">Egalito: Layout-Agnostic Binary Recompilation</a> is an interesting presentation by David Williams-King on a binary recompiler that lifts linux (x86-64, aarch64, and experimental RISC-V) ELF binaries to an intermediate language, applies modifications (i.e. patches, function trampolines, etc), and recompiles back to a binary. The spirit of this project is for binary hardening and after the fact patching, but I can see it being the basis of an advanced binary obfuscator or a tool to repurpose existing binary malaware automatically. All the code is GPL-3 and <a href="https://github.com/columbia/egalito" target="_blank">on GitHub</a>.</li>
<li><a href="https://blog.fox-it.com/2020/03/19/ldapfragger-command-and-control-over-ldap-attributes/" target="_blank">LDAPFragger: Command and Control over LDAP attributes</a> introduces a tool for C2 via LDAP to use in environments where LDAP queries to a shared AD are allowed from both an isolated network and network with internet access. The C# project is available <a href="https://github.com/fox-it/LDAPFragger" target="_blank">on GitHub</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1094/" target="_blank">T1094 Custom Command and Control Protocol</a>]</li>
<li><a href="https://github.com/horsicq/PDBRipper" target="_blank">PDBRipper</a> is a utility for extract an information from PDB-files, the Program Database multi-stream symbol file which contains lots of useful information about a binary.</li>
<li><a href="https://github.com/woj-ciech/LeakLooker-X" target="_blank">LeakLooker-X</a> is a GUI for discovering, browsing, and monitoring databases that leverages <a href="https://www.binaryedge.io/" target="_blank">Binary Edge</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0007/" target="_blank">TA0007 Discovery</a>]</li>
<li><a href="https://github.com/hotnops/gtunnel" target="_blank">gTunnel</a> is a new tunneling solution written in golang. It may be useful as a base for how to implement tunneling in a custom golang access tool. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1090/" target="_blank">T1090 Connection Proxy</a>]</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/Invoke-SharpLoader" target="_blank">Invoke-SharpLoader</a> loads encrypted and compressed C# Code from a remote Webserver or from a local file straight to memory and executes it there. Very useful AV/EDR evasion tool. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1500/" target="_blank">T1500 Compile After Delivery</a>]</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/DerekSelander/dsdump" target="_blank">dsdump</a> is an improved nm + objective-d/swift class-dump. If you have worked with macOS or iOS binaries and tried to use the various forms of class dump, you know the issues with the change from objective-c to swift had on their output. dsdump has fixed these issues and provided even more options and output! Derek Selander provides a very in depth <a href="https://derekselander.github.io/dsdump/" target="_blank">writeup</a> on the inner workings as well.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
</section>
