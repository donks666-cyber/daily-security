Title: Last Week in Security (LWiS) - 2023-01-23
Date: 2023-01-23 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-01-23
Author: Erik
Summary: No Fly List leak (<a href="https://twitter.com/_nyancrimew" target="_blank">@_nyancrimew</a>), LogSlash (<a href="https://twitter.com/4A4133" target="_blank">@4A4133</a>), Okta issues (<a href="https://twitter.com/varonis" target="_blank">@varonis</a>), ARM bug pwns Pixel (<a href="https://twitter.com/mmolgtm" target="_blank">@mmolgtm</a>), golddigger (<a href="https://twitter.com/ustayready" target="_blank">@ustayready</a>), APCLdr (<a href="https://twitter.com/NUL0x4C" target="_blank">@NUL0x4C</a>), build your own SANS760 (<a href="https://twitter.com/Void_Sec" target="_blank">@Void_Sec</a>), SOCKS4a shellcode, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-01-16 to 2023-01-23.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://maia.crimew.gay/posts/how-to-hack-an-airline/" target="_blank">how to completely own an airline in 3 easy steps</a>. The US "No fly list" was found on an exposed jenkins server belonging to CommuteAir. 80MB of NOFLY.CSV. Classic.</li>
<li><a href="https://blog.foxio.io/introducing-logslash-and-the-end-of-traditional-logging-2c6708b6fc1c" target="_blank">Introducing LogSlash and The End of Traditional Logging</a>. An interesting idea so save the "meaning" of a series of logs without all the raw data. I think large firms will still be saving all the raw data as all their detections are built on it, but I like the idea.</li>
<li><a href="https://sqlite.org/hctree/doc/hctree/doc/hctree/index.html" target="_blank">HC-tree</a>. A very non-descriptive title for a really cool feature. HC-tree is a high performance backend for SQLite that enables concurrency, replication, and massive size SQLite DBs. There aren't many small applications that shouldn't be using SQLite today as their DB, but with HC-tree, there will be almost none that need anything but SQLite.</li>
<li><a href="https://devblogs.microsoft.com/visualstudio/visual-studio-spell-checker-preview-now-available/" target="_blank">Visual Studio Spell Checker Preview Now Available</a>. Misspellers of the world, untie! (it won't help in this case... oh well.)</li>
<li><a href="https://www.theinsaneapp.com/2023/01/pirate-bay-proxy-portal-taken-down-by-github.html" target="_blank">Pirate Bay Proxy Portal Taken Down by Github</a>. Opinions of The Pirate Bay aside, GitHub took down a page that was hosting links to proxies, not even The Pirate Bay itself. <a href="https://github.com/TheTorProject" target="_blank">The Tor Project</a> is still on GitHub. Strange to see where the line is drawn sometimes.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.zerodayinitiative.com/blog/2023/1/18/cve-2022-35690-unauthenticated-rce-in-adobe-coldfusion" target="_blank">CVE-2022-35690: Unauthenticated RCE in Adobe ColdFusion</a>. ColdFusion is not only still a thing, but it's also still full of holes.</li>
<li><a href="https://github.blog/2023-01-23-pwning-the-all-google-phone-with-a-non-google-bug/" target="_blank">Pwning the all Google phone with a non-Google bug</a>. The bug here is cool, and the patch gap between ARM and Android on a hardware controlled by it's OS maker (Pixel 6) is worrying.</li>
<li><a href="https://blog.stratumsecurity.com/2023/01/23/remote-code-execution-through-deserializtion/" target="_blank">CVE from 2018 Strikes Again</a>. I've said it before and I'll say it again, just because a vulnerability is patched, doesn't mean its fixed. This is a one such case, albeit a simple one.</li>
<li><a href="https://palant.info/2023/01/23/bitwarden-design-flaw-server-side-iterations/" target="_blank">Bitwarden design flaw: Server side iterations</a>. With LastPass's recent issue, many have been searching for a new password manager, and researchers have been taking a look too. Positive change has already taken place because of this, and the open source BitWarden is getting more secure. However, you may want to manually increase your PBKDF2 iteration setting (Vaultwarden is also set at 100,000 by default as of 2023-01-23). The use of a secret key like <a href="https://blog.1password.com/what-the-secret-key-does/" target="_blank">1Password</a> has is a feature many would like to see implemented in other password managers. Need more password manager (patched) flaws? <a href="https://github.com/google/security-research/security/advisories/GHSA-mhhf-w9xw-pp9x" target="_blank">Unsandboxed Password Manager</a> has them.</li>
<li><a href="https://blog.geekycat.in/client-side-ssrf-to-google-cloud-project-takeover/" target="_blank">Client-Side SSRF to Google Cloud Project Takeover [Google VRP]</a>. A combo of Google properties (FeedBurner + VertexAI) combined for a nice Google Cloud takeover. It's not just Google, as <a href="https://msrc-blog.microsoft.com/2023/01/17/microsoft-resolves-four-ssrf-vulnerabilities-in-azure-cloud-services/" target="_blank">Microsoft resolves four SSRF vulnerabilities in Azure cloud services</a>.</li>
<li><a href="https://securitylabs.datadoghq.com/articles/iamadmin-cloudtrail-bypass/" target="_blank">AWS CloudTrail vulnerability: Undocumented API allows CloudTrail bypass</a>. Why is a CloudTrail bypass a big deal? When you are looking for ways to validate AWS keys without falling victim to a <a href="https://www.canarytokens.org/generate" target="_blank">Canary Token</a> finding a method to use them without showing up in CloudTrail is the only way. Speaking of canary tokens they just released new <a href="https://blog.thinkst.com/2023/01/swipe-right-on-our-new-credit-card-tokens.html" target="_blank">credit card tokens</a>.</li>
<li><a href="https://www.horizon3.ai/manageengine-cve-2022-47966-technical-deep-dive/" target="_blank">ManageEngine CVE-2022-47966 Technical Deep Dive</a>. A quick run through of the RCE starting with the patch.</li>
<li><a href="https://www.synacktiv.com/sites/default/files/2023-01/sudo-CVE-2023-22809.pdf" target="_blank">[PDF] Sudoedit bypass in Sudo &lt;= 1.9.12p1 CVE-2023-22809</a>. A simple command injection-style bug in the EDITOR environement variable allowed a user with sudoedit permissions on a single file to write to arbitray files as root. Perhaps not a common setup to have sudoedit enabled, but an easy LPE if it is!</li>
<li><a href="https://www.varonis.com/blog/okta-attack-vectors" target="_blank">CrossTalk and Secret Agent: Two Attack Vectors on Okta's Identity Suite</a>. Some excelent creative hacking that will become more important as more things move to SaaS.</li>
<li><a href="https://googleprojectzero.blogspot.com/2023/01/exploiting-null-dereferences-in-linux.html" target="_blank">Exploiting null-dereferences in the Linux kernel</a>. Not crashing the kernel and instead "oops"-ing is better, but can have unintended consequences.</li>
<li><a href="https://steve-s.gitbook.io/0xtriboulet/making-malware/making-malware-0#part-five-is-it-detected" target="_blank">making malware #0</a>. Not sure a public "API" is the best for tooling's long term evasion, but it might help in some cases.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Muirey03/CVE-2022-42864" target="_blank">CVE-2022-42864</a> - Proof-of-concept for the CVE-2022-42864 IOHIDFamily race condition that was fixed in iOS 16.2 / macOS Ventura 13.1. Read more at <a href="https://muirey03.blogspot.com/2023/01/cve-2022-42864-diabolical-cookies.html" target="_blank">Diabolical Cookies</a>.</li>
<li><a href="https://whynotsecurity.com/blog/credmaster2/" target="_blank">Credmaster2</a>. Your favorite credential spraying tool is back with more plugins.</li>
<li><a href="https://github.com/projectdiscovery/pdtm" target="_blank">pdtm</a> -  ProjectDiscovery's Open Source Tool Manager.</li>
<li><a href="https://caido.io/" target="_blank">Caido</a> - A lightweight web security auditing toolkit. Built from the ground up in Rust, Caido aims to help security professionals and enthusiasts audit web applications with efficiency and ease.</li>
<li><a href="https://github.com/elastic/silhouette" target="_blank">Silhouette</a> is a POC that mitigates the use of physical memory to dump credentials from LSASS.</li>
<li><a href="https://initialcommit.com/blog/git-sim" target="_blank">git-sim: Visually simulate Git operations in your own repos</a>. Complex git operations can be scary. They're less scary if you can see a pretty picture of what is happening.</li>
<li><a href="https://github.com/nobodyisnobody/docs/tree/main/a.socks.proxy.shellcode" target="_blank">a.socks.proxy.shellcode</a> is SOCKS4 server in shellcode for armv5, armv7, mipseb, and x64.</li>
<li><a href="https://github.com/nopbrick/SeeProxy" target="_blank">SeeProxy</a> - Golang reverse proxy with CobaltStrike malleable profile validation.</li>
<li><a href="https://github.com/ustayready/golddigger" target="_blank">golddigger</a> is a simple tool used to help quickly discover sensitive information in files recursively.</li>
<li><a href="https://github.com/NUL0x4C/APCLdr" target="_blank">APCLdr</a> - Payload Loader With Evasion Features.</li>
<li><a href="https://github.com/TurtleARM/CVE-2023-0179-PoC" target="_blank">CVE-2023-0179-PoC</a>. This is the Linux CVE from last week where the PoC was pulled. It's out now!</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/orhun/git-cliff" target="_blank">git-cliff</a> -  A highly customizable Changelog Generator that follows Conventional Commit specifications ⛰️</li>
<li><a href="https://github.com/kpcyrd/sh4d0wup" target="_blank">sh4d0wup</a> -  Signing-key abuse and update exploitation framework. This thing is fully featured and scary!</li>
<li><a href="https://github.com/anvilsecure/ulexecve" target="_blank">ulexecve</a> is a userland execve() implementation which helps you execute arbitrary ELF binaries on Linux from userland without the binaries ever having to touch storage. This is useful for red-teaming and anti-forensics purposes.</li>
<li><a href="https://voidsec.com/sans-sec760-advanced-exploit-development-for-penetration-testers-review/" target="_blank">SANS SEC760: Advanced Exploit Development for Penetration Testers - Review</a>. The review isn't the interesting part here, its section 3: Recommendations that are gold.</li>
<li><a href="https://github.com/Infisical/infisical" target="_blank">infisical</a> ♾ Infisical is an open-source, end-to-end encrypted tool to sync secrets and configs across your team and infrastructure.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 423 (+0)</p>
<p>Blogs monitored: 336 (+3)</p>
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
