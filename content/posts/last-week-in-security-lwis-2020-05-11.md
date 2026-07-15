Title: Last Week in Security (LWiS) - 2020-05-11
Date: 2020-05-11 06:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-05-11
Author: Erik
Summary: Evil-Maid attacks make a comeback thanks to <a href="https://twitter.com/0Xiphorus" target="_blank">@0Xiphorus</a>, 2FA interception by <a href="https://twitter.com/0x09al" target="_blank">@0x09AL</a>, new .NET C2 by <a href="https://twitter.com/_RastaMouse" target="_blank">@_RastaMouse</a>, a simple but powerful trick from <a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a> to disable any protected service on Windows, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-05-04 to 2020-05-11.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://git.lsd.cat/g/nokia-keygen" target="_blank">ALU/Nokia GPON Admin and WIFI keygen</a>. While default WiFi credentials have gotten much better in the last decade, some suppliers are still using bad algorithms to generate default passwords. In this case Nokia is using the OUI and serial number. The full background, device teardown, and keygen is in the git readme.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2002" target="_blank">Samsung Android multiple interactionless RCEs and other remote access issues in Qmage image codec built into Skia</a> is as bad as it sounds. With enough malformed images, an attacker can leak address space layout randomization (ASLR) offsets and create a payload image that will provide a remote code execution. While the demo shows lots of alerts for incoming messages, think if this was productized or conducted while the victim is asleep and then cleaned. If you have or manage Samsung devices, ensure they are updated with the May 2020 update. Demo <a href="https://www.youtube.com/watch?v=nke8Z3G4jnc" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0001/" target="_blank">TA0001 Initial Access</a>]</li>
<li><a href="https://github.com/features/codespaces" target="_blank">Github Code Spaces</a> is a hosted Visual Studio Code for Github. Great for quick edits or perhaps remote development. It remains to be seen how it will handle files not in git (secrets, .env, etc) and what it will cost.</li>
<li><a href="https://grsecurity.net/huawei_hksp_introduces_trivially_exploitable_vulnerability" target="_blank">Huawei HKSP Introduces Trivially Exploitable Vulnerability</a>. Huawei manages to royally screw up its custom kernel protection mechanism which turns out is exploitable with a 10 line PoC.</li>
<li><a href="https://matrix.org/blog/2020/05/06/cross-signing-and-end-to-end-encryption-by-default-is-here" target="_blank">Matrix enables end-to-end encryption by default</a>. The go-to choice for privacy respecting chat services just enabled end-to-end encryption by default after a long beta period. For federated, self-hostable, encrypted messaging and chat rooms Matrix + <a href="https://about.riot.im/" target="_blank">Riot</a> is the way to go. For ease of use, <a href="https://www.signal.org/" target="_blank">Signal</a> wins for now.</li>
<li><a href="https://thunderspy.io/" target="_blank">Thunderspy: When Lightning Strikes Thrice: Breaking Thunderbolt 3 Security</a> is an evolution to Thunderbolt Direct Memory Access (DMA) attacks that re-flashes the Thunderbolt controller flash to allow classic DMA attacks. This enables an attacker with physical access to a running, locked Windows or Linux machine (macOS has additional protections that are not bypassed), even with full disk encryption, to be accessed in under 5 minutes. Some laptops produced after 2019 have mitigations, but many do not. Take 5 minutes to <a href="https://youtu.be/7uvSZA1F9os" target="_blank">watch the demo</a> and think twice about leaving your running laptop unattended. Full paper <a href="https://thunderspy.io/assets/reports/breaking-thunderbolt-security-bjorn-ruytenberg-20200417.pdf" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1200/" target="_blank">T1200 Hardware Additions</a>]</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.youtube.com/watch?v=VTTq-wBFu-o" target="_blank">POWER-SUPPLaY</a> manages to use the power supply of a computer to transmit data ultrasonically at 50bit/sec by manipulating the internal switching frequency of the power supply, controlling the sound waveforms generated from its capacitors and transformers. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1011/" target="_blank">T1011 Exfiltration Over Other Network Medium</a>]</li>
<li><a href="https://www.mdsec.co.uk/2020/05/t1111-two-factor-interception-rsa-securid-software-tokens/" target="_blank">T1111: Two Factor Interception, RSA SecurID Software Tokens</a>. Rio Sherri demonstrates how to extract RSA SecureID Tokens silently, without process injection, or suspect API calls, just COM. Code <a href="https://github.com/0x09AL/RsaTokenExtractor" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1111/" target="_blank">T1111 Two-Factor Authentication Interception</a>]</li>
<li><a href="https://ijustwannared.team/2020/05/05/com-hijacking-for-lateral-movement/" target="_blank">COM Hijacking for Lateral Movement</a>. Given credentials and the need to move latterly, this tool enables remote registry and uses COM hijacking to get code running on remote systems. While it will probably bypass most anti-virus or other detections, it could fail catastrophically (major registry modifications), so use with care.  Demo <a href="https://video.wordpress.com/embed/DffWZr3q" target="_blank">here</a>, tool <a href="https://github.com/ThunderGunExpress/DCOM_Work" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1175/" target="_blank">T1175 Component Object Model and Distributed COM</a>]</li>
<li><a href="https://gist.github.com/tyranid/c65520160b61ec851e68811de3cd646d" target="_blank">Using TrustedInstaller to disable Protect Process Light services</a>. Normally, even Administrator cannot disable a Protected Service, but this trick uses TrustedInstaller to allow an Administrator to disable Windows Defender (or any other protected service). Extra points for its simplicity. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1089/" target="_blank">T1089 Disabling Security Tools</a>]</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt>Windows loaders [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1066/" target="_blank">T1066 Indicator Removal from Tools</a>]</dt>
<dd><ul>
<li><a href="https://github.com/Flangvik/NetLoader" target="_blank">NetLoader</a> loads any C# binary in memory, patching AMSI, and bypassing Windows Defender. It includes  tons of C# tools and an MSBuld payload.</li>
<li><a href="https://github.com/slaeryan/FALCONSTRIKE" target="_blank">FALCONSTRIKE</a> a stealthy, targeted Windows Loader for delivering second-stage payloads (shellcode) to the host machine undetected. Blog post <a href="https://slaeryan.github.io/posts/falcon-zero-alpha.html" target="_blank">here</a>.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://rastamouse.me/2020/05/sharpc2/" target="_blank">SharpC2</a> is a new .NET C2 framework "proof of concept" that looks fairly polished. It has a modular design, supports many "advanced" features (port forwarding, PPID spoofing, ETW patching), and has a nice web UI on the server side. Code <a href="https://github.com/SharpC2/SharpC2/tree/dev" target="_blank">here</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1071/" target="_blank">T1071 Standard Application Layer Protocol</a>]</li>
<li><a href="https://github.com/zznop/drow" target="_blank">drow</a> is a command-line utility that is used to inject code and hook the entrypoint of ELF executables (post-build). It takes unmodified ELF executables as input and exports a modified ELF containing an embedded user-supplied payload that executes at runtime. This is the linux "easy button" of stealthy persistence. Find a binary that runs on boot or on a schedule and infect it with drow to run your implant as well as its normal job. Be sure to fork or inject to allow the process to function normally (don't block). [<a class="m-text m-dim" href="https://attack.mitre.org/tactics/TA0003/" target="_blank">TA0003 Persistence</a>]</li>
<li><a href="https://github.com/decoder-it/NetworkServiceExploit" target="_blank">NetworkServiceExploit</a> is a self contained binary to escalate from Network Service to SYSTEM on windows when a SYSTEM token is available. Use this with last week's <a href="https://github.com/itm4n/PrintSpoofer" target="_blank">Print Spoofer</a> if <a href="https://github.com/itm4n/FullPowers" target="_blank">FullPowers</a> isn't working for you. I suspect next week we will see a tool that combines all three of these in a "one click to SYSTEM" binary. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
<li><a href="https://github.com/PaperMtn/slack-watchman" target="_blank">slack-watchman</a> monitors your (or your target's) Slack workspaces for sensitive information. Given a Slack API key this tool will search for sensitive files (API keys, certificates, passwords, etc) and generate a report. Useful for both red and blue teams.</li>
<li><a href="https://github.com/maxpl0it/CVE-2020-0674-Exploit" target="_blank">CVE-2020-0674-Exploit</a> is a UAF exploit for the x64 version of IE 8, 9, 10, and 11 on Windows 7 that was patched in January 2020 after it was found being exploited in the wild as an 0day. This could be handy when targeting legacy workstations in a corporate environment (out of date and forced to use IE). [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1192/" target="_blank">T1192 Spearphishing Link</a>]</li>
<li><a href="https://github.com/InfosecMatter/Minimalistic-offensive-security-tools" target="_blank">Minimalistic-offensive-security-tools</a> are short but useful powershell scripts that can be used in VDI or other restricted environments where you may have to manually recreate your security tools.</li>
<li><a href="https://github.com/benbusby/whoogle-search" target="_blank">whoogle-search</a> is a self-hosted, ad-free, privacy-respecting proxy for Google search. Think of it as a first step to search privacy. The next step is <a href="https://github.com/asciimoo/searx" target="_blank">searx</a>.</li>
<li><a href="https://github.com/steeve/itool" target="_blank">itool</a> is an easy iOS and composable device management command line interface. It was made to simplify and automate common development and provisioning tasks, but could be used to assist with iOS app hacking as well.</li>
<li><a href="https://github.com/tothi/rbcd-attack" target="_blank">rbcd-attack</a>  is a practical attack against Kerberos Resource-Based Constrained Delegation in a Windows Active Directory Domain.</li>
<li><a href="https://github.com/Accenture/CLRvoyance" target="_blank">CLRvoyance</a> is a shellcode kit that supports bootstrapping managed assemblies into unmanaged (or managed) processes. It provides three different implementations of position independent shellcode for CLR hosting, as well as a generator script for quickly embedding a managed assembly in position independent shellcode.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/HoShiMin/Kernel-Bridge" target="_blank">Kernel-Bridge</a> is a Windows kernel hacking framework, driver template, hypervisor, and API written on C++ but the magic is that it is a signed kernel driver that is allowed in SecureBoot and allows all kinds of kernel tampering. It seems strange that Microsoft allows this.</li>
<li><a href="https://github.com/cytopia/pwncat" target="_blank">pwncat</a> - netcat on steroids with Firewall, IDS/IPS evasion, bind and reverse shell, and port forwarding magic; fully scriptable with Python.</li>
<li><a href="https://www.beekeeperstudio.io/" target="_blank">Beekeeper Studio</a> is a cross platform open source SQL editor and Database manager that works with MySQL/MariaDB, Postgres, SQLite, SQL Server, and Amazon Redshift.</li>
<li><a href="https://github.com/CERT-Polska/drakvuf-sandbox" target="_blank">DRAKVUF Sandbox</a> is an automated black-box malware analysis system with <a href="https://drakvuf.com/" target="_blank">DRAKVUF</a> engine under the hood, which does not require an agent on guest OS.</li>
<li><a href="https://github.com/ionescu007/faxhell" target="_blank">faxhell</a> is a bind shell using the Fax service and a DLL hijack based on Ualapi.dll. A good base for stealthy persistence in Windows.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
