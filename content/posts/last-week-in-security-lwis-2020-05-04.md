Title: Last Week in Security (LWiS) - 2020-05-04
Date: 2020-05-04 06:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-05-04
Author: Erik
Summary: Wormable account takeover via GIF in MS Teams by <a href="https://twitter.com/CyberArk" target="_blank">@CyberArk</a>, asynchronous password spraying in C# by <a href="https://twitter.com/ustayready" target="_blank">@ustayready</a>, NTLM relay improvements from <a href="https://twitter.com/SecureAuth" target="_blank">@SecureAuth</a>, Chrome extension hacking and defense by <a href="https://twitter.com/IAmMandatory" target="_blank">@IAmMandatory</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-04-27 to 2020-05-04.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://siguza.github.io/psychicpaper/" target="_blank">iOS Sandbox escape "Psychic Paper" 0day released</a>. It turns out having 4 custom XML parsers leads to trivial sandbox escape. The patch ironically adds two additional parsers. I would hope Apple is screening App Store apps to prevent this from <a href="https://wojciechregula.blog/post/stealing-your-sms-messages-with-ios-0day/" target="_blank">being abused</a>.</li>
<li><a href="https://www.cyberark.com/threat-research-blog/beware-of-the-gif-account-takeover-vulnerability-in-microsoft-teams/" target="_blank">Beware of the GIF: Account Takeover Vulnerability in Microsoft Teams</a>. Subdomain takeover combined with the way Teams includes GIFs allowed the Cyberark team to exfiltrate user's json web tokens which allows them to scrape messages if a user views their GIF. This is extra powerful because the JWT also allows the attacker to impersonate the victim and send the GIF to all contacts, essentially making this vulnerability wormable. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1193/" target="_blank">T1193 Spearphishing Attachment</a>]</li>
<li><a href="https://www.fcc.gov/document/fcc-scrutinizes-four-chinese-government-controlled-telecom-entities" target="_blank">FCC Scrutinizes Four Chinese Government-Controlled Telecom Entities</a>. The FFC issues show cause orders to China Telecom Americas, China Unicom Americas, Pacific Networks, and ComNet demanding explanation of why the FCC should not initiate proceedings to revoke their authorizations. These Telecoms have 30 days to prove their operations and subsidiaries are "not subject to the influence and control of the Chinese government."</li>
<li><a href="https://www.patreon.com/posts/36524207" target="_blank">#OBTS v3.0 Talks &amp; Photos</a> All the slides from the macOS security conference "Objective by the Sea" have been posted.</li>
<li><dl>
<dt>Other "Weeks"</dt>
<dd><ul>
<li><a href="https://bushidotoken.blogspot.com/2020/05/this-week-in-malware.html" target="_blank">This Week in Malware</a> - day by day malware news.</li>
<li><a href="https://medium.com/week-in-osint" target="_blank">Week in OSINT</a> - your weekly dose of OSINT sites and tools!</li>
<li><a href="https://www.lastweekinaws.com/" target="_blank">Last Week in AWS</a> - weekly newsletter focused excessively on AWS.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon" target="_blank">Sysmon v11 Released</a> and includes file delete monitoring and archive to help responders capture attacker tools and adds an option to disable reverse DNS lookup. This will be huge for defenders allowing them to easily get samples of malware that only exists on disk for a short period of time.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://krebsonsecurity.com/2020/04/would-you-have-fallen-for-this-phone-scam/" target="_blank">Would You Have Fallen for This Phone Scam?</a> This article details a complex vishing attack that fooled a security expert. Always hang up and call your bank back if contacted. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1199/" target="_blank">T1199 Trusted Relationship</a>]</li>
<li><a href="https://github.com/ChrisMiuchiz/Plasma-Writeup" target="_blank">Restoring Picroma Plasma Without Patching it</a> is a detailed writeup of the entire process of creating a license server for vector image editor (Picroma). The reverse engineering concepts are generally applicable.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2020/4/28/cve-2020-0932-remote-code-execution-on-microsoft-sharepoint-using-typeconverters" target="_blank">CVE-2020-0932: Remote Code Execution on Microsoft SharePoint Using TypeConverters</a> is an echo of last spring's SharePoint remote code execution vulnerability. Zero Day Initiative breaks it down in this post. Proof of Concept on <a href="https://github.com/thezdi/PoC/tree/master/CVE-2020-0932" target="_blank">Github</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://shells.systems/open-audit-v3-3-1-remote-command-execution-cve-2020-12078/" target="_blank">Open-AudIT v3.3.1 Remote Command Execution (CVE-2020-12078)</a> shows the process of auditing a PHP application, finding a remote command execution vulnerability, and writing an exploit. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://github.com/p3nt4/Nuages/wiki/Tutorial:-Creating-a-custom-full-featured-implant" target="_blank">Tutorial: Creating a custom full featured implant</a> is a nice tutorial on using the Nuages C2 framework to bootstrap an implant quickly. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1094/" target="_blank">T1094 Custom Command and Control</a>]</li>
<li><a href="https://www.secureauth.com/blog/what-old-new-again-relay-attack" target="_blank">What is old is new again: The Relay Attack</a> discusses additions to <a href="https://github.com/SecureAuthCorp/impacket/blob/master/examples/ntlmrelayx.py" target="_blank">ntlmrelayx.py</a> allowing multi-relay attacks, i.e. using just a single connection to attack several targets. On top of this, Secure Auth added the capability of relaying connections for specific target users. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1171/" target="_blank">T1171 LLMNR/NBT-NS Poisoning and Relay</a>]</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt>Windows Local Privilege Escalation [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</dt>
<dd><ul>
<li><a href="https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/" target="_blank">Printer Spoofer - Abusing Impersonation Privileges on Windows 10 and Server 2019</a> is another great post from <a href="https://twitter.com/itm4n" target="_blank">@itm4an</a> that enables local service to SYSTEM escilation as long as SeImpersonatePrivilege is enabled. Don't have SeImpersonatePrivilege? <a href="https://github.com/itm4n/FullPowers" target="_blank">No problem</a>. This means that any exploit that lands you as local service now gets you SYSTEM on Windows 10 or Server 2016/2019. What a time to be alive. Code <a href="https://github.com/itm4n/PrintSpoofer" target="_blank">here</a>, Powershell <a href="https://github.com/S3cur3Th1sSh1t/Creds/blob/master/PowershellScripts/printspoof_interactive.ps1" target="_blank">here</a>.</li>
<li><a href="https://github.com/active-labs/Advisories/blob/master/2020/ACTIVE-2020-003.md" target="_blank">Trident Z Lighting Control Driver Local Privilege Escalation</a>. Another gaming driver provides local privilege escalation.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/mandatoryprogrammer/CursedChrome" target="_blank">CursedChrome</a> is a Chrome-extension implant that turns victim Chrome browsers into fully-functional HTTP proxies, allowing you to browse sites as your victims. To defend against this, use <a href="https://github.com/mandatoryprogrammer/ChromeGalvanizer" target="_blank">ChromeGalvanizer</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1176/" target="_blank">T1176 Browser Extensions</a> and <a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1185/" target="_blank">T1185 Man in the Browser</a>]</li>
<li><a href="https://github.com/xfhg/intercept" target="_blank">intercept</a> is a stupidly easy to use, small footprint Policy as Code subsecond command-line scanner that leverages the power of the fastest multi-line search tool to scan your codebase. It can be used as a linter, guard rail control or simple data collector and inspector. Consider it a cross-platform weaponized ripgrep. I could see this being used to audit large amounts of code for similar vulnerabilities.</li>
<li><a href="https://github.com/evilpenguin/BoringSSLKeys" target="_blank">BoringSSLKeys</a> allows the extraction of BoringSSL keys from jailbroken iOS devices to enable the decryption of pcaps of collected from apps.</li>
<li><a href="https://github.com/FSecureLABS/Ninjasploit" target="_blank">Ninjasploit</a> is meterpreter extension for applying hooks to avoid windows defender memory scans. Details on the <a href="https://labs.f-secure.com/blog/bypassing-windows-defender-runtime-scanning/" target="_blank">F-Secure Blog</a>. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1066/" target="_blank">T1066 Indicator Removal from Tools</a>]</li>
<li><a href="https://github.com/ustayready/SharpHose" target="_blank">SharpHose</a> is an asynchronous Password Spraying Tool in C# for Windows Environments. It can be executed via Cobalt Strikes execute-assembly (or your in-memory C# loader of choice).</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/devanshbatham/ParamSpider" target="_blank">ParamSpider</a> helps discover http parameters by mining parameters from the dark corners of Web Archives.</li>
<li><a href="https://github.com/EUA/wxHexEditor" target="_blank">wxHexEditor</a> is a great cross platform free and open source hex editor.</li>
<li><a href="https://github.com/microsoft/DbgShell" target="_blank">DbgShell</a> is a PowerShell front-end for the Windows debugger engine.</li>
<li><a href="https://github.com/federicodotta/ysoserial" target="_blank">ysoserial fork</a> is a fork of the official great ysoserial project with some improvements added to create payloads for the Burp Suite plugin Java Deserialization Scanner and more generally to speed-up and improve the detection and the exploitation of Java serialization issues with ysoserial.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
