Title: Last Week in Security (LWiS) - 2022-02-22
Date: 2022-02-22 23:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-02-22
Author: Erik
Summary: VMware RCEs (<a href="https://twitter.com/__mn1__" target="_blank">@__mn1__</a> and <a href="https://twitter.com/elk0kc" target="_blank">@elk0kc</a>), un-redacting text (<a href="https://twitter.com/2600AltF4" target="_blank">@2600AltF4</a>), undetectible AirTags (<a href="https://twitter.com/positive_sec" target="_blank">@positive_sec</a>), Kerberos relaying via DNS (<a href="https://twitter.com/_dirkjan" target="_blank">@_dirkjan</a>), tmp.Out volume 2 (<a href="https://twitter.com/tmpout" target="_blank">@tmpout</a>), tclsh macOS dylib loading (<a href="https://twitter.com/_D00mfist" target="_blank">@_D00mfist</a>), Athena agent (<a href="https://twitter.com/checkymander" target="_blank">@checkymander</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-02-14 to 2022-02-22.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.foreignaffairs.com/articles/united-states/2022-02-21/cyber-social-contract" target="_blank">The Cyber Social Contract How to Rebuild Trust in a Digital World</a>. US National Cyber Director Chris Inglis postulates that the free market can't solve cybersecurity. It will be interesting to see how this develops.</li>
<li><a href="https://www.gosecure.net/blog/2022/02/14/current-mfa-fatigue-attack-campaign-targeting-microsoft-office-365-users/" target="_blank">Current MFA Fatigue Attack Campaign Targeting Microsoft Office 365 Users</a>. Overwhelming victims with tons of push MFA messages until they finally click allow just to make them stop is a valid attack. Does your organization detect MFA floods, or does your MFA system lock accounts after a threshold of MFA tokens have been requested with no user action?</li>
<li><a href="https://blog.coinbase.com/retrospective-recent-coinbase-bug-bounty-award-9f127e04f060" target="_blank">Retrospective: Recent Coinbase Bug Bounty Award</a>. Logic bugs in web apps can be bad, or they can be horrific. This one is horrific. A $250k bounty proves again cryptocurrency is where the money is for bug bounty hunters.</li>
<li><a href="https://tmpout.sh/2/" target="_blank">tmp.Out Volume 2 released</a>. tmp.Out is becoming a linux focused Phrak, and I'm here for it. Excited to dig into these articles!</li>
<li><a href="https://www.forensicfocus.com/news/passware-kit-forensic-t2-add-on-the-first-password-recovery-tool-for-macs-with-t2-chips/" target="_blank">Passware Kit Forensic T2 Add-on: The First Password Recovery Tool for Macs With T2 Chips</a>. According to <a href="https://9to5mac.com/2022/02/17/t2-mac-security-vulnerability-passware/" target="_blank">9to5mac</a>, the exploit only allows ~15 attempts per second, so your 15+ character macOS password is probably safe. The attack requires phyiscal access. M1 macs are not affected.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://dirkjanm.io/relaying-kerberos-over-dns-with-krbrelayx-and-mitm6/" target="_blank">Relaying Kerberos over DNS using krbrelayx and mitm6</a>. This is the next generation of WPAD relaying! Dirk-jan delivers yet again. I had no idea there was such a thing as an authenticated dynamic update via DNS. I'm not sure how often this happens in production environments, but it's a neat technique to add to your toolbox.</li>
<li><a href="https://swarm.ptsecurity.com/hunting-for-bugs-in-vmware-view-planner-and-vrealize-business-for-cloud/" target="_blank">Hunting for bugs in VMware: View Planner and vRealize Business for Cloud</a>. Seemingly tiny mistakes lead to big vulnerabilities (unauth RCE) in VMware products in this post. A great read for anyone who does web app assessments or source code review.</li>
<li><a href="https://3xpl01tc0d3r.blogspot.com/2022/02/a-primer-on-dcsync-attack-and-detection.html" target="_blank">A primer on DCSync attack and detection</a>. DCSync is the "slam dunk" of many internal assessments, and this post shows how its done and details how to detect it in your environment including using <a href="https://github.com/shellster/DCSYNCMonitor" target="_blank">DCSYNCMonitor</a>.</li>
<li><a href="https://blog.cloudflare.com/tubular-fixing-the-socket-api-with-ebpf/" target="_blank">Production ready eBPF, or how we fixed the BSD socket API</a>. Cloudflare's use case for <a href="https://github.com/cloudflare/tubular" target="_blank">tubular</a>, a BSD socket API on steroids is to provide multiple service on the same port and listen on every port, but I can think of some more "rootkity" uses for tubular...</li>
<li><a href="https://blog.sonarsource.com/zabbix-case-study-of-unsafe-session-storage" target="_blank">Zabbix - A Case Study of Unsafe Session Storage</a>. Many web apps store authentication information on the client side in cookies or other browser storage. Problems arrise when misconfigurations allow clients to dictate their role without backend checks, as was this case with Zabbix, whech led to full authentication bypass.</li>
<li><a href="https://bishopfox.com/blog/unredacter-tool-never-pixelation" target="_blank">Never, Ever, Ever Use Pixelation for Redacting Text</a>. "When you need to redact text, use black bars covering the whole text. Never use anything else. No pixelization, no blurring, no fuzzing, no swirling. Oh, and be sure to actually edit the text as an image. Don’t make the mistake of changing your Word document so that it has black background with black text." If you need convincing, check out <a href="https://github.com/bishopfox/unredacter" target="_blank">unredacter</a>.</li>
<li><a href="https://positive.security/blog/find-you" target="_blank">Find You: Building a stealth AirTag clone</a>. By exploiting the privacy functioanlity of AirTags and the amazing (and previously blogged about) <a href="https://github.com/seemoo-lab/openhaystack" target="_blank">openhaystack</a> procject, this post shows how you can create, and detect, otherwise undetectable trackers. Check out the code in <a href="https://github.com/positive-security/find-you" target="_blank">find-you</a>.</li>
<li><a href="https://captmeelo.com//redteam/maldev/2022/02/16/libraries-for-maldev.html" target="_blank">Useful Libraries for Malware Development</a>. Some old and new friends in here. Worth a read for any tool developer!</li>
<li><a href="https://blog.nviso.eu/2022/02/22/kernel-karnage-part-9-finishing-touches/" target="_blank">Kernel Karnage – Part 9 (Finishing Touches)</a>. This series has been a fun ride. The only sad part is no PoCs.</li>
<li><a href="https://posts.specterops.io/dylib-loads-that-tickle-your-fancy-d25196addd8c" target="_blank">Dylib Loads that Tickle your Fancy</a>. macOS is full of strange, archaic, binaries (to be fair, so is every OS). One such binary, tclsh can load arbitrary dynamic libraries.</li>
<li><a href="https://blog.zsec.uk/chasing-the-silver-petit-potam/" target="_blank">Chasing the Silver Petit Potam to Domain Admin</a>. Sometimes you get lucky and can crack the NTLMv1 hash from a DC authentication illicatation. In that case, its just one more step to DA!</li>
<li><a href="https://mrd0x.com/bypass-2fa-using-novnc/?no-cache=1" target="_blank">Steal Credentials &amp; Bypass 2FA Using noVNC</a>. Simply genious. Why bother with a tricky proxy solution, when you can just have the user log into a site with a browswer you control?</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/MythicAgents/Athena" target="_blank">Athena</a> is a fully-featured cross-platform agent designed using the .NET 6. Athena is designed for Mythic 2.2 and newer. <a href="https://blog.checkymander.com/red%20team/c2/Athena/" target="_blank">Crossplatform operations with Athena</a> has all the details.</li>
<li><a href="https://github.com/gtworek/PSBits/tree/master/AppLockerBypass" target="_blank">IgnoreAppLocker.dll</a> is a DLL to launch a cmd.exe as NT AUTHORITYSERVICE, which doesn't get blocked or logged by AppLocker, and neither do any processes launched by this cmd.exe process.</li>
<li><a href="https://github.com/Hagrid29/PELoader" target="_blank">PELoader</a> is a PELoader implement various shellcode injection techniques, and use libpeconv library to load encrypted PE files instead of injecting shellcode into remote thread.</li>
<li><a href="https://github.com/arcaneiceman/kraken" target="_blank">kraken</a> is a dockerized multi-platform distributed brute-force password cracking system with a web front end.</li>
<li><a href="https://github.com/bflattened/bflat" target="_blank">bflat</a> is a concoction of Roslyn - the "official" C# compiler that produces .NET executables - and NativeAOT (née CoreRT) - the ahead of time compiler for .NET based on CoreCLR. Thanks to this, you get access to the latest C# features using the high performance CoreCLR GC and native code generator (RyuJIT). C# as you know it but with Go-inspired tooling (small, selfcontained, and native executables).</li>
<li><a href="https://github.com/C-Sto/BananaPhone/" target="_blank">BananaPhone</a> is a go variant of Hells gate! (directly calling windows kernel functions, but from Go!) - not new, but now with Halo's gate!</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/mifi/lossless-cut" target="_blank">lossless-cut</a> aims to be the ultimate cross platform FFmpeg GUI for extremely fast and lossless operations on video, audio, subtitle and other related media files. The main feature is lossless trimming and cutting of video and audio files, which is great for saving space by rough-cutting your large video files taken from a video camera, GoPro, drone, etc. It lets you quickly extract the good parts from your videos and discard many gigabytes of data without doing a slow re-encode and thereby losing quality. Not offsec related, but useful!</li>
<li><a href="https://github.com/codeyourweb/fastfinder" target="_blank">fastfinder</a> is a lightweight tool made for threat hunting, live forensics and triage on both Windows and Linux Platforms.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
