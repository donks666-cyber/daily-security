Title: Last Week in Security (LWiS) - 2022-10-10
Date: 2022-10-10 23:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-10-10
Author: Erik
Summary: Intel Alder Lake src leak (<a href="https://twitter.com/vxunderground" target="_blank">@vxunderground</a> ), PHP payloads in PNGs (<a href="https://twitter.com/ROLANDQuentin2" target="_blank">@ROLANDQuentin2</a>), Zimbra RCE via email, macOS Gatekeeper bypass (<a href="https://twitter.com/JamfSoftware" target="_blank">@JamfSoftware</a>), ShadowSpray (<a href="https://twitter.com/dec0ne" target="_blank">@dec0ne</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-10-03 to 2022-10-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://twitter.com/vxunderground/status/1578575040647266304" target="_blank">The source code to the Intel Alder Lake has been leaked online.</a> Critically, this seems to include the <a href="https://twitter.com/_markel___/status/1578771873508519936" target="_blank">KetManifest signing key</a> needed to sign BootPolicy and therefore bypass SecureBoot. A boon to CoreBoot and bootkits alike.</li>
<li><a href="https://forums.zimbra.org/viewtopic.php?t=71153&amp;p=306532" target="_blank">Attacker managed to upload files into Web Client directory</a>. CPIO unpacking in the AV engine used by Zimbra lead to arbitrary file writes (webshell) and RCE. You hate to see the AV used as an attack vector but it does happen.</li>
<li><a href="https://securelist.com/onionpoison-infected-tor-browser-installer-youtube/107627/" target="_blank">OnionPoison: infected Tor Browser installer distributed through popular YouTube channel</a>. Always check the hash from the official source.</li>
<li><a href="https://leaningtech.com/webvm-virtual-machine-with-networking-via-tailscale/" target="_blank">WebVM: Linux Virtualization in WebAssembly with Full Networking via Tailscale</a>. The x86 VM running in javascript in your browser window now has a networking stack. This must be a sign of the end times.</li>
<li><a href="https://www.rapid7.com/blog/post/2022/10/07/metasploit-weekly-wrap-up-179/" target="_blank">Bofloader - Windows Meterpreter Gets Beacon Object File Loader Support</a>. BOFs are the atomic element of offensive tools now.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://driesdepoorter.be/thefollower/" target="_blank">The Follower - Using open cameras and AI to find how an Instagram photo is taken.</a>. Imagine what governments/surveillance companies are doing...</li>
<li><a href="https://www.jamf.com/blog/jamf-threat-labs-macos-archive-utility-vulnerability/" target="_blank">Jamf Threat Labs identifies macOS Archive Utility vulnerability allowing for Gatekeeper bypass</a>. Very thorough research into a sneaky bug in the archive utility on macOS.</li>
<li><a href="https://www.synacktiv.com/en/publications/persistent-php-payloads-in-pngs-how-to-inject-php-code-in-an-image-and-keep-it-there.html" target="_blank">Persistent php payloads in PNGs: how to inject php code in an image - and keep it there!</a>. Some nice tricks to stashing PHP payloads in PNGs.</li>
<li><a href="https://m365internals.com/2022/10/10/how-to-implement-the-exchange-split-permissions-model/" target="_blank">How To Implement The Exchange Split Permissions Model?</a>. If you still have on-prem exchange, this is for you. Also, seek help.</li>
<li><a href="https://www.trustedsec.com/blog/common-conditional-access-misconfigurations-and-bypasses-in-azure/" target="_blank">Common conditional access misconfigurations and bypasses in Azure</a>. Your target may required MFA, except if certain conditions are met.</li>
<li><a href="https://tbhaxor.com/evil-twin-wifi-network-using-hostapd-mana/" target="_blank">Evil Twin Enterprise WiFi Network using Hostapd-Mana</a>. A good one for your next on-site or physical assessment.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://talosintelligence.com/vulnerability_reports/TALOS-2022-1587" target="_blank">VMware vCenter Server Platform Services Controller Unsafe Deserialization vulnerability</a>. "A post-authentication java deserialization vulnerability exists in the data handler of the psc (Platform Services Controller) service."</li>
<li><a href="https://github.com/D1rkMtr/ObfLoader/tree/main" target="_blank">ObfLoader</a> - MAC, IPv4, UUID shellcode Loaders and Obfuscators to obfuscate the shellcode and using some native API to converts it to it binary format and loads it.</li>
<li><a href="https://github.com/jamf/aftermath" target="_blank">aftermath</a> is a free macOS IR framework from Jamf.</li>
<li><a href="https://github.com/m3n0sd0n4ld/GooFuzz" target="_blank">GooFuzz</a> is a tool to perform fuzzing with an OSINT approach, managing to enumerate directories, files, subdomains or parameters without leaving evidence on the target's server and by means of advanced Google searches (Google Dorking).</li>
<li><a href="https://github.com/mxrch/GitFive" target="_blank">GitFive</a> - 🐙 Track down GitHub users.</li>
<li><a href="https://github.com/t3l3machus/eviltree" target="_blank">eviltree</a> - A python3 remake of the classic "tree" command with the additional feature of searching for user provided keywords/regex in files, highlighting those that contain matches.</li>
<li><a href="https://labs.withsecure.com/publications/hunting-for-timer-queue-timers" target="_blank">Caught somewhere in time: Hunting for timer-queue timers</a>. Timers are the "default" method rats use to sleep in memory. If you can detect suspect timers, you can probably find some interesting things. Code <a href="https://github.com/WithSecureLabs/TickTock" target="_blank">here</a>.</li>
<li><a href="https://github.com/tyranid/Rubeus/commit/3092e1f11164bf379708b815a05061783653e834" target="_blank">Added simple command to test CVE_2022_33679.</a>. Now you can run 'askrc4' and exploit CVE-2022-33679 (KDC allows an interposing attacker to downgrade to RC4 MD4 encryption in compromising the user's TGT session key resulting in EoP). See <cite>this tweet &lt;https://twitter.com/m3g9tr0n/status/1577783061919457281&gt;</cite> and <a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2310" target="_blank">this project zero post</a>.</li>
<li><a href="https://github.com/med0x2e/vba2clr" target="_blank">vba2clr</a> - Running .NET from VBA.</li>
<li><a href="https://github.com/its-a-feature/LockSmith" target="_blank">LockSmith</a> - ObjectiveC CLI tool for interacting with macOS Keychain. I was just struggling with this a few weeks ago! Be sure to check out the slides in the repo.</li>
<li><a href="https://github.com/palera1n/palera1n" target="_blank">palera1n</a> - iOS 15.0-15.3.1 tethered checkm8 "jailbreak" (rootless is 15.0-15.7 semi-tethered, no tweaks),</li>
<li><a href="https://github.com/Dec0ne/ShadowSpray/" target="_blank">ShadowSpray</a> - A tool to spray Shadow Credentials across an entire domain in hopes of abusing long forgotten GenericWrite/GenericAll DACLs over other objects in the domain.</li>
<li><a href="https://github.com/Tw1sm/RITM" target="_blank">RITM</a> - Roast in the Middle.</li>
<li><a href="https://github.com/fox-it/dissect" target="_blank">dissect</a> - This project is a meta package, it will install all other Dissect modules with the right combination of versions.</li>
<li><a href="https://github.com/X-C3LL/SharpNTLMRawUnHide" target="_blank">SharpNTLMRawUnHide</a> - C# version of NTLMRawUnHide.</li>
<li><a href="https://github.com/S3cur3Th1sSh1t/NimShellcodeFluctuation" target="_blank">NimShellcodeFluctuation</a> - ShellcodeFluctuation PoC ported to Nim.</li>
<li><a href="https://github.com/rasta-mouse/MinHook.NET" target="_blank">MinHook.NET</a> - A C# port of the MinHook API hooking library (now with D/Invoke).</li>
<li><a href="https://github.com/CodeXTF2/HavocNotion" target="_blank">HavocNotion</a> - A simple ExternalC2 POC for Havoc C2. Communicates over Notion using a custom python agent, handler and extc2 channel.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/PinoyWH1Z/AoratosWin" target="_blank">AoratosWin</a> - A tool that removes traces of executed applications on Windows OS.</li>
<li><a href="https://github.com/InitRoot/wodat" target="_blank">wodat</a> - Windows Oracle Database Attack Toolkit.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 421 (+0)</p>
<p>Blogs monitored: 325 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
