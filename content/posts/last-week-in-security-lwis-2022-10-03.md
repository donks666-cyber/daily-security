Title: Last Week in Security (LWiS) - 2022-10-03
Date: 2022-10-03 23:52
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-10-03
Author: Erik
Summary: Kerberos downgrade attack (<a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a>), Havoc C2 (<a href="https://twitter.com/C5pider" target="_blank">@C5pider</a>), ASNmap (<a href="https://twitter.com/pdiscoveryio" target="_blank">@pdiscoveryio</a>), static vs behavioral detection (<a href="https://twitter.com/ShitSecure" target="_blank">@ShitSecure</a>), Freeze payload toolkit (<a href="https://twitter.com/Tyl0us" target="_blank">@Tyl0us</a>), multiple tools from <a href="https://twitter.com/D1rkMtr" target="_blank">@D1rkMtr</a>, cheap Yubikeys, Playstation 5 jailbreak, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-09-26 to 2022-10-03.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cloudflare.com/products/zero-trust/phishing-resistant-mfa/#HTMLIdYubicoOffer/" target="_blank">Activate phishing-resistant MFA</a>. No excuse to not have hardware MFA at this point. Cloudflare makes it $10 per key for high quality Yubikey 5's. This is the best $-to-protection ratio you will ever spend (if you enforce it).</li>
<li><a href="https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/" target="_blank">Customer Guidance for Reported Zero-day Vulnerabilities in Microsoft Exchange Server</a>. Microsoft pushed out a temporary rewrite rule to Exchange on prem, but my advice would be to stop hosting this RCE-as-a-service product in your environment. Sadly, the big providers have taken over the dream of a decentralized internet with email for now.</li>
<li><a href="https://www.justice.gov/usao-co/pr/former-nsa-employee-arrested-espionage-related-charges" target="_blank">Former NSA Employee Arrested on Espionage-Related Charges</a> . I suppose you only read about the ones with bad OPSEC but man, this guy wasn't even really trying. I suspect his short employment period also put him under extra scrutiny. With OPSEC this bad, perhaps he should have applied to work at the CIA and contribute to <a href="https://www.reuters.com/investigates/special-report/usa-spies-iran/" target="_blank">America's Throwaway Spies</a>.</li>
<li><a href="https://www.chainguard.dev/unchained/introducing-wolfi-the-first-linux-un-distro" target="_blank">Introducing Wolfi - the first Linux (Un)distro designed for securing the software supply chain</a>. I'm not fully sold on this "undistro." Seems a bit like <a href="https://nixos.org/" target="_blank">Nix</a> but with the package manager removed?</li>
<li><a href="https://github.com/Cryptogenic/PS5-4.03-Kernel-Exploit" target="_blank">PS5-4.03-Kernel-Exploit</a> An experimental webkit-based kernel exploit (Arb. R/W) for the PS5 on 4.03FW. Not really useful for red teaming, but a neat exploit chain.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.praetorian.com/blog/fingerprintx/" target="_blank">Introducing FingerprintX: The fastest port fingerprint scanner</a>. <a href="https://github.com/projectdiscovery/httpx" target="_blank">httpx</a> is a great tool for web scanning, but fingerprintx expands it other ports and protocols. Grab the <a href="https://github.com/praetorian-inc/fingerprintx" target="_blank">code</a> and start scanning!</li>
<li><a href="https://trenchant.io/two-lines-of-jscript-for-20000-pwn2own-miami-2022/" target="_blank">Two Lines of JScript for $20,000 - Pwn2Own Miami 2022</a>. Exploitation doesn't always have to be "hard." If calc pops, it doesn't matter if you spent 2 hours or 2 years working on the exploit. Try some simple things first!</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2310" target="_blank">Issue 2310: Windows: Kerberos RC4 MD4 Encryption Downgrade EoP</a>. James Forshaw, destroyer of Windows worlds, is at it again. Who knew you could downgrade Kerberos encryption so badly, as well as other tricks to get the actual amount of data you need to brute force down to a single byte. Well played.</li>
<li><a href="https://s3cur3th1ssh1t.github.io/Signature_vs_Behaviour/" target="_blank">The difference between signature-based and behavioral detections</a>. A good primer on types of AV/EDR detections and ideas for how to get around them. TLDR: You will be writing custom code.</li>
<li><a href="https://medium.com/@nynan/what-i-learnt-from-reading-220-idor-bug-reports-6efbea44db7" target="_blank">What I learnt from reading 220* IDOR bug reports.</a>. You're going to learn about IDOR today!</li>
<li><a href="https://engineering.avast.io/yari-a-new-era-of-yara-debugging/" target="_blank">YARI: A New Era of YARA Debugging</a>. Woah, this is seriously cool if you work with yara. Code <a href="https://github.com/avast/yari" target="_blank">here</a>.</li>
<li><a href="https://0x64marsh.com/?p=314" target="_blank">Kernel Driver Exploit: System Mechanic</a>. I know I am late on this one (technically not last week), but it was too good to not include. Don't worry the blog is now monitored.</li>
<li><a href="https://mrd0x.com/phishing-with-chromium-application-mode/?no-cache=1" target="_blank">Phishing With Chromium's Application Mode</a> In this blog post mr.d0x shows how Chromium's application mode allows us to easily create realistic desktop phishing applications.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://gitlab.com/badsectorlabs/iscariot-suite" target="_blank">Iscariot Suite</a> is a collection of tools to enhance and augment trusted open-source and commercial Blue Team/Sysadmin products, turning them into traitorware to achieve offensive security goals.</li>
<li><a href="https://github.com/HavocFramework/Havoc" target="_blank">Havoc</a>. This is the much anticipated C2 from <a href="https://twitter.com/C5pider" target="_blank">@C5pider</a>. It also supports <a href="https://codex-7.gitbook.io/codexs-terminal-window/red-team/red-team-dev/extending-havoc-c2/third-party-agents" target="_blank">Third Party Agents</a>.</li>
<li><a href="https://blog.projectdiscovery.io/asnmap/" target="_blank">ASNMap</a> - A Golang CLI tool for speedy reconnaissance using ASN data.</li>
<li><a href="https://github.com/edgelesssys/constellation" target="_blank">constellation</a> is the first Confidential Kubernetes. Constellation shields entire Kubernetes clusters from the (cloud) infrastructure using confidential computing.</li>
<li><a href="https://github.com/D1rkMtr/VirusTotalC2" target="_blank">VirusTotalC2</a> Abusing VirusTotal API to host our C2 traffic, useful for bypassing blocking firewall rules if VirusTotal is in the target white list, and in case you don't have C2 infrastructure, now you have a free one.</li>
<li><a href="https://github.com/HackmichNet/AzTokenFinder" target="_blank">AzTokenFinder</a> is a small tool to extract JWT (or JWT like looking data) from different processes, like PowerShell, Excel, Word or others.</li>
<li><a href="https://github.com/optiv/Freeze" target="_blank">Freeze</a> is a payload toolkit for bypassing EDRs using suspended processes, direct syscalls, and alternative execution methods.</li>
<li><a href="https://github.com/D1rkMtr/ChTimeStamp/tree/main" target="_blank">ChTimeStamp</a> - Changing the Creation time and the Last Written time of a dropped file by the timestamp of other one , like the "kernel32.dll" timestamp.</li>
<li><a href="https://github.com/D1rkMtr/ADSrunner" target="_blank">ADSrunner</a> - Write a UUIDs bytes array "*" collected to the Alternate Data Stream of the current binary , then the ADS Runner will get the DATA tranfert it into a char table nice UUIDS shellcode and Run it.</li>
<li><a href="https://github.com/D1rkMtr/FileLessRemoteShellcode" target="_blank">FileLessRemoteShellcode</a> - Run Fileless Remote Shellcode directly in memory with Module Unhooking, Module Stomping, No New Thread. This repository contains the TeamServer and the Stager.</li>
<li><a href="https://github.com/D1rkMtr/DumpThatLSASS" target="_blank">DumpThatLSASS</a> - Dumping LSASS by Unhooking MiniDumpWriteDump by getting a fresh DbgHelp.dll copy from the disk, plus functions and strings obfuscation, it contains Anti-sandbox, if you run it under unperformant Virtual Machine you need to uncomment the code related to it and recompile.</li>
<li><a href="https://github.com/smokeme/airstrike" target="_blank">airstrike</a> is a basic stage 0 implant.</li>
<li><a href="https://github.com/ORCx41/KnownDllUnhook" target="_blank">KnownDllUnhook</a> - Replace the .txt section of the current loaded modules from KnownDllsto bypass edrs.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/silverhack/monkey365" target="_blank">monkey365</a> provides a tool for security consultants to easily conduct not only Microsoft 365, but also Azure subscriptions and Azure Active Directory security configuration reviews.</li>
<li><a href="https://github.com/swanandx/lemmeknow" target="_blank">lemmeknow</a>.  The fastest way to identify anything!</li>
<li><a href="https://github.com/araekiel/jot" target="_blank">jot</a> - Rapid note management for the terminal.</li>
<li><a href="https://github.com/nheiniger/SnaffPoint" target="_blank">SnaffPoint</a> - A tool for pointesters to find candies in SharePoint.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+1)</p>
<p>Blogs monitored: 325 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
