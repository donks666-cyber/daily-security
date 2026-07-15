Title: Last Week in Security (LWiS) - 2025-06-09
Date: 2025-06-09 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-06-09
Author: Erik
Summary: Windows self-delete on 24H2 (<a href="https://x.com/TKYNSEC" target="_blank">@TKYNSEC</a>), DNS rebinding (<a href="https://x.com/yarlob" target="_blank">@yarlob</a>), VSCode backdoor (<a href="https://x.com/d1rkmtr" target="_blank">@d1rkmtr</a>), leak Google users' 📞# (<a href="https://x.com/brutecat" target="_blank">@brutecat</a>), Entra sync dumping (<a href="https://x.com/hotnops" target="_blank">@hotnops</a>), Delegations (<a href="https://x.com/podalirius_" target="_blank">@podalirius_</a>), Chrome abuse for screenshots, mic, and camera access (<a href="https://x.com/mrd0x" target="_blank">@mrd0x</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-06-02 to 2025-06-09.</p>
<aside class="m-note m-success">
Last Week in Security will be off next two weeks. Don't worry, the 2025-06-30 edition will be packed!</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.corellium.com/blog/cellebrite-to-acquire-corellium" target="_blank">Cellebrite to Acquire Corellium</a> - How much is the world's best "virtual hardware" platform worth? $200 million USD apparently. Congrats to Corellium founders Amanda Gorton, Chris Wade, and Stan Skowronek. Chris Wade (current Corellium CTO) will join Cellebrite as their new CTO. Hopefully the innovation continues!</li>
<li><a href="https://localmess.github.io/" target="_blank">Disclosure: Covert Web-to-App Tracking via Localhost on Android</a> - A novel combination of techniques to link web browsing to user identities on Android. Looks like Yandex was the first to use it back in 2017, and Meta picked it up in late 2024. Creative, but creepy.</li>
<li><a href="https://www.rnz.co.nz/news/world/563357/hmas-canberra-accidentally-blocks-wireless-internet-and-radio-services-in-new-zealand" target="_blank">HMAS Canberra accidentally blocks wireless internet and radio services in New Zealand</a> - Next time you have an outage, maybe you can blame radar interference from a warship.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.redteam-pentesting.de/2025/windows-coercion/" target="_blank">The Ultimate Guide to Windows Coercion Techniques in 2025</a> - Computer accounts in an active directory network can be extremly valuable, and there are a lot of ways to convince them to authenticate to your compromised host.</li>
<li><a href="https://jonny-johnson.medium.com/no-agent-no-problem-discovering-remote-edr-8ca60596559f" target="_blank">No Agent, No Problem: Discovering Remote EDR</a> - Use event tracing for windows (ETW) remotely to gather data on hosts without having to compromise them.</li>
<li><a href="https://tkyn.dev/2025-6-8-The-Not-So-Self-Deleting-Executable-on-24h2/" target="_blank">The Not So Self Deleting Executable on 24h2</a> - Windows changed some low level kernel handling of delete disposition flags, and thus broke an old faithful technique to self-delete files on Windows (normally not allowed). <a href="https://x.com/TKYNSEC" target="_blank">@TKYNSEC</a> dug in with Ghirda and found a method that works with 24H2.</li>
<li><a href="https://starlabs.sg/blog/2025/06-solo-a-pixel-6-pro-story-when-one-bug-is-all-you-need/" target="_blank">Solo: A Pixel 6 Pro Story (When one bug is all you need)</a> - Some hardcore Android exploitation. Lin rewrites a <a href="https://github.com/0x36/Pixel_GPU_Exploit" target="_blank">Mali GPU exploit</a> that required previously relied on a kernel address leak to only require the GPU exploit for the Pixel 6.</li>
<li><a href="https://github.blog/security/application-security/dns-rebinding-attacks-explained-the-lookup-is-coming-from-inside-the-house/" target="_blank">DNS rebinding attacks explained: The lookup is coming from inside the house!</a> - DNS rebinding isn't new, but it does have the power to expose "private" services to attacks. This article is a good overview with a real-life example (Deluge torrent server).</li>
<li><a href="https://talosintelligence.com/vulnerability_reports/TALOS-2024-2126" target="_blank">Parallels Desktop prl_vmarchiver Unarchive Hard Link Privilege Escalation</a> - macOS privilege escalations aren't all that common, and they usually come in the form of 3rd party software being exploited (like this one). Perhaps all the cool OS bugs are being sold/kept by researchers? There are <a href="https://talosintelligence.com/vulnerability_reports/TALOS-2025-2160" target="_blank">two</a> <a href="https://talosintelligence.com/vulnerability_reports/TALOS-2024-2123" target="_blank">other</a> Parallels privilege escalation bugs released as well.</li>
<li><a href="https://aff-wg.org/2025/06/04/planting-a-tradecraft-garden/" target="_blank">Planting a Tradecraft Garden</a> - "Tradecraft Garden is a collection of projects centered around the development of position-independent DLL loaders." The mastermind behind beacon object files (BOFs) drops "PICOs" - a BOF-like convention to run one-time or persistent COFFs from position-independent code. Visit the <a href="https://tradecraftgarden.org/tradecraft.html" target="_blank">Tradecraft Garden</a> to see the current collection of position-independent DLL loaders. I like Raphael's statement: "Develop technologies that give individual operators and researchers LEVERAGE acting on hypothesis and make it fast to try things, adapt, and modify." It echos what we are doing with the free and open source <a href="https://ludus.cloud/" target="_blank">Ludus</a>, making it fast and easy to try complex networks.</li>
<li><a href="https://rastamouse.me/harvesting-the-tradecraft-garden/" target="_blank">Harvesting the Tradecraft Garden</a> - Rasta Mouse incorporates the tools from the Tradecraft Garden into Cobalt Strike.</li>
<li><a href="https://brutecat.com/articles/leaking-google-phones" target="_blank">Bruteforcing the phone number of any Google user</a> - A combination of a display name leak from "Google Looker Studio" and the strange condition where a no-javascript endpoint would not rate limit when combined with a javascript created botguard token led to the ability to brute force the phone number of any Google user.</li>
<li><a href="https://posts.specterops.io/update-dumping-entra-connect-sync-credentials-4a9114734f71" target="_blank">Update: Dumping Entra Connect Sync Credentials</a> - The command <cite>Get-AADIntSyncCredentials</cite> no longer works, but fear not, you can still dump the Entra Connect Sync Credentials with <a href="https://github.com/hotnops/ECUtilities/tree/main/SharpECUtils" target="_blank">GetEntraConnectCreds.exe</a>.</li>
<li><a href="https://trustedsec.com/blog/teaching-a-new-dog-old-tricks-phishing-with-mcp" target="_blank">Teaching a New Dog Old Tricks - Phishing With MCP</a> - This is just the beginning of tailored phishing with AI. It only get's "worse" from here.</li>
<li><a href="https://trustedsec.com/blog/full-disclosure-graphghost-are-you-afraid-of-failed-logins" target="_blank">Full Disclosure, GraphGhost: Are You Afraid of Failed Logins?</a> - The ability to check for valid password without creating a log event is a valuable primitive. Microsoft fixed this specific flaw on 2025-04-11.</li>
<li><a href="https://blog.z-labs.eu/2025/06/04/all-about-cli4bofs-tool.html" target="_blank">So you want to rapidly run a BOF? Let's look at this 'cli4bofs' thing then</a> - Yet another standard for Beacon object file (BOF) metadata, in yaml this time. The one thing missing from the original BOF spec was a standard format for metadata instead of relying on .cna scripts. Pretty soon someone will write a .cna parser than can translate to both Sliver json and cli4bofs yaml.</li>
<li><a href="https://mrd0x.com/spying-with-chromium-browsers-screensharing/" target="_blank">Spying On Screen Activity Using Chromium Browsers</a> - Since browsers have to see your entire screen to be able to share it, they can also be used to take screenshots of your screen. A similar technique can be used for <a href="https://mrd0x.com/spying-with-chromium-browsers-camera/" target="_blank">Camera and Microphone Spying Using Chromium Browsers</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/SaadAhla/VSCode-Backdoor" target="_blank">VSCode-Backdoor</a> - Backdooring VSCode Projects.</li>
<li><a href="https://github.com/MarkBaggett/srum-dump" target="_blank">srum-dump</a> - A forensics tool to convert the data in the Windows srum (System Resource Usage Monitor) database to an xlsx spreadsheet.</li>
<li><a href="https://github.com/MaangoTaachyon/SelfDeletion-Updated" target="_blank">SelfDeletion-Updated</a> - Updated version of a long known self deletion technique to work with 24H2.</li>
<li><a href="https://github.com/hotnops/ECUtilities" target="_blank">ECUtilities</a> - Powershell and python utilities for Entra Connect.</li>
<li><a href="https://github.com/jonny-jhnson/JonMon-Lite" target="_blank">JonMon-Lite</a> is a research proof-of-concept "Remote Agentless EDR" that creates an ETW Trace Session through a Data Collector Set. This session can be created locally or remotely.</li>
<li><a href="https://github.com/cybersectroll/TrollRPC" target="_blank">TrollRPC</a> - a library to blind RPC calls based on UUID and OPNUM. A more surgical version of <a href="https://github.com/andreisss/Ghosting-AMSI" target="_blank">Ghosting-AMSI</a>.</li>
<li><a href="https://github.com/assetnote/newtowner" target="_blank">newtowner</a> - Abuse trust-boundaries to bypass firewalls and network controls.</li>
<li><a href="https://github.com/TheManticoreProject/Delegations" target="_blank">Delegations</a> - A tool to work with all types of Kerberos delegations (unconstrained, constrained, and resource-based constrained delegations) in Active Directory.</li>
<li><a href="https://github.com/interruptlabs/VRDP-Training-Material" target="_blank">VRDP-Training-Material</a> - This repository contains the pre-joining training materials given to aspiring researchers on the Vulnerability Researcher Development Program.</li>
<li><a href="https://github.com/jfjallid/kerbtool" target="_blank">kerbtool</a> - A tool to interact with Kerberos to request, forge and convert various types of tickets in an Active Directory environment.</li>
<li><a href="https://github.com/whokilleddb/funcshenanigans" target="_blank">funcshenanigans</a> - A bunch of shenanigans using functions, VEH and more.</li>
<li><a href="https://github.com/ibaiC/SafeHarbor-BOF" target="_blank">SafeHarbor-BOF</a> - Safe Harbor is a BOF that streamlines process reconnaissance for red team operations by identifying trusted, low-noise targets to maintain stealth and robust OPSEC.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://blog.cybershenanigans.space/posts/boflink-a-linker-for-beacon-object-files/" target="_blank">Boflink: A Linker For Beacon Object Files</a> - Boflink was presented in last week's blog, but without explanation. Here are all the details!</li>
<li><a href="https://anemato.de/blog/kctf-vdf" target="_blank">Beating the kCTF PoW with AVX512IFMA for $51k</a> - Serious CTF players are on a different level. Timothy implemented a proof of work solver in AVX512 to beat other teams to a flag submission by solving the proof of work over 4x faster. That is to say nothing about the fact to win you also needed a stable Linux kernel 0day! 🤯</li>
<li><a href="https://fly.io/blog/youre-all-nuts/" target="_blank">My AI Skeptic Friends Are All Nuts</a> - If you find yourself getting sick of AI hype, this is for you.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 454 (+1)</p>
<p>Blogs monitored: 423 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
