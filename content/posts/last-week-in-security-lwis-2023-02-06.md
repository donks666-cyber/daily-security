Title: Last Week in Security (LWiS) - 2023-02-06
Date: 2023-02-06 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-02-06
Author: Erik
Summary: Pre-Auth RCE (<a href="https://twitter.com/infosec_au" target="_blank">@infosec_au</a> + <a href="https://twitter.com/TheGrandPew" target="_blank">@TheGrandPew</a>), IP phone pwnage (Dylan Pindur), GoAnywhere RCE (<a href="https://twitter.com/frycos" target="_blank">@frycos</a>), Toyota supplier network hack (<a href="https://twitter.com/XeEaton" target="_blank">@XeEaton</a>), PipeViewer (<a href="https://twitter.com/g3rzi" target="_blank">@g3rzi</a>), reverse socks5 (<a href="https://twitter.com/aceb0nd" target="_blank">@aceb0nd</a>), certsync, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-01-30 to 2023-02-06.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2023/02/taking-next-step-oss-fuzz-in-2023.html" target="_blank">Taking the next step: OSS-Fuzz in 2023</a>. Increased bounties for integrating projects into OSS-Fuzz. Nice!</li>
<li><a href="https://www.vice.com/en/article/wxnve9/dutch-police-read-messages-of-exclu" target="_blank">Dutch Police Read Messages of Encrypted Messenger 'Exclu'</a>. If you messenger is not open source and the server is not self-hosted, someone could be reading your messages. Yes, this includes Signal (what is actually running on the servers?).</li>
<li><a href="https://github.com/es0j/CVE-2023-0045" target="_blank">CVE-2023-0045</a>. Speculative execution bugs are going to be with us for a while. "The current implementation of the prctl syscall for speculative control fails to protect the user against attackers executing before the mitigation. The seccomp mitigation also fails in this scenario."</li>
<li><a href="https://blog.google/technology/ai/bard-google-ai-search-updates/" target="_blank">An important next step on our AI journey</a>. Google's response to ChatGPT is... a blog post and no working product? Meanwhile, I'm out here having GPT-3 write my <a href="https://github.com/zurawiki/gptcommit" target="_blank">commit messages</a>.</li>
<li><a href="https://github.com/orgs/community/discussions/45830" target="_blank">Checksum mismatches on .tar.gz files</a>. GitHub temporarily broke a lot of deployments after changing the default compression algorithm for releases. The change has been reverted, but showed how fragile the some software release ecosystems are and how reliant they are on a single third party.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.assetnote.io/2023/02/02/pre-auth-rce-aspera-faspex/" target="_blank">Pre-Auth RCE in Aspera Faspex: Case Guide for Auditing Ruby on Rails</a>. The first of two great posts from Assetnote this week.</li>
<li><a href="https://blog.assetnote.io/2023/02/01/rce-in-avaya-aura/" target="_blank">RCE in Avaya Aura Device Services</a>. This is the second post. They're pwning your phone system too...</li>
<li><a href="https://gynvael.coldwind.pl/?id=763" target="_blank">2023-02-05: Solving a VM-based CTF challenge without solving it properly</a>. A neat solve of a hard challenge with using side channels to not "actually" solve it. Hey, a flag is a flag.</li>
<li><a href="https://marcoramilli.com/2023/02/04/onenote-malware-classification-and-personal-notes/" target="_blank">Onenote Malware: Classification and Personal Notes</a>. '.one' based droppers are on the rise. Grab yourself <a href="https://github.com/knight0x07/OneNoteAnalyzer" target="_blank">OneNoteAnalyzer</a>, a C# based tool for analyzing malicious OneNote documents, and dig in.</li>
<li><a href="https://research.nccgroup.com/2023/02/06/rustproofing-linux-part-1-4-leaking-addresses/" target="_blank">Rustproofing Linux (Part 1/4 Leaking Addresses)</a>. While Rust provides some very nice memory safety, it also has to exist in the real world, where programmers will use 'unsafe' blocks to interact with raw memory and hardware. This series aims to show what can go wrong with 'unsafe' rust. Rust is pretty awesome though, as it can <a href="https://github.blog/2023-02-06-the-technology-behind-githubs-new-code-search/" target="_blank">regex search 45 million repos in seconds</a>.</li>
<li><a href="https://eaton-works.com/2023/02/06/toyota-gspims-hack/" target="_blank">Hacking into Toyota's global supplier management network</a>. I like these "real world" hacks that don't stop at "oh I can get access," but build on that to show how bad the combination of flaws can be. Bravo. The $0 bounty is rough.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://bishopfox.com/blog/spoofy-email-domain-spoofing" target="_blank">Spoofy: An Email Domain Spoofing Tool</a>. This is the new gold standard of "can I spoof this domain?" tools.</li>
<li><a href="https://frycos.github.io/vulns4free/2023/02/06/goanywhere-forgotten.html" target="_blank">GoAnywhere MFT - A Forgotten Bug</a>. Some serious Java web app code review leads to - you guessed it - hard coded keys and a deserialization vulnerability.</li>
<li><a href="https://github.com/CoolElectronics/sh1mmer" target="_blank">sh1mmer</a> chromebook jailbreak. This is a cool "jailbreak" for Chromebooks that uses a modified Google signed RMA shim to boot into an environment that allows unenrolling Chromebooks from their parent organization.</li>
<li><a href="https://github.com/cyberark/PipeViewer" target="_blank">PipeViewer</a> - A tool that shows detailed information about named pipes in Windows. For why, read <a href="https://www.cyberark.com/resources/threat-research-blog/breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1" target="_blank">Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation - Part 1</a>.</li>
<li><a href="https://github.com/crisprss/RasmanPotato" target="_blank">RasmanPotato</a> - Abuse Impersonate Privilege from Service to SYSTEM like other potatoes do.</li>
<li><a href="https://github.com/CMEPW/BypassAV" target="_blank">BypassAV</a> This map lists the essential techniques to bypass anti-virus and EDR.</li>
<li><a href="https://github.com/reveng007/AMSI-patches-learned-till-now" target="_blank">AMSI-patches-learned-till-now</a> - all of the AMSI patches that I learned till now.</li>
<li><a href="https://github.com/TheD1rkMtr/AMSI_patch" target="_blank">AMSI_patch</a> - Patching AmsiOpenSession by forcing an error branching.</li>
<li><a href="https://twitter.com/duff22b/status/1622344090640855040" target="_blank">Bloodhound python from @_dirkjan is now integrated to CrackMapExec as a core feature</a>.</li>
<li><a href="https://github.com/GhostManager/Ghostwriter/releases/tag/v3.2.0" target="_blank">Ghostwriter</a>. Automate those reports!</li>
<li><a href="https://github.com/Acebond/ReverseSocks5" target="_blank">ReverseSocks5</a> - Single executable reverse socks5 proxy written in Golang.</li>
<li><a href="https://github.com/zblurx/certsync" target="_blank">certsync</a> - Dump NTDS with golden certificates and UnPAC the hash.</li>
<li><a href="https://github.com/mandatoryprogrammer/comfortably-run" target="_blank">comfortably-run</a> - A CLI tool which can be used to inject JavaScript into arbitrary Chrome origins via the Chrome DevTools Protocol.</li>
<li><a href="https://github.com/TheD1rkMtr/D1rkLrd" target="_blank">D1rkLrd</a> - Shellcode Loader with Indirect Dynamic syscall Implementation , shellcode in MAC format, API resolving from PEB, Syscall calll and syscall instruction address resolving at run time.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/pr0v3rbs/FirmAE" target="_blank">FirmAE</a> - Towards Large-Scale Emulation of IoT Firmware for Dynamic Analysis.</li>
<li><a href="https://github.com/aleixrodriala/wa-tunnel" target="_blank">wa-tunnel</a> -Tunneling Internet traffic over Whatsapp.</li>
<li><a href="https://github.com/OmriBaso/RToolZ" target="_blank">RToolZ</a> - A Stealthy Lsass Dumper - can abuse ProcExp152.sys driver to dump PPL Lsass, no dbghelp.lib calls.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+1)</p>
<p>Blogs monitored: 336 (+0)</p>
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
