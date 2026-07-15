Title: Last Week in Security (LWiS) - 2024-09-03
Date: 2024-09-03 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-09-03
Author: Erik
Summary: argv[0] tampering (<a href="https://x.com/wietze" target="_blank">@Wietze</a>), Moodle eval() misuse (<a href="https://x.com/redteampt" target="_blank">@RedTeamPT</a>), ntoskrnl.exe PoC (<a href="https://x.com/b1thvn_" target="_blank">@b1thvn_</a>), 4x wappd exploits (<a href="https://x.com/hyprdude" target="_blank">@hyprdude</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-08-26 to 2024-09-03.</p>
<aside class="m-block m-success">
<h3>LWiS #200</h3>
<p>This post marks the 200th edition of Last Week in Security. The first post was <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2020-02-10.html">2020-02-10</a>, and we've published almost every week since. If you have enjoyed the content, or it's made it easier to keep up with the fast pace of cybersecurity, please share it with your friends and colleagues!</p>
<p>Here's to 200 more 🍻</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://techcommunity.microsoft.com/t5/windows-it-pro-blog/windows-app-general-availability-coming-soon/ba-p/4206647" target="_blank">Windows App general availability coming soon</a> - The Remote Desktop app on macOS/iOS is being renamed to "Windows App." I'm sure no one will find that confusing.</li>
<li><a href="https://www.intrinsec.com/wp-content/uploads/2024/08/TLP-CLEAR-20240828-The-EV-Signature-Market-EN.pdf" target="_blank">[PDF] The EV Code Signature Market for eCrime</a> - Criminals are getting "extended validation" (EV) certificates for $2,000 to $6,000 to bypass antivirus. Are you assessors emulating this threat?</li>
<li><a href="https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/" target="_blank">State-backed attackers and commercial surveillance vendors repeatedly use the same exploits</a> - The question is: did they buy the exploits, steal them, or find them in the wild and repurpose them?</li>
<li><a href="https://x.com/PratyushRT/status/1828183761055330373" target="_blank">[X] Lets breakdown this Intel SGX (TEE) breach.</a> - Researchers have managed to leak Intel's Software Guard Extensions (SGX) Fuse Key0 from some older processors. This key was supposed to remain unknown to everyone (even Intel) to maintain the security of SGX. Odds that a similar attack is possible on modern chips?</li>
<li><a href="https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/" target="_blank">Is Telegram really an encrypted messaging app?</a> - After the <a href="https://apnews.com/article/france-telegram-pavel-durov-arrest-6e213d227458f330ed16e7fe221a696c" target="_blank">Telegram CEO Pavel Durov</a> was arrested in France and charged with failing to sufficiently moderate content on Telegram, many have described Telegram as an "encrypted messaging app." This post breaks down the limited, and strange use of encryption in Telegram. And that is to say nothing of the metadata. For comparison review the <a href="https://signal.org/bigbrother/santaclara/" target="_blank">search warrant for Signal user data</a> and what they were able to provide.</li>
<li><a href="https://arstechnica.com/security/2024/09/yubikeys-are-vulnerable-to-cloning-attacks-thanks-to-newly-discovered-side-channel/" target="_blank">YubiKeys are vulnerable to cloning attacks thanks to newly discovered side channel</a> - Yubikeys sold before 2024-05-6 are vulnerable to a side-channel attack that can clone the key. The attack requires physical access to the key, partial disassembly, and an oscilloscope. They firmware of the Yubikey cannot be updated, so add a PIN to your keys or replace them if physical access is in your threat model, but note that physical access is <em>always</em> root access - it's just a matter of how difficult it is.</li>
<li><a href="https://posts.specterops.io/mythic-3-3-out-of-beta-9979e82660c3" target="_blank">Mythic 3.3 — Out of Beta</a> - New Mythic is out with new features like file previews, a new file browser, interactive mode task output tracking, and host/bridge Docker networking options.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.zerodayinitiative.com/blog/2024/8/27/cve-2024-37079-vmware-vcenter-server-integer-underflow-code-execution-vulnerability" target="_blank">CVE-2024-37079: Vmware vCenter Server Integer Underflow Code Execution Vulnerability</a> - This vCenter heap overflow was patched in <a href="https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24453" target="_blank">June</a>, but this post delievers the details.</li>
<li><a href="https://www.wietzebeukema.nl/blog/why-bother-with-argv0" target="_blank">Why bother with argv[0]?</a> - "The first argument of a program's command line, typically reflecting the program's name/path and often referred to as argv[0], can in most cases be set to an arbitrary value without affecting the process' flow. Making the case against argv[0], this post demonstrates how it can be used to deceive security analysts, bypass detections and break defensive software, across all main operating systems."</li>
<li><a href="https://summoning.team/blog/progress-whatsup-gold-sqli-cve-2024-6670/" target="_blank">Breaking Down Barriers: Exploiting Pre-Auth SQL Injection In WhatsUp Gold: CVE-2024-6670</a> - Some .NET reversing and a little SQL injection result in remote code execution. Full PoC provided.</li>
<li><a href="https://blog.redteam-pentesting.de/2024/moodle-rce/" target="_blank">Back to School - Exploiting a Remote Code Execution Vulnerability in Moodle</a> - "If eval() is the answer, you're almost certainly asking the wrong question."</li>
<li><a href="https://gosecure.ai/blog/2024/08/30/key-and-e-a-pentesters-tale-on-how-a-photo-opened-real-doors/" target="_blank">Key and E: A Pentester's Tale on How a Photo Opened Real Doors</a> - Keys are the physical codes that open doors. Pictures of them are usually enough to clone them.</li>
<li><a href="https://www.pixiepointsecurity.com/blog/nday-cve-2024-38106/" target="_blank">Dissecting the CVE-2024-38106 Fix</a> - Quick breakdown and PoC for the ntoskrnl.exe bug patched on August 14.</li>
<li><a href="https://blog.coffinsec.com/0day/2024/08/30/exploiting-CVE-2024-20017-four-different-ways.html" target="_blank">4 exploits, 1 bug: exploiting cve-2024-20017 4 different ways</a> - My favorite post of the week. Love the in depth walk through as the mitigations ramp up. PoCs are <a href="https://github.com/mellow-hype/cve-2024-20017" target="_blank">here</a>.</li>
<li><a href="https://blog.scrt.ch/2024/09/02/ghost-in-the-ppl-part-3-lsass-memory-dump/" target="_blank">Ghost in the PPL Part 3: LSASS Memory Dump</a> - Perhaps the most complicated way to dump lsass memory, but an interesting read. <a href="https://github.com/Slowerzs/PPLSystem" target="_blank">PPLSystem</a> is the current go-to technique for PPL bypass or <a href="https://github.com/ricardojoserf/TrickDump" target="_blank">TrickDump</a> or <a href="https://github.com/ricardojoserf/NativeDump" target="_blank">NativeDump</a> if PPL is not enabled.</li>
<li><a href="https://cybenari.com/2024/08/whats-the-worst-place-to-leave-your-secrets/" target="_blank">What's the worst place to leave your secrets? - Research into what happens to AWS credentials that are left in public places</a> - Less than 60 seconds for a secret in an NPM package to be used is impressively fast.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/RedTeamOperations/Red-Infra-Craft/" target="_blank">Red-Infra-Craft</a> automates the deployment of powerful red team infrastructures! It streamlines the setup of C2s, makes it easy to create advanced phishing &amp; payload infrastructure.</li>
<li><a href="https://github.com/convisolabs/CVE-2024-43044-jenkins" target="_blank">CVE-2024-43044-jenkins</a> - Exploit for the vulnerability CVE-2024-43044 in Jenkins.</li>
<li><a href="https://github.com/Octoberfest7/enumhandles_BOF" target="_blank">enumhandles_BOF</a> - This BOF can be used to identify processes that hold handles to a given file. This can be useful to identify which process is locking a file on disk.</li>
<li><a href="https://github.com/mistymntncop/CVE-2024-5274" target="_blank">CVE-2024-5274</a> - PoC for the type confusion in V8 in Google Chrome prior to 125.0.6422.112 that allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page.</li>
<li><a href="https://github.com/jonpalmisc/limoncello" target="_blank">limoncello</a> - Yet another LLVM-based obfuscator.</li>
<li><a href="https://github.com/hackerschoice/hackshell" target="_blank">hackshell</a> - Make BASH stealthy and hacker friendly with lots of bash functions.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.archcloudlabs.com/projects/5-years-of-homelab/" target="_blank">5 Years of InfoSec Focused Homelabbing</a> - Start a homelab, start a blog, achieve great things.</li>
<li><a href="https://github.com/coder/wush" target="_blank">wush</a> - simplest &amp; fastest way to transfer files between computers via WireGuard.</li>
<li><a href="https://github.com/zodiacon/VerifierDLL" target="_blank">VerifierDLL</a> - Example of building an application verifier DLL.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 433 (+1)</p>
<p>Blogs monitored: 386 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
