Title: Last Week in Security (LWiS) - 2021-09-14
Date: 2021-09-14 20:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-09-14
Author: Erik
Summary: Word RCE, Advanced Nim tradecraft (<a href="https://twitter.com/snovvcrash" target="_blank">@snovvcrash</a>), TCC bypass (<a href="https://twitter.com/_r3ggi" target="_blank">@_r3ggi</a>), encrypted heap allocations (<a href="https://twitter.com/waldoirc" target="_blank">@waldoirc</a>), vuln hunting with binary ninja (<a href="https://twitter.com/renorobertr" target="_blank">@renorobertr</a>), token priv manipulation BOF (<a href="https://twitter.com/the_bit_diddler" target="_blank">@the_bit_diddler</a> + <a href="https://twitter.com/hackersoup" target="_blank">@hackersoup</a>), Outlook for C2 (<a href="https://twitter.com/0xBoku" target="_blank">@0xBoku</a>), automated DLL hijacking (<a href="https://twitter.com/knight0x07" target="_blank">@knight0x07</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-09-07 to 2021-09-14 (bonus day!).</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2021/09/introducing-androids-private-compute.html" target="_blank">Introducing Android’s Private Compute Services</a>. Google is aiming to put the Private Compute Core from Android in the cloud and they're vouching to do 3rd party validation via audits.</li>
<li><a href="https://portswigger.net/daily-swig/vmware-denies-allegations-it-leaked-confluence-rce-exploit" target="_blank">VMware denies allegations it leaked Confluence RCE exploit</a>. Bug bounty drama as a payload sent to VMware as part of a bounty was later <a href="https://github.com/projectdiscovery/nuclei-templates/pull/2529/commits/f1f5add7971078c239c9862c361f834fa9bdbb61" target="_blank">added to the Nuclei scanner</a> by a researcher who claimed they found it via "Pastebin scraping" and could not produce the source URL to the paste. Bug bounties rely on trust, and these types of incidents underscore that.</li>
<li><a href="https://citizenlab.ca/2021/09/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/" target="_blank">FORCEDENTRY NSO Group iMessage Zero-Click Exploit Captured in the Wild</a>. If your threat model includes nation states with massive war chests willing to burn 0days to get on your device, I think any stock OS is going to be insufficient to protect you. Perhaps the best way to fight against this type of exploitation is to capture and expose the exploits fast enough to make it economically unfeasible to use them against activists? Props to Citizen Lab for doing the work here.</li>
<li><a href="https://www.vice.com/en/article/3aq9a5/us-company-sold-zero-click-exploit-project-raven-uae" target="_blank">U.S. Company Sold Zero-Click Hacking Tool to UAE Spy Operation</a>. Three members of the <a href="https://www.reuters.com/investigates/special-report/usa-spying-raven" target="_blank">RAVEN</a> crew pled guilty in exchange for a three-year deferred prosecution agreement and fines. Interesting that the CFAA wasn't used in this case, as it is typically the hammer for anything computer related. How much taxpayer money did the US spend investigating and prosecuting these three? Imagine if the US Government instead paid competitive salaries so their own hackers didn't travel to the Middle East and hack for other governments...</li>
<li><a href="https://twitter.com/peter_szilagyi/status/1437646118700175360" target="_blank">Between the 3 Sept and 10 Sept, secure env vars of *all* public @travisci repositories were injected into PR builds.</a>. Self host that CI/CD, that way the mistakes are your own.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="http://noahblog.360.cn/burp-suite-rce/?fbclid=IwAR1rLHh_8tL7PqEyY3WJQkVvlqqXcFNCN5_avycMdERigIaClrvjHdIFBt8" target="_blank">Burp Suite RCE</a>. The built-in Chrome browser in Burp Suite 2.0 is an old Chrome version, which can be combined with the "Use dynamic analysis techniques" feature to trigger RCE on an assessors Windows machine by simply browsing a site via the embedded Chrome browser. Is this ultimate WAF? Ransomware any Burp Suite users that browse your site?</li>
<li><a href="https://labs.detectify.com/2021/09/13/hacking-cloudkit-how-i-accidentally-deleted-your-apple-shortcuts/" target="_blank">Hacking CloudKit - How I accidentally deleted your Apple Shortcuts</a>. Even the big companies are not immune to misconfigured access controls. In this case the result was an assessor was able to delete all shared "shortcuts" links for iOS.</li>
<li><a href="https://secret.club/2021/09/08/vmprotect-llvm-lifting-1.html" target="_blank">Tickling VMProtect with LLVM: Part 1</a>. This series gets into the weeds of using LLVM as a software based deobfuscation framework that initially targets binaries protected with VMProtect.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2021/9/9/analysis-of-a-parallels-desktop-stack-clash-vulnerability-and-variant-hunting-using-binary-ninja" target="_blank">Analysis of a Parallels Desktop Stack Clash Vulnerability and Variant Hunting using Binary Ninja</a>. Supporting macOS back to 10.13 had the effect of silently dripping stack protections, and the author uses the Binary Ninja Python API to help automate bug finding.</li>
<li><a href="https://wojciechregula.blog/post/change-home-directory-and-bypass-tcc-aka-cve-2020-27937/" target="_blank">Change home directory and bypass TCC aka CVE-2020-27937</a>. By planting your own TCC database you can bypass the whole user TCC (Desktop, Documents, Address Book, Camera, Microphone, Photos and more).</li>
<li><a href="https://www.arashparsa.com/hook-heaps-and-live-free/" target="_blank">Hook Heaps and Live Free</a>. Ecnrypted heap allocations. Now that is some legit tradecraft! This post is a gold mine of information about "in memory evasion" and practical examples of how to implement it with Cobalt Strike. Example code (for the first basic example) <a href="https://github.com/waldo-irc/LockdExeDemo" target="_blank">here</a>. If you liked this post be sure to check out <a href="https://www.solomonsklash.io/SleepyCrypt-shellcode-to-encrypt-a-running-image.html" target="_blank">SleepyCrypt: Encrypting a running PE image while it sleeps</a> which also dropped last week.</li>
<li><a href="https://www.sentinelone.com/labs/cve-2021-3437-hp-omen-gaming-hub-privilege-escalation-bug-hits-millions-of-gaming-devices/" target="_blank">CVE-2021-3437 | HP OMEN Gaming Hub Privilege Escalation Bug Hits Millions of Gaming Devices</a>. Perhaps its time to download any gaming related drivers and do a vulnerability hunt... 🤔</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt><a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40444" target="_blank">Microsoft MSHTML Remote Code Execution Vulnerability CVE-2021-40444</a>. This was the big news of last week. RCE from simply opening a Word doc, thanks to old friends - directory traversal, IE, and ActiveX.</dt>
<dd><ul>
<li><a href="https://twitter.com/Dinosn/status/1436268750689480707" target="_blank">Demo of an RTF variant working in the explorer preview</a></li>
<li><a href="https://blog.nviso.eu/2021/09/09/kusto-hunting-query-for-cve-2021-40444/" target="_blank">KQL query</a></li>
<li><a href="https://github.com/lockedbyte/CVE-2021-40444" target="_blank">Malicious docx generator</a></li>
<li><a href="https://www.bleepingcomputer.com/news/microsoft/windows-mshtml-zero-day-defenses-bypassed-as-new-info-emerges/" target="_blank">Windows MSHTML zero-day defenses bypassed as new info emerges</a></li>
<li><a href="https://xret2pwn.github.io/CVE-2021-40444-Analysis-and-Exploit/" target="_blank">CVE-2021-40444 Analysis/Exploit</a> - This is the best analysis/walkthrough I have come across.</li>
<li><a href="https://blog.palantir.com/microsoft-defender-attack-surface-reduction-recommendations-a5c7d41c3cf8" target="_blank">Microsoft Defender Attack Surface Reduction recommendations</a> - Old but gold. <a href="https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide#block-all-office-applications-from-creating-child-processes" target="_blank">"Block all Office applications from creating child processes"</a> is what you want for this vulnerability specifically.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://gitlab.com/nephosec/bof-adios" target="_blank">BOF-Adios</a> is a BOF that will zero, then delete your beacon's executable on exit! Useful if you are dropping a loader to disk as part of a phishing campaign.</li>
<li><a href="https://github.com/snovvcrash/NimHollow" target="_blank">NimHollow</a> is a Nim implementation of Process Hollowing using syscalls with some nice features like shellcode encryption, sandbox detection, and AMSI patching.</li>
<li><a href="https://github.com/BishopFox/iam-vulnerable" target="_blank">iam-vulnerable</a> - Use Terraform to create your own vulnerable by design AWS IAM privilege escalation playground. More details on the <a href="https://labs.bishopfox.com/tech-blog/iam-vulnerable-an-aws-iam-privilege-escalation-playground" target="_blank">BishopFox blog</a>.</li>
<li><a href="https://github.com/EspressoCake/Toggle_Token_Privileges_BOF" target="_blank">Toggle_Token_Privileges_BOF</a> is an (almost) syscall-only BOF file intended to either add or remove token privileges within the context of your current process.</li>
<li><a href="https://github.com/cube0x0/SharpSystemTriggers" target="_blank">SharpSystemTriggers</a> is a collection of remote authentication triggers coded in C# using MIDL compiler for avoiding 3rd party dependencies.</li>
<li><a href="https://github.com/boku7/azureOutlookC2" target="_blank">azureOutlookC2</a> - Azure Outlook Command &amp; Control (C2) - Remotely control a compromised Windows Device from your Outlook mailbox. Threat Emulation Tool for North Korean APT InkySquid / ScarCruft / APT37. TTP: Use Microsoft Graph API for C2 Operations.</li>
<li><a href="https://github.com/knight0x07/ImpulsiveDLLHijack" target="_blank">ImpulsiveDLLHijack</a> is a C# tool which automates the process of discovering and exploiting DLL Hijacks in target binaries. The Hijacked paths discovered can later be weaponized during Red Team Operations to evade EDR's.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/OWASP/wwwgrep" target="_blank">wwwgrep</a> is a rapid search “grepping” mechanism that examines HTML elements by type and permits focused (single), multiple (file based URLs) and recursive (with respect to root domain or not) searches to be performed.</li>
<li><a href="https://github.com/mrexodia/AppInitHook" target="_blank">AppInitHook</a> is a global user-mode hooking framework, based on AppInit_DLLs. The goal is to allow you to rapidly develop hooks to inject in an arbitrary process. Developed to reverse engineer and customize random applications, it has broad implications for read teaming.</li>
<li><a href="https://github.com/mgeeky/ElusiveMice" target="_blank">ElusiveMice</a> is a Cobalt Strike User-Defined Reflective Loader with AV/EDR Evasion in mind.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
